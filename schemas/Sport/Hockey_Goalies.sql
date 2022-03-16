-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: Hockey
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
-- Table structure for table `Goalies`
--

DROP TABLE IF EXISTS `Goalies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Goalies` (
  `playerID` varchar(255) NOT NULL,
  `year` int(11) NOT NULL,
  `stint` int(11) NOT NULL,
  `tmID` varchar(255) DEFAULT NULL,
  `lgID` varchar(255) DEFAULT NULL,
  `GP` varchar(255) DEFAULT NULL,
  `Min` varchar(255) DEFAULT NULL,
  `W` varchar(255) DEFAULT NULL,
  `L` varchar(255) DEFAULT NULL,
  `T/OL` varchar(255) DEFAULT NULL,
  `ENG` varchar(255) DEFAULT NULL,
  `SHO` varchar(255) DEFAULT NULL,
  `GA` varchar(255) DEFAULT NULL,
  `SA` varchar(255) DEFAULT NULL,
  `PostGP` varchar(255) DEFAULT NULL,
  `PostMin` varchar(255) DEFAULT NULL,
  `PostW` varchar(255) DEFAULT NULL,
  `PostL` varchar(255) DEFAULT NULL,
  `PostT` varchar(255) DEFAULT NULL,
  `PostENG` varchar(255) DEFAULT NULL,
  `PostSHO` varchar(255) DEFAULT NULL,
  `PostGA` varchar(255) DEFAULT NULL,
  `PostSA` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`playerID`,`year`,`stint`),
  KEY `Goalies_year_tmID` (`year`,`tmID`) USING BTREE,
  CONSTRAINT `Goalies_ibfk_1` FOREIGN KEY (`playerID`) REFERENCES `Master` (`playerID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Goalies_ibfk_2` FOREIGN KEY (`year`, `tmID`) REFERENCES `Teams` (`year`, `tmID`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 19:46:29
