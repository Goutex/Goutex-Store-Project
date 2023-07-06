CREATE DATABASE  IF NOT EXISTS `projeto1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `projeto1`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: projeto1
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `generosjogo`
--

DROP TABLE IF EXISTS `generosjogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generosjogo` (
  `idgeneroj` int NOT NULL AUTO_INCREMENT,
  `nomegeneroj` varchar(45) NOT NULL,
  `descricaogeneroj` varchar(150) NOT NULL,
  PRIMARY KEY (`idgeneroj`),
  UNIQUE KEY `nomegeneroj_UNIQUE` (`nomegeneroj`),
  UNIQUE KEY `idgenerosj_UNIQUE` (`idgeneroj`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generosjogo`
--

LOCK TABLES `generosjogo` WRITE;
/*!40000 ALTER TABLE `generosjogo` DISABLE KEYS */;
INSERT INTO `generosjogo` VALUES (1,'RPG','Jogo de Historia e Interpretação de Personagens'),(2,'Ação','Um jogo eletrônico de ação é um tipo de jogo eletrônico que desafia a velocidade, reflexo e raciocínio rápido do jogador.');
/*!40000 ALTER TABLE `generosjogo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jogos`
--

DROP TABLE IF EXISTS `jogos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jogos` (
  `idjogo` int NOT NULL AUTO_INCREMENT,
  `nomejogo` varchar(45) DEFAULT NULL,
  `descricaojogo` varchar(255) DEFAULT NULL,
  `idgeneroj` int DEFAULT NULL,
  PRIMARY KEY (`idjogo`),
  KEY `idgeneroj` (`idgeneroj`),
  CONSTRAINT `jogos_ibfk_1` FOREIGN KEY (`idgeneroj`) REFERENCES `generosjogo` (`idgeneroj`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jogos`
--

LOCK TABLES `jogos` WRITE;
/*!40000 ALTER TABLE `jogos` DISABLE KEYS */;
INSERT INTO `jogos` VALUES (1,'Elden Ring','O jogo de historia e construcao de personagem que joga poderzinho conta inimigos mortais.',1),(3,'Elden Ring 2','O jogo de historia e construcao de personagem que joga poderzinho conta inimigos mortais. (2.0)',1),(4,'Apex Legends','Jogo de battle royale e poderzinho com movimentacao insana e o melhor dos ttk\'s',2);
/*!40000 ALTER TABLE `jogos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-06 12:15:58
