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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `c_customer_sk` int(11) NOT NULL,
  `c_customer_id` char(16) NOT NULL,
  `c_current_cdemo_sk` int(11) DEFAULT NULL,
  `c_current_hdemo_sk` int(11) DEFAULT NULL,
  `c_current_addr_sk` int(11) DEFAULT NULL,
  `c_first_shipto_date_sk` int(11) DEFAULT NULL,
  `c_first_sales_date_sk` int(11) DEFAULT NULL,
  `c_salutation` char(10) DEFAULT NULL,
  `c_first_name` char(20) DEFAULT NULL,
  `c_last_name` char(30) DEFAULT NULL,
  `c_preferred_cust_flag` char(1) DEFAULT NULL,
  `c_birth_day` int(11) DEFAULT NULL,
  `c_birth_month` int(11) DEFAULT NULL,
  `c_birth_year` int(11) DEFAULT NULL,
  `c_birth_country` varchar(20) DEFAULT NULL,
  `c_login` char(13) DEFAULT NULL,
  `c_email_address` char(50) DEFAULT NULL,
  `c_last_review_date` char(10) DEFAULT NULL,
  PRIMARY KEY (`c_customer_sk`),
  KEY `c_fsd2` (`c_first_shipto_date_sk`),
  KEY `c_fsd` (`c_first_sales_date_sk`),
  KEY `c_hd` (`c_current_hdemo_sk`),
  KEY `c_cd` (`c_current_cdemo_sk`),
  KEY `c_a` (`c_current_addr_sk`),
  CONSTRAINT `c_a` FOREIGN KEY (`c_current_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `c_cd` FOREIGN KEY (`c_current_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `c_fsd` FOREIGN KEY (`c_first_sales_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `c_fsd2` FOREIGN KEY (`c_first_shipto_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `c_hd` FOREIGN KEY (`c_current_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:43:57
