SELECT * FROM issues as t1 WHERE t1.osm_way_id NOT IN (SELECT osm_way_id FROM user_task WHERE guid = "A37CA11D-5D72-97CD-3312-8E6D288C572S");
