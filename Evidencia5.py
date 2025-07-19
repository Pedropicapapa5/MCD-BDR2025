#
# TABLE STRUCTURE FOR: Ingrediente
#

DROP TABLE IF EXISTS `Ingrediente`;

CREATE TABLE `Ingrediente` (
  `ID_Ingrediente` int(11) NOT NULL,
  `Tipo` enum('Natural','Químico') DEFAULT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID_Ingrediente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (0, 'Natural', '1949890263838');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (1, 'Químico', '1568354379658');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (2, 'Químico', '6470701437308');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (3, 'Natural', '1708670948514');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (4, 'Químico', '1026604454192');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (5, 'Natural', '2397820650514');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (6, 'Químico', '2857699147817');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (7, 'Químico', '6236374461091');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (8, 'Químico', '1761895110876');
INSERT INTO `Ingrediente` (`ID_Ingrediente`, `Tipo`, `Nombre`) VALUES (9, 'Natural', '6193572349791');


#
# TABLE STRUCTURE FOR: Marca
#

DROP TABLE IF EXISTS `Marca`;

CREATE TABLE `Marca` (
  `ID_Marca` int(11) NOT NULL,
  `Categoria` enum('Lujo','Semi','NoLujo') DEFAULT NULL,
  PRIMARY KEY (`ID_Marca`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (0, 'Lujo');
INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (1, 'Semi');
INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (2, 'Semi');
INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (3, 'Semi');
INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (4, 'Lujo');
INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (5, 'Semi');
INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (6, 'Semi');
INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (7, 'Semi');
INSERT INTO `Marca` (`ID_Marca`, `Categoria`) VALUES (8, 'Semi');


#
# TABLE STRUCTURE FOR: Origen
#

DROP TABLE IF EXISTS `Origen`;

CREATE TABLE `Origen` (
  `ID_Origen` int(11) NOT NULL,
  `Pais` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_Origen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (0, 'Guadeloupe');
INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (1, 'Cape Verde');
INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (2, 'Netherlands Antilles');
INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (3, 'Ghana');
INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (5, 'Maldives');
INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (6, 'Bhutan');
INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (7, 'Mali');
INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (8, 'Czech Republic');
INSERT INTO `Origen` (`ID_Origen`, `Pais`) VALUES (9, 'Saint Vincent and the Grenadines');


#
# TABLE STRUCTURE FOR: Producto
#

DROP TABLE IF EXISTS `Producto`;

CREATE TABLE `Producto` (
  `ID_Producto` int(11) NOT NULL,
  `Tipo` enum('Labial','Base','Ojos','Primer') DEFAULT NULL,
  `Subtipo` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID_Producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (0, 'Labial', 'Spray');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (1, 'Ojos', 'Barra');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (2, 'Labial', 'Tubo');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (3, 'Primer', 'Spray');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (4, 'Primer', 'Spray');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (5, 'Labial', 'Spray');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (6, 'Base', 'Barra');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (7, 'Primer', 'Barra');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (8, 'Labial', 'Tubo');
INSERT INTO `Producto` (`ID_Producto`, `Tipo`, `Subtipo`) VALUES (9, 'Base', 'Barra');


#
# TABLE STRUCTURE FOR: Resena
#

DROP TABLE IF EXISTS `Resena`;

CREATE TABLE `Resena` (
  `ID_Resena` int(20) NOT NULL,
  `Calificacion` enum('1','2','3','4','5') DEFAULT NULL,
  PRIMARY KEY (`ID_Resena`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (0, '1');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (1, '5');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (2, '1');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (3, '1');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (4, '5');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (5, '4');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (6, '4');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (7, '5');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (8, '5');
INSERT INTO `Resena` (`ID_Resena`, `Calificacion`) VALUES (9, '2');


#
# TABLE STRUCTURE FOR: Tono
#

DROP TABLE IF EXISTS `Tono`;

CREATE TABLE `Tono` (
  `ID_Tono` int(11) NOT NULL,
  `Tipo` enum('Neutro','Cálido','Frío') DEFAULT NULL,
  `Subtono` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID_Tono`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `Tono` (`ID_Tono`, `Tipo`, `Subtono`) VALUES (0, 'Frío', 'Opaco');
INSERT INTO `Tono` (`ID_Tono`, `Tipo`, `Subtono`) VALUES (1, 'Cálido', 'Brillante');
INSERT INTO `Tono` (`ID_Tono`, `Tipo`, `Subtono`) VALUES (2, 'Neutro', 'Opaco');
INSERT INTO `Tono` (`ID_Tono`, `Tipo`, `Subtono`) VALUES (4, 'Cálido', 'Opaco');
INSERT INTO `Tono` (`ID_Tono`, `Tipo`, `Subtono`) VALUES (5, 'Cálido', 'Brillante');
INSERT INTO `Tono` (`ID_Tono`, `Tipo`, `Subtono`) VALUES (6, 'Frío', 'Opaco');
INSERT INTO `Tono` (`ID_Tono`, `Tipo`, `Subtono`) VALUES (8, 'Neutro', 'Opaco');
INSERT INTO `Tono` (`ID_Tono`, `Tipo`, `Subtono`) VALUES (9, 'Frío', 'Brillante');

