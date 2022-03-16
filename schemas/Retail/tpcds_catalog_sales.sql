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
-- Table structure for table `catalog_sales`
--

DROP TABLE IF EXISTS `catalog_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catalog_sales` (
  `cs_sold_date_sk` int(11) DEFAULT NULL,
  `cs_sold_time_sk` int(11) DEFAULT NULL,
  `cs_ship_date_sk` int(11) DEFAULT NULL,
  `cs_bill_customer_sk` int(11) DEFAULT NULL,
  `cs_bill_cdemo_sk` int(11) DEFAULT NULL,
  `cs_bill_hdemo_sk` int(11) DEFAULT NULL,
  `cs_bill_addr_sk` int(11) DEFAULT NULL,
  `cs_ship_customer_sk` int(11) DEFAULT NULL,
  `cs_ship_cdemo_sk` int(11) DEFAULT NULL,
  `cs_ship_hdemo_sk` int(11) DEFAULT NULL,
  `cs_ship_addr_sk` int(11) DEFAULT NULL,
  `cs_call_center_sk` int(11) DEFAULT NULL,
  `cs_catalog_page_sk` int(11) DEFAULT NULL,
  `cs_ship_mode_sk` int(11) DEFAULT NULL,
  `cs_warehouse_sk` int(11) DEFAULT NULL,
  `cs_item_sk` int(11) NOT NULL,
  `cs_promo_sk` int(11) DEFAULT NULL,
  `cs_order_number` int(11) NOT NULL,
  `cs_quantity` int(11) DEFAULT NULL,
  `cs_wholesale_cost` decimal(7,2) DEFAULT NULL,
  `cs_list_price` decimal(7,2) DEFAULT NULL,
  `cs_sales_price` decimal(7,2) DEFAULT NULL,
  `cs_ext_discount_amt` decimal(7,2) DEFAULT NULL,
  `cs_ext_sales_price` decimal(7,2) DEFAULT NULL,
  `cs_ext_wholesale_cost` decimal(7,2) DEFAULT NULL,
  `cs_ext_list_price` decimal(7,2) DEFAULT NULL,
  `cs_ext_tax` decimal(7,2) DEFAULT NULL,
  `cs_coupon_amt` decimal(7,2) DEFAULT NULL,
  `cs_ext_ship_cost` decimal(7,2) DEFAULT NULL,
  `cs_net_paid` decimal(7,2) DEFAULT NULL,
  `cs_net_paid_inc_tax` decimal(7,2) DEFAULT NULL,
  `cs_net_paid_inc_ship` decimal(7,2) DEFAULT NULL,
  `cs_net_paid_inc_ship_tax` decimal(7,2) DEFAULT NULL,
  `cs_net_profit` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`cs_item_sk`,`cs_order_number`),
  KEY `cs_w` (`cs_warehouse_sk`),
  KEY `cs_t` (`cs_sold_time_sk`),
  KEY `cs_d2` (`cs_sold_date_sk`),
  KEY `cs_sm` (`cs_ship_mode_sk`),
  KEY `cs_s_hd` (`cs_ship_hdemo_sk`),
  KEY `cs_d1` (`cs_ship_date_sk`),
  KEY `cs_s_c` (`cs_ship_customer_sk`),
  KEY `cs_s_cd` (`cs_ship_cdemo_sk`),
  KEY `cs_s_a` (`cs_ship_addr_sk`),
  KEY `cs_p` (`cs_promo_sk`),
  KEY `cs_cp` (`cs_catalog_page_sk`),
  KEY `cs_cc` (`cs_call_center_sk`),
  KEY `cs_b_hd` (`cs_bill_hdemo_sk`),
  KEY `cs_b_c` (`cs_bill_customer_sk`),
  KEY `cs_b_cd` (`cs_bill_cdemo_sk`),
  KEY `cs_b_a` (`cs_bill_addr_sk`),
  CONSTRAINT `cs_b_a` FOREIGN KEY (`cs_bill_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_b_c` FOREIGN KEY (`cs_bill_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_b_cd` FOREIGN KEY (`cs_bill_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_b_hd` FOREIGN KEY (`cs_bill_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_cc` FOREIGN KEY (`cs_call_center_sk`) REFERENCES `call_center` (`cc_call_center_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_cp` FOREIGN KEY (`cs_catalog_page_sk`) REFERENCES `catalog_page` (`cp_catalog_page_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_d1` FOREIGN KEY (`cs_ship_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_d2` FOREIGN KEY (`cs_sold_date_sk`) REFERENCES `date_dim` (`d_date_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_i` FOREIGN KEY (`cs_item_sk`) REFERENCES `item` (`i_item_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_p` FOREIGN KEY (`cs_promo_sk`) REFERENCES `promotion` (`p_promo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_s_a` FOREIGN KEY (`cs_ship_addr_sk`) REFERENCES `customer_address` (`ca_address_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_s_c` FOREIGN KEY (`cs_ship_customer_sk`) REFERENCES `customer` (`c_customer_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_s_cd` FOREIGN KEY (`cs_ship_cdemo_sk`) REFERENCES `customer_demographics` (`cd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_s_hd` FOREIGN KEY (`cs_ship_hdemo_sk`) REFERENCES `household_demographics` (`hd_demo_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_sm` FOREIGN KEY (`cs_ship_mode_sk`) REFERENCES `ship_mode` (`sm_ship_mode_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_t` FOREIGN KEY (`cs_sold_time_sk`) REFERENCES `time_dim` (`t_time_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cs_w` FOREIGN KEY (`cs_warehouse_sk`) REFERENCES `warehouse` (`w_warehouse_sk`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2022-02-20 18:44:06
