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
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `i_item_sk` int(11) NOT NULL,
  `i_item_id` char(16) NOT NULL,
  `i_rec_start_date` date DEFAULT NULL,
  `i_rec_end_date` date DEFAULT NULL,
  `i_item_desc` varchar(200) DEFAULT NULL,
  `i_current_price` decimal(7,2) DEFAULT NULL,
  `i_wholesale_cost` decimal(7,2) DEFAULT NULL,
  `i_brand_id` int(11) DEFAULT NULL,
  `i_brand` char(50) DEFAULT NULL,
  `i_class_id` int(11) DEFAULT NULL,
  `i_class` char(50) DEFAULT NULL,
  `i_category_id` int(11) DEFAULT NULL,
  `i_category` char(50) DEFAULT NULL,
  `i_manufact_id` int(11) DEFAULT NULL,
  `i_manufact` char(50) DEFAULT NULL,
  `i_size` char(20) DEFAULT NULL,
  `i_formulation` char(20) DEFAULT NULL,
  `i_color` char(20) DEFAULT NULL,
  `i_units` char(10) DEFAULT NULL,
  `i_container` char(10) DEFAULT NULL,
  `i_manager_id` int(11) DEFAULT NULL,
  `i_product_name` char(50) DEFAULT NULL,
  PRIMARY KEY (`i_item_sk`)
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

-- Dump completed on 2022-02-20 18:44:23
