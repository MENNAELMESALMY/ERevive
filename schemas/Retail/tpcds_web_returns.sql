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
-- Table structure for table `web_returns`
--

DROP TABLE IF EXISTS `web_returns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_returns` (
  `wr_returned_date_sk` int(11) DEFAULT NULL,
  `wr_returned_time_sk` int(11) DEFAULT NULL,
  `wr_item_sk` int(11) NOT NULL,
  `wr_refunded_customer_sk` int(11) DEFAULT NULL,
  `wr_refunded_cdemo_sk` int(11) DEFAULT NULL,
  `wr_refunded_hdemo_sk` int(11) DEFAULT NULL,
  `wr_refunded_addr_sk` int(11) DEFAULT NULL,
  `wr_returning_customer_sk` int(11) DEFAULT NULL,
  `wr_returning_cdemo_sk` int(11) DEFAULT NULL,
  `wr_returning_hdemo_sk` int(11) DEFAULT NULL,
  `wr_returning_addr_sk` int(11) DEFAULT NULL,
  `wr_web_page_sk` int(11) DEFAULT NULL,
  `wr_reason_sk` int(11) DEFAULT NULL,
  `wr_order_number` int(11) NOT NULL,
  `wr_return_quantity` int(11) DEFAULT NULL,
  `wr_return_amt` decimal(7,2) DEFAULT NULL,
  `wr_return_tax` decimal(7,2) DEFAULT NULL,
  `wr_return_amt_inc_tax` decimal(7,2) DEFAULT NULL,
  `wr_fee` decimal(7,2) DEFAULT NULL,
  `wr_return_ship_cost` decimal(7,2) DEFAULT NULL,
  `wr_refunded_cash` decimal(7,2) DEFAULT NULL,
  `wr_reversed_charge` decimal(7,2) DEFAULT NULL,
  `wr_account_credit` decimal(7,2) DEFAULT NULL,
  `wr_net_loss` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`wr_item_sk`,`wr_order_number`),
  KEY `wr_wp` (`wr_web_page_sk`),
  KEY `wr_ret_hd` (`wr_returning_hdemo_sk`),
  KEY `wr_ret_c` (`wr_returning_customer_sk`),
  KEY `wr_ret_cd` (`wr_returning_cdemo_sk`),
  KEY `wr_ret_a` (`wr_returning_addr_sk`),
  KEY `wr_ret_t` (`wr_returned_time_sk`),
  KEY `wr_ret_d` (`wr_returned_date_sk`),
  KEY `wr_ref_hd` (`wr_refunded_hdemo_sk`),
  KEY `wr_ref_c` (`wr_refunded_customer_sk`),
  KEY `wr_ref_cd` (`wr_refunded_cdemo_sk`),
  KEY `wr_ref_a` (`wr_refunded_addr_sk`),
  KEY `wr_r` (`wr_reason_sk`),
  CONSTRAINT `wr_i` FOREIGN KEY (`wr_item_sk`) REFERENCES `item` (`i_item_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_r` FOREIGN KEY (`wr_reason_sk`) REFERENCES `reason` (`r_reason_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ref_a` FOREIGN KEY (`wr_refunded_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ref_c` FOREIGN KEY (`wr_refunded_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ref_cd` FOREIGN KEY (`wr_refunded_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ref_hd` FOREIGN KEY (`wr_refunded_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ret_a` FOREIGN KEY (`wr_returning_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ret_c` FOREIGN KEY (`wr_returning_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ret_cd` FOREIGN KEY (`wr_returning_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ret_d` FOREIGN KEY (`wr_returned_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ret_hd` FOREIGN KEY (`wr_returning_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_ret_t` FOREIGN KEY (`wr_returned_time_sk`) REFERENCES `time_dim` (`t_time_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `wr_wp` FOREIGN KEY (`wr_web_page_sk`) REFERENCES `web_page` (`wp_web_page_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:44:01
