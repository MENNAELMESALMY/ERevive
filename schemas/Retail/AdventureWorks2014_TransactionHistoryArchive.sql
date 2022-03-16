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
-- Table structure for table `TransactionHistoryArchive`
--

DROP TABLE IF EXISTS `TransactionHistoryArchive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TransactionHistoryArchive` (
  `TransactionID` int(11) NOT NULL COMMENT 'Primary key for TransactionHistoryArchive records.',
  `ProductID` int(11) NOT NULL COMMENT 'Product identification number. Foreign key to Product.ProductID.',
  `ReferenceOrderID` int(11) NOT NULL COMMENT 'Purchase order, sales order, or work order identification number.',
  `ReferenceOrderLineID` int(11) NOT NULL DEFAULT 0 COMMENT 'Line number associated with the purchase order, sales order, or work order.',
  `TransactionDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time of the transaction.',
  `TransactionType` char(1) NOT NULL COMMENT 'W = Work Order, S = Sales Order, P = Purchase Order',
  `Quantity` int(11) NOT NULL COMMENT 'Product quantity.',
  `ActualCost` decimal(19,4) NOT NULL COMMENT 'Product cost.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`TransactionID`),
  KEY `IX_TransactionHistoryArchive_ProductID` (`ProductID`),
  KEY `IX_TransactionHistoryArchive_ReferenceOrderID_ReferenceOrderLi2` (`ReferenceOrderID`,`ReferenceOrderLineID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Transactions for previous years.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:31:34
