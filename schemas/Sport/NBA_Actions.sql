-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: NBA
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
-- Table structure for table `Actions`
--

DROP TABLE IF EXISTS `Actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Actions` (
  `GameId` int(11) NOT NULL,
  `TeamId` int(11) DEFAULT NULL,
  `PlayerId` int(11) NOT NULL,
  `Minutes` int(11) DEFAULT NULL,
  `FieldGoalsMade` int(11) DEFAULT NULL,
  `FieldGoalAttempts` int(11) DEFAULT NULL,
  `3PointsMade` int(11) DEFAULT NULL,
  `3PointAttempts` int(11) DEFAULT NULL,
  `FreeThrowsMade` int(11) DEFAULT NULL,
  `FreeThrowAttempts` int(11) DEFAULT NULL,
  `PlusMinus` int(11) DEFAULT NULL,
  `OffensiveRebounds` int(11) DEFAULT NULL,
  `DefensiveRebounds` int(11) DEFAULT NULL,
  `TotalRebounds` int(11) DEFAULT NULL,
  `Assists` int(11) DEFAULT NULL,
  `PersonalFouls` int(11) DEFAULT NULL,
  `Steals` int(11) DEFAULT NULL,
  `Turnovers` int(11) DEFAULT NULL,
  `BlockedShots` int(11) DEFAULT NULL,
  `BlocksAgainst` int(11) DEFAULT NULL,
  `Points` int(11) DEFAULT NULL,
  `Starter` int(11) DEFAULT NULL,
  PRIMARY KEY (`GameId`,`PlayerId`),
  KEY `GameId_idx` (`GameId`),
  KEY `PlayerId_idx` (`PlayerId`),
  KEY `TeamId_idx` (`TeamId`),
  CONSTRAINT `GameId` FOREIGN KEY (`GameId`) REFERENCES `Game` (`GameId`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `playerId-A` FOREIGN KEY (`PlayerId`) REFERENCES `Player` (`PlayerId`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `teamId_A` FOREIGN KEY (`TeamId`) REFERENCES `Team` (`TeamId`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:35:08
