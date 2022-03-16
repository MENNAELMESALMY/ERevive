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
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Employee` (
  `BusinessEntityID` int(11) NOT NULL COMMENT 'Primary key for Employee records.  Foreign key to BusinessEntity.BusinessEntityID.',
  `NationalIDNumber` varchar(15) NOT NULL COMMENT 'Unique national identification number such as a social security number.',
  `LoginID` varchar(256) NOT NULL COMMENT 'Network login.',
  `OrganizationNode` varchar(255) DEFAULT NULL COMMENT 'Where the employee is located in corporate hierarchy.',
  `OrganizationLevel` smallint(6) DEFAULT NULL COMMENT 'The depth of the employee in the corporate hierarchy.',
  `JobTitle` varchar(50) NOT NULL COMMENT 'Work title such as Buyer or Sales Representative.',
  `BirthDate` date NOT NULL COMMENT 'Date of birth.',
  `MaritalStatus` char(1) NOT NULL COMMENT 'M = Married, S = Single',
  `Gender` char(1) NOT NULL COMMENT 'M = Male, F = Female',
  `HireDate` date NOT NULL COMMENT 'Employee hired on this date.',
  `SalariedFlag` tinyint(1) NOT NULL DEFAULT 1 COMMENT 'Job classification. 0 = Hourly, not exempt from collective bargaining. 1 = Salaried, exempt from collective bargaining.',
  `VacationHours` smallint(6) NOT NULL DEFAULT 0 COMMENT 'Number of available vacation hours.',
  `SickLeaveHours` smallint(6) NOT NULL DEFAULT 0 COMMENT 'Number of available sick leave hours.',
  `CurrentFlag` tinyint(1) NOT NULL DEFAULT 1 COMMENT '0 = Inactive, 1 = Active',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`BusinessEntityID`),
  UNIQUE KEY `AK_Employee_NationalIDNumber` (`NationalIDNumber`),
  UNIQUE KEY `AK_Employee_rowguid` (`rowguid`),
  UNIQUE KEY `AK_Employee_LoginID` (`LoginID`(255)),
  KEY `IX_Employee_OrganizationNode` (`OrganizationNode`),
  KEY `IX_Employee_OrganizationLevel_OrganizationNode` (`OrganizationLevel`,`OrganizationNode`),
  KEY `GUID_Employee` (`rowguid`),
  CONSTRAINT `FK_Employee_Person_BusinessEntityID` FOREIGN KEY (`BusinessEntityID`) REFERENCES `Person` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Employee information such as salary, department, and title.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:31:41
