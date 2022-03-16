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
-- Table structure for table `ProductVendor`
--

DROP TABLE IF EXISTS `ProductVendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProductVendor` (
  `ProductID` int(11) NOT NULL COMMENT 'Primary key. Foreign key to Product.ProductID.',
  `BusinessEntityID` int(11) NOT NULL COMMENT 'Primary key. Foreign key to Vendor.BusinessEntityID.',
  `AverageLeadTime` int(11) NOT NULL COMMENT 'The average span of time (in days) between placing an order with the vendor and receiving the purchased product.',
  `StandardPrice` decimal(19,4) NOT NULL COMMENT 'The vendor''s usual selling price.',
  `LastReceiptCost` decimal(19,4) DEFAULT NULL COMMENT 'The selling price when last purchased.',
  `LastReceiptDate` datetime DEFAULT NULL COMMENT 'Date the product was last received by the vendor.',
  `MinOrderQty` int(11) NOT NULL COMMENT 'The maximum quantity that should be ordered.',
  `MaxOrderQty` int(11) NOT NULL COMMENT 'The minimum quantity that should be ordered.',
  `OnOrderQty` int(11) DEFAULT NULL COMMENT 'The quantity currently on order.',
  `UnitMeasureCode` char(3) NOT NULL COMMENT 'The product''s unit of measure.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`ProductID`,`BusinessEntityID`),
  KEY `IX_ProductVendor_UnitMeasureCode` (`UnitMeasureCode`),
  KEY `IX_ProductVendor_BusinessEntityID` (`BusinessEntityID`),
  CONSTRAINT `FK_ProductVendor_Product_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `Product` (`ProductID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_ProductVendor_UnitMeasure_UnitMeasureCode` FOREIGN KEY (`UnitMeasureCode`) REFERENCES `UnitMeasure` (`UnitMeasureCode`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_ProductVendor_Vendor_BusinessEntityID` FOREIGN KEY (`BusinessEntityID`) REFERENCES `Vendor` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Cross-reference table mapping vendors with the products they supply.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:30:35
