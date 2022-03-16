-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: ErgastF1
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
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `results` (
  `resultId` int(11) NOT NULL AUTO_INCREMENT,
  `raceId` int(11) NOT NULL DEFAULT 0,
  `driverId` int(11) NOT NULL DEFAULT 0,
  `constructorId` int(11) NOT NULL DEFAULT 0,
  `number` int(11) DEFAULT NULL,
  `grid` int(11) NOT NULL DEFAULT 0,
  `position` int(11) DEFAULT NULL,
  `positionText` varchar(255) NOT NULL DEFAULT '',
  `positionOrder` int(11) NOT NULL DEFAULT 0,
  `points` float NOT NULL DEFAULT 0,
  `laps` int(11) NOT NULL DEFAULT 0,
  `time` varchar(255) DEFAULT NULL,
  `milliseconds` int(11) DEFAULT NULL,
  `fastestLap` int(11) DEFAULT NULL,
  `rank` int(11) DEFAULT 0,
  `fastestLapTime` varchar(255) DEFAULT NULL,
  `fastestLapSpeed` varchar(255) DEFAULT NULL,
  `statusId` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`resultId`),
  KEY `constructorId` (`constructorId`),
  KEY `driverId` (`driverId`),
  KEY `statusId` (`statusId`),
  KEY `raceId` (`raceId`),
  CONSTRAINT `results_ibfk_1` FOREIGN KEY (`constructorId`) REFERENCES `constructors` (`constructorId`),
  CONSTRAINT `results_ibfk_2` FOREIGN KEY (`driverId`) REFERENCES `drivers` (`driverId`),
  CONSTRAINT `results_ibfk_3` FOREIGN KEY (`statusId`) REFERENCES `status` (`statusId`),
  CONSTRAINT `results_ibfk_4` FOREIGN KEY (`raceId`) REFERENCES `races` (`raceId`)
) ENGINE=InnoDB AUTO_INCREMENT=23662 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:45:45
