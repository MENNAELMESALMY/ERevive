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
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Product` (
  `ProductID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key for Product records.',
  `Name` varchar(100) NOT NULL COMMENT 'Name of the product.',
  `ProductNumber` varchar(25) NOT NULL COMMENT 'Unique product identification number.',
  `MakeFlag` tinyint(1) NOT NULL DEFAULT 1 COMMENT '0 = Product is purchased, 1 = Product is manufactured in-house.',
  `FinishedGoodsFlag` tinyint(1) NOT NULL DEFAULT 1 COMMENT '0 = Product is not a salable item. 1 = Product is salable.',
  `Color` varchar(15) DEFAULT NULL COMMENT 'Product color.',
  `SafetyStockLevel` smallint(6) NOT NULL COMMENT 'Minimum inventory quantity. ',
  `ReorderPoint` smallint(6) NOT NULL COMMENT 'Inventory level that triggers a purchase order or work order. ',
  `StandardCost` decimal(19,4) NOT NULL COMMENT 'Standard cost of the product.',
  `ListPrice` decimal(19,4) NOT NULL COMMENT 'Selling price.',
  `Size` varchar(5) DEFAULT NULL COMMENT 'Product size.',
  `SizeUnitMeasureCode` char(3) DEFAULT NULL COMMENT 'Unit of measure for Size column.',
  `WeightUnitMeasureCode` char(3) DEFAULT NULL COMMENT 'Unit of measure for Weight column.',
  `Weight` decimal(8,2) DEFAULT NULL COMMENT 'Product weight.',
  `DaysToManufacture` int(11) NOT NULL COMMENT 'Number of days required to manufacture the product.',
  `ProductLine` char(2) DEFAULT NULL COMMENT 'R = Road, M = Mountain, T = Touring, S = Standard',
  `Class` char(2) DEFAULT NULL COMMENT 'H = High, M = Medium, L = Low',
  `Style` char(2) DEFAULT NULL COMMENT 'W = Womens, M = Mens, U = Universal',
  `ProductSubcategoryID` int(11) DEFAULT NULL COMMENT 'Product is a member of this product subcategory. Foreign key to ProductSubCategory.ProductSubCategoryID. ',
  `ProductModelID` int(11) DEFAULT NULL COMMENT 'Product is a member of this product model. Foreign key to ProductModel.ProductModelID.',
  `SellStartDate` datetime NOT NULL COMMENT 'Date the product was available for sale.',
  `SellEndDate` datetime DEFAULT NULL COMMENT 'Date the product was no longer available for sale.',
  `DiscontinuedDate` datetime DEFAULT NULL COMMENT 'Date the product was discontinued.',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`ProductID`),
  UNIQUE KEY `AK_Product_ProductNumber` (`ProductNumber`),
  UNIQUE KEY `AK_Product_Name` (`Name`),
  UNIQUE KEY `AK_Product_rowguid` (`rowguid`),
  KEY `FK_Product_UnitMeasure_SizeUnitMeasureCode` (`SizeUnitMeasureCode`),
  KEY `FK_Product_UnitMeasure_WeightUnitMeasureCode` (`WeightUnitMeasureCode`),
  KEY `FK_Product_ProductModel_ProductModelID` (`ProductModelID`),
  KEY `FK_Product_ProductSubcategory_ProductSubcategoryID` (`ProductSubcategoryID`),
  KEY `GUID_Product` (`rowguid`),
  CONSTRAINT `FK_Product_ProductModel_ProductModelID` FOREIGN KEY (`ProductModelID`) REFERENCES `ProductModel` (`ProductModelID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_Product_ProductSubcategory_ProductSubcategoryID` FOREIGN KEY (`ProductSubcategoryID`) REFERENCES `ProductSubcategory` (`ProductSubcategoryID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_Product_UnitMeasure_SizeUnitMeasureCode` FOREIGN KEY (`SizeUnitMeasureCode`) REFERENCES `UnitMeasure` (`UnitMeasureCode`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_Product_UnitMeasure_WeightUnitMeasureCode` FOREIGN KEY (`WeightUnitMeasureCode`) REFERENCES `UnitMeasure` (`UnitMeasureCode`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COMMENT='Products sold or used in the manfacturing of sold products.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:31:52
