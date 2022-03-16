-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: lahman_2014
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
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `lahmanID` int(11) NOT NULL,
  `playerID` varchar(9) DEFAULT NULL,
  `managerID` varchar(10) DEFAULT NULL,
  `hofID` varchar(10) DEFAULT NULL,
  `birthYear` int(11) DEFAULT NULL,
  `birthMonth` int(11) DEFAULT NULL,
  `birthDay` int(11) DEFAULT NULL,
  `birthCountry` varchar(50) DEFAULT NULL,
  `birthState` varchar(2) DEFAULT NULL,
  `birthCity` varchar(50) DEFAULT NULL,
  `deathYear` int(11) DEFAULT NULL,
  `deathMonth` int(11) DEFAULT NULL,
  `deathDay` int(11) DEFAULT NULL,
  `deathCountry` varchar(50) DEFAULT NULL,
  `deathState` varchar(2) DEFAULT NULL,
  `deathCity` varchar(50) DEFAULT NULL,
  `nameFirst` varchar(50) DEFAULT NULL,
  `nameLast` varchar(50) DEFAULT NULL,
  `nameNote` varchar(255) DEFAULT NULL,
  `nameGiven` varchar(255) DEFAULT NULL,
  `nameNick` varchar(255) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `bats` varchar(1) DEFAULT NULL,
  `throws` varchar(1) DEFAULT NULL,
  `debut` varchar(10) DEFAULT NULL,
  `finalGame` varchar(10) DEFAULT NULL,
  `college` varchar(50) DEFAULT NULL,
  `lahman40ID` varchar(9) DEFAULT NULL,
  `lahman45ID` varchar(9) DEFAULT NULL,
  `retroID` varchar(9) DEFAULT NULL,
  `holtzID` varchar(9) DEFAULT NULL,
  `bbrefID` varchar(9) DEFAULT NULL,
  PRIMARY KEY (`lahmanID`),
  KEY `players_playerID` (`playerID`),
  KEY `players_hofID` (`hofID`),
  KEY `players_hofID_2` (`hofID`),
  CONSTRAINT `players_ibfk_1` FOREIGN KEY (`hofID`) REFERENCES `halloffame` (`hofID`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 18:38:24
