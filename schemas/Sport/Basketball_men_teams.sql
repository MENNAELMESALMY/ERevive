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
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teams` (
  `year` int(11) NOT NULL,
  `lgID` varchar(255) DEFAULT NULL,
  `tmID` varchar(255) NOT NULL,
  `franchID` varchar(255) DEFAULT NULL,
  `confID` varchar(255) DEFAULT NULL,
  `divID` varchar(255) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  `confRank` int(11) DEFAULT NULL,
  `playoff` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `o_fgm` int(11) DEFAULT NULL,
  `o_fga` int(11) DEFAULT NULL,
  `o_ftm` int(11) DEFAULT NULL,
  `o_fta` int(11) DEFAULT NULL,
  `o_3pm` int(11) DEFAULT NULL,
  `o_3pa` int(11) DEFAULT NULL,
  `o_oreb` int(11) DEFAULT NULL,
  `o_dreb` int(11) DEFAULT NULL,
  `o_reb` int(11) DEFAULT NULL,
  `o_asts` int(11) DEFAULT NULL,
  `o_pf` int(11) DEFAULT NULL,
  `o_stl` int(11) DEFAULT NULL,
  `o_to` int(11) DEFAULT NULL,
  `o_blk` int(11) DEFAULT NULL,
  `o_pts` int(11) DEFAULT NULL,
  `d_fgm` int(11) DEFAULT NULL,
  `d_fga` int(11) DEFAULT NULL,
  `d_ftm` int(11) DEFAULT NULL,
  `d_fta` int(11) DEFAULT NULL,
  `d_3pm` int(11) DEFAULT NULL,
  `d_3pa` int(11) DEFAULT NULL,
  `d_oreb` int(11) DEFAULT NULL,
  `d_dreb` int(11) DEFAULT NULL,
  `d_reb` int(11) DEFAULT NULL,
  `d_asts` int(11) DEFAULT NULL,
  `d_pf` int(11) DEFAULT NULL,
  `d_stl` int(11) DEFAULT NULL,
  `d_to` int(11) DEFAULT NULL,
  `d_blk` int(11) DEFAULT NULL,
  `d_pts` int(11) DEFAULT NULL,
  `o_tmRebound` int(11) DEFAULT NULL,
  `d_tmRebound` int(11) DEFAULT NULL,
  `homeWon` int(11) DEFAULT NULL,
  `homeLost` int(11) DEFAULT NULL,
  `awayWon` int(11) DEFAULT NULL,
  `awayLost` int(11) DEFAULT NULL,
  `neutWon` int(11) DEFAULT NULL,
  `neutLoss` int(11) DEFAULT NULL,
  `confWon` int(11) DEFAULT NULL,
  `confLoss` int(11) DEFAULT NULL,
  `divWon` int(11) DEFAULT NULL,
  `divLoss` int(11) DEFAULT NULL,
  `pace` int(11) DEFAULT NULL,
  `won` int(11) DEFAULT NULL,
  `lost` int(11) DEFAULT NULL,
  `games` int(11) DEFAULT NULL,
  `min` int(11) DEFAULT NULL,
  `arena` varchar(255) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  `bbtmID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`year`,`tmID`),
  KEY `tmID` (`tmID`),
  KEY `tmID_2` (`tmID`,`year`)
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

-- Dump completed on 2022-02-20 19:43:47
