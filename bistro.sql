CREATE DATABASE  IF NOT EXISTS `bistro` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish2_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bistro`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: bistro
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_local`
--

DROP TABLE IF EXISTS `tbl_local`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_local` (
  `Id_local` int NOT NULL AUTO_INCREMENT,
  `local` varchar(45) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`Id_local`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_local`
--

LOCK TABLES `tbl_local` WRITE;
/*!40000 ALTER TABLE `tbl_local` DISABLE KEYS */;
INSERT INTO `tbl_local` VALUES (1,'Belgrano'),(2,'Caballito'),(3,'Córdoba'),(4,'Mar del Plata'),(5,'Puerto Madero');
/*!40000 ALTER TABLE `tbl_local` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_reservas`
--

DROP TABLE IF EXISTS `tbl_reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_reservas` (
  `Id_reserva` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `nro_telefono` varchar(45) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `cant_comensales` int NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `local_Id` int NOT NULL,
  `preferencias` text COLLATE utf8mb3_spanish2_ci,
  `confirmacion` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Id_reserva`),
  KEY `fk_reservas_local_idx` (`local_Id`),
  CONSTRAINT `fk_reservas_local` FOREIGN KEY (`local_Id`) REFERENCES `tbl_local` (`Id_local`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_reservas`
--

LOCK TABLES `tbl_reservas` WRITE;
/*!40000 ALTER TABLE `tbl_reservas` DISABLE KEYS */;
INSERT INTO `tbl_reservas` VALUES (1,'Carlos Gómez','carlos.gomez@example.com','1122334455',2,'2024-07-10','20:00:00',1,'Vegetariano',0),(2,'Lucía Fernández','lucia.fernandez@example.com','2233445566',4,'2024-07-11','19:30:00',2,'Sin gluten',0),(3,'Martín Pérez','martin.perez@example.com','3344556677',3,'2024-07-12','18:45:00',3,'Mesa cerca de la ventana',0),(4,'Ana López','ana.lopez@example.com','4455667788',5,'2024-07-13','21:00:00',4,'Alta chair para bebé',0),(5,'José Martínez','jose.martinez@example.com','5566778899',2,'2024-07-14','20:30:00',5,'Sin lactosa',0);
/*!40000 ALTER TABLE `tbl_reservas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-24 20:32:04
