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
-- Table structure for table `store_sales`
--

DROP TABLE IF EXISTS `store_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `store_sales` (
  `ss_sold_date_sk` int(11) DEFAULT NULL,
  `ss_sold_time_sk` int(11) DEFAULT NULL,
  `ss_item_sk` int(11) NOT NULL,
  `ss_customer_sk` int(11) DEFAULT NULL,
  `ss_cdemo_sk` int(11) DEFAULT NULL,
  `ss_hdemo_sk` int(11) DEFAULT NULL,
  `ss_addr_sk` int(11) DEFAULT NULL,
  `ss_store_sk` int(11) DEFAULT NULL,
  `ss_promo_sk` int(11) DEFAULT NULL,
  `ss_ticket_number` int(11) NOT NULL,
  `ss_quantity` int(11) DEFAULT NULL,
  `ss_wholesale_cost` decimal(7,2) DEFAULT NULL,
  `ss_list_price` decimal(7,2) DEFAULT NULL,
  `ss_sales_price` decimal(7,2) DEFAULT NULL,
  `ss_ext_discount_amt` decimal(7,2) DEFAULT NULL,
  `ss_ext_sales_price` decimal(7,2) DEFAULT NULL,
  `ss_ext_wholesale_cost` decimal(7,2) DEFAULT NULL,
  `ss_ext_list_price` decimal(7,2) DEFAULT NULL,
  `ss_ext_tax` decimal(7,2) DEFAULT NULL,
  `ss_coupon_amt` decimal(7,2) DEFAULT NULL,
  `ss_net_paid` decimal(7,2) DEFAULT NULL,
  `ss_net_paid_inc_tax` decimal(7,2) DEFAULT NULL,
  `ss_net_profit` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`ss_item_sk`,`ss_ticket_number`),
  KEY `ss_s` (`ss_store_sk`),
  KEY `ss_t` (`ss_sold_time_sk`),
  KEY `ss_d` (`ss_sold_date_sk`),
  KEY `ss_p` (`ss_promo_sk`),
  KEY `ss_hd` (`ss_hdemo_sk`),
  KEY `ss_c` (`ss_customer_sk`),
  KEY `ss_cd` (`ss_cdemo_sk`),
  KEY `ss_a` (`ss_addr_sk`),
  CONSTRAINT `ss_a` FOREIGN KEY (`ss_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ss_c` FOREIGN KEY (`ss_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ss_cd` FOREIGN KEY (`ss_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ss_d` FOREIGN KEY (`ss_sold_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ss_hd` FOREIGN KEY (`ss_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ss_i` FOREIGN KEY (`ss_item_sk`) REFERENCES `item` (`i_item_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ss_p` FOREIGN KEY (`ss_promo_sk`) REFERENCES `promotion` (`p_promo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ss_s` FOREIGN KEY (`ss_store_sk`) REFERENCES `store` (`s_store_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ss_t` FOREIGN KEY (`ss_sold_time_sk`) REFERENCES `time_dim` (`t_time_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:43:28
