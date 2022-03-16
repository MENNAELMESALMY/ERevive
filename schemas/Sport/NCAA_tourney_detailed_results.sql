-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: NCAA
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
-- Table structure for table `tourney_detailed_results`
--

DROP TABLE IF EXISTS `tourney_detailed_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tourney_detailed_results` (
  `season` int(11) NOT NULL,
  `daynum` int(11) NOT NULL,
  `wteam` int(11) NOT NULL,
  `wscore` int(11) DEFAULT NULL,
  `lteam` int(11) NOT NULL,
  `lscore` int(11) DEFAULT NULL,
  `wloc` varchar(255) DEFAULT NULL,
  `numot` int(11) DEFAULT NULL,
  `wfgm` int(11) DEFAULT NULL,
  `wfga` int(11) DEFAULT NULL,
  `wfgm3` int(11) DEFAULT NULL,
  `wfga3` int(11) DEFAULT NULL,
  `wftm` int(11) DEFAULT NULL,
  `wfta` int(11) DEFAULT NULL,
  `wor` int(11) DEFAULT NULL,
  `wdr` int(11) DEFAULT NULL,
  `wast` int(11) DEFAULT NULL,
  `wto` int(11) DEFAULT NULL,
  `wstl` int(11) DEFAULT NULL,
  `wblk` int(11) DEFAULT NULL,
  `wpf` int(11) DEFAULT NULL,
  `lfgm` int(11) DEFAULT NULL,
  `lfga` int(11) DEFAULT NULL,
  `lfgm3` int(11) DEFAULT NULL,
  `lfga3` int(11) DEFAULT NULL,
  `lftm` int(11) DEFAULT NULL,
  `lfta` int(11) DEFAULT NULL,
  `lor` int(11) DEFAULT NULL,
  `ldr` int(11) DEFAULT NULL,
  `last` int(11) DEFAULT NULL,
  `lto` int(11) DEFAULT NULL,
  `lstl` int(11) DEFAULT NULL,
  `lblk` int(11) DEFAULT NULL,
  `lpf` int(11) DEFAULT NULL,
  PRIMARY KEY (`season`,`daynum`,`wteam`,`lteam`),
  KEY `detailed_season` (`season`) USING BTREE,
  KEY `detailed_wteam` (`wteam`) USING BTREE,
  KEY `detailed_lteam` (`lteam`) USING BTREE,
  CONSTRAINT `tourney_detailed_results_ibfk_1` FOREIGN KEY (`season`) REFERENCES `seasons` (`season`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tourney_detailed_results_ibfk_2` FOREIGN KEY (`wteam`) REFERENCES `teams` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tourney_detailed_results_ibfk_3` FOREIGN KEY (`lteam`) REFERENCES `teams` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 18:16:29
