-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: CDESchools
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
-- Table structure for table `schools`
--

DROP TABLE IF EXISTS `schools`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schools` (
  `CDSCode` varchar(14) NOT NULL,
  `NCESDist` varchar(7) DEFAULT NULL,
  `NCESSchool` varchar(5) DEFAULT NULL,
  `StatusType` varchar(7) NOT NULL,
  `County` varchar(15) NOT NULL,
  `District` varchar(74) NOT NULL,
  `School` varchar(89) DEFAULT NULL,
  `Street` varchar(62) DEFAULT NULL,
  `StreetAbr` varchar(59) DEFAULT NULL,
  `City` varchar(25) DEFAULT NULL,
  `Zip` varchar(10) DEFAULT NULL,
  `State` varchar(4) DEFAULT NULL,
  `MailStreet` varchar(70) DEFAULT NULL,
  `MailStrAbr` varchar(70) DEFAULT NULL,
  `MailCity` varchar(22) DEFAULT NULL,
  `MailZip` varchar(10) DEFAULT NULL,
  `MailState` varchar(4) DEFAULT NULL,
  `Phone` varchar(14) DEFAULT NULL,
  `Ext` varchar(6) DEFAULT NULL,
  `Website` varchar(96) DEFAULT NULL,
  `OpenDate` date DEFAULT NULL,
  `ClosedDate` date DEFAULT NULL,
  `Charter` smallint(6) DEFAULT NULL,
  `CharterNum` varchar(4) DEFAULT NULL,
  `FundingType` varchar(23) DEFAULT NULL,
  `DOC` varchar(2) NOT NULL,
  `DOCType` varchar(42) NOT NULL,
  `SOC` varchar(4) DEFAULT NULL,
  `SOCType` varchar(41) DEFAULT NULL,
  `EdOpsCode` varchar(7) DEFAULT NULL,
  `EdOpsName` varchar(43) DEFAULT NULL,
  `EILCode` varchar(8) DEFAULT NULL,
  `EILName` varchar(31) DEFAULT NULL,
  `GSoffered` varchar(16) DEFAULT NULL,
  `GSserved` varchar(5) DEFAULT NULL,
  `Virtual` varchar(4) DEFAULT NULL,
  `Magnet` smallint(6) DEFAULT NULL,
  `Latitude` double DEFAULT NULL,
  `Longitude` double DEFAULT NULL,
  `AdmFName1` varchar(17) DEFAULT NULL,
  `AdmLName1` varchar(22) DEFAULT NULL,
  `AdmEmail1` varchar(49) DEFAULT NULL,
  `AdmFName2` varchar(15) DEFAULT NULL,
  `AdmLName2` varchar(18) DEFAULT NULL,
  `AdmEmail2` varchar(40) DEFAULT NULL,
  `AdmFName3` varchar(8) DEFAULT NULL,
  `AdmLName3` varchar(15) DEFAULT NULL,
  `AdmEmail3` varchar(39) DEFAULT NULL,
  `LastUpdate` date NOT NULL,
  PRIMARY KEY (`CDSCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 18:40:29
