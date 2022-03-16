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
-- Table structure for table `Person`
--

DROP TABLE IF EXISTS `Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Person` (
  `BusinessEntityID` int(11) NOT NULL COMMENT 'Primary key for Person records.',
  `PersonType` char(2) NOT NULL COMMENT 'Primary type of person: SC = Store Contact, IN = Individual (retail) customer, SP = Sales person, EM = Employee (non-sales), VC = Vendor contact, GC = General contact',
  `NameStyle` tinyint(1) NOT NULL DEFAULT 0 COMMENT '0 = The data in FirstName and LastName are stored in western style (first name, last name) order.  1 = Eastern style (last name, first name) order.',
  `Title` varchar(8) DEFAULT NULL COMMENT 'A courtesy title. For example, Mr. or Ms.',
  `FirstName` varchar(100) NOT NULL COMMENT 'First name of the person.',
  `MiddleName` varchar(100) DEFAULT NULL COMMENT 'Middle name or middle initial of the person.',
  `LastName` varchar(100) NOT NULL COMMENT 'Last name of the person.',
  `Suffix` varchar(10) DEFAULT NULL COMMENT 'Surname suffix. For example, Sr. or Jr.',
  `EmailPromotion` int(11) NOT NULL DEFAULT 0 COMMENT '0 = Contact does not wish to receive e-mail promotions, 1 = Contact does wish to receive e-mail promotions from AdventureWorks, 2 = Contact does wish to receive e-mail promotions from AdventureWorks and selected partners. ',
  `AdditionalContactInfo` text DEFAULT NULL COMMENT 'Additional contact information about the person stored in xml format. ',
  `Demographics` text DEFAULT NULL COMMENT 'Personal information such as hobbies, and income collected from online shoppers. Used for sales analysis.',
  `rowguid` varchar(64) NOT NULL COMMENT 'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`BusinessEntityID`),
  UNIQUE KEY `AK_Person_rowguid` (`rowguid`),
  KEY `IX_Person_LastName_FirstName_MiddleName` (`LastName`,`FirstName`,`MiddleName`),
  KEY `PXML_Person_AddContact` (`AdditionalContactInfo`(255)),
  KEY `PXML_Person_Demographics` (`Demographics`(255)),
  KEY `XMLPATH_Person_Demographics` (`Demographics`(255)),
  KEY `XMLPROPERTY_Person_Demographics` (`Demographics`(255)),
  KEY `XMLVALUE_Person_Demographics` (`Demographics`(255)),
  KEY `GUID_Person` (`rowguid`),
  CONSTRAINT `FK_Person_BusinessEntity_BusinessEntityID` FOREIGN KEY (`BusinessEntityID`) REFERENCES `BusinessEntity` (`BusinessEntityID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Human beings involved with AdventureWorks: employees, customer contacts, and vendor contacts.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:30:48
