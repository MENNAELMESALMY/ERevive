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
-- Table structure for table `SalesOrderDetail`
--

DROP TABLE IF EXISTS `SalesOrderDetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SalesOrderDetail` (
  `SalesOrderID` int(11) NOT NULL COMMENT 'Primary key. Foreign key to SalesOrderHeader.SalesOrderID.',
  `SalesOrderDetailID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key. One incremental unique number per product sold.',
  `CarrierTrackingNumber` varchar(25) DEFAULT NULL COMMENT 'Shipment tracking number supplied by the shipper.',
  `OrderQty` smallint(6) NOT NULL COMMENT 'Quantity ordered per product.',
  `ProductID` int(11) NOT NULL COMMENT 'Product sold to customer. Foreign key to Product.ProductID.',
  `SpecialOfferID` int(11) NOT NULL COMMENT 'Promotional code. Foreign key to SpecialOffer.SpecialOfferID.',
  `UnitPrice` decimal(19,4) NOT NULL COMMENT 'Selling price of a single product.',
  `UnitPriceDiscount` decimal(19,4) NOT NULL DEFAULT 0.0000 COMMENT 'Discount amount.',
  `LineTotal` decimal(38,6) NOT NULL COMMENT 'Per product subtotal. Computed as UnitPrice * (1 - UnitPriceDiscount) * OrderQty.',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`SalesOrderDetailID`,`SalesOrderID`),
  UNIQUE KEY `AK_SalesOrderDetail_rowguid` (`rowguid`),
  KEY `IX_SalesOrderDetail_ProductID` (`ProductID`),
  KEY `FK_SalesOrderDetail_SalesOrderHeader_SalesOrderID` (`SalesOrderID`),
  KEY `FK_SalesOrderDetail_SpecialOfferProduct_SpecialOfferIDProductID` (`SpecialOfferID`,`ProductID`),
  KEY `GUID_SalesOrderDetail` (`rowguid`),
  CONSTRAINT `FK_SalesOrderDetail_SalesOrderHeader_SalesOrderID` FOREIGN KEY (`SalesOrderID`) REFERENCES `SalesOrderHeader` (`SalesOrderID`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `FK_SalesOrderDetail_SpecialOfferProduct_SpecialOfferIDProductID` FOREIGN KEY (`SpecialOfferID`, `ProductID`) REFERENCES `SpecialOfferProduct` (`SpecialOfferID`, `ProductID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=121318 DEFAULT CHARSET=utf8 COMMENT='Individual products associated with a specific sales order. See SalesOrderHeader.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:31:23
