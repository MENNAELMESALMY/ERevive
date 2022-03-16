-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: tpcc
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
-- Table structure for table `C_History`
--

DROP TABLE IF EXISTS `C_History`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `C_History` (
  `h_c_id` int(11) DEFAULT NULL,
  `h_c_d_id` int(11) DEFAULT NULL,
  `h_c_w_id` int(11) DEFAULT NULL,
  `h_d_id` int(11) DEFAULT NULL,
  `h_w_id` int(11) DEFAULT NULL,
  `h_date` datetime DEFAULT NULL,
  `h_amount` float DEFAULT NULL,
  `h_data` char(24) DEFAULT NULL,
  KEY `h_c_w_id` (`h_c_w_id`),
  KEY `h_d_id` (`h_d_id`),
  KEY `h_c_id` (`h_c_id`,`h_c_d_id`,`h_c_w_id`),
  KEY `h_d_id_2` (`h_d_id`,`h_w_id`),
  CONSTRAINT `C_History_ibfk_3` FOREIGN KEY (`h_c_id`, `h_c_d_id`, `h_c_w_id`) REFERENCES `C_Customer` (`c_id`, `c_d_id`, `c_w_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `C_History_ibfk_4` FOREIGN KEY (`h_d_id`, `h_w_id`) REFERENCES `C_District` (`d_id`, `d_w_id`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 19:25:58
