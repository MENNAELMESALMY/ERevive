-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: Mondial
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
-- Table structure for table `located`
--

DROP TABLE IF EXISTS `located`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `located` (
  `City` varchar(35) DEFAULT NULL,
  `Province` varchar(35) DEFAULT NULL,
  `Country` varchar(4) DEFAULT NULL,
  `River` varchar(35) DEFAULT NULL,
  `Lake` varchar(35) DEFAULT NULL,
  `Sea` varchar(35) DEFAULT NULL,
  KEY `ix_located_Country` (`Country`) USING BTREE,
  KEY `ix_located_River` (`River`) USING BTREE,
  KEY `ix_located_Lake` (`Lake`) USING BTREE,
  KEY `ix_located_Sea` (`Sea`) USING BTREE,
  KEY `ix_located_City` (`City`,`Province`) USING BTREE,
  KEY `ix_located_Province` (`Province`,`Country`) USING BTREE,
  CONSTRAINT `located_ibfk_1` FOREIGN KEY (`Country`) REFERENCES `country` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `located_ibfk_2` FOREIGN KEY (`City`, `Province`) REFERENCES `city` (`Name`, `Province`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `located_ibfk_3` FOREIGN KEY (`River`) REFERENCES `river` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `located_ibfk_4` FOREIGN KEY (`Lake`) REFERENCES `lake` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `located_ibfk_5` FOREIGN KEY (`Sea`) REFERENCES `sea` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `located_ibfk_6` FOREIGN KEY (`Province`, `Country`) REFERENCES `province` (`Name`, `Country`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 20:36:13
