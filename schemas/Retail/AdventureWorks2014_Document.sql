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
-- Table structure for table `Document`
--

DROP TABLE IF EXISTS `Document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Document` (
  `DocumentNode` varchar(255) NOT NULL COMMENT 'Primary key for Document records.',
  `DocumentLevel` smallint(6) DEFAULT NULL COMMENT 'Depth in the document hierarchy.',
  `Title` varchar(50) NOT NULL COMMENT 'Title of the document.',
  `Owner` int(11) NOT NULL COMMENT 'Employee who controls the document.  Foreign key to Employee.BusinessEntityID',
  `FolderFlag` tinyint(1) NOT NULL DEFAULT 0 COMMENT '0 = This is a folder, 1 = This is a document.',
  `FileName` varchar(400) NOT NULL COMMENT 'File name of the document',
  `FileExtension` varchar(8) NOT NULL COMMENT 'File extension indicating the document type. For example, .doc or .txt.',
  `Revision` char(5) NOT NULL COMMENT 'Revision number of the document. ',
  `ChangeNumber` int(11) NOT NULL DEFAULT 0 COMMENT 'Engineering change approval number.',
  `Status` tinyint(3) unsigned NOT NULL COMMENT '1 = Pending approval, 2 = Approved, 3 = Obsolete',
  `DocumentSummary` longtext DEFAULT NULL COMMENT 'Document abstract.',
  `Document` longblob DEFAULT NULL COMMENT 'Complete document.',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Required for FileStream.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`DocumentNode`),
  UNIQUE KEY `UQ__Document__F73921F763026E5E` (`rowguid`),
  UNIQUE KEY `AK_Document_rowguid` (`rowguid`),
  UNIQUE KEY `AK_Document_DocumentLevel_DocumentNode` (`DocumentLevel`,`DocumentNode`),
  KEY `IX_Document_FileName_Revision` (`FileName`(255),`Revision`),
  KEY `FK_Document_Employee_Owner` (`Owner`),
  KEY `GUID_Document` (`rowguid`),
  CONSTRAINT `FK_Document_Employee_Owner` FOREIGN KEY (`Owner`) REFERENCES `Employee` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Product maintenance documents.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:30:14
