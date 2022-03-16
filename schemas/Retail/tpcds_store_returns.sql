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
-- Table structure for table `store_returns`
--

DROP TABLE IF EXISTS `store_returns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `store_returns` (
  `sr_returned_date_sk` int(11) DEFAULT NULL,
  `sr_return_time_sk` int(11) DEFAULT NULL,
  `sr_item_sk` int(11) NOT NULL,
  `sr_customer_sk` int(11) DEFAULT NULL,
  `sr_cdemo_sk` int(11) DEFAULT NULL,
  `sr_hdemo_sk` int(11) DEFAULT NULL,
  `sr_addr_sk` int(11) DEFAULT NULL,
  `sr_store_sk` int(11) DEFAULT NULL,
  `sr_reason_sk` int(11) DEFAULT NULL,
  `sr_ticket_number` int(11) NOT NULL,
  `sr_return_quantity` int(11) DEFAULT NULL,
  `sr_return_amt` decimal(7,2) DEFAULT NULL,
  `sr_return_tax` decimal(7,2) DEFAULT NULL,
  `sr_return_amt_inc_tax` decimal(7,2) DEFAULT NULL,
  `sr_fee` decimal(7,2) DEFAULT NULL,
  `sr_return_ship_cost` decimal(7,2) DEFAULT NULL,
  `sr_refunded_cash` decimal(7,2) DEFAULT NULL,
  `sr_reversed_charge` decimal(7,2) DEFAULT NULL,
  `sr_store_credit` decimal(7,2) DEFAULT NULL,
  `sr_net_loss` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`sr_item_sk`,`sr_ticket_number`),
  KEY `sr_s` (`sr_store_sk`),
  KEY `sr_t` (`sr_return_time_sk`),
  KEY `sr_ret_d` (`sr_returned_date_sk`),
  KEY `sr_r` (`sr_reason_sk`),
  KEY `sr_hd` (`sr_hdemo_sk`),
  KEY `sr_c` (`sr_customer_sk`),
  KEY `sr_cd` (`sr_cdemo_sk`),
  KEY `sr_a` (`sr_addr_sk`),
  CONSTRAINT `sr_a` FOREIGN KEY (`sr_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sr_c` FOREIGN KEY (`sr_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sr_cd` FOREIGN KEY (`sr_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sr_hd` FOREIGN KEY (`sr_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sr_i` FOREIGN KEY (`sr_item_sk`) REFERENCES `item` (`i_item_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sr_r` FOREIGN KEY (`sr_reason_sk`) REFERENCES `reason` (`r_reason_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sr_ret_d` FOREIGN KEY (`sr_returned_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sr_s` FOREIGN KEY (`sr_store_sk`) REFERENCES `store` (`s_store_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sr_t` FOREIGN KEY (`sr_return_time_sk`) REFERENCES `time_dim` (`t_time_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:44:30
