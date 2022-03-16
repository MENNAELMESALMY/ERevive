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
-- Table structure for table `SalesOrderHeader`
--

DROP TABLE IF EXISTS `SalesOrderHeader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SalesOrderHeader` (
  `SalesOrderID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key.',
  `RevisionNumber` tinyint(3) unsigned NOT NULL DEFAULT 0 COMMENT 'Incremental number to track changes to the sales order over time.',
  `OrderDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Dates the sales order was created.',
  `DueDate` datetime NOT NULL COMMENT 'Date the order is due to the customer.',
  `ShipDate` datetime DEFAULT NULL COMMENT 'Date the order was shipped to the customer.',
  `Status` tinyint(3) unsigned NOT NULL DEFAULT 1 COMMENT 'Order current status. 1 = In process; 2 = Approved; 3 = Backordered; 4 = Rejected; 5 = Shipped; 6 = Cancelled',
  `OnlineOrderFlag` tinyint(1) NOT NULL DEFAULT 1 COMMENT '0 = Order placed by sales person. 1 = Order placed online by customer.',
  `SalesOrderNumber` varchar(25) NOT NULL COMMENT 'Unique sales order identification number.',
  `PurchaseOrderNumber` varchar(50) DEFAULT NULL COMMENT 'Customer purchase order number reference. ',
  `AccountNumber` varchar(30) DEFAULT NULL COMMENT 'Financial accounting number reference.',
  `CustomerID` int(11) NOT NULL COMMENT 'Customer identification number. Foreign key to Customer.BusinessEntityID.',
  `SalesPersonID` int(11) DEFAULT NULL COMMENT 'Sales person who created the sales order. Foreign key to SalesPerson.BusinessEntityID.',
  `TerritoryID` int(11) DEFAULT NULL COMMENT 'Territory in which the sale was made. Foreign key to SalesTerritory.SalesTerritoryID.',
  `BillToAddressID` int(11) NOT NULL COMMENT 'Customer billing address. Foreign key to Address.AddressID.',
  `ShipToAddressID` int(11) NOT NULL COMMENT 'Customer shipping address. Foreign key to Address.AddressID.',
  `ShipMethodID` int(11) NOT NULL COMMENT 'Shipping method. Foreign key to ShipMethod.ShipMethodID.',
  `CreditCardID` int(11) DEFAULT NULL COMMENT 'Credit card identification number. Foreign key to CreditCard.CreditCardID.',
  `CreditCardApprovalCode` varchar(15) DEFAULT NULL COMMENT 'Approval code provided by the credit card company.',
  `CurrencyRateID` int(11) DEFAULT NULL COMMENT 'Currency exchange rate used. Foreign key to CurrencyRate.CurrencyRateID.',
  `SubTotal` decimal(19,4) NOT NULL DEFAULT 0.0000 COMMENT 'Sales subtotal. Computed as SUM(SalesOrderDetail.LineTotal)for the appropriate SalesOrderID.',
  `TaxAmt` decimal(19,4) NOT NULL DEFAULT 0.0000 COMMENT 'Tax amount.',
  `Freight` decimal(19,4) NOT NULL DEFAULT 0.0000 COMMENT 'Shipping cost.',
  `TotalDue` decimal(19,4) NOT NULL COMMENT 'Total due from customer. Computed as Subtotal + TaxAmt + Freight.',
  `Comment` varchar(128) DEFAULT NULL COMMENT 'Sales representative comments.',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`SalesOrderID`),
  UNIQUE KEY `AK_SalesOrderHeader_rowguid` (`rowguid`),
  UNIQUE KEY `AK_SalesOrderHeader_SalesOrderNumber` (`SalesOrderNumber`),
  KEY `IX_SalesOrderHeader_CustomerID` (`CustomerID`),
  KEY `IX_SalesOrderHeader_SalesPersonID` (`SalesPersonID`),
  KEY `FK_SalesOrderHeader_Address_BillToAddressID` (`BillToAddressID`),
  KEY `FK_SalesOrderHeader_Address_ShipToAddressID` (`ShipToAddressID`),
  KEY `FK_SalesOrderHeader_CreditCard_CreditCardID` (`CreditCardID`),
  KEY `FK_SalesOrderHeader_CurrencyRate_CurrencyRateID` (`CurrencyRateID`),
  KEY `FK_SalesOrderHeader_ShipMethod_ShipMethodID` (`ShipMethodID`),
  KEY `FK_SalesOrderHeader_SalesTerritory_TerritoryID` (`TerritoryID`),
  KEY `GUID_SalesOrderHeader` (`rowguid`),
  CONSTRAINT `FK_SalesOrderHeader_Address_BillToAddressID` FOREIGN KEY (`BillToAddressID`) REFERENCES `Address` (`AddressID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SalesOrderHeader_Address_ShipToAddressID` FOREIGN KEY (`ShipToAddressID`) REFERENCES `Address` (`AddressID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SalesOrderHeader_CreditCard_CreditCardID` FOREIGN KEY (`CreditCardID`) REFERENCES `CreditCard` (`CreditCardID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SalesOrderHeader_CurrencyRate_CurrencyRateID` FOREIGN KEY (`CurrencyRateID`) REFERENCES `CurrencyRate` (`CurrencyRateID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SalesOrderHeader_Customer_CustomerID` FOREIGN KEY (`CustomerID`) REFERENCES `Customer` (`CustomerID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SalesOrderHeader_SalesPerson_SalesPersonID` FOREIGN KEY (`SalesPersonID`) REFERENCES `SalesPerson` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SalesOrderHeader_SalesTerritory_TerritoryID` FOREIGN KEY (`TerritoryID`) REFERENCES `SalesTerritory` (`TerritoryID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SalesOrderHeader_ShipMethod_ShipMethodID` FOREIGN KEY (`ShipMethodID`) REFERENCES `ShipMethod` (`ShipMethodID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=75124 DEFAULT CHARSET=utf8 COMMENT='General sales order information.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:32:36
