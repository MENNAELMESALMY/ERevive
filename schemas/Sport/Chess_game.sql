-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: Chess
-- ------------------------------------------------------
-- Server version	5.5.5-10.3.15-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game` (
  `game_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `opening_id` int(10) DEFAULT NULL,
  `event` text COLLATE utf8_bin DEFAULT NULL,
  `site` text COLLATE utf8_bin DEFAULT NULL,
  `event_date` date DEFAULT NULL,
  `round` text COLLATE utf8_bin DEFAULT NULL,
  `white` text COLLATE utf8_bin DEFAULT NULL,
  `black` text COLLATE utf8_bin DEFAULT NULL,
  `game_result` text COLLATE utf8_bin DEFAULT NULL,
  `ECO` text COLLATE utf8_bin DEFAULT NULL,
  `whiteElo` int(10) DEFAULT NULL,
  `BlackElo` int(10) DEFAULT NULL,
  `opening` text COLLATE utf8_bin DEFAULT NULL,
  `w1` text COLLATE utf8_bin DEFAULT NULL,
  `b1` text COLLATE utf8_bin DEFAULT NULL,
  `w2` text COLLATE utf8_bin DEFAULT NULL,
  `b2` text COLLATE utf8_bin DEFAULT NULL,
  `w3` text COLLATE utf8_bin DEFAULT NULL,
  `b3` text COLLATE utf8_bin DEFAULT NULL,
  `w4` text COLLATE utf8_bin DEFAULT NULL,
  `b4` text COLLATE utf8_bin DEFAULT NULL,
  `w5` text COLLATE utf8_bin DEFAULT NULL,
  `b5` text COLLATE utf8_bin DEFAULT NULL,
  `w6` text COLLATE utf8_bin DEFAULT NULL,
  `b6` text COLLATE utf8_bin DEFAULT NULL,
  `w7` text COLLATE utf8_bin DEFAULT NULL,
  `b7` text COLLATE utf8_bin DEFAULT NULL,
  `w8` text COLLATE utf8_bin DEFAULT NULL,
  `b8` text COLLATE utf8_bin DEFAULT NULL,
  `w9` text COLLATE utf8_bin DEFAULT NULL,
  `b9` text COLLATE utf8_bin DEFAULT NULL,
  `w10` text COLLATE utf8_bin DEFAULT NULL,
  `b10` text COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`game_id`),
  KEY `opening_id` (`opening_id`),
  CONSTRAINT `game_ibfk_1` FOREIGN KEY (`opening_id`) REFERENCES `opening` (`opening_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=296 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 18:25:13
