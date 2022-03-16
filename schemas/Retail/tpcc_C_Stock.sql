-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: tpcc
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
-- Table structure for table `C_Stock`
--

DROP TABLE IF EXISTS `C_Stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `C_Stock` (
  `s_i_id` int(11) NOT NULL,
  `s_w_id` int(11) NOT NULL,
  `s_quantity` int(11) DEFAULT NULL,
  `s_dist_01` char(24) DEFAULT NULL,
  `s_dist_02` char(24) DEFAULT NULL,
  `s_dist_03` char(24) DEFAULT NULL,
  `s_dist_04` char(24) DEFAULT NULL,
  `s_dist_05` char(24) DEFAULT NULL,
  `s_dist_06` char(24) DEFAULT NULL,
  `s_dist_07` char(24) DEFAULT NULL,
  `s_dist_08` char(24) DEFAULT NULL,
  `s_dist_09` char(24) DEFAULT NULL,
  `s_dist_10` char(24) DEFAULT NULL,
  `s_ytd` int(11) DEFAULT NULL,
  `s_order_cnt` int(11) DEFAULT NULL,
  `s_remote_cnt` int(11) DEFAULT NULL,
  `s_data` char(50) DEFAULT NULL,
  PRIMARY KEY (`s_i_id`,`s_w_id`),
  UNIQUE KEY `C_Stock_I1` (`s_i_id`,`s_w_id`),
  KEY `s_w_id` (`s_w_id`),
  CONSTRAINT `C_Stock_ibfk_1` FOREIGN KEY (`s_i_id`) REFERENCES `C_Item` (`i_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `C_Stock_ibfk_2` FOREIGN KEY (`s_w_id`) REFERENCES `C_Warehouse` (`w_id`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 19:25:55
