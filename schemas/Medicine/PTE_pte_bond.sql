-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: PTE
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
-- Table structure for table `pte_bond`
--

DROP TABLE IF EXISTS `pte_bond`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pte_bond` (
  `drug_id` varchar(80) DEFAULT NULL,
  `atom_id1` varchar(80) NOT NULL,
  `atom_id2` varchar(80) NOT NULL,
  `Arg3` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`atom_id1`,`atom_id2`),
  KEY `pte_bond_drug_id` (`drug_id`) USING BTREE,
  KEY `pte_bond_atom_id1` (`atom_id1`) USING BTREE,
  KEY `pte_bond_atom_id2` (`atom_id2`) USING BTREE,
  CONSTRAINT `pte_bond_ibfk_1` FOREIGN KEY (`atom_id1`) REFERENCES `pte_atm` (`atom_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pte_bond_ibfk_2` FOREIGN KEY (`atom_id2`) REFERENCES `pte_atm` (`atom_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pte_bond_ibfk_3` FOREIGN KEY (`drug_id`) REFERENCES `pte_drug` (`drug_id`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 18:33:39
