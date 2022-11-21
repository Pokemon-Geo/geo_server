DROP TABLE IF EXISTS `issues`;

CREATE TABLE `issues` (  
  `osm_way_id` mediumint default NULL,
  `image_id` mediumint NOT NULL,
  `lat` varchar(30) default NULL,
  `lng` varchar(30) default NULL,
  `points` mediumint default NULL,
  PRIMARY KEY (`osm_way_id`)
);

INSERT INTO `issues` (`osm_way_id`, `image_id`, `lat`,`lng`,`points`)
VALUES
  (998466140, 777394979647773, "11.666603","48.265283",100),
  (22757935, 1777883682416299, "11.668844378278436","48.262945675200626",100),
  (30275349, 738137103547425, "11.670989","48.264445",100),
  (476948281, 866020890615760, "11.670317","48.261969",100),
  (392233418, 364290981677816, "11.67101","48.266888",100);