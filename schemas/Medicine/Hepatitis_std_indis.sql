-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: Hepatitis_std
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
-- Table structure for table `indis`
--

DROP TABLE IF EXISTS `indis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indis` (
  `got` varchar(10) DEFAULT NULL,
  `gpt` varchar(10) DEFAULT NULL,
  `alb` varchar(45) DEFAULT NULL,
  `tbil` varchar(45) DEFAULT NULL,
  `dbil` varchar(45) DEFAULT NULL,
  `che` varchar(45) DEFAULT NULL,
  `ttt` varchar(45) DEFAULT NULL,
  `ztt` varchar(45) DEFAULT NULL,
  `tcho` varchar(45) DEFAULT NULL,
  `tp` varchar(45) DEFAULT NULL,
  `in_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`in_id`),
  KEY `indis_got` (`got`),
  KEY `indis_gpt` (`gpt`),
  KEY `indis_alb` (`alb`),
  KEY `indis_tbil` (`tbil`),
  KEY `indis_dbil` (`dbil`),
  KEY `indis_che` (`che`),
  KEY `indis_ttt` (`ttt`),
  KEY `indis_ztt` (`ztt`),
  KEY `indis_tcho` (`tcho`),
  KEY `indis_tp` (`tp`)
) ENGINE=InnoDB AUTO_INCREMENT=5692 DEFAULT CHARSET=latin1 AVG_ROW_LENGTH=50;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-20 19:43:36
