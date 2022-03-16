-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: NBA
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
-- Table structure for table `joined_drafted_all_players_original`
--

DROP TABLE IF EXISTS `joined_drafted_all_players_original`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `joined_drafted_all_players_original` (
  `ID` int(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `draft_g` int(11) DEFAULT NULL,
  `mp` int(11) DEFAULT NULL,
  `draft_fg` int(11) DEFAULT NULL,
  `fga` int(11) DEFAULT NULL,
  `3p` int(11) DEFAULT NULL,
  `3pa` int(11) DEFAULT NULL,
  `draft_ft` int(11) DEFAULT NULL,
  `fta` int(11) DEFAULT NULL,
  `orb` int(11) DEFAULT NULL,
  `draft_trb` int(11) DEFAULT NULL,
  `draft_ast` int(11) DEFAULT NULL,
  `draft_stl` int(11) DEFAULT NULL,
  `draft_blk` int(11) DEFAULT NULL,
  `draft_tov` int(11) DEFAULT NULL,
  `draft_pf` int(11) DEFAULT NULL,
  `draft_pts` int(11) DEFAULT NULL,
  `fg_per` double DEFAULT NULL,
  `3p_per` int(11) DEFAULT NULL,
  `ft_per` double DEFAULT NULL,
  `mp_per` double DEFAULT NULL,
  `pts_per` double DEFAULT NULL,
  `trb_per` double DEFAULT NULL,
  `ast_per` double DEFAULT NULL,
  `season` text DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `position` text DEFAULT NULL,
  `shoots` text DEFAULT NULL,
  `born` text DEFAULT NULL,
  `draft_year` int(11) DEFAULT NULL,
  `pk` int(11) DEFAULT NULL,
  `amature_honor` int(11) DEFAULT NULL,
  `college` text DEFAULT NULL,
  `raw_data` int(11) DEFAULT NULL,
  `career_g` int(11) DEFAULT NULL,
  `career_per` double DEFAULT NULL,
  `career_ws` double DEFAULT NULL,
  `career_ws48` double DEFAULT NULL
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

-- Dump completed on 2022-02-20 19:35:05
