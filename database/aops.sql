-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: aops
-- ------------------------------------------------------
-- Server version	5.1.73-log

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
-- Table structure for table `cabinet`
--

DROP TABLE IF EXISTS `cabinet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cabinet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `info` varchar(255) DEFAULT NULL COMMENT '机柜信息',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (11,'1号机柜'),(12,'2号机柜'),(13,'3号机柜'),(14,'4号机柜'),(15,'5号机柜'),(27,'村落'),(28,'茜'),(29,'茜2'),(30,'茜23');
/*!40000 ALTER TABLE `cabinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb`
--

DROP TABLE IF EXISTS `cmdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `appliction` varchar(255) NOT NULL COMMENT '应用信息',
  `ip` varchar(255) NOT NULL COMMENT 'IP地址',
  `port` int(255) NOT NULL,
  `username` varchar(255) NOT NULL COMMENT 'ssh用户名',
  `password` varchar(255) NOT NULL COMMENT 'ssh密码',
  `cpu` int(11) DEFAULT NULL,
  `mem` int(11) DEFAULT NULL,
  `disk` int(11) DEFAULT NULL,
  `room_id` int(11) DEFAULT NULL,
  `cabinet_id` int(11) DEFAULT NULL,
  `location` int(11) DEFAULT NULL COMMENT '机位信息',
  PRIMARY KEY (`id`),
  KEY `room_id` (`room_id`),
  KEY `cabinet_id` (`cabinet_id`),
  CONSTRAINT `cabinet_id` FOREIGN KEY (`cabinet_id`) REFERENCES `cabinet` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `room_id` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb`
--

LOCK TABLES `cmdb` WRITE;
/*!40000 ALTER TABLE `cmdb` DISABLE KEYS */;
INSERT INTO `cmdb` VALUES (7,'load-nginx','192.168.100.50',22,'root','zuoloveyou',4,4,300,1,11,1),(8,'web1','192.168.100.51',22,'root','zuoloveyou',4,4,300,1,11,2),(9,'web2','192.168.100.58',22,'root','zuoloveyou',4,4,300,1,13,1),(10,'数据库','192.168.100.88',22,'root','zuoloveyou',2,2,200,1,11,2);
/*!40000 ALTER TABLE `cmdb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message_log`
--

DROP TABLE IF EXISTS `message_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` bigint(20) NOT NULL,
  `content` varchar(255) NOT NULL COMMENT '短信内容',
  `time` datetime DEFAULT NULL COMMENT '发送时间',
  `status` tinyint(4) DEFAULT NULL COMMENT '发送状态',
  PRIMARY KEY (`id`,`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message_log`
--

LOCK TABLES `message_log` WRITE;
/*!40000 ALTER TABLE `message_log` DISABLE KEYS */;
INSERT INTO `message_log` VALUES (4,13720027400,'【京峰课堂】尊敬的王兵:我们将于晚上8点进行python上课，上课内容为[到了你就知道],请准时上课。',NULL,1),(5,13434111885,'【京峰课堂】尊敬的黄学新:我们将于晚上8点进行python上课，上课内容为[到了你就知道],请准时上课。',NULL,1),(6,18706170878,'【京峰课堂】尊敬的梁琨:我们将于晚上8点进行python上课，上课内容为[到了你就知道],请准时上课。',NULL,1),(7,13720027400,'【京峰课堂】尊敬的王兵:我们将于晚上8点进行python上课，上课内容为[到了你就知道],请准时上课。',NULL,1),(8,13434111885,'【京峰课堂】尊敬的黄学新:我们将于晚上8点进行python上课，上课内容为[到了你就知道],请准时上课。',NULL,1),(9,187061708788,'【京峰课堂】尊敬的梁琨:我们将于晚上8点进行python上课，上课内容为[到了你就知道],请准时上课。',NULL,0),(14,13720027400,'【京峰课堂】尊敬的王兵:我们将于晚上8点进行python上课，上课内容为[【京峰课堂】尊敬的{username}:我们将于{time}进行{class_type}上课，上课内容为[{content}],请准时上课。],请准时上课。',NULL,0),(15,13434111885,'【京峰课堂】尊敬的黄学新:我们将于晚上8点进行python上课，上课内容为[【京峰课堂】尊敬的{username}:我们将于{time}进行{class_type}上课，上课内容为[{content}],请准时上课。],请准时上课。',NULL,0),(16,18706170878,'【京峰课堂】尊敬的梁琨:我们将于晚上8点进行python上课，上课内容为[【京峰课堂】尊敬的{username}:我们将于{time}进行{class_type}上课，上课内容为[{content}],请准时上课。],请准时上课。',NULL,0),(33,13720027400,'【京峰课堂】尊敬的王兵:我们将于晚上8点进行python上课，上课内容为[到了你就知道了],请准时上课。',NULL,1),(34,13434111885,'【京峰课堂】尊敬的黄学新:我们将于晚上8点进行python上课，上课内容为[到了你就知道了],请准时上课。',NULL,1),(35,18706170878,'【京峰课堂】尊敬的梁琨:我们将于晚上8点进行python上课，上课内容为[到了你就知道了],请准时上课。',NULL,1);
/*!40000 ALTER TABLE `message_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `info` varchar(255) DEFAULT NULL COMMENT '机柜信息',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (1,'北京鹏博士'),(2,'北京酒仙桥'),(3,'武汉双雄'),(6,'西安光谷'),(44,'广州机房'),(58,'基本原则地 '),(59,'基本原则地 '),(64,'基本原则地 ');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` bigint(20) NOT NULL COMMENT '手机号',
  `passwd` varchar(255) NOT NULL COMMENT '密码',
  `class_type` varchar(10) NOT NULL COMMENT '班级类型',
  `class_num` int(11) NOT NULL COMMENT '班级号',
  `sex` tinyint(4) DEFAULT '0' COMMENT '姓别',
  `qq` bigint(20) DEFAULT NULL COMMENT 'QQ',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '激活状态',
  `username` varchar(255) NOT NULL COMMENT '用户名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,15010220814,'d7a1409691d168a8386ab49ec5fcdc6e','python',1,0,2,1,'品茶'),(10,13720027400,'c31e5f4fbf78838569edd4a34cf86ea8','python',3,0,NULL,1,'王兵'),(11,13434111885,'fc5dcfc983db6013191cc5936ee6494b','python',3,0,NULL,1,'黄学新'),(12,18706170878,'0b4318afb831bd132024d8e734dbae70','python',3,0,NULL,1,'梁琨');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-14 10:23:33
