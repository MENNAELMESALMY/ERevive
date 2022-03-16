-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: Countries
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
-- Table structure for table `Data`
--

DROP TABLE IF EXISTS `Data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Data` (
  `Country Name` varchar(255) DEFAULT NULL,
  `Country Code` varchar(255) NOT NULL,
  `Indicator Name` varchar(255) DEFAULT NULL,
  `Indicator Code` varchar(255) NOT NULL,
  `1960` double DEFAULT NULL,
  `1961` double DEFAULT NULL,
  `1962` double DEFAULT NULL,
  `1963` double DEFAULT NULL,
  `1964` double DEFAULT NULL,
  `1965` double DEFAULT NULL,
  `1966` double DEFAULT NULL,
  `1967` double DEFAULT NULL,
  `1968` double DEFAULT NULL,
  `1969` double DEFAULT NULL,
  `1970` double DEFAULT NULL,
  `1971` double DEFAULT NULL,
  `1972` double DEFAULT NULL,
  `1973` double DEFAULT NULL,
  `1974` double DEFAULT NULL,
  `1975` double DEFAULT NULL,
  `1976` double DEFAULT NULL,
  `1977` double DEFAULT NULL,
  `1978` double DEFAULT NULL,
  `1979` double DEFAULT NULL,
  `1980` double DEFAULT NULL,
  `1981` double DEFAULT NULL,
  `1982` double DEFAULT NULL,
  `1983` double DEFAULT NULL,
  `1984` double DEFAULT NULL,
  `1985` double DEFAULT NULL,
  `1986` double DEFAULT NULL,
  `1987` double DEFAULT NULL,
  `1988` double DEFAULT NULL,
  `1989` double DEFAULT NULL,
  `1990` double DEFAULT NULL,
  `1991` double DEFAULT NULL,
  `1992` double DEFAULT NULL,
  `1993` double DEFAULT NULL,
  `1994` double DEFAULT NULL,
  `1995` double DEFAULT NULL,
  `1996` double DEFAULT NULL,
  `1997` double DEFAULT NULL,
  `1998` double DEFAULT NULL,
  `1999` double DEFAULT NULL,
  `2000` double DEFAULT NULL,
  `2001` double DEFAULT NULL,
  `2002` double DEFAULT NULL,
  `2003` double DEFAULT NULL,
  `2004` double DEFAULT NULL,
  `2005` double DEFAULT NULL,
  `2006` double DEFAULT NULL,
  `2007` double DEFAULT NULL,
  `2008` double DEFAULT NULL,
  `2009` double DEFAULT NULL,
  `2010` double DEFAULT NULL,
  `2011` double DEFAULT NULL,
  PRIMARY KEY (`Country Code`,`Indicator Code`),
  KEY `Indicator Code` (`Indicator Code`),
  KEY `Country Code` (`Country Code`),
  CONSTRAINT `Data_ibfk_1` FOREIGN KEY (`Indicator Code`) REFERENCES `Metadata - Indicators` (`INDICATOR_CODE`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Data_ibfk_2` FOREIGN KEY (`Country Code`) REFERENCES `Metadata - Countries` (`Country Code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 20:50:34
