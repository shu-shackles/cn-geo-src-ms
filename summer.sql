-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2022-08-02 13:35:23
-- 服务器版本： 5.7.37-log
-- PHP 版本： 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `summer`
--
CREATE DATABASE IF NOT EXISTS `summer` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `summer`;

-- --------------------------------------------------------

--
-- 表的结构 `analysisdata`
--

DROP TABLE IF EXISTS `analysisdata`;
CREATE TABLE `analysisdata` (
  `province` varchar(16) COLLATE utf8_bin NOT NULL,
  `yearvalue` tinyint(4) NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 转存表中的数据 `analysisdata`
--

INSERT INTO `analysisdata` (`province`, `yearvalue`, `value`) VALUES
('福建', 0, 34.8),
('福建', 1, 48.5),
('福建', 2, 37),
('福建', 3, 41.18),
('福建', 4, 50.6),
('福建', 5, 60.52),
('福建', 6, 62.96),
('福建', 7, 63.1),
('福建', 8, 65.95),
('福建', 9, 66.8),
('福建', 99, 67.19);

-- --------------------------------------------------------

--
-- 表的结构 `areas`
--

DROP TABLE IF EXISTS `areas`;
CREATE TABLE `areas` (
  `area` varchar(20) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 转存表中的数据 `areas`
--

INSERT INTO `areas` (`area`) VALUES
('----'),
('上海'),
('云南'),
('内蒙古'),
('北京'),
('台湾'),
('吉林'),
('四川'),
('天津'),
('宁夏'),
('安徽'),
('山东'),
('山西'),
('广东'),
('广西'),
('新疆'),
('江苏'),
('江西'),
('河北'),
('河南'),
('浙江'),
('海南'),
('湖北'),
('湖南'),
('澳门'),
('甘肃'),
('福建'),
('西藏'),
('贵州'),
('辽宁'),
('重庆'),
('陕西'),
('青海'),
('香港'),
('黑龙江');

-- --------------------------------------------------------

--
-- 表的结构 `eventype`
--

DROP TABLE IF EXISTS `eventype`;
CREATE TABLE `eventype` (
  `etype` enum('0','1','2','3','4','5') COLLATE utf8_bin NOT NULL,
  `desc` varchar(31) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 转存表中的数据 `eventype`
--

INSERT INTO `eventype` (`etype`, `desc`) VALUES
('0', '其他'),
('1', '动物'),
('2', '植物'),
('3', '景观'),
('4', '矿物'),
('5', '事件');

-- --------------------------------------------------------

--
-- 表的结构 `forest`
--

DROP TABLE IF EXISTS `forest`;
CREATE TABLE `forest` (
  `province/company` varchar(45) NOT NULL,
  `forest coverage` int(10) DEFAULT NULL,
  `increase percentage points` varchar(45) DEFAULT NULL,
  `natural forest area` varchar(45) DEFAULT NULL,
  `plantation area` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `forest`
--

INSERT INTO `forest` (`province/company`, `forest coverage`, `increase percentage points`, `natural forest area`, `plantation area`) VALUES
('上海', 9, '14.04', '0', '9'),
('北京', 72, '43.77', '28', '44'),
('吉林', 785, '41.49', '609', '174'),
('吉林森工集团', 121, '85.46', '105', '16'),
('大兴安岭林业集团公司', 679, '81.352', '665', '17'),
('宁夏', 66, '12.63', '6', '15'),
('安徽', 396, '28.65', '160', '233'),
('山西', 321, '20.5', '140', '156'),
('广西', 1430, '60.17', '465', '734'),
('新疆', 802, '4.87', '681', '121'),
('江苏', 156, '15.2', '5', '151'),
('江西', 1021, '61.16', '652', '369'),
('河北', 503, '26.78', '239', '264'),
('浙江', 605, '59.43', '360', '245'),
('湖北', 736, '39.61', '486', '197'),
('湖南', 1053, '49.68', '500', '502'),
('甘肃', 510, '11.33', '383', '127'),
('西藏', 1491, '12.14', '1486', '8'),
('贵州', 771, '43.77', '336', '315'),
('辽宁', 572, '39.24', '220', '309'),
('长白山森工集团', 194, '86.46', '183', '11'),
('陕西', 887, '43.06', '562', '247'),
('黑龙江', 1990, '43.78', '1747', '243'),
('龙江森林工业(集团)总公司', 816, '81.16', '766', '50');

-- --------------------------------------------------------

--
-- 表的结构 `hotpoints`
--

DROP TABLE IF EXISTS `hotpoints`;
CREATE TABLE `hotpoints` (
  `name` varchar(16) COLLATE utf8_bin NOT NULL,
  `value` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 转存表中的数据 `hotpoints`
--

INSERT INTO `hotpoints` (`name`, `value`) VALUES
('一带一路', 9449),
('三北防护林\r\n', 621),
('世界林产品贸易\r\n', 4692),
('国家林木良种名录\r\n', 562),
('国家森林城市\r\n', 7201),
('国家生态定位站\r\n', 259),
('天然林保护\r\n', 8632),
('授权新品种\r\n', 547),
('木材安全\r\n', 439),
('林木良种\r\n', 855),
('林草标准\r\n', 392),
('树种资源\r\n', 3570),
('森林灾害', 59841),
('森林病害\r\n', 1258),
('森林覆盖率', 64386),
('森林警察\r\n', 522),
('森林防火', 12472),
('森林面积\r\n', 6479),
('油茶与花卉\r\n', 425),
('碳中和\r\n', 632),
('自然保护区\r\n', 5210),
('草原保护\r\n', 5682),
('营地生产\r\n', 4938),
('退耕还林', 49852),
('重点保护动植物\r\n', 945),
('青藏科考\r\n', 1025);

-- --------------------------------------------------------

--
-- 表的结构 `informal_tags`
--

DROP TABLE IF EXISTS `informal_tags`;
CREATE TABLE `informal_tags` (
  `area` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `uid` int(11) NOT NULL,
  `lng` double DEFAULT NULL,
  `lat` double DEFAULT NULL,
  `title` varchar(31) COLLATE utf8mb4_bin NOT NULL,
  `desc` varchar(2048) COLLATE utf8mb4_bin DEFAULT NULL,
  `etype` enum('0','1','2','3','4','5') COLLATE utf8mb4_bin DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `imgSrc` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `eid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- 转存表中的数据 `informal_tags`
--

INSERT INTO `informal_tags` (`area`, `uid`, `lng`, `lat`, `title`, `desc`, `etype`, `time`, `imgSrc`, `eid`) VALUES
('中华人民共和国', 1, 120, 40, '巫山', '你好', '2', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/16/WTJIFuOK.jpg', 21),
('中华人民共和国', 1, 120, 40, '巫山', '你好', '2', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/16/WTJIFuOK.jpg', 25),
('江西省新余市渝水区下村镇中共城坊村总支部委员会', 1, 115, 30, '蔚', '第一，我现在很愤怒；第二，我不叫喂,我叫楚雨荨；第三，如果你们再找我玩这种无聊的游戏，我一定让你们变真的猪头；第四，我不是脑残！', '4', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/17/BQXdUSlK.jpg', 28),
('新疆维吾尔自治区巴音郭楞蒙古自治州和硕县乌什塔拉回族民族乡', 1, 88, 42, '动物测试', '这是个动物', '0', '2022-07-17 15:07:57', 'https://img1.imgtp.com/2022/07/17/GdXSDr3j.jpg', 31),
('新疆维吾尔自治区巴音郭楞蒙古自治州尉犁县墩阔坦乡', 1, 89, 41, 'animal', 'this is an animal', '1', '2022-07-17 15:09:58', 'https://img1.imgtp.com/2022/07/17/IhzdXqAn.jpg', 32),
('新疆维吾尔自治区巴音郭楞蒙古自治州且末县阿羌镇', 1, 85, 37, 'other', 'other the other anothor others', '0', '2022-07-17 15:11:19', 'https://img1.imgtp.com/2022/07/17/goGPIxiW.jpg', 33),
('北京', 2, 116.44534, 39.928226, '动物踪迹', '小熊猫', '1', '2022-01-07 00:00:00', 'images/avator.jpg', 34),
('河北省保定市顺平县安阳镇357县道', 2, 118, 39, 'test', 'string', '1', '2022-07-14 00:00:00', 'images/avator.jpg', 36),
('河北省保定市顺平县安阳镇357县道', 2, 115, 39, 'testpic', 'picture', '0', '2022-07-15 00:00:00', 'images/9AN_OBkEAM95U7hdKe8pSWGI.jpg(3)', 37),
('河北省保定市顺平县安阳镇357县道', 2, 115, 39, 'testupload', 'upload formal', '0', '2022-07-16 00:00:00', '/', 38),
('河北', 2, 115, 39, 'testloc', 'location', '0', '2022-07-19 00:00:00', 'string', 39),
('北京', 2, 116.302554, 39.978216, '植物', '云杉', '1', '2022-01-05 14:30:00', 'images/avator.jpg', 40),
('北京', 3, 116.302544, 39.938216, 'alice', 'asdsd', '1', '2022-02-13 23:31:43', 'images/avator.jpg', 41),
('北京', 3, 115.50268, 75.124375, '景观', '瀑布', '2', '2022-01-03 14:39:09', 'images/avator.jpg', 42),
('河北省保定市顺平县安阳镇357县道', 3, 115, 39, 'testpic2', 'picture', '1', '2022-07-15 00:00:00', 'images/SWNhy_UjFoKsJwz72ESwFqxQ.jpg(1)', 43),
('中华', 40, 125, 30, '测试未审核', '我测试一下', '0', '2022-07-26 11:04:04', 'https://img1.imgtp.com/2022/07/17/H44WHWSd.jpg', 45),
('河北', 40, 115, 36.45, 'dffdfdfdf', 'dfdfdfdfd', '5', '2022-07-27 09:06:16', 'https://img1.imgtp.com/2022/07/27/69WwaI5j.jpg', 46),
('中华', 41, 120, 40, '55555', '55555555', '4', '2022-07-26 15:38:42', 'https://img1.imgtp.com/2022/07/16/bdxWuQp8.jpg', 53);

-- --------------------------------------------------------

--
-- 表的结构 `mineral_history`
--

DROP TABLE IF EXISTS `mineral_history`;
CREATE TABLE `mineral_history` (
  `ore` varchar(45) NOT NULL,
  `2011` varchar(45) DEFAULT NULL,
  `2012` varchar(45) DEFAULT NULL,
  `2013` varchar(45) DEFAULT NULL,
  `2014` varchar(45) DEFAULT NULL,
  `2015` varchar(45) DEFAULT NULL,
  `2016` varchar(45) DEFAULT NULL,
  `2017` varchar(45) DEFAULT NULL,
  `2018` varchar(45) DEFAULT NULL,
  `2019` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `mineral_history`
--

INSERT INTO `mineral_history` (`ore`, `2011`, `2012`, `2013`, `2014`, `2015`, `2016`, `2017`, `2018`, `2019`) VALUES
('bronze', '8612.1', '9036.9', '9111.9', '9689.6', '9910.2', '10110.63', '10607.75', '11443.49', '16812.29'),
('coal', '13778.9', '14208', '14842.9', '15317.0', '15663.1', '15980.01', '16666.73', '17085.73', '17358.83'),
('FeS2', '56.8', '56.9', '56.9', '58.3', '58.8', '60.4', '60.60', '63.00', '69.86'),
('fossil_oil', '32.4', '33.3', '33.7', '34.3', '35.0', '35.01', '35.42', '35.73', '46.93'),
('gas', '40206.4', '43790.0', '46428.', '49451.8', '51939.5', '54365.46', '55220.96', '57936.08', '66206.98'),
('gold', '7419.4', '8196.2', '8974.7', '9816.0', '11563.5', '12166.98', '13195.56', '13638.40', '14126.10'),
('iron', '743.9', '775.3', '798.5', '843.4', '850.8', '840.63', '848.88', '852.19', '857.49'),
('lead', '5602.8', '6173.5', '6737.2', '7384.9', '7766.9', '8546.77', '8967.00', '9216.31', '9820.51'),
('silver', '18.7', '21.3', '22.3', '23.7', '25.4', '27.5', '31.60', '32.91', '35.11'),
('zinc', '11568', '12355.8', '13737.7', '14486.1', '14985.2', '17798.89', '18493.86', '18755.67', '20235.57');

-- --------------------------------------------------------

--
-- 表的结构 `mineral_resources`
--

DROP TABLE IF EXISTS `mineral_resources`;
CREATE TABLE `mineral_resources` (
  `province` varchar(45) NOT NULL,
  `coal(100M tons)` varchar(45) DEFAULT NULL,
  `fossil_oil(10K tons)` varchar(45) DEFAULT NULL,
  `gas(100M cubic meters)` varchar(45) DEFAULT NULL,
  `iron(100M tons)` varchar(45) DEFAULT NULL,
  `bronze(10K tons)` varchar(45) DEFAULT NULL,
  `gold(tons)` varchar(45) DEFAULT NULL,
  `silver(tons)` varchar(45) DEFAULT NULL,
  `lead(10k tons)` varchar(45) DEFAULT NULL,
  `zinc(10k tons)` varchar(45) DEFAULT NULL,
  `FeS2(10k tons)` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `mineral_resources`
--

INSERT INTO `mineral_resources` (`province`, `coal(100M tons)`, `fossil_oil(10K tons)`, `gas(100M cubic meters)`, `iron(100M tons)`, `bronze(10K tons)`, `gold(tons)`, `silver(tons)`, `lead(10k tons)`, `zinc(10k tons)`, `FeS2(10k tons)`) VALUES
('上海', '', '', '', '', '', '', '', NULL, NULL, NULL),
('云南', '44.54', '10.15', '0.47', '3.8', '361.26', '91.45', '3423.38\n', '208.28', '766.81', '302.75'),
('内蒙古', '194.47', '6676.91', '10123.53', '6.12', '84.55', '76.07', '19801.8\n', '284.17', '652.65', '4875.87'),
('北京', '0.97', '', '', '0.67', '', '', '', NULL, NULL, NULL),
('吉林', '7.03', '16902.02', '767.11', '4.27', '17.85', '106.52', '213.89\n', '12.63', '39.41', '568.40'),
('四川', '26.66', '555.4', '15274.98', '18.89', '31.73', '52.68', '463.28\n', '31.63', '92.93', '19110.40'),
('天津', '', '3999.87', '293.09', '', '', '', '', NULL, NULL, NULL),
('宁夏', '35.01', '4670.51', '280.67', '', '388.05', '', '', NULL, NULL, NULL),
('安徽', '58.27', '135.23', '0.24', '10.85', '129.77', '36.45', '375.01\n', '6.08', '5.86', NULL),
('山东', '41.32', '25493.92', '343.52', '7.86', '7.59', '456.43', '156.37\n', '2.96', '0.81', '13.14'),
('山西', '507.25', '', '1402.04', '11.51', '81.08', '39.68', '379.71\n', '1.47', '1.92', '194.40'),
('广东', '0.01', '12.27', '0.97', '0.14', '0.84', '7.29', '201.46\n', '8.67', '8.34', '2073.06'),
('广西', '0.88', '146.37', '1.38', '0.54', '5.59', '19.15', '1380.74\n', '137.83', '117.70', '1006.49'),
('新疆', '190.14', '62590.34', '11237.85', '3.64', '156.91', '79.86', '395.87\n', '17.91', '155.27', '3271.64'),
('江苏', '3.74', '1951.1', '21.39', '0.63', '4.21', '3.1', '200.15\n', '11.37', '17.00', '304.53'),
('江西', '2.1', '', '', '4.94', '625.08', '217.65', '9399.86\n', '116.22', '222.90', '21651.30'),
('河北', '26.05', '25538.63', '372.26', '7.4', '0.89', '30.94', '310.57\n', '6.87', '26.34', '295.94'),
('河南', '33.65', '3022.24', '62.82', '1.21', '0.47', '68.77', '936.3\n', '15.08', '13.26', '97.21'),
('浙江', '0.15', '', '', '0.42', '3.53', '5.86', '526.46\n', '8.44', '28.05', NULL),
('海南', '0', '454.82', '21.47', '0.76', '', '21.07', '', NULL, NULL, NULL),
('湖北', '0.1', '1055.5', '44.59', '2.07', '63.59', '28.43', '743.13\n', '3.54', '14.54', '112.03'),
('湖南', '4.86', '', '', '1.67', '9.84', '76.68', '1710.65\n', '51.19', '75.81', '1067.71'),
('甘肃', '15.31', '39560.97', '588', '2.87', '202.56', '228.88', '1758.4\n', '138.82', '483.40', NULL),
('福建', '2.5', '', '', '2.4', '140.77', '14.09', '1062.97\n', '15.43', '31.20', NULL),
('西藏', '0.11', '', '', '209.42', '735.99', '92.64', '6039.45\n', '71.66', '79.68', NULL),
('贵州', '91.35', '', '6.1', '0.11', '0.11', '59.42', '37.12\n', '7.52', '73.44', '3830.84'),
('辽宁', '12.57', '14372.28', '164.53', '13.81', '8.71', '21.98', '251.01\n', '2.31', '14.30', '604.76'),
('重庆', '1.87', '228.34', '2500.73', '830.73', '0.89', '', '', '0.89', '3.45', '1.84'),
('陕西', '293.9', '36812.83', '11096.45', '0.98', '18.03', '22.54', '43.16\n', '18.02', '75.73', '9.24'),
('青海', '2.26', '8251.85', '1055.32', '0.72', '9.53', '33.24', '796.75\n', '52.25', '91.27', NULL),
('黑龙江', '25.81', '36287.27', '1494.64', '0.5', '0.82', '36.5', '64.77\n', '0.86', '2.76', '19.30');

-- --------------------------------------------------------

--
-- 表的结构 `provincedata`
--

DROP TABLE IF EXISTS `provincedata`;
CREATE TABLE `provincedata` (
  `name` varchar(32) COLLATE utf8_bin NOT NULL,
  `value` float NOT NULL,
  `province` varchar(16) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 转存表中的数据 `provincedata`
--

INSERT INTO `provincedata` (`name`, `value`, `province`) VALUES
('东城区', 0.78, '北京市'),
('丰台区', 2.3, '北京市'),
('大兴区', 2.35, '北京市'),
('密云区', 4.29, '北京市'),
('平谷区', 3.73, '北京市'),
('延庆区', 3.35, '北京市'),
('怀柔区', 4.58, '北京市'),
('房山区', 4.07, '北京市'),
('昌平区', 2.61, '北京市'),
('朝阳区', 1.41, '北京市'),
('海淀区', 2.46, '北京市'),
('石景山区', 2.52, '北京市'),
('西城区', 0.99, '北京市'),
('通州区', 1.92, '北京市'),
('门头沟区', 4.66, '北京市'),
('顺义区', 1.75, '北京市');

-- --------------------------------------------------------

--
-- 表的结构 `tags`
--

DROP TABLE IF EXISTS `tags`;
CREATE TABLE `tags` (
  `area` varchar(50) COLLATE utf8_bin NOT NULL,
  `uid` int(11) NOT NULL,
  `lng` double DEFAULT NULL,
  `lat` double DEFAULT NULL,
  `title` varchar(31) COLLATE utf8_bin NOT NULL,
  `desc` varchar(2048) COLLATE utf8_bin DEFAULT NULL,
  `etype` enum('0','1','2','3','4','5') COLLATE utf8_bin NOT NULL,
  `time` datetime DEFAULT NULL,
  `imgSrc` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `eid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 转存表中的数据 `tags`
--

INSERT INTO `tags` (`area`, `uid`, `lng`, `lat`, `title`, `desc`, `etype`, `time`, `imgSrc`, `eid`) VALUES
('河北省保定市顺平县安阳镇357县道', 1, 115, 39, 'test', 'string', '0', '2022-07-14 00:00:00', 'images/avator.jpg', 5),
('河北省保定市顺平县安阳镇357县道', 1, 115, 39, 'test2', 'string', '0', '2022-07-14 00:00:00', 'images/avator.jpg', 6),
('中华人民共和国', 1, 120, 40, '巫山', '你好', '2', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/16/WTJIFuOK.jpg', 14),
('浙江省杭州市富阳区大源镇G25长深高速', 1, 120, 30, '男枪', '我是刘备', '3', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/17/qgp0zOE4.jpg', 15),
('四川省甘孜藏族自治州理塘县禾尼乡', 1, 100, 30, '女枪', '我是厄运小姐', '0', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/17/TEx895RU.jpg', 16),
('江西省新余市渝水区下村镇中共城坊村总支部委员会', 1, 115, 30, '蔚', '第一，我现在很愤怒；第二，我不叫喂,我叫楚雨荨；第三，如果你们再找我玩这种无聊的游戏，我一定让你们变真的猪头；第四，我不是脑残！', '4', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/17/BQXdUSlK.jpg', 17),
('江西省赣州市定南县岭北镇陈皮坑', 1, 115, 25, '高育良', '工作时请称呼植物', '1', '2022-07-17 15:04:05', 'https://img1.imgtp.com/2022/07/17/USZ4eXCd.jpg', 19),
('新疆维吾尔自治区巴音郭楞蒙古自治州若羌县罗布泊镇', 1, 90, 40, '植物测试', '这是个植物', '1', '2022-07-17 15:06:19', 'https://img1.imgtp.com/2022/07/17/CjJ6hmgW.jpg', 20),
('新疆维吾尔自治区巴音郭楞蒙古自治州和硕县乌什塔拉回族民族乡', 1, 88, 42, '动物测试', '这是个动物', '0', '2022-07-17 15:07:57', 'https://img1.imgtp.com/2022/07/17/GdXSDr3j.jpg', 21),
('新疆维吾尔自治区巴音郭楞蒙古自治州尉犁县墩阔坦乡', 1, 89, 41, 'animal', 'this is an animal', '1', '2022-07-17 15:09:58', 'https://img1.imgtp.com/2022/07/17/IhzdXqAn.jpg', 22),
('新疆维吾尔自治区巴音郭楞蒙古自治州且末县阿羌镇', 1, 85, 37, 'other', 'other the other anothor others', '0', '2022-07-17 15:11:19', 'https://img1.imgtp.com/2022/07/17/goGPIxiW.jpg', 23),
('河北省保定市顺平县安阳镇357县道', 1, 115, 39, 'test', 'string', '0', '2022-07-14 00:00:00', 'images/avator.jpg', 40),
('河北省保定市顺平县安阳镇357县道', 1, 115, 39, 'test2', 'string', '0', '2022-07-14 00:00:00', 'images/avator.jpg', 41),
('中华人民共和国', 1, 120, 40, '巫山', '你好', '2', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/16/WTJIFuOK.jpg', 42),
('浙江省杭州市富阳区大源镇G25长深高速', 1, 120, 30, '男枪', '我是刘备', '3', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/17/qgp0zOE4.jpg', 43),
('四川省甘孜藏族自治州理塘县禾尼乡', 1, 100, 30, '女枪', '我是厄运小姐', '0', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/17/TEx895RU.jpg', 44),
('浙江省杭州市富阳区大源镇G25长深高速', 1, 120, 30, '男枪', '我是刘备', '2', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/17/qgp0zOE4.jpg', 45),
('江西省赣州市定南县岭北镇陈皮坑', 1, 115, 25, '高育良', '工作时请称呼植物', '0', '2022-07-17 15:04:05', 'https://img1.imgtp.com/2022/07/17/USZ4eXCd.jpg', 50),
('北京', 2, 116.44534, 39.928226, '动物踪迹', '小熊猫', '1', '2022-01-07 00:00:00', 'images/avator.jpg', 1),
('北京', 2, 116.402554, 39.978216, '植物', '云杉', '2', '2022-01-05 14:30:00', 'images/avator.jpg', 3),
('河北省保定市顺平县安阳镇357县道', 2, 118, 39, 'test', 'string', '1', '2022-07-14 00:00:00', 'images/avator.jpg', 9),
('河北省保定市顺平县安阳镇357县道', 2, 115, 39, 'testpic', 'picture', '0', '2022-07-15 00:00:00', 'images/9AN_OBkEAM95U7hdKe8pSWGI.jpg(3)', 12),
('河北省保定市顺平县安阳镇357县道', 2, 115, 39, 'testupload', 'upload formal', '0', '2022-07-16 00:00:00', '/', 13),
('河北', 2, 115, 39, 'testloc', 'location', '0', '2022-07-19 00:00:00', 'string', 24),
('北京', 2, 116.302554, 39.978216, '植物', '云杉', '1', '2022-01-05 14:30:00', 'images/avator.jpg', 27),
('北京', 2, 116.402554, 39.978216, '植物', '云杉', '1', '2022-01-05 14:30:00', 'images/avator.jpg', 49),
('北京', 3, 116.302544, 39.938216, 'alice', 'asdsd', '1', '2022-02-13 23:31:43', 'images/avator.jpg', 8),
('北京', 3, 115.50268, 75.124375, '景观', '瀑布', '2', '2022-01-03 14:39:09', 'images/avator.jpg', 38),
('河北省保定市顺平县安阳镇357县道', 3, 115, 39, 'testpic2', 'picture', '1', '2022-07-15 00:00:00', 'images/SWNhy_UjFoKsJwz72ESwFqxQ.jpg(1)', 39),
('上海', 40, 121.5, 31.25, '香樟', '一大片香樟树', '2', '2022-07-26 10:05:29', 'https://img1.imgtp.com/2022/07/26/Dzabifrb.jpg', 25),
('中华', 40, 125, 30, '测试未审核', '我测试一下', '0', '2022-07-26 11:04:04', 'https://img1.imgtp.com/2022/07/17/H44WHWSd.jpg', 26),
('河北', 40, 115, 36.45, 'dffdfdfdf', 'dfdfdfdfd', '5', '2022-07-27 09:06:16', 'https://img1.imgtp.com/2022/07/27/69WwaI5j.jpg', 28),
('河北', 40, 114, 37, 'wsdadd', 'sdsdxcxcvsdv', '5', '2022-07-27 09:09:20', 'https://img1.imgtp.com/2022/07/27/z7DgqVkz.jpg', 29),
('中华', 40, 120, 35, 'kjkj', 'kjkjkjkjkj', '2', '2022-07-27 09:10:57', 'https://img1.imgtp.com/2022/07/27/KmsLIowM.jpg', 30),
('内蒙古', 40, 110, 40, '2424', '22222222222222', '5', '2022-07-27 09:12:32', 'https://img1.imgtp.com/2022/07/27/ENYhetXL.jpg', 31),
('内蒙古', 40, 110, 41, '12', '1111111111111', '4', '2022-07-27 09:13:21', 'https://img1.imgtp.com/2022/07/27/cB2BVmUS.jpg', 32),
('内蒙古', 40, 110, 40, '2424', '22222222222222', '4', '2022-07-27 09:12:32', 'https://img1.imgtp.com/2022/07/27/ENYhetXL.jpg', 46),
('中华', 40, 120, 35, 'kjkj', 'kjkjkjkjkj', '1', '2022-07-27 09:10:57', 'https://img1.imgtp.com/2022/07/27/KmsLIowM.jpg', 47),
('内蒙古', 40, 110, 41, '12', '1111111111111', '3', '2022-07-27 09:13:21', 'https://img1.imgtp.com/2022/07/27/cB2BVmUS.jpg', 48),
('江苏', 40, 119, 31.25, 'qwer', '哈撒给', '1', '2022-07-29 10:06:15', 'https://img1.imgtp.com/2022/07/29/d1kVxxci.jpg', 51),
('内蒙古', 41, 102, 42, '121', '255555555', '3', '2022-07-27 09:14:07', 'https://img1.imgtp.com/2022/07/27/ENYhetXL.jpg', 33),
('中华', 41, 120, 35, '风格豆腐干风格', '发发打发打发打发', '1', '2022-07-26 16:51:25', 'https://img1.imgtp.com/2022/07/16/bdxWuQp8.jpg', 34),
('中华', 41, 120, 40, '55555', '55555555', '4', '2022-07-26 15:38:42', 'https://img1.imgtp.com/2022/07/16/bdxWuQp8.jpg', 35),
('安徽', 41, 118, 31.25, '测试', '未审核', '0', '2022-07-26 11:29:21', 'https://img1.imgtp.com/2022/07/26/06jKRgpb.jpg', 36),
('陕西', 41, 110, 36.7, '标题', '简单描述一下', '0', '2022-07-17 09:00:00', 'https://img1.imgtp.com/2022/07/17/BQXdUSlK.jpg', 37);

-- --------------------------------------------------------

--
-- 表的结构 `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `uid` int(11) NOT NULL,
  `name` varchar(20) COLLATE utf8_bin NOT NULL,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `type` enum('0','1','2') COLLATE utf8_bin DEFAULT NULL,
  `area` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `IDName` varchar(20) COLLATE utf8_bin NOT NULL,
  `ID` varchar(20) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 转存表中的数据 `users`
--

INSERT INTO `users` (`uid`, `name`, `password`, `type`, `area`, `IDName`, `ID`) VALUES
(1, 'root', 'root', '0', NULL, '万叶', '130202197902108198'),
(2, 'type1_user1', 'type1uer1', '1', '北京', '宵宫', '130202197902109975'),
(3, 'type2_user1', 'type2user1', '2', NULL, '可莉', '130202197902106512'),
(4, 'test', '123123', '2', '----', '123', '123'),
(40, 'testpassword', '$2b$12$AsnPKedvicHhd7lrUU0r1uZEMAS1CdicMKJEWpMy5FHHXJEDkZE1y', '1', '上海', '郑昕', '140107200104260614'),
(41, 'shackles', '$2b$12$/Hyl17cG9oy8JS4gAU6.m.MPzS8c1BKXgbcvMERZZ0RlwERxPGMbm', '1', '上海', '杨君豪', '310230200105150450'),
(45, 'test3', '$2b$12$pgpFp.txl7wxQU9hj4Pt/eWoAhpe0fcLM8krPnUUYaxd4hJVgGJYu', '0', NULL, '测试', 'ceshi'),
(46, 'newroot', '$2b$12$eS8wXjXZ/2hP12Ned5xlpu2whY.Bappv6D7wnKjTGpOo51tfu6uWC', '0', NULL, '杨君豪', '310230200105150450');

--
-- 转储表的索引
--

--
-- 表的索引 `analysisdata`
--
ALTER TABLE `analysisdata`
  ADD PRIMARY KEY (`province`,`yearvalue`);

--
-- 表的索引 `areas`
--
ALTER TABLE `areas`
  ADD PRIMARY KEY (`area`);

--
-- 表的索引 `eventype`
--
ALTER TABLE `eventype`
  ADD PRIMARY KEY (`etype`);

--
-- 表的索引 `forest`
--
ALTER TABLE `forest`
  ADD PRIMARY KEY (`province/company`);

--
-- 表的索引 `hotpoints`
--
ALTER TABLE `hotpoints`
  ADD PRIMARY KEY (`name`);

--
-- 表的索引 `informal_tags`
--
ALTER TABLE `informal_tags`
  ADD PRIMARY KEY (`eid`);

--
-- 表的索引 `mineral_history`
--
ALTER TABLE `mineral_history`
  ADD PRIMARY KEY (`ore`);

--
-- 表的索引 `mineral_resources`
--
ALTER TABLE `mineral_resources`
  ADD PRIMARY KEY (`province`),
  ADD UNIQUE KEY `province_UNIQUE` (`province`);

--
-- 表的索引 `provincedata`
--
ALTER TABLE `provincedata`
  ADD PRIMARY KEY (`name`,`province`);

--
-- 表的索引 `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`uid`,`eid`),
  ADD KEY `eid` (`eid`),
  ADD KEY `tags-uid-users` (`uid`),
  ADD KEY `tags-etype-eventype` (`etype`);

--
-- 表的索引 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uid`),
  ADD KEY `area` (`area`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `informal_tags`
--
ALTER TABLE `informal_tags`
  MODIFY `eid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- 使用表AUTO_INCREMENT `tags`
--
ALTER TABLE `tags`
  MODIFY `eid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- 使用表AUTO_INCREMENT `users`
--
ALTER TABLE `users`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- 限制导出的表
--

--
-- 限制表 `tags`
--
ALTER TABLE `tags`
  ADD CONSTRAINT `tags-etype-eventype` FOREIGN KEY (`etype`) REFERENCES `eventype` (`etype`),
  ADD CONSTRAINT `tags-uid-users` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`);

--
-- 限制表 `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `area` FOREIGN KEY (`area`) REFERENCES `areas` (`area`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
