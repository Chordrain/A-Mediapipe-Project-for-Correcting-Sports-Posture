/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80036 (8.0.36)
 Source Host           : localhost:3306
 Source Schema         : leti

 Target Server Type    : MySQL
 Target Server Version : 80036 (8.0.36)
 File Encoding         : 65001

 Date: 03/03/2024 11:13:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int UNSIGNED NOT NULL,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sex` enum('male','female') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `class` int UNSIGNED NOT NULL,
  `number` int UNSIGNED NOT NULL,
  `lastLogin` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (0, '彭家豪', '123456', 'male', 1, 21, '2024-03-02 18:10:17');
INSERT INTO `user` VALUES (1, '冯晓明', 'pkb9KUE0Mg', 'female', 1, 15, '2023-09-23 13:57:48');
INSERT INTO `user` VALUES (2, '阎睿', '0Rjz1CmU47', 'male', 1, 4, '2023-01-26 16:33:42');
INSERT INTO `user` VALUES (3, '赵詩涵', '3tbdXTM4uj', 'male', 1, 13, '2023-10-14 10:30:17');
INSERT INTO `user` VALUES (4, '董子韬', 'jyyjc2VpF2', 'male', 1, 7, '2023-10-14 13:32:18');
INSERT INTO `user` VALUES (5, '朱睿', 'Pb1EQ748NN', 'male', 1, 8, '2023-06-29 09:56:53');
INSERT INTO `user` VALUES (6, '段安琪', 'mF8v8A3vyt', 'male', 1, 19, '2023-06-09 16:55:59');
INSERT INTO `user` VALUES (7, '谭云熙', 'OFFbgUkBbX', 'female', 1, 18, '2023-07-05 13:00:20');
INSERT INTO `user` VALUES (8, '莫震南', '4PxoxrkZbf', 'male', 1, 5, '2024-01-28 16:28:23');
INSERT INTO `user` VALUES (9, '常子韬', 'AeHDZNuQGZ', 'male', 1, 17, '2023-03-25 13:37:18');
INSERT INTO `user` VALUES (10, '唐晓明', 'c0EO4kYzib', 'female', 1, 16, '2023-12-09 13:49:07');
INSERT INTO `user` VALUES (11, '曾晓明', 'GSihyqEGuT', 'female', 1, 3, '2023-07-18 15:44:03');
INSERT INTO `user` VALUES (12, '程秀英', '5ECwCwS4uz', 'male', 1, 20, '2023-03-17 11:20:41');
INSERT INTO `user` VALUES (13, '段岚', 'bkKRJ2TcpO', 'female', 1, 11, '2023-06-10 13:50:51');
INSERT INTO `user` VALUES (14, '孙安琪', 'uxmE4Y7DxP', 'female', 1, 14, '2023-08-18 17:37:10');
INSERT INTO `user` VALUES (15, '石詩涵', 'YR7NI88Sm9', 'female', 1, 10, '2023-05-31 09:21:01');
INSERT INTO `user` VALUES (16, '汪杰宏', 'Rf4WJoMp8l', 'male', 1, 6, '2023-12-30 10:00:12');
INSERT INTO `user` VALUES (17, '谢子异', 'UkO0S2HIsp', 'male', 1, 1, '2023-09-16 13:27:20');
INSERT INTO `user` VALUES (18, '吕晓明', 'BK90pokOVw', 'male', 1, 12, '2023-08-30 11:32:22');
INSERT INTO `user` VALUES (19, '方璐', 'UceyVxGdFH', 'male', 1, 9, '2023-10-04 11:22:34');
INSERT INTO `user` VALUES (20, '任嘉伦', '9x2VePcb3x', 'male', 1, 2, '2024-02-11 11:18:39');

SET FOREIGN_KEY_CHECKS = 1;
