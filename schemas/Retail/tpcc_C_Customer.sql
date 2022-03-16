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
-- Table structure for table `C_Customer`
--

DROP TABLE IF EXISTS `C_Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `C_Customer` (
  `c_id` int(11) NOT NULL,
  `c_d_id` int(11) NOT NULL,
  `c_w_id` int(11) NOT NULL,
  `c_first` char(16) DEFAULT NULL,
  `c_middle` char(2) DEFAULT NULL,
  `c_last` char(16) DEFAULT NULL,
  `c_street_1` char(20) DEFAULT NULL,
  `c_street_2` char(20) DEFAULT NULL,
  `c_city` char(20) DEFAULT NULL,
  `c_state` char(2) DEFAULT NULL,
  `c_zip` char(9) DEFAULT NULL,
  `c_phone` char(16) DEFAULT NULL,
  `c_since` datetime DEFAULT NULL,
  `c_credit` char(2) DEFAULT NULL,
  `c_credit_lim` float DEFAULT NULL,
  `c_discount` float DEFAULT NULL,
  `c_balance` float DEFAULT NULL,
  `c_ytd_payment` float DEFAULT NULL,
  `c_payment_cnt` int(11) DEFAULT NULL,
  `c_delivery_cnt` int(11) DEFAULT NULL,
  `c_data1` char(250) DEFAULT NULL,
  `c_data2` char(250) DEFAULT NULL,
  PRIMARY KEY (`c_id`,`c_d_id`,`c_w_id`),
  UNIQUE KEY `C_Customer_I1` (`c_w_id`,`c_d_id`,`c_id`),
  UNIQUE KEY `C_Customer_I2` (`c_w_id`,`c_d_id`,`c_last`,`c_first`,`c_id`),
  KEY `c_d_id` (`c_d_id`),
  KEY `c_d_id_2` (`c_d_id`,`c_id`,`c_w_id`),
  CONSTRAINT `C_Customer_ibfk_1` FOREIGN KEY (`c_d_id`) REFERENCES `C_District` (`d_id`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 19:26:08
