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
-- Table structure for table `catalog_returns`
--

DROP TABLE IF EXISTS `catalog_returns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catalog_returns` (
  `cr_returned_date_sk` int(11) DEFAULT NULL,
  `cr_returned_time_sk` int(11) DEFAULT NULL,
  `cr_item_sk` int(11) NOT NULL,
  `cr_refunded_customer_sk` int(11) DEFAULT NULL,
  `cr_refunded_cdemo_sk` int(11) DEFAULT NULL,
  `cr_refunded_hdemo_sk` int(11) DEFAULT NULL,
  `cr_refunded_addr_sk` int(11) DEFAULT NULL,
  `cr_returning_customer_sk` int(11) DEFAULT NULL,
  `cr_returning_cdemo_sk` int(11) DEFAULT NULL,
  `cr_returning_hdemo_sk` int(11) DEFAULT NULL,
  `cr_returning_addr_sk` int(11) DEFAULT NULL,
  `cr_call_center_sk` int(11) DEFAULT NULL,
  `cr_catalog_page_sk` int(11) DEFAULT NULL,
  `cr_ship_mode_sk` int(11) DEFAULT NULL,
  `cr_warehouse_sk` int(11) DEFAULT NULL,
  `cr_reason_sk` int(11) DEFAULT NULL,
  `cr_order_number` int(11) NOT NULL,
  `cr_return_quantity` int(11) DEFAULT NULL,
  `cr_return_amount` decimal(7,2) DEFAULT NULL,
  `cr_return_tax` decimal(7,2) DEFAULT NULL,
  `cr_return_amt_inc_tax` decimal(7,2) DEFAULT NULL,
  `cr_fee` decimal(7,2) DEFAULT NULL,
  `cr_return_ship_cost` decimal(7,2) DEFAULT NULL,
  `cr_refunded_cash` decimal(7,2) DEFAULT NULL,
  `cr_reversed_charge` decimal(7,2) DEFAULT NULL,
  `cr_store_credit` decimal(7,2) DEFAULT NULL,
  `cr_net_loss` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`cr_item_sk`,`cr_order_number`),
  KEY `cr_w2` (`cr_warehouse_sk`),
  KEY `cr_sm` (`cr_ship_mode_sk`),
  KEY `cr_hd2` (`cr_returning_hdemo_sk`),
  KEY `cr_c2` (`cr_returning_customer_sk`),
  KEY `cr_cd2` (`cr_returning_cdemo_sk`),
  KEY `cr_a2` (`cr_returning_addr_sk`),
  KEY `cr_t` (`cr_returned_time_sk`),
  KEY `cr_d1` (`cr_returned_date_sk`),
  KEY `cr_hd1` (`cr_refunded_hdemo_sk`),
  KEY `cr_c1` (`cr_refunded_customer_sk`),
  KEY `cr_cd1` (`cr_refunded_cdemo_sk`),
  KEY `cr_a1` (`cr_refunded_addr_sk`),
  KEY `cr_r` (`cr_reason_sk`),
  KEY `cr_cp` (`cr_catalog_page_sk`),
  KEY `cr_cc` (`cr_call_center_sk`),
  CONSTRAINT `cr_a1` FOREIGN KEY (`cr_refunded_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_a2` FOREIGN KEY (`cr_returning_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_c1` FOREIGN KEY (`cr_refunded_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_c2` FOREIGN KEY (`cr_returning_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_cc` FOREIGN KEY (`cr_call_center_sk`) REFERENCES `call_center` (`cc_call_center_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_cd1` FOREIGN KEY (`cr_refunded_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_cd2` FOREIGN KEY (`cr_returning_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_cp` FOREIGN KEY (`cr_catalog_page_sk`) REFERENCES `catalog_page` (`cp_catalog_page_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_d1` FOREIGN KEY (`cr_returned_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_hd1` FOREIGN KEY (`cr_refunded_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_hd2` FOREIGN KEY (`cr_returning_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_i` FOREIGN KEY (`cr_item_sk`) REFERENCES `item` (`i_item_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_r` FOREIGN KEY (`cr_reason_sk`) REFERENCES `reason` (`r_reason_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_sm` FOREIGN KEY (`cr_ship_mode_sk`) REFERENCES `ship_mode` (`sm_ship_mode_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_t` FOREIGN KEY (`cr_returned_time_sk`) REFERENCES `time_dim` (`t_time_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cr_w2` FOREIGN KEY (`cr_warehouse_sk`) REFERENCES `warehouse` (`w_warehouse_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:43:52
