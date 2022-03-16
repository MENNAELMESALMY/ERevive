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
-- Table structure for table `PurchaseOrderDetail`
--

DROP TABLE IF EXISTS `PurchaseOrderDetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PurchaseOrderDetail` (
  `PurchaseOrderID` int(11) NOT NULL COMMENT 'Primary key. Foreign key to PurchaseOrderHeader.PurchaseOrderID.',
  `PurchaseOrderDetailID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key. One line number per purchased product.',
  `DueDate` datetime NOT NULL COMMENT 'Date the product is expected to be received.',
  `OrderQty` smallint(6) NOT NULL COMMENT 'Quantity ordered.',
  `ProductID` int(11) NOT NULL COMMENT 'Product identification number. Foreign key to Product.ProductID.',
  `UnitPrice` decimal(19,4) NOT NULL COMMENT 'Vendor''s selling price of a single product.',
  `LineTotal` decimal(19,4) NOT NULL COMMENT 'Per product subtotal. Computed as OrderQty * UnitPrice.',
  `ReceivedQty` decimal(8,2) NOT NULL COMMENT 'Quantity actually received from the vendor.',
  `RejectedQty` decimal(8,2) NOT NULL COMMENT 'Quantity rejected during inspection.',
  `StockedQty` decimal(9,2) NOT NULL COMMENT 'Quantity accepted into inventory. Computed as ReceivedQty - RejectedQty.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`PurchaseOrderDetailID`,`PurchaseOrderID`),
  KEY `IX_PurchaseOrderDetail_ProductID` (`ProductID`),
  KEY `FK_PurchaseOrderDetail_PurchaseOrderHeader_PurchaseOrderID` (`PurchaseOrderID`),
  CONSTRAINT `FK_PurchaseOrderDetail_Product_ProductID` FOREIGN KEY (`ProductID`) REFERENCES `Product` (`ProductID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_PurchaseOrderDetail_PurchaseOrderHeader_PurchaseOrderID` FOREIGN KEY (`PurchaseOrderID`) REFERENCES `PurchaseOrderHeader` (`PurchaseOrderID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8846 DEFAULT CHARSET=utf8 COMMENT='Individual products associated with a specific purchase order. See PurchaseOrderHeader.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:30:09
