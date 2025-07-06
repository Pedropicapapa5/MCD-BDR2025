-- Crear base de datos
CREATE DATABASE MCD_BD_MAQUILLAJE;
USE MCD_BD_MAQUILLAJE;

-- Crear tabla PRODUCTO
CREATE TABLE PRODUCTO (
    ID_Producto INT PRIMARY KEY AUTO_INCREMENT,
    Tipo VARCHAR(20),
    Subtipo VARCHAR(20)
);

-- Crear tabla TONO
CREATE TABLE TONO (
    ID_Tono INT PRIMARY KEY AUTO_INCREMENT,
    Tipo VARCHAR(20),
    Subtono VARCHAR(20)
);

-- Crear tabla ORIGEN
CREATE TABLE ORIGEN (
    ID_Origen INT PRIMARY KEY AUTO_INCREMENT,
    País VARCHAR(50)
);

-- Crear tabla MARCA
CREATE TABLE MARCA (
    ID_Marca INT PRIMARY KEY AUTO_INCREMENT,
    Categoria VARCHAR(20)
);

-- Crear tabla INGREDIENTE
CREATE TABLE INGREDIENTE (
    ID_Ingrediente INT PRIMARY KEY AUTO_INCREMENT,
    Tipo VARCHAR(20),
    Nombre VARCHAR(50)
);

-- Crear tabla RESEÑA
CREATE TABLE RESEÑA (
    ID_Reseña INT PRIMARY KEY AUTO_INCREMENT,
    Usuario VARCHAR(50),
    Calificacion FLOAT
);

-- Crear tabla MAQUILLAJE
CREATE TABLE MAQUILLAJE (
    ID_Maquillaje INT PRIMARY KEY AUTO_INCREMENT,
    ID_Producto INT,
    ID_Tono INT,
    ID_Origen INT,
    ID_Marca INT,
    FOREIGN KEY (ID_Producto) REFERENCES PRODUCTO(ID_Producto),
    FOREIGN KEY (ID_Tono) REFERENCES TONO(ID_Tono),
    FOREIGN KEY (ID_Origen) REFERENCES ORIGEN(ID_Origen),
    FOREIGN KEY (ID_Marca) REFERENCES MARCA(ID_Marca)
);

-- Crear tabla MAQUILLAJE_INGREDIENTE
CREATE TABLE MAQUILLAJE_INGREDIENTE (
    ID_Maquillaje INT,
    ID_Ingrediente INT,
    FOREIGN KEY (ID_Maquillaje) REFERENCES MAQUILLAJE(ID_Maquillaje),
    FOREIGN KEY (ID_Ingrediente) REFERENCES INGREDIENTE(ID_Ingrediente)
);

-- Crear tabla MAQUILLAJE_RESEÑA
CREATE TABLE MAQUILLAJE_RESEÑA (
    ID_Maquillaje INT,
    ID_Reseña INT,
    FOREIGN KEY (ID_Maquillaje) REFERENCES MAQUILLAJE(ID_Maquillaje),
    FOREIGN KEY (ID_Reseña) REFERENCES RESEÑA(ID_Reseña)
);

-- Insertar datos en PRODUCTO
INSERT INTO PRODUCTO (Tipo, Subtipo) VALUES
('Labial', 'Gloss'), ('Labial', 'Tinta'), ('Base', 'Matte'), ('Ojos', 'Sombras'),
('Base', 'Satinado'), ('Labial', 'Barra'), ('Ojos', 'Rimel'), ('Primer', 'Spray'),
('Primer', 'Tubo'), ('Base', 'SemiMatte');

-- Insertar datos en TONO
INSERT INTO TONO (Tipo, Subtono) VALUES
('Neutro', 'Mute'), ('Frío', 'Bright'), ('Cálido', 'Deep'), ('Neutro', 'Deep'), ('Frío', 'Mute');

-- Insertar datos en ORIGEN
INSERT INTO ORIGEN (País) VALUES
('México'), ('Estados Unidos'), ('Corea del Sur');

-- Insertar datos en MARCA
INSERT INTO MARCA (Categoria) VALUES
('Lujo'), ('Semi'), ('NoLujo');

-- Insertar datos en INGREDIENTE
INSERT INTO INGREDIENTE (Tipo, Nombre) VALUES
('Natural', 'Aloe Vera'), ('Natural', 'Centella Asiática'), ('Químico', 'Ceramida'),
('Natural', 'Leche de arroz'), ('Químico', 'Panthenol');

-- Insertar datos en RESEÑA
INSERT INTO RESEÑA (Usuario, Calificacion) VALUES
('Usuaria_1', 4.5), ('Usuaria_2', 5.0), ('Usuaria_3', 2.9),
('Usuaria_4', 4.2), ('Usuaria_5', 3.7), ('Usuaria_6', 4.8);

-- Insertar datos en MAQUILLAJE
INSERT INTO MAQUILLAJE (ID_Producto, ID_Tono, ID_Origen, ID_Marca) VALUES
(1, 1, 1, 2), (2, 2, 3, 1), (3, 3, 2, 2), (4, 2, 3, 3), (5, 1, 1, 1),
(6, 5, 2, 3), (7, 2, 3, 2), (8, 3, 2, 2), (9, 4, 1, 1), (10, 1, 3, 2),
(1, 3, 3, 3), (2, 5, 1, 1), (3, 1, 2, 2), (4, 2, 2, 3), (5, 5, 3, 1),
(6, 3, 2, 3), (7, 2, 1, 2), (8, 1, 3, 3), (9, 4, 2, 1), (10, 2, 3, 2);

-- Insertar datos en MAQUILLAJE_INGREDIENTE
INSERT INTO MAQUILLAJE_INGREDIENTE VALUES
(1,1), (1,2), (2,1), (3,3), (4,1), (5,5), (6,4), (7,3), (8,5), (9,2),
(10,1), (11,4), (12,1), (13,3), (14,5), (15,2), (16,3), (17,2), (18,1), (19,4);

-- Insertar datos en MAQUILLAJE_RESEÑA
INSERT INTO MAQUILLAJE_RESEÑA VALUES
(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,1), (8,2), (9,3), (10,4),
(11,5), (12,6), (13,1), (14,2), (15,3), (16,4), (17,5), (18,6), (19,1), (20,2);
