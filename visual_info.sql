-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: visual
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `information`
--

DROP TABLE IF EXISTS `information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `information` (
  `value` double DEFAULT NULL,
  `city` text DEFAULT NULL,
  `occupation` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `information`
--

LOCK TABLES `information` WRITE;
/*!40000 ALTER TABLE `information` DISABLE KEYS */;
INSERT INTO `information` VALUES (41.48,'Salt Lake City','Computer Programmer'),(120.03,'Salt Lake City','Physician'),(24.78,'Salt Lake City','Roofer'),(15.78,'Salt Lake City','Retail Sales Person'),(42.82,'Salt Lake City','Detective'),(43.53,'Denver','Computer Programmer'),(119.46,'Denver','Physician'),(21.33,'Denver','Roofer'),(16.33,'Denver','Retail Sales Person'),(47.86,'Denver','Detective'),(40.15,'El Paso','Computer Programmer'),(113.76,'El Paso','Physician'),(15.54,'El Paso','Roofer'),(11.77,'El Paso','Retail Sales Person'),(42.56,'El Paso','Detective'),(44.18,'Phoenix','Computer Programmer'),(117.44,'Phoenix','Physician'),(19.57,'Phoenix','Roofer'),(15.31,'Phoenix','Retail Sales Person'),(41.9,'Phoenix','Detective'),(41.89,'Pittsburg','Computer Programmer'),(61.88,'Pittsburg','Physician'),(21.76,'Pittsburg','Roofer'),(14.07,'Pittsburg','Retail Sales Person'),(42.1,'Pittsburg','Detective');
/*!40000 ALTER TABLE `information` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-08 16:24:23
