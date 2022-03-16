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
-- Table structure for table `StateProvince`
--

DROP TABLE IF EXISTS `StateProvince`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StateProvince` (
  `StateProvinceID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key for StateProvince records.',
  `StateProvinceCode` char(3) NOT NULL COMMENT 'ISO standard state or province code.',
  `CountryRegionCode` varchar(3) NOT NULL COMMENT 'ISO standard country or region code. Foreign key to CountryRegion.CountryRegionCode. ',
  `IsOnlyStateProvinceFlag` tinyint(1) NOT NULL DEFAULT 1 COMMENT '0 = StateProvinceCode exists. 1 = StateProvinceCode unavailable, using CountryRegionCode.',
  `Name` varchar(100) NOT NULL COMMENT 'State or province description.',
  `TerritoryID` int(11) NOT NULL COMMENT 'ID of the territory in which the state or province is located. Foreign key to SalesTerritory.SalesTerritoryID.',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`StateProvinceID`),
  UNIQUE KEY `AK_StateProvince_Name` (`Name`),
  UNIQUE KEY `AK_StateProvince_StateProvinceCode_CountryRegionCode` (`StateProvinceCode`,`CountryRegionCode`),
  UNIQUE KEY `AK_StateProvince_rowguid` (`rowguid`),
  KEY `FK_StateProvince_CountryRegion_CountryRegionCode` (`CountryRegionCode`),
  KEY `FK_StateProvince_SalesTerritory_TerritoryID` (`TerritoryID`),
  KEY `GUID_StateProvince` (`rowguid`),
  CONSTRAINT `FK_StateProvince_CountryRegion_CountryRegionCode` FOREIGN KEY (`CountryRegionCode`) REFERENCES `CountryRegion` (`CountryRegionCode`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_StateProvince_SalesTerritory_TerritoryID` FOREIGN KEY (`TerritoryID`) REFERENCES `SalesTerritory` (`TerritoryID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=182 DEFAULT CHARSET=utf8 COMMENT='State and province lookup table.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:30:40
