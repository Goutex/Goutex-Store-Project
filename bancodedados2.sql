CREATE DATABASE  IF NOT EXISTS `projetinho` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `projetinho`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: projetinho
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `amigos`
--

DROP TABLE IF EXISTS `amigos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amigos` (
  `idamigo` varchar(20) NOT NULL,
  `nomeamigo` varchar(60) NOT NULL,
  PRIMARY KEY (`idamigo`),
  UNIQUE KEY `idamigos_UNIQUE` (`idamigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amigos`
--

LOCK TABLES `amigos` WRITE;
/*!40000 ALTER TABLE `amigos` DISABLE KEYS */;
/*!40000 ALTER TABLE `amigos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `baixados`
--

DROP TABLE IF EXISTS `baixados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baixados` (
  `idjogo` int NOT NULL,
  `jogos` varchar(45) NOT NULL,
  PRIMARY KEY (`idjogo`),
  UNIQUE KEY `idjogo_UNIQUE` (`idjogo`),
  UNIQUE KEY `jogos_UNIQUE` (`jogos`),
  KEY `jogos_idx` (`jogos`),
  CONSTRAINT `idjogo` FOREIGN KEY (`idjogo`) REFERENCES `jogos` (`idjogo`),
  CONSTRAINT `jogos` FOREIGN KEY (`jogos`) REFERENCES `jogos` (`nomejogo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baixados`
--

LOCK TABLES `baixados` WRITE;
/*!40000 ALTER TABLE `baixados` DISABLE KEYS */;
/*!40000 ALTER TABLE `baixados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cadastrouser`
--

DROP TABLE IF EXISTS `cadastrouser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cadastrouser` (
  `idcadastro` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  `usuario` varchar(20) DEFAULT NULL,
  `senha` varchar(20) DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idcadastro`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadastrouser`
--

LOCK TABLES `cadastrouser` WRITE;
/*!40000 ALTER TABLE `cadastrouser` DISABLE KEYS */;
/*!40000 ALTER TABLE `cadastrouser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generosjogo`
--

DROP TABLE IF EXISTS `generosjogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generosjogo` (
  `idgeneroj` int NOT NULL AUTO_INCREMENT,
  `descricaogeneroj` varchar(150) NOT NULL,
  `nomegeneroj` varchar(45) NOT NULL,
  PRIMARY KEY (`idgeneroj`),
  UNIQUE KEY `idestilojogo_UNIQUE` (`idgeneroj`),
  UNIQUE KEY `nomegeneroj_UNIQUE` (`nomegeneroj`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generosjogo`
--

LOCK TABLES `generosjogo` WRITE;
/*!40000 ALTER TABLE `generosjogo` DISABLE KEYS */;
INSERT INTO `generosjogo` VALUES (1,'Historia e Construcao de Personagem','RPG'),(2,'RPG JAPONES','JRPG'),(3,'Muito loucura e adrenalina doida tiro porrada e bomba','Ação');
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
  `nomejogo` varchar(45) NOT NULL,
  `descricaojogo` varchar(255) DEFAULT NULL,
  `idgeneroj` int DEFAULT NULL,
  PRIMARY KEY (`idjogo`),
  UNIQUE KEY `nomejogo_UNIQUE` (`nomejogo`),
  KEY `idgeneroj` (`idgeneroj`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jogos`
--

LOCK TABLES `jogos` WRITE;
/*!40000 ALTER TABLE `jogos` DISABLE KEYS */;
INSERT INTO `jogos` VALUES (2,'Apex Legends','Battle Royale com poderzinho e move insana',3),(5,'Elden Ring','Jogo mais dificil do mundo',1),(6,'Call of Duty','Jogo de sem mae de arrombado de sem tracking',3);
/*!40000 ALTER TABLE `jogos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil`
--

DROP TABLE IF EXISTS `perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfil` (
  `idcadastro` int NOT NULL,
  `baixados` varchar(45) NOT NULL,
  `favoritos` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcadastro`),
  UNIQUE KEY `idcadastro_UNIQUE` (`idcadastro`),
  UNIQUE KEY `baixados_UNIQUE` (`baixados`),
  KEY `baixados_idx` (`baixados`),
  CONSTRAINT `id_Cadastrinho` FOREIGN KEY (`idcadastro`) REFERENCES `cadastrouser` (`idcadastro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil`
--

LOCK TABLES `perfil` WRITE;
/*!40000 ALTER TABLE `perfil` DISABLE KEYS */;
/*!40000 ALTER TABLE `perfil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `nick` varchar(20) NOT NULL,
  `idcadastro` int DEFAULT NULL,
  PRIMARY KEY (`nick`),
  KEY `idcadastro_idx` (`idcadastro`),
  CONSTRAINT `idcadastro` FOREIGN KEY (`idcadastro`) REFERENCES `cadastrouser` (`idcadastro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-10 11:27:52
