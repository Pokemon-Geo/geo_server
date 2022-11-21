DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (  
  `guid` varchar(36) NOT NULL,
  `name` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `level` mediumint default NULL,
  `points` mediumint default NULL,
  `university` varchar(255) default NULL,
  PRIMARY KEY (`guid`)
)

INSERT INTO `users` (`guid`,`name`,`email`,`level`,`points`,`university`)
VALUES
  ("187FA962-49BD-E762-E114-23C4AF27276C","Cyrus Casey","molestie@hotmail.edu",0,3500, "Free University Bozen"),
  ("BA16CE3F-1BE4-274E-C449-E213CEEA8A56","Evangeline Keith","purus.duis@yahoo.net",0,1800, "Free University Bozen"),
  ("CCB60E1E-7ED3-165A-E823-B256CE1176D9","Unity Frye","ac.facilisis@icloud.edu",0,2400, "Free University Bozen"),
  ("BB27AB1C-28ED-E383-9418-1A67E5A71F90","Keegan Diaz","integer.urna@hotmail.org",0,0, "Free University Bozen"),
  ("A37CA11D-5D72-97CD-3312-8E6D288C572E","Lydia Stone","luctus.ut.pellentesque@aol.org",0,60, "TUM"),
  ("A37CA11D-5D72-97CD-3312-8E6D288C572S","Sebastian Cavada","seb@dev.com",0,5400, "TUM"),
  ("BB27AB1C-28ED-1231-9418-1A67E5A71F90","Jakob Eigenmann","eigen.boolean@me.org",0,4000, "TUM"),
  ("BB27AB1C-28ED-6789-9418-1A67E5A71F90","Fabian Nahn","fabian.de@hotmail.org",0,4200,"TUM"),
  ("BB27AB1C-1234-E383-9418-1A67E5A71F90","Gabriel Kuznik","gabriel.yay@tum.org",0,7630, "TUM");


UPDATE `users` SET `points` = 1800 WHERE `guid` = "A37CA11D-5D72-97CD-3312-8E6D288C572S";