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
-- Table structure for table `web_sales`
--

DROP TABLE IF EXISTS `web_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `web_sales` (
  `ws_sold_date_sk` int(11) DEFAULT NULL,
  `ws_sold_time_sk` int(11) DEFAULT NULL,
  `ws_ship_date_sk` int(11) DEFAULT NULL,
  `ws_item_sk` int(11) NOT NULL,
  `ws_bill_customer_sk` int(11) DEFAULT NULL,
  `ws_bill_cdemo_sk` int(11) DEFAULT NULL,
  `ws_bill_hdemo_sk` int(11) DEFAULT NULL,
  `ws_bill_addr_sk` int(11) DEFAULT NULL,
  `ws_ship_customer_sk` int(11) DEFAULT NULL,
  `ws_ship_cdemo_sk` int(11) DEFAULT NULL,
  `ws_ship_hdemo_sk` int(11) DEFAULT NULL,
  `ws_ship_addr_sk` int(11) DEFAULT NULL,
  `ws_web_page_sk` int(11) DEFAULT NULL,
  `ws_web_site_sk` int(11) DEFAULT NULL,
  `ws_ship_mode_sk` int(11) DEFAULT NULL,
  `ws_warehouse_sk` int(11) DEFAULT NULL,
  `ws_promo_sk` int(11) DEFAULT NULL,
  `ws_order_number` int(11) NOT NULL,
  `ws_quantity` int(11) DEFAULT NULL,
  `ws_wholesale_cost` decimal(7,2) DEFAULT NULL,
  `ws_list_price` decimal(7,2) DEFAULT NULL,
  `ws_sales_price` decimal(7,2) DEFAULT NULL,
  `ws_ext_discount_amt` decimal(7,2) DEFAULT NULL,
  `ws_ext_sales_price` decimal(7,2) DEFAULT NULL,
  `ws_ext_wholesale_cost` decimal(7,2) DEFAULT NULL,
  `ws_ext_list_price` decimal(7,2) DEFAULT NULL,
  `ws_ext_tax` decimal(7,2) DEFAULT NULL,
  `ws_coupon_amt` decimal(7,2) DEFAULT NULL,
  `ws_ext_ship_cost` decimal(7,2) DEFAULT NULL,
  `ws_net_paid` decimal(7,2) DEFAULT NULL,
  `ws_net_paid_inc_tax` decimal(7,2) DEFAULT NULL,
  `ws_net_paid_inc_ship` decimal(7,2) DEFAULT NULL,
  `ws_net_paid_inc_ship_tax` decimal(7,2) DEFAULT NULL,
  `ws_net_profit` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`ws_item_sk`,`ws_order_number`),
  KEY `ws_ws` (`ws_web_site_sk`),
  KEY `ws_wp` (`ws_web_page_sk`),
  KEY `ws_w2` (`ws_warehouse_sk`),
  KEY `ws_t` (`ws_sold_time_sk`),
  KEY `ws_d2` (`ws_sold_date_sk`),
  KEY `ws_sm` (`ws_ship_mode_sk`),
  KEY `ws_s_hd` (`ws_ship_hdemo_sk`),
  KEY `ws_s_d` (`ws_ship_date_sk`),
  KEY `ws_s_c` (`ws_ship_customer_sk`),
  KEY `ws_s_cd` (`ws_ship_cdemo_sk`),
  KEY `ws_s_a` (`ws_ship_addr_sk`),
  KEY `ws_p` (`ws_promo_sk`),
  KEY `ws_b_hd` (`ws_bill_hdemo_sk`),
  KEY `ws_b_c` (`ws_bill_customer_sk`),
  KEY `ws_b_cd` (`ws_bill_cdemo_sk`),
  KEY `ws_b_a` (`ws_bill_addr_sk`),
  CONSTRAINT `ws_b_a` FOREIGN KEY (`ws_bill_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_b_c` FOREIGN KEY (`ws_bill_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_b_cd` FOREIGN KEY (`ws_bill_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_b_hd` FOREIGN KEY (`ws_bill_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_d2` FOREIGN KEY (`ws_sold_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_i` FOREIGN KEY (`ws_item_sk`) REFERENCES `item` (`i_item_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_p` FOREIGN KEY (`ws_promo_sk`) REFERENCES `promotion` (`p_promo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_s_a` FOREIGN KEY (`ws_ship_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_s_c` FOREIGN KEY (`ws_ship_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_s_cd` FOREIGN KEY (`ws_ship_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_s_d` FOREIGN KEY (`ws_ship_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_s_hd` FOREIGN KEY (`ws_ship_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_sm` FOREIGN KEY (`ws_ship_mode_sk`) REFERENCES `ship_mode` (`sm_ship_mode_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_t` FOREIGN KEY (`ws_sold_time_sk`) REFERENCES `time_dim` (`t_time_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_w2` FOREIGN KEY (`ws_warehouse_sk`) REFERENCES `warehouse` (`w_warehouse_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_wp` FOREIGN KEY (`ws_web_page_sk`) REFERENCES `web_page` (`wp_web_page_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ws_ws` FOREIGN KEY (`ws_web_site_sk`) REFERENCES `web_site` (`web_site_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:43:55
