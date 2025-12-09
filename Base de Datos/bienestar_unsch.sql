-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: bienestar_unsch
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `idAdmin` int NOT NULL AUTO_INCREMENT,
  `idUsuario` int NOT NULL,
  `area` varchar(100) DEFAULT NULL,
  `cargo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idAdmin`),
  KEY `idUsuario` (`idUsuario`),
  CONSTRAINT `administrador_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
INSERT INTO `administrador` VALUES (2,5,'Sistemas','Administrador General'),(3,6,'Recursos Humanos','Coordinador'),(4,5,'Sistemas','Administrador General'),(5,10,'bineastar universitario ','coordinador ');
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atencionmedica`
--

DROP TABLE IF EXISTS `atencionmedica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atencionmedica` (
  `idAtencion` int NOT NULL AUTO_INCREMENT,
  `idCita` int NOT NULL,
  `idPersonal` int NOT NULL,
  `diagnostico` text,
  `fechaAtencion` datetime DEFAULT NULL,
  `observacion` text,
  `tratamiento` text,
  PRIMARY KEY (`idAtencion`),
  KEY `idCita` (`idCita`),
  KEY `idPersonal` (`idPersonal`),
  CONSTRAINT `atencionmedica_ibfk_1` FOREIGN KEY (`idCita`) REFERENCES `cita` (`idCita`),
  CONSTRAINT `atencionmedica_ibfk_2` FOREIGN KEY (`idPersonal`) REFERENCES `personalsalud` (`idPersonal`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atencionmedica`
--

LOCK TABLES `atencionmedica` WRITE;
/*!40000 ALTER TABLE `atencionmedica` DISABLE KEYS */;
INSERT INTO `atencionmedica` VALUES (4,1,1,'Gripe viral moderada','2025-11-30 04:04:13','Indica fiebre y malestar general','Paracetamol 500mg cada 8h por 5 días'),(5,1,1,'Gripe viral','2025-11-30 04:07:51','Fiebre y dolor general','Paracetamol 500mg'),(6,1,1,'Gripe viral','2025-11-30 04:07:53','Fiebre y dolor general','Paracetamol 500mg');
/*!40000 ALTER TABLE `atencionmedica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cita`
--

DROP TABLE IF EXISTS `cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cita` (
  `idCita` int NOT NULL AUTO_INCREMENT,
  `idEstudiante` int NOT NULL,
  `especialidad` varchar(100) NOT NULL,
  `fechaCita` date NOT NULL,
  `horaCita` time NOT NULL,
  `estado` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idCita`),
  KEY `idEstudiante` (`idEstudiante`),
  CONSTRAINT `cita_ibfk_1` FOREIGN KEY (`idEstudiante`) REFERENCES `estudiante` (`idEstudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cita`
--

LOCK TABLES `cita` WRITE;
/*!40000 ALTER TABLE `cita` DISABLE KEYS */;
INSERT INTO `cita` VALUES (1,1,'Medicina General','2025-12-15','09:30:00','Cancelada'),(2,1,'Odontología','2025-12-12','09:10:00','Cancelada'),(3,1,'Odontología','2025-12-12','09:10:00','Cancelada'),(4,1,'Odontología','2025-12-12','09:10:00','Cancelada'),(5,1,'Obstetricia','2025-12-05','03:52:00','Programada'),(6,1,'Enfermería','2025-12-19','04:57:00','Programada'),(7,2,'Odontología','2025-12-19','05:51:00','Cancelada'),(8,2,'Odontología','2025-12-19','05:51:00','Pendiente'),(9,2,'Medicina General','2025-12-12','07:32:00','Atendida'),(10,3,'Medicina General','2025-12-02','09:40:00','Atendida');
/*!40000 ALTER TABLE `cita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `derivacion`
--

DROP TABLE IF EXISTS `derivacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `derivacion` (
  `idDerivacion` int NOT NULL AUTO_INCREMENT,
  `idAtencion` int NOT NULL,
  `especialidadDestino` varchar(100) DEFAULT NULL,
  `fechaDerivacion` date DEFAULT NULL,
  `comentarios` text,
  PRIMARY KEY (`idDerivacion`),
  KEY `idAtencion` (`idAtencion`),
  CONSTRAINT `derivacion_ibfk_1` FOREIGN KEY (`idAtencion`) REFERENCES `atencionmedica` (`idAtencion`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `derivacion`
--

LOCK TABLES `derivacion` WRITE;
/*!40000 ALTER TABLE `derivacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `derivacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiante`
--

DROP TABLE IF EXISTS `estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante` (
  `idEstudiante` int NOT NULL AUTO_INCREMENT,
  `idUsuario` int NOT NULL,
  `codigo` varchar(20) DEFAULT NULL,
  `escuela` varchar(150) DEFAULT NULL,
  `ciclo` varchar(10) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `dni` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idEstudiante`),
  KEY `idUsuario` (`idUsuario`),
  CONSTRAINT `estudiante_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante`
--

LOCK TABLES `estudiante` WRITE;
/*!40000 ALTER TABLE `estudiante` DISABLE KEYS */;
INSERT INTO `estudiante` VALUES (1,2,NULL,NULL,NULL,NULL,NULL,NULL),(2,13,'202412345','Ingeniería de Sistemas','V','Luis','Huamán','12345678'),(3,14,'202412345','Ingeniería de Sistemas','V','Juan','Pérez',NULL),(4,14,'202512345','Ingeniería de Sistemas','V','Juan','Pérez','78945612'),(5,14,'202512345','Ingeniería de Sistemas','V','Juan','Pérez','78945612');
/*!40000 ALTER TABLE `estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historialmedico`
--

DROP TABLE IF EXISTS `historialmedico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historialmedico` (
  `idHistorial` int NOT NULL AUTO_INCREMENT,
  `idEstudiante` int NOT NULL,
  `descripcion` text,
  `fechaRegistro` datetime DEFAULT NULL,
  PRIMARY KEY (`idHistorial`),
  KEY `idEstudiante` (`idEstudiante`),
  CONSTRAINT `historialmedico_ibfk_1` FOREIGN KEY (`idEstudiante`) REFERENCES `estudiante` (`idEstudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historialmedico`
--

LOCK TABLES `historialmedico` WRITE;
/*!40000 ALTER TABLE `historialmedico` DISABLE KEYS */;
INSERT INTO `historialmedico` VALUES (1,1,'Paciente presenta dolor de cabeza.',NULL),(2,1,'Control actualizado.','2025-11-30 09:42:25'),(3,1,'Dolor de cabeza. Se recomienda descanso.','2025-12-09 03:44:16'),(5,2,'Atención por dolor de cabeza. Se recetó paracetamol.',NULL),(6,3,'Control general. Paciente estable.','2025-12-09 07:12:01'),(7,3,'Consulta odontológica. Limpieza dental.','2025-12-09 07:12:01');
/*!40000 ALTER TABLE `historialmedico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil`
--

DROP TABLE IF EXISTS `perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfil` (
  `idPerfil` int NOT NULL AUTO_INCREMENT,
  `direccion` varchar(255) DEFAULT NULL,
  `dni` varchar(20) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `genero` varchar(20) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idPerfil`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil`
--

LOCK TABLES `perfil` WRITE;
/*!40000 ALTER TABLE `perfil` DISABLE KEYS */;
INSERT INTO `perfil` VALUES (2,'Ayacucho','12345678','2002-05-10','Masculino','987654321'),(3,'Ayacucho','87654321','1995-10-20','Femenino','987111222'),(4,'Ayacucho','44556677','1990-01-05','Masculino','999888777'),(5,NULL,NULL,NULL,NULL,NULL),(6,NULL,NULL,NULL,NULL,NULL),(7,NULL,NULL,NULL,NULL,NULL),(8,NULL,NULL,NULL,NULL,NULL),(9,NULL,NULL,NULL,NULL,NULL),(10,NULL,NULL,NULL,NULL,NULL),(11,NULL,'65432198',NULL,NULL,NULL),(12,'Ayacucho','78945612','2002-08-20','Masculino','912345678'),(13,'Ayacucho','11223344','1980-05-10','Masculino','987654321'),(14,'Ayacucho','78945612','2000-08-15','Masculino','987654321');
/*!40000 ALTER TABLE `perfil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personalsalud`
--

DROP TABLE IF EXISTS `personalsalud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personalsalud` (
  `idPersonal` int NOT NULL AUTO_INCREMENT,
  `idUsuario` int NOT NULL,
  `especialidad` varchar(100) DEFAULT NULL,
  `nroColegiatura` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idPersonal`),
  KEY `idUsuario` (`idUsuario`),
  CONSTRAINT `personalsalud_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personalsalud`
--

LOCK TABLES `personalsalud` WRITE;
/*!40000 ALTER TABLE `personalsalud` DISABLE KEYS */;
INSERT INTO `personalsalud` VALUES (1,2,'Medicina General','COL-12345'),(2,4,'Medicina General',NULL),(3,11,'Odontología',NULL),(4,12,'Odontología',NULL),(5,3,'Medicina General','COL-99999'),(6,15,'Medicina General','COL-998877');
/*!40000 ALTER TABLE `personalsalud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reporte`
--

DROP TABLE IF EXISTS `reporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reporte` (
  `idReporte` int NOT NULL AUTO_INCREMENT,
  `idAdmin` int NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `dni` varchar(20) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `genero` varchar(20) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idReporte`),
  KEY `idAdmin` (`idAdmin`),
  CONSTRAINT `reporte_ibfk_1` FOREIGN KEY (`idAdmin`) REFERENCES `administrador` (`idAdmin`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reporte`
--

LOCK TABLES `reporte` WRITE;
/*!40000 ALTER TABLE `reporte` DISABLE KEYS */;
/*!40000 ALTER TABLE `reporte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `idRol` int NOT NULL AUTO_INCREMENT,
  `nombreRol` varchar(50) NOT NULL,
  `permisos` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (1,'Estudiante','Puede reservar citas y ver su historial'),(2,'Personal Salud','Puede atender citas y registrar diagnósticos'),(3,'Administrador','Puede gestionar usuarios y ver reportes');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `contrasena` varchar(255) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `isUser` int DEFAULT '1',
  `tipoUsuario` varchar(50) NOT NULL,
  `idPerfil` int DEFAULT NULL,
  `idRol` int DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `correo` (`correo`),
  KEY `idPerfil` (`idPerfil`),
  KEY `idRol` (`idRol`),
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`idPerfil`) REFERENCES `perfil` (`idPerfil`),
  CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`idRol`) REFERENCES `rol` (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (2,'123456','test1@gmail.com',1,'estudiante',2,1),(3,'123456','doctor1@gmail.com',1,'personal',NULL,2),(4,'abc123','doctor@gmail.com',1,'personal',3,1),(5,'admin123','admin@gmail.com',1,'administrador',4,1),(6,'admin123','admin@correo.com',1,'administrador',NULL,NULL),(9,'123456','sofia@unsch.edu.pe',1,'estudiante',7,1),(10,'987564','jhonatan.27@unsch.edu.pe',1,'administrador',8,1),(11,'357159','andrea56@gmail.com',1,'personal',9,1),(12,'987654','elio159@unsch.edu.pe',1,'personal',10,1),(13,'123456','lhuaman@unsch.edu.pe',1,'estudiante',11,1),(14,'123456','juan.perez@unsch.edu.pe',1,'estudiante',12,1),(15,'doctor123','doctor.general@unsch.edu.pe',1,'personal',13,2);
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

-- Dump completed on 2025-12-09 16:57:10
