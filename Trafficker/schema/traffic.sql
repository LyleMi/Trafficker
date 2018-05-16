DROP DATABASE IF EXISTS traffic;

CREATE DATABASE `traffic` DEFAULT CHARACTER SET utf8 collate utf8_general_ci;

USE traffic;

CREATE TABLE `flow` (
  `id` INT AUTO_INCREMENT,
  `pcapName` VARCHAR(100) NULL,
  `packetNum` INT NOT NULL,
  `data` BLOB NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE USER 'traffic'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, UPDATE, DELETE ON traffic.flow TO 'traffic'@'localhost';
