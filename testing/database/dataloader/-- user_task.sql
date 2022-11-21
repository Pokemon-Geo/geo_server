DROP TABLE IF EXISTS `user_task`;

CREATE TABLE `user_task` (  
  `osm_way_id` mediumint NOT NULL,
  `guid` varchar(36) NOT NULL,
  `photo_id` varchar(64) NOT NULL,
  `taken_at` datetime NOT NULL,
  `user_category` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`guid`, `osm_way_id`),
  FOREIGN KEy (`osm_way_id`) REFERENCES `issues` (`osm_way_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`guid`) REFERENCES `user` (`guid`) ON DELETE CASCADE ON UPDATE CASCADE
);
