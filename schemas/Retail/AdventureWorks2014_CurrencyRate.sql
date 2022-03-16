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
-- Table structure for table `CurrencyRate`
--

DROP TABLE IF EXISTS `CurrencyRate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CurrencyRate` (
  `CurrencyRateID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key for CurrencyRate records.',
  `CurrencyRateDate` datetime NOT NULL COMMENT 'Date and time the exchange rate was obtained.',
  `FromCurrencyCode` char(3) NOT NULL COMMENT 'Exchange rate was converted from this currency code.',
  `ToCurrencyCode` char(3) NOT NULL COMMENT 'Exchange rate was converted to this currency code.',
  `AverageRate` decimal(19,4) NOT NULL COMMENT 'Average exchange rate for the day.',
  `EndOfDayRate` decimal(19,4) NOT NULL COMMENT 'Final exchange rate for the day.',
  `ModifiedDate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT 'Date and time the record was last updated.',
  PRIMARY KEY (`CurrencyRateID`),
  UNIQUE KEY `AK_CurrencyRate_CurrencyRateDate_FromCurrencyCode_ToCurrencyCode` (`CurrencyRateDate`,`FromCurrencyCode`,`ToCurrencyCode`),
  KEY `FK_CurrencyRate_Currency_FromCurrencyCode` (`FromCurrencyCode`),
  KEY `FK_CurrencyRate_Currency_ToCurrencyCode` (`ToCurrencyCode`),
  CONSTRAINT `FK_CurrencyRate_Currency_FromCurrencyCode` FOREIGN KEY (`FromCurrencyCode`) REFERENCES `Currency` (`CurrencyCode`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_CurrencyRate_Currency_ToCurrencyCode` FOREIGN KEY (`ToCurrencyCode`) REFERENCES `Currency` (`CurrencyCode`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13533 DEFAULT CHARSET=utf8 COMMENT='Currency exchange rates.';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:31:31
