-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: nations
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
-- Table structure for table `stat`
--

DROP TABLE IF EXISTS `stat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stat` (
  `country_id` int(11) NOT NULL,
  `telephone` int(11) DEFAULT NULL,
  `agriculturalpop` int(11) DEFAULT NULL,
  `energyconsume` int(11) DEFAULT NULL,
  `illiterates` int(11) DEFAULT NULL,
  `GNP` int(11) DEFAULT NULL,
  `popxenergabs` int(11) DEFAULT NULL,
  `incomeabs` int(11) DEFAULT NULL,
  `popabs` int(11) DEFAULT NULL,
  `unassessment` int(11) DEFAULT NULL,
  `defenseexpabs` int(11) DEFAULT NULL,
  `englishtitles` int(11) DEFAULT NULL,
  `blocmembership0` int(11) DEFAULT NULL,
  `usaidreceived` int(11) DEFAULT NULL,
  `freedomofopposition0` int(11) DEFAULT NULL,
  `IFCandIBRD` int(11) DEFAULT NULL,
  `threats` int(11) DEFAULT NULL,
  `accusations` int(11) DEFAULT NULL,
  `killedforeignviolence` int(11) DEFAULT NULL,
  `militaryaction` int(11) DEFAULT NULL,
  `protests` int(11) DEFAULT NULL,
  `killeddomesticviolence` int(11) DEFAULT NULL,
  `riots` int(11) DEFAULT NULL,
  `purges` int(11) DEFAULT NULL,
  `demonstrations` int(11) DEFAULT NULL,
  `catholics` int(11) DEFAULT NULL,
  `airdistance` int(11) DEFAULT NULL,
  `medicinengo` int(11) DEFAULT NULL,
  `diplomatexpelled` int(11) DEFAULT NULL,
  `divorces` int(11) DEFAULT NULL,
  `popn/land` int(11) DEFAULT NULL,
  `arable` int(11) DEFAULT NULL,
  `area` int(11) DEFAULT NULL,
  `roadlength` int(11) DEFAULT NULL,
  `railroadlength` int(11) DEFAULT NULL,
  `religions` int(11) DEFAULT NULL,
  `immigrants/migrants` int(11) DEFAULT NULL,
  `rainfall` int(11) DEFAULT NULL,
  `largestrelgn` int(11) DEFAULT NULL,
  `runningwater` int(11) DEFAULT NULL,
  `foreigncollegestud` int(11) DEFAULT NULL,
  `neutralblock` int(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `religioustitles` int(11) DEFAULT NULL,
  `emigrants` int(11) DEFAULT NULL,
  `seabornegoods` int(11) DEFAULT NULL,
  `lawngos` int(11) DEFAULT NULL,
  `unemployed` int(11) DEFAULT NULL,
  `export` int(11) DEFAULT NULL,
  `languages` int(11) DEFAULT NULL,
  `largestlang` int(11) DEFAULT NULL,
  `ethnicgrps` int(11) DEFAULT NULL,
  `economicaidtaken` int(11) DEFAULT NULL,
  `techassistancetaken` int(11) DEFAULT NULL,
  `goveducationspend` int(11) DEFAULT NULL,
  `femaleworkers` int(11) DEFAULT NULL,
  `exports` int(11) DEFAULT NULL,
  `foreignmail` int(11) DEFAULT NULL,
  `imports` int(11) DEFAULT NULL,
  `caloriesconsumed` int(11) DEFAULT NULL,
  `protein` int(11) DEFAULT NULL,
  `russiantitles` int(11) DEFAULT NULL,
  `militarypersonnel` int(11) DEFAULT NULL,
  `investments` int(11) DEFAULT NULL,
  `politicalparties` int(11) DEFAULT NULL,
  `artsculturengo` int(11) DEFAULT NULL,
  `communistparty` int(11) DEFAULT NULL,
  `govspending` int(11) DEFAULT NULL,
  `monarchy` int(11) DEFAULT NULL,
  `primaryschool` int(11) DEFAULT NULL,
  `govchangelegal0` int(11) DEFAULT NULL,
  `legitgov0` int(11) DEFAULT NULL,
  `largestethnic` int(11) DEFAULT NULL,
  `assassinations` int(11) DEFAULT NULL,
  `majgovcrisis` int(11) DEFAULT NULL,
  `unpaymentdelinq` int(11) DEFAULT NULL,
  `balancepayments` int(11) DEFAULT NULL,
  `balanceinvestments` int(11) DEFAULT NULL,
  `systemstyle0` int(11) DEFAULT NULL,
  `constitutional0` int(11) DEFAULT NULL,
  `electoralsystem0` int(11) DEFAULT NULL,
  `noncommunist` int(11) DEFAULT NULL,
  `politicalleadership0` int(11) DEFAULT NULL,
  `horizontalpower0` int(11) DEFAULT NULL,
  `military0` int(11) DEFAULT NULL,
  `bureaucracy0` int(11) DEFAULT NULL,
  `censorship0` int(11) DEFAULT NULL,
  `geographyx` int(11) DEFAULT NULL,
  `geographyy` int(11) DEFAULT NULL,
  `geographyz` int(11) DEFAULT NULL,
  `blocmembership1` int(11) DEFAULT NULL,
  `blocmembership2` int(11) DEFAULT NULL,
  `freedomofopposition1` int(11) DEFAULT NULL,
  `freedomofopposition2` int(11) DEFAULT NULL,
  `govchangelegal1` int(11) DEFAULT NULL,
  `govchangelegal2` int(11) DEFAULT NULL,
  `legitgov1` int(11) DEFAULT NULL,
  `systemstyle1` int(11) DEFAULT NULL,
  `systemstyle2` int(11) DEFAULT NULL,
  `constitutional1` int(11) DEFAULT NULL,
  `constitutional2` int(11) DEFAULT NULL,
  `electoralsystem1` int(11) DEFAULT NULL,
  `electoralsystem2` int(11) DEFAULT NULL,
  `politicalleadership1` int(11) DEFAULT NULL,
  `politicalleadership2` int(11) DEFAULT NULL,
  `horizontalpower2` int(11) DEFAULT NULL,
  `military1` int(11) DEFAULT NULL,
  `military2` int(11) DEFAULT NULL,
  `bureaucracy1` int(11) DEFAULT NULL,
  `bureaucracy2` int(11) DEFAULT NULL,
  `censorship1` int(11) DEFAULT NULL,
  `censorship2` int(11) DEFAULT NULL,
  PRIMARY KEY (`country_id`),
  KEY `country_id'` (`country_id`)
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

-- Dump completed on 2022-02-20 19:42:56
