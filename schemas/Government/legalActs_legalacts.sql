-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: legalActs
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
-- Table structure for table `legalacts`
--

DROP TABLE IF EXISTS `legalacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `legalacts` (
  `id` int(11) NOT NULL,
  `hash` char(32) NOT NULL,
  `update` timestamp NOT NULL DEFAULT current_timestamp(),
  `Court` varchar(100) DEFAULT NULL,
  `CaseKind` varchar(50) DEFAULT NULL,
  `CaseNumber` smallint(6) DEFAULT NULL,
  `ActYear` smallint(6) DEFAULT NULL,
  `Judge` varchar(255) DEFAULT NULL,
  `ActKind` varchar(20) DEFAULT NULL,
  `ActNumber` smallint(6) DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `LegalDate` date DEFAULT NULL,
  `Status` varchar(20) DEFAULT NULL,
  `ActLink` tinyint(1) NOT NULL DEFAULT 0,
  `MotiveDate` date DEFAULT NULL,
  `MotiveLink` tinyint(1) NOT NULL DEFAULT 0,
  `HighCourt` varchar(100) DEFAULT NULL,
  `OutNumber` smallint(6) DEFAULT NULL,
  `YearHigherCourt` smallint(6) DEFAULT NULL,
  `TypeOfDocument` varchar(100) DEFAULT NULL,
  `SendDate` date DEFAULT NULL,
  `ResultOfAppeal` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
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

-- Dump completed on 2022-02-20 19:56:24
