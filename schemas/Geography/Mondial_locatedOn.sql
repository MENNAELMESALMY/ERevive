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
-- Table structure for table `locatedOn`
--

DROP TABLE IF EXISTS `locatedOn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locatedOn` (
  `City` varchar(35) NOT NULL DEFAULT '',
  `Province` varchar(35) NOT NULL DEFAULT '',
  `Country` varchar(4) NOT NULL DEFAULT '',
  `Island` varchar(35) NOT NULL DEFAULT '',
  PRIMARY KEY (`City`,`Province`,`Country`,`Island`),
  KEY `ix_locatedOn_Country` (`Country`) USING BTREE,
  KEY `ix_locatedOn_Island` (`Island`) USING BTREE,
  KEY `ix_locatedOn_Province` (`Province`) USING BTREE,
  KEY `Province` (`Province`,`Country`),
  CONSTRAINT `locatedOn_ibfk_1` FOREIGN KEY (`Country`) REFERENCES `country` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `locatedOn_ibfk_2` FOREIGN KEY (`Island`) REFERENCES `island` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `locatedOn_ibfk_3` FOREIGN KEY (`City`, `Province`) REFERENCES `city` (`Name`, `Province`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `locatedOn_ibfk_4` FOREIGN KEY (`Province`, `Country`) REFERENCES `province` (`Name`, `Country`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 20:36:55
