-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: Mondial
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
-- Table structure for table `river`
--

DROP TABLE IF EXISTS `river`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `river` (
  `Name` varchar(35) NOT NULL DEFAULT '',
  `River` varchar(35) DEFAULT NULL,
  `Lake` varchar(35) DEFAULT NULL,
  `Sea` varchar(35) DEFAULT NULL,
  `Length` float DEFAULT NULL,
  `SourceLongitude` float DEFAULT NULL,
  `SourceLatitude` float DEFAULT NULL,
  `Mountains` varchar(35) DEFAULT NULL,
  `SourceAltitude` float DEFAULT NULL,
  `EstuaryLongitude` float DEFAULT NULL,
  `EstuaryLatitude` float DEFAULT NULL,
  PRIMARY KEY (`Name`),
  KEY `ix_river_Lake` (`Lake`) USING BTREE,
  KEY `ix_river_River` (`River`) USING BTREE,
  KEY `ix_river_Sea` (`Sea`) USING BTREE,
  KEY `ix_river_Mountains` (`Mountains`) USING BTREE,
  CONSTRAINT `river_ibfk_1` FOREIGN KEY (`Lake`) REFERENCES `lake` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 20:37:24
