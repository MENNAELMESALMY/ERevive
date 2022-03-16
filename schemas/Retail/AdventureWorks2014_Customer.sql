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
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `CustomerID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key.',
  `PersonID` int(11) DEFAULT NULL COMMENT 'Foreign key to Person.BusinessEntityID',
  `StoreID` int(11) DEFAULT NULL COMMENT 'Foreign key to Store.BusinessEntityID',
  `TerritoryID` int(11) DEFAULT NULL COMMENT 'ID of the territory in which the customer is located. Foreign key to SalesTerritory.SalesTerritoryID.',
  `AccountNumber` varchar(10) NOT NULL COMMENT 'Unique number identifying the customer assigned by the accounting system.',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`CustomerID`),
  UNIQUE KEY `AK_Customer_rowguid` (`rowguid`),
  UNIQUE KEY `AK_Customer_AccountNumber` (`AccountNumber`),
  KEY `IX_Customer_TerritoryID` (`TerritoryID`),
  KEY `FK_Customer_Person_PersonID` (`PersonID`),
  KEY `FK_Customer_Store_StoreID` (`StoreID`),
  KEY `GUID_Customer` (`rowguid`),
  CONSTRAINT `FK_Customer_Person_PersonID` FOREIGN KEY (`PersonID`) REFERENCES `Person` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_Customer_SalesTerritory_TerritoryID` FOREIGN KEY (`TerritoryID`) REFERENCES `SalesTerritory` (`TerritoryID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_Customer_Store_StoreID` FOREIGN KEY (`StoreID`) REFERENCES `Store` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30119 DEFAULT CHARSET=utf8 COMMENT='Current customer information. Also see the Person and Store tables.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:32:29
