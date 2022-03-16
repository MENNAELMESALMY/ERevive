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
-- Table structure for table `call_center`
--

DROP TABLE IF EXISTS `call_center`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `call_center` (
  `cc_call_center_sk` int(11) NOT NULL,
  `cc_call_center_id` char(16) NOT NULL,
  `cc_rec_start_date` date DEFAULT NULL,
  `cc_rec_end_date` date DEFAULT NULL,
  `cc_closed_date_sk` int(11) DEFAULT NULL,
  `cc_open_date_sk` int(11) DEFAULT NULL,
  `cc_name` varchar(50) DEFAULT NULL,
  `cc_class` varchar(50) DEFAULT NULL,
  `cc_employees` int(11) DEFAULT NULL,
  `cc_sq_ft` int(11) DEFAULT NULL,
  `cc_hours` char(20) DEFAULT NULL,
  `cc_manager` varchar(40) DEFAULT NULL,
  `cc_mkt_id` int(11) DEFAULT NULL,
  `cc_mkt_class` char(50) DEFAULT NULL,
  `cc_mkt_desc` varchar(100) DEFAULT NULL,
  `cc_market_manager` varchar(40) DEFAULT NULL,
  `cc_division` int(11) DEFAULT NULL,
  `cc_division_name` varchar(50) DEFAULT NULL,
  `cc_company` int(11) DEFAULT NULL,
  `cc_company_name` char(50) DEFAULT NULL,
  `cc_street_number` char(10) DEFAULT NULL,
  `cc_street_name` varchar(60) DEFAULT NULL,
  `cc_street_type` char(15) DEFAULT NULL,
  `cc_suite_number` char(10) DEFAULT NULL,
  `cc_city` varchar(60) DEFAULT NULL,
  `cc_county` varchar(30) DEFAULT NULL,
  `cc_state` char(2) DEFAULT NULL,
  `cc_zip` char(10) DEFAULT NULL,
  `cc_country` varchar(20) DEFAULT NULL,
  `cc_gmt_offset` decimal(5,2) DEFAULT NULL,
  `cc_tax_percentage` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`cc_call_center_sk`),
  KEY `cc_d2` (`cc_open_date_sk`),
  KEY `cc_d1` (`cc_closed_date_sk`),
  CONSTRAINT `cc_d1` FOREIGN KEY (`cc_closed_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cc_d2` FOREIGN KEY (`cc_open_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:43:38
