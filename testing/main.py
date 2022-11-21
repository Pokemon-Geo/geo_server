import datetime
from flask import Flask, request, flash, redirect
from database.database import get_db
from upload.upload import allowed_file, upload_photo
from machine.infer import predict_image

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/api/v1/issues/<uuid>/", methods=["GET"], strict_slashes=False)
def get_issues(uuid):
    cur = get_db().cursor()    
    # get issues from database that the user did not do yet
    cur.execute("SELECT * FROM issues as t1 WHERE t1.osm_way_id NOT IN (SELECT osm_way_id FROM user_task WHERE guid = ?);", (uuid,))
    data = cur.fetchall()
    res = [dict(r) for r in data]
    return {"data": res}

# leaderboard 
@app.route("/api/v1/leaderboard/", methods=["GET"])
def leaderboard():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users ORDER BY points DESC")
    data = cur.fetchall()  
    res = [dict(r) for r in data]     
    return {"data": res}

# leaderboard 
@app.route("/api/v1/teamleaderboard/", methods=["GET"])
def uni_leaderboard():
    cur = get_db().cursor()
    cur.execute("SELECT `university`, SUM(`points`) AS `total_points` FROM `users` GROUP BY `university` ORDER BY `total_points` DESC;")
    data = cur.fetchall()  
    res = [dict(r) for r in data]     
    return {"data": res}

# data user
@app.route("/api/v1/user/<uuid>/", methods=["GET"])
def hello_world(uuid):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users WHERE guid = ?", (uuid,))
    data = dict(cur.fetchone())
    return {"data": data}


# vote for issue
@app.route("/api/v1/voting/<uuid>/<issue_id>/", methods=["GET"])
def vote(uuid, issue_id):
    #get params from request
    category = request.args.get('category')
    print(category)
    if(category in("footway", "primary")):            

        # connect to db
        cur = get_db().cursor()
        # update category of isser
        cur.execute("UPDATE user_task SET user_category = ? WHERE osm_way_id = ? AND guid = ?", (category, issue_id, uuid))  
        get_db().commit()

        return {"data": "ok"}
    
    return {"data": "error"}

@app.route("/api/v1/infer/<uuid>/<timestamp>", methods=["GET"])
def infer(uuid, timestamp):
    res = predict_image(uuid, timestamp)

    return {"data": res}

# save task
@app.route("/api/v1/photo/<uuid>/<task_id>/<multiplier>", methods=["POST"], strict_slashes=False)
def upload_file(uuid, task_id, multiplier):    

    print(request.files)    
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        print("no file")
        return {"message": "No file part"}, 400
    file = request.files['file']
    
    # if user does not select file, browser also   
    
    if file.filename == '':
        flash('No selected file')
        print("no selected file")
        return {"message": "No selected file"}, 400    

    if file:
        res = upload_photo(file, uuid)        

        if res:            
            cur = get_db().cursor()
            cur.execute("INSERT INTO user_task (osm_way_id, guid, photo_id, taken_at) VALUES (?, ?, ?, ?)", (task_id, uuid, res, datetime.datetime.now()))
            cur.execute("UPDATE users SET points = points + ? WHERE guid = ?", (100*int(multiplier),uuid,))
            get_db().commit()

            cat = predict_image(uuid, res)

            data = {"image_id": res, "category": cat}

            return {"data": data}, 200
        else:
            return {"data": "error"}, 400

    return {"data": "error"}    