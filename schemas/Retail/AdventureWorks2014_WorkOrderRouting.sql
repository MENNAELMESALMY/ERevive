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
-- Table structure for table `WorkOrderRouting`
--

DROP TABLE IF EXISTS `WorkOrderRouting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WorkOrderRouting` (
  `WorkOrderID` int(11) NOT NULL COMMENT 'Primary key. Foreign key to WorkOrder.WorkOrderID.',
  `ProductID` int(11) NOT NULL COMMENT 'Primary key. Foreign key to Product.ProductID.',
  `OperationSequence` smallint(6) NOT NULL COMMENT 'Primary key. Indicates the manufacturing process sequence.',
  `LocationID` smallint(6) NOT NULL COMMENT 'Manufacturing location where the part is processed. Foreign key to Location.LocationID.',
  `ScheduledStartDate` datetime NOT NULL COMMENT 'Planned manufacturing start date.',
  `ScheduledEndDate` datetime NOT NULL COMMENT 'Planned manufacturing end date.',
  `ActualStartDate` datetime DEFAULT NULL COMMENT 'Actual start date.',
  `ActualEndDate` datetime DEFAULT NULL COMMENT 'Actual end date.',
  `ActualResourceHrs` decimal(9,4) DEFAULT NULL COMMENT 'Number of manufacturing hours used.',
  `PlannedCost` decimal(19,4) NOT NULL COMMENT 'Estimated manufacturing cost.',
  `ActualCost` decimal(19,4) DEFAULT NULL COMMENT 'Actual manufacturing cost.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`WorkOrderID`,`ProductID`,`OperationSequence`),
  KEY `IX_WorkOrderRouting_ProductID` (`ProductID`),
  KEY `FK_WorkOrderRouting_Location_LocationID` (`LocationID`),
  CONSTRAINT `FK_WorkOrderRouting_Location_LocationID` FOREIGN KEY (`LocationID`) REFERENCES `Location` (`LocationID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_WorkOrderRouting_WorkOrder_WorkOrderID` FOREIGN KEY (`WorkOrderID`) REFERENCES `WorkOrder` (`WorkOrderID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Work order details.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:32:46
