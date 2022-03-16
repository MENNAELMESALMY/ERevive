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
-- Table structure for table `web_site`
--

DROP TABLE IF EXISTS `web_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_site` (
  `web_site_sk` int(11) NOT NULL,
  `web_site_id` char(16) NOT NULL,
  `web_rec_start_date` date DEFAULT NULL,
  `web_rec_end_date` date DEFAULT NULL,
  `web_name` varchar(50) DEFAULT NULL,
  `web_open_date_sk` int(11) DEFAULT NULL,
  `web_close_date_sk` int(11) DEFAULT NULL,
  `web_class` varchar(50) DEFAULT NULL,
  `web_manager` varchar(40) DEFAULT NULL,
  `web_mkt_id` int(11) DEFAULT NULL,
  `web_mkt_class` varchar(50) DEFAULT NULL,
  `web_mkt_desc` varchar(100) DEFAULT NULL,
  `web_market_manager` varchar(40) DEFAULT NULL,
  `web_company_id` int(11) DEFAULT NULL,
  `web_company_name` char(50) DEFAULT NULL,
  `web_street_number` char(10) DEFAULT NULL,
  `web_street_name` varchar(60) DEFAULT NULL,
  `web_street_type` char(15) DEFAULT NULL,
  `web_suite_number` char(10) DEFAULT NULL,
  `web_city` varchar(60) DEFAULT NULL,
  `web_county` varchar(30) DEFAULT NULL,
  `web_state` char(2) DEFAULT NULL,
  `web_zip` char(10) DEFAULT NULL,
  `web_country` varchar(20) DEFAULT NULL,
  `web_gmt_offset` decimal(5,2) DEFAULT NULL,
  `web_tax_percentage` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`web_site_sk`),
  KEY `web_d2` (`web_open_date_sk`),
  KEY `web_d1` (`web_close_date_sk`),
  CONSTRAINT `web_d1` FOREIGN KEY (`web_close_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `web_d2` FOREIGN KEY (`web_open_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:44:13
