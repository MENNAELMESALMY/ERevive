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
-- Table structure for table `PurchaseOrderHeader`
--

DROP TABLE IF EXISTS `PurchaseOrderHeader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PurchaseOrderHeader` (
  `PurchaseOrderID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key.',
  `RevisionNumber` tinyint(3) unsigned NOT NULL DEFAULT 0 COMMENT 'Incremental number to track changes to the purchase order over time.',
  `Status` tinyint(3) unsigned NOT NULL DEFAULT 1 COMMENT 'Order current status. 1 = Pending; 2 = Approved; 3 = Rejected; 4 = Complete',
  `EmployeeID` int(11) NOT NULL COMMENT 'Employee who created the purchase order. Foreign key to Employee.BusinessEntityID.',
  `VendorID` int(11) NOT NULL COMMENT 'Vendor with whom the purchase order is placed. Foreign key to Vendor.BusinessEntityID.',
  `ShipMethodID` int(11) NOT NULL COMMENT 'Shipping method. Foreign key to ShipMethod.ShipMethodID.',
  `OrderDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Purchase order creation date.',
  `ShipDate` datetime DEFAULT NULL COMMENT 'Estimated shipment date from the vendor.',
  `SubTotal` decimal(19,4) NOT NULL DEFAULT 0.0000 COMMENT 'Purchase order subtotal. Computed as SUM(PurchaseOrderDetail.LineTotal)for the appropriate PurchaseOrderID.',
  `TaxAmt` decimal(19,4) NOT NULL DEFAULT 0.0000 COMMENT 'Tax amount.',
  `Freight` decimal(19,4) NOT NULL DEFAULT 0.0000 COMMENT 'Shipping cost.',
  `TotalDue` decimal(19,4) NOT NULL COMMENT 'Total due to vendor. Computed as Subtotal + TaxAmt + Freight.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`PurchaseOrderID`),
  KEY `IX_PurchaseOrderHeader_VendorID` (`VendorID`),
  KEY `IX_PurchaseOrderHeader_EmployeeID` (`EmployeeID`),
  KEY `FK_PurchaseOrderHeader_ShipMethod_ShipMethodID` (`ShipMethodID`),
  CONSTRAINT `FK_PurchaseOrderHeader_Employee_EmployeeID` FOREIGN KEY (`EmployeeID`) REFERENCES `Employee` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_PurchaseOrderHeader_ShipMethod_ShipMethodID` FOREIGN KEY (`ShipMethodID`) REFERENCES `ShipMethod` (`ShipMethodID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_PurchaseOrderHeader_Vendor_VendorID` FOREIGN KEY (`VendorID`) REFERENCES `Vendor` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4013 DEFAULT CHARSET=utf8 COMMENT='General purchase order information. See PurchaseOrderDetail.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:31:06
