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
-- Table structure for table `TeamSplits`
--

DROP TABLE IF EXISTS `TeamSplits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TeamSplits` (
  `year` int(11) NOT NULL,
  `lgID` varchar(255) DEFAULT NULL,
  `tmID` varchar(255) NOT NULL,
  `hW` int(11) DEFAULT NULL,
  `hL` int(11) DEFAULT NULL,
  `hT` int(11) DEFAULT NULL,
  `hOTL` varchar(255) DEFAULT NULL,
  `rW` int(11) DEFAULT NULL,
  `rL` int(11) DEFAULT NULL,
  `rT` int(11) DEFAULT NULL,
  `rOTL` varchar(255) DEFAULT NULL,
  `SepW` varchar(255) DEFAULT NULL,
  `SepL` varchar(255) DEFAULT NULL,
  `SepT` varchar(255) DEFAULT NULL,
  `SepOL` varchar(255) DEFAULT NULL,
  `OctW` varchar(255) DEFAULT NULL,
  `OctL` varchar(255) DEFAULT NULL,
  `OctT` varchar(255) DEFAULT NULL,
  `OctOL` varchar(255) DEFAULT NULL,
  `NovW` varchar(255) DEFAULT NULL,
  `NovL` varchar(255) DEFAULT NULL,
  `NovT` varchar(255) DEFAULT NULL,
  `NovOL` varchar(255) DEFAULT NULL,
  `DecW` varchar(255) DEFAULT NULL,
  `DecL` varchar(255) DEFAULT NULL,
  `DecT` varchar(255) DEFAULT NULL,
  `DecOL` varchar(255) DEFAULT NULL,
  `JanW` int(11) DEFAULT NULL,
  `JanL` int(11) DEFAULT NULL,
  `JanT` int(11) DEFAULT NULL,
  `JanOL` varchar(255) DEFAULT NULL,
  `FebW` int(11) DEFAULT NULL,
  `FebL` int(11) DEFAULT NULL,
  `FebT` int(11) DEFAULT NULL,
  `FebOL` varchar(255) DEFAULT NULL,
  `MarW` varchar(255) DEFAULT NULL,
  `MarL` varchar(255) DEFAULT NULL,
  `MarT` varchar(255) DEFAULT NULL,
  `MarOL` varchar(255) DEFAULT NULL,
  `AprW` varchar(255) DEFAULT NULL,
  `AprL` varchar(255) DEFAULT NULL,
  `AprT` varchar(255) DEFAULT NULL,
  `AprOL` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`year`,`tmID`),
  KEY `TeamSplits_year` (`year`) USING BTREE,
  CONSTRAINT `TeamSplits_ibfk_1` FOREIGN KEY (`year`, `tmID`) REFERENCES `Teams` (`year`, `tmID`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 19:46:39
