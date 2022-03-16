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
-- Table structure for table `frpm`
--

DROP TABLE IF EXISTS `frpm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frpm` (
  `CDSCode` varchar(14) NOT NULL,
  `Academic Year` varchar(9) DEFAULT NULL,
  `County Code` varchar(4) DEFAULT NULL,
  `District Code` int(11) DEFAULT NULL,
  `School Code` varchar(7) DEFAULT NULL,
  `County Name` varchar(15) DEFAULT NULL,
  `District Name` varchar(75) DEFAULT NULL,
  `School Name` varchar(85) DEFAULT NULL,
  `District Type` varchar(32) DEFAULT NULL,
  `School Type` varchar(41) DEFAULT NULL,
  `Educational Option Type` varchar(43) DEFAULT NULL,
  `NSLP Provision Status` varchar(24) DEFAULT NULL,
  `Charter School (Y/N)` smallint(6) DEFAULT NULL,
  `Charter School Number` varchar(4) DEFAULT NULL,
  `Charter Funding Type` varchar(23) DEFAULT NULL,
  `IRC` smallint(6) DEFAULT NULL,
  `Low Grade` varchar(5) DEFAULT NULL,
  `High Grade` varchar(14) DEFAULT NULL,
  `Enrollment (K-12)` double DEFAULT NULL,
  `Free Meal Count (K-12)` double DEFAULT NULL,
  `Percent (%) Eligible Free (K-12)` double DEFAULT NULL,
  `FRPM Count (K-12)` double DEFAULT NULL,
  `Percent (%) Eligible FRPM (K-12)` double DEFAULT NULL,
  `Enrollment (Ages 5-17)` double DEFAULT NULL,
  `Free Meal Count (Ages 5-17)` double DEFAULT NULL,
  `Percent (%) Eligible Free (Ages 5-17)` double DEFAULT NULL,
  `FRPM Count (Ages 5-17)` double DEFAULT NULL,
  `Percent (%) Eligible FRPM (Ages 5-17)` double DEFAULT NULL,
  `2013-14 CALPADS Fall 1 Certification Status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`CDSCode`),
  CONSTRAINT `frpm_ibfk_1` FOREIGN KEY (`CDSCode`) REFERENCES `schools` (`CDSCode`)
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

-- Dump completed on 2022-02-20 18:40:31
