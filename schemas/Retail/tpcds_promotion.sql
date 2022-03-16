-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: tpcds
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
-- Table structure for table `promotion`
--

DROP TABLE IF EXISTS `promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promotion` (
  `p_promo_sk` int(11) NOT NULL,
  `p_promo_id` char(16) NOT NULL,
  `p_start_date_sk` int(11) DEFAULT NULL,
  `p_end_date_sk` int(11) DEFAULT NULL,
  `p_item_sk` int(11) DEFAULT NULL,
  `p_cost` decimal(15,2) DEFAULT NULL,
  `p_response_target` int(11) DEFAULT NULL,
  `p_promo_name` char(50) DEFAULT NULL,
  `p_channel_dmail` char(1) DEFAULT NULL,
  `p_channel_email` char(1) DEFAULT NULL,
  `p_channel_catalog` char(1) DEFAULT NULL,
  `p_channel_tv` char(1) DEFAULT NULL,
  `p_channel_radio` char(1) DEFAULT NULL,
  `p_channel_press` char(1) DEFAULT NULL,
  `p_channel_event` char(1) DEFAULT NULL,
  `p_channel_demo` char(1) DEFAULT NULL,
  `p_channel_details` varchar(100) DEFAULT NULL,
  `p_purpose` char(15) DEFAULT NULL,
  `p_discount_active` char(1) DEFAULT NULL,
  PRIMARY KEY (`p_promo_sk`),
  KEY `p_start_date` (`p_start_date_sk`),
  KEY `p_i` (`p_item_sk`),
  KEY `p_end_date` (`p_end_date_sk`),
  CONSTRAINT `p_end_date` FOREIGN KEY (`p_end_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `p_i` FOREIGN KEY (`p_item_sk`) REFERENCES `item` (`i_item_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `p_start_date` FOREIGN KEY (`p_start_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:44:17
