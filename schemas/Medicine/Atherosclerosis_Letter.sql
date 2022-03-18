-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: Atherosclerosis
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
-- Table structure for table `Letter`
--

DROP TABLE IF EXISTS `Letter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Letter` (
  `ICO` int(11) NOT NULL,
  `MESDOT` varchar(255) DEFAULT NULL,
  `ROKDOT` int(11) DEFAULT NULL,
  `LEKCHOL` int(11) DEFAULT NULL,
  `LEKTK` int(11) DEFAULT NULL,
  `NEMOC1` int(11) DEFAULT NULL,
  `ROK1` int(11) DEFAULT NULL,
  `NEMOC2` varchar(255) DEFAULT NULL,
  `ROK2` varchar(255) DEFAULT NULL,
  `NEMOC3` varchar(255) DEFAULT NULL,
  `ROK3` varchar(255) DEFAULT NULL,
  `NEMOC4` varchar(255) DEFAULT NULL,
  `ROK4` varchar(255) DEFAULT NULL,
  `NEMOC5` varchar(255) DEFAULT NULL,
  `ROK5` varchar(255) DEFAULT NULL,
  `HYPTK` int(11) DEFAULT NULL,
  `ROKHYPTK` varchar(255) DEFAULT NULL,
  `HYPLP` int(11) DEFAULT NULL,
  `ROKHYPLP` varchar(255) DEFAULT NULL,
  `CUKROVKA` int(11) DEFAULT NULL,
  `ROKCUKR` varchar(255) DEFAULT NULL,
  `CUKRTAB` varchar(255) DEFAULT NULL,
  `ODCUTAB` varchar(255) DEFAULT NULL,
  `DOCUTAB` varchar(255) DEFAULT NULL,
  `CUKRINS` varchar(255) DEFAULT NULL,
  `ODCUINS` varchar(255) DEFAULT NULL,
  `DOCUINS` varchar(255) DEFAULT NULL,
  `AP` int(11) DEFAULT NULL,
  `SI` int(11) DEFAULT NULL,
  `ROKSI` varchar(255) DEFAULT NULL,
  `MM` varchar(255) DEFAULT NULL,
  `ROKMM` varchar(255) DEFAULT NULL,
  `BDK` int(11) DEFAULT NULL,
  `ROKBDK1` varchar(255) DEFAULT NULL,
  `DUSNOST` varchar(255) DEFAULT NULL,
  `ROKDUS` varchar(255) DEFAULT NULL,
  `DUSCHUZE` varchar(255) DEFAULT NULL,
  `DUSBEH` varchar(255) DEFAULT NULL,
  `DUSROVIN` varchar(255) DEFAULT NULL,
  `DUKLID` varchar(255) DEFAULT NULL,
  `DUSNOC` varchar(255) DEFAULT NULL,
  `KURAK` varchar(255) DEFAULT NULL,
  `KURAKBYV` varchar(255) DEFAULT NULL,
  `ROKPRKOUR` varchar(255) DEFAULT NULL,
  `KOURLET` varchar(255) DEFAULT NULL,
  `CIGDENMIN` varchar(255) DEFAULT NULL,
  `CIGDEN` varchar(255) DEFAULT NULL,
  `KOURODLET` varchar(255) DEFAULT NULL,
  `DYMKA` varchar(255) DEFAULT NULL,
  `PASED` varchar(255) DEFAULT NULL,
  `PAMIRNA` varchar(255) DEFAULT NULL,
  `PAVELKA` varchar(255) DEFAULT NULL,
  `PAPRED10` varchar(255) DEFAULT NULL,
  `DIETA` varchar(255) DEFAULT NULL,
  `DIECUOD` varchar(255) DEFAULT NULL,
  `DIETUKOD` varchar(255) DEFAULT NULL,
  `JINADIE` varchar(255) DEFAULT NULL,
  `JINADIEOD` varchar(255) DEFAULT NULL,
  `VAHA` varchar(255) DEFAULT NULL,
  `VAHAPRED10` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ICO`),
  KEY `ICO` (`ICO`),
  CONSTRAINT `Letter_ibfk_1` FOREIGN KEY (`ICO`) REFERENCES `Entry` (`ICO`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:33:31