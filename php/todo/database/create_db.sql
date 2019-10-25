CREATE DATABASE `todo_dev` /*!40100 DEFAULT CHARACTER SET utf8 */;

CREATE TABLE `tasks`
(
  `id` int
(11) NOT NULL AUTO_INCREMENT,
  `title` varchar
(100) NOT NULL,
  `description` varchar
(45) DEFAULT NULL,
  PRIMARY KEY
(`id`),
  UNIQUE KEY `id_UNIQUE`
(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

