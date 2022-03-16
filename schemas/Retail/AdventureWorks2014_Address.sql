-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: AdventureWorks2014
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
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Address` (
  `AddressID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key for Address records.',
  `AddressLine1` varchar(60) NOT NULL COMMENT 'First street address line.',
  `AddressLine2` varchar(60) DEFAULT NULL COMMENT 'Second street address line.',
  `City` varchar(30) NOT NULL COMMENT 'Name of the city.',
  `StateProvinceID` int(11) NOT NULL COMMENT 'Unique identification number for the state or province. Foreign key to StateProvince table.',
  `PostalCode` varchar(15) NOT NULL COMMENT 'Postal code for the street address.',
  `SpatialLocation` geometry DEFAULT NULL COMMENT 'Latitude and longitude of this address.',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`AddressID`),
  UNIQUE KEY `AK_Address_rowguid` (`rowguid`),
  UNIQUE KEY `IX_Address_AddressLine1_AddressLine2_City_StateProvinceID_Post1` (`AddressLine1`,`AddressLine2`,`City`,`StateProvinceID`,`PostalCode`),
  KEY `IX_Address_StateProvinceID` (`StateProvinceID`),
  KEY `GUID_Address` (`rowguid`),
  CONSTRAINT `FK_Address_StateProvince_StateProvinceID` FOREIGN KEY (`StateProvinceID`) REFERENCES `StateProvince` (`StateProvinceID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=32522 DEFAULT CHARSET=utf8 COMMENT='Street address information for customers, employees, and vendors.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:32:15
