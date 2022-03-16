-- MySQL dump 10.13  Distrib 5.7.37, for Linux (x86_64)
--
-- Host: relational.fit.cvut.cz    Database: stats
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
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `Id` int(11) NOT NULL,
  `PostTypeId` int(11) DEFAULT NULL,
  `AcceptedAnswerId` int(11) DEFAULT NULL,
  `CreaionDate` datetime DEFAULT NULL,
  `Score` int(11) DEFAULT NULL,
  `ViewCount` int(11) DEFAULT NULL,
  `Body` longtext DEFAULT NULL,
  `OwnerUserId` int(11) DEFAULT NULL,
  `LasActivityDate` datetime DEFAULT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Tags` varchar(255) DEFAULT NULL,
  `AnswerCount` int(11) DEFAULT NULL,
  `CommentCount` int(11) DEFAULT NULL,
  `FavoriteCount` int(11) DEFAULT NULL,
  `LastEditorUserId` int(11) DEFAULT NULL,
  `LastEditDate` datetime DEFAULT NULL,
  `CommunityOwnedDate` datetime DEFAULT NULL,
  `ParentId` int(11) DEFAULT NULL,
  `ClosedDate` datetime DEFAULT NULL,
  `OwnerDisplayName` varchar(255) DEFAULT NULL,
  `LastEditorDisplayName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `posts_Id_key` (`Id`),
  KEY `posts_ParentId_fkey` (`ParentId`),
  KEY `posts_OwnerUserId_fkey` (`OwnerUserId`),
  KEY `posts_LastEditorUserId_fkey` (`LastEditorUserId`),
  CONSTRAINT `posts_LastEditorUserId_fkey` FOREIGN KEY (`LastEditorUserId`) REFERENCES `users` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `posts_OwnerUserId_fkey` FOREIGN KEY (`OwnerUserId`) REFERENCES `users` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `posts_ParentId_fkey` FOREIGN KEY (`ParentId`) REFERENCES `posts` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
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

-- Dump completed on 2022-02-20 18:29:18
