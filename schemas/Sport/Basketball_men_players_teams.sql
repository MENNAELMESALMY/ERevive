-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: Basketball_men
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
-- Table structure for table `players_teams`
--

DROP TABLE IF EXISTS `players_teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players_teams` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `playerID` varchar(255) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `stint` int(11) DEFAULT NULL,
  `tmID` varchar(255) DEFAULT NULL,
  `lgID` varchar(255) DEFAULT NULL,
  `GP` int(11) DEFAULT NULL,
  `GS` int(11) DEFAULT NULL,
  `minutes` int(11) DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `oRebounds` int(11) DEFAULT NULL,
  `dRebounds` int(11) DEFAULT NULL,
  `rebounds` int(11) DEFAULT NULL,
  `assists` int(11) DEFAULT NULL,
  `steals` int(11) DEFAULT NULL,
  `blocks` int(11) DEFAULT NULL,
  `turnovers` int(11) DEFAULT NULL,
  `PF` int(11) DEFAULT NULL,
  `fgAttempted` int(11) DEFAULT NULL,
  `fgMade` int(11) DEFAULT NULL,
  `ftAttempted` int(11) DEFAULT NULL,
  `ftMade` int(11) DEFAULT NULL,
  `threeAttempted` int(11) DEFAULT NULL,
  `threeMade` int(11) DEFAULT NULL,
  `PostGP` int(11) DEFAULT NULL,
  `PostGS` int(11) DEFAULT NULL,
  `PostMinutes` int(11) DEFAULT NULL,
  `PostPoints` int(11) DEFAULT NULL,
  `PostoRebounds` int(11) DEFAULT NULL,
  `PostdRebounds` int(11) DEFAULT NULL,
  `PostRebounds` int(11) DEFAULT NULL,
  `PostAssists` int(11) DEFAULT NULL,
  `PostSteals` int(11) DEFAULT NULL,
  `PostBlocks` int(11) DEFAULT NULL,
  `PostTurnovers` int(11) DEFAULT NULL,
  `PostPF` int(11) DEFAULT NULL,
  `PostfgAttempted` int(11) DEFAULT NULL,
  `PostfgMade` int(11) DEFAULT NULL,
  `PostftAttempted` int(11) DEFAULT NULL,
  `PostftMade` int(11) DEFAULT NULL,
  `PostthreeAttempted` int(11) DEFAULT NULL,
  `PostthreeMade` int(11) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `playerID` (`playerID`),
  KEY `year` (`year`,`tmID`),
  KEY `tmID` (`tmID`,`year`),
  KEY `tmID_2` (`tmID`,`year`),
  KEY `tmID_3` (`tmID`,`year`),
  KEY `fgAttempted` (`fgAttempted`),
  KEY `fgAttempted_2` (`fgAttempted`),
  CONSTRAINT `players_teams_ibfk_1` FOREIGN KEY (`playerID`) REFERENCES `players` (`playerID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `players_teams_ibfk_2` FOREIGN KEY (`tmID`, `year`) REFERENCES `teams` (`tmID`, `year`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23752 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:44:10
