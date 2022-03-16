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
-- Table structure for table `BillOfMaterials`
--

DROP TABLE IF EXISTS `BillOfMaterials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BillOfMaterials` (
  `BillOfMaterialsID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key for BillOfMaterials records.',
  `ProductAssemblyID` int(11) DEFAULT NULL COMMENT 'Parent product identification number. Foreign key to Product.ProductID.',
  `ComponentID` int(11) NOT NULL COMMENT 'Component identification number. Foreign key to Product.ProductID.',
  `StartDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date the component started being used in the assembly item.',
  `EndDate` datetime DEFAULT NULL COMMENT 'Date the component stopped being used in the assembly item.',
  `UnitMeasureCode` char(3) NOT NULL COMMENT 'Standard code identifying the unit of measure for the quantity.',
  `BOMLevel` smallint(6) NOT NULL COMMENT 'Indicates the depth the component is from its parent (AssemblyID).',
  `PerAssemblyQty` decimal(8,2) NOT NULL DEFAULT 1.00 COMMENT 'Quantity of the component needed to create the assembly.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`BillOfMaterialsID`),
  UNIQUE KEY `AK_BillOfMaterials_ProductAssemblyID_ComponentID_StartDate` (`ProductAssemblyID`,`ComponentID`,`StartDate`),
  KEY `IX_BillOfMaterials_UnitMeasureCode` (`UnitMeasureCode`),
  KEY `FK_BillOfMaterials_Product_ComponentID` (`ComponentID`),
  CONSTRAINT `FK_BillOfMaterials_Product_ComponentID` FOREIGN KEY (`ComponentID`) REFERENCES `Product` (`ProductID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_BillOfMaterials_Product_ProductAssemblyID` FOREIGN KEY (`ProductAssemblyID`) REFERENCES `Product` (`ProductID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_BillOfMaterials_UnitMeasure_UnitMeasureCode` FOREIGN KEY (`UnitMeasureCode`) REFERENCES `UnitMeasure` (`UnitMeasureCode`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3483 DEFAULT CHARSET=utf8 COMMENT='Items required to make bicycles and bicycle subassemblies. It identifies the heirarchical relationship between a parent product and its components.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:30:06
