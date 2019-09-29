/*
Navicat MySQL Data Transfer

Source Server         : 本地mysql
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : scrapy

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2019-09-29 16:32:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for douban
-- ----------------------------
DROP TABLE IF EXISTS `douban`;
CREATE TABLE `douban` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `mIndex` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `star` varchar(255) DEFAULT NULL,
  `digest` varchar(255) DEFAULT NULL,
  `quote` varchar(255) DEFAULT NULL,
  `imgSrc` varchar(255) DEFAULT NULL,
  `doubanHref` varchar(255) DEFAULT NULL,
  `createTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=277 DEFAULT CHARSET=utf8;
