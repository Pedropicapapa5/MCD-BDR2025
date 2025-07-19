CREATE TABLE Producto (
  ID_Producto INTEGER PRIMARY KEY,
  Tipo VARCHAR(20),
  Subtipo VARCHAR(30)
);

CREATE TABLE Tono (
  ID_Tono INTEGER PRIMARY KEY,
  Tipo VARCHAR(10),
  Subtono VARCHAR(30)
);

CREATE TABLE Origen (
  ID_Origen INTEGER PRIMARY KEY,
  Pais VARCHAR(50)
);

CREATE TABLE Marca (
  ID_Marca INTEGER PRIMARY KEY,
  Categoria VARCHAR(10)
);

CREATE TABLE Ingrediente (
  ID_Ingrediente INTEGER PRIMARY KEY,
  Tipo VARCHAR(10),
  Nombre VARCHAR(30)
);

CREATE TABLE Reseña (
  ID_Reseña INTEGER PRIMARY KEY,
  Usuario VARCHAR(50),
  Calificacion INTEGER
);

INSERT INTO Producto (ID_Producto, Tipo, Subtipo) VALUES
  (1, 'Labial', 'tempore'),
  (2, 'Labial', 'culpa'),
  (3, 'Ojos', 'alias'),
  (4, 'Base', 'harum'),
  (5, 'Base', 'exercitationem'),
  (6, 'Base', 'et'),
  (7, 'Labial', 'deserunt'),
  (8, 'Labial', 'corporis'),
  (9, 'Primer', 'veritatis'),
  (10, 'Labial', 'quisquam'),
  (11, 'Labial', 'commodi'),
  (12, 'Labial', 'rerum'),
  (13, 'Base', 'nisi'),
  (14, 'Base', 'aliquid'),
  (15, 'Labial', 'aliquam'),
  (16, 'Base', 'consectetur'),
  (17, 'Primer', 'esse'),
  (18, 'Base', 'eveniet'),
  (19, 'Primer', 'quae'),
  (20, 'Ojos', 'sed');
INSERT INTO Tono (ID_Tono, Tipo, Subtono) VALUES
  (1, 'Neutro', 'alias'),
  (2, 'Neutro', 'ratione'),
  (3, 'Frío', 'eius'),
  (4, 'Cálido', 'totam'),
  (5, 'Cálido', 'voluptates'),
  (6, 'Cálido', 'quisquam'),
  (7, 'Neutro', 'nihil'),
  (8, 'Neutro', 'est'),
  (9, 'Cálido', 'occaecati'),
  (10, 'Neutro', 'repudiandae'),
  (11, 'Neutro', 'hic'),
  (12, 'Cálido', 'ab'),
  (13, 'Neutro', 'dolore'),
  (14, 'Cálido', 'voluptatem'),
  (15, 'Cálido', 'nisi'),
  (16, 'Frío', 'laboriosam'),
  (17, 'Cálido', 'hic'),
  (18, 'Neutro', 'dolor'),
  (19, 'Frío', 'esse'),
  (20, 'Cálido', 'labore');
INSERT INTO Origen (ID_Origen, Pais) VALUES
  (1, 'Brunei Darussalam'),
  (2, 'Bosnia y Herzegovina'),
  (3, 'Lesotho'),
  (4, 'Botswana'),
  (5, 'Jordania'),
  (6, 'Italia'),
  (7, 'Samoa'),
  (8, 'Georgia'),
  (9, 'Austria'),
  (10, 'Uzbekistán'),
  (11, 'Mongolia'),
  (12, 'Portugal'),
  (13, 'Camboya'),
  (14, 'Kuwait'),
  (15, 'Benin'),
  (16, 'República Centroafricana'),
  (17, 'Guyana'),
  (18, 'Serbia'),
  (19, 'San Vicente y las Granadinas'),
  (20, 'Kazajstán');
INSERT INTO Marca (ID_Marca, Categoria) VALUES
  (1, 'NoLujo'),
  (2, 'Lujo'),
  (3, 'Semi'),
  (4, 'Lujo'),
  (5, 'NoLujo'),
  (6, 'Semi'),
  (7, 'NoLujo'),
  (8, 'NoLujo'),
  (9, 'Semi'),
  (10, 'NoLujo'),
  (11, 'Lujo'),
  (12, 'NoLujo'),
  (13, 'Lujo'),
  (14, 'Lujo'),
  (15, 'NoLujo'),
  (16, 'Lujo'),
  (17, 'Semi'),
  (18, 'Lujo'),
  (19, 'Lujo'),
  (20, 'Lujo');
INSERT INTO Ingrediente (ID_Ingrediente, Tipo, Nombre) VALUES
  (1, 'Químico', 'repellat'),
  (2, 'Químico', 'earum'),
  (3, 'Químico', 'voluptatibus'),
  (4, 'Químico', 'atque'),
  (5, 'Natural', 'aperiam'),
  (6, 'Químico', 'ut'),
  (7, 'Químico', 'eum'),
  (8, 'Natural', 'illum'),
  (9, 'Químico', 'beatae'),
  (10, 'Natural', 'eveniet'),
  (11, 'Natural', 'consequuntur'),
  (12, 'Natural', 'modi'),
  (13, 'Natural', 'hic'),
  (14, 'Químico', 'odit'),
  (15, 'Químico', 'tempora'),
  (16, 'Químico', 'maiores'),
  (17, 'Natural', 'dolorem'),
  (18, 'Químico', 'maxime'),
  (19, 'Natural', 'libero'),
  (20, 'Natural', 'eos');
INSERT INTO Reseña (ID_Reseña, Usuario, Calificacion) VALUES
  (1, 'Vicente Angélica de la Torre Tejeda', 1),
  (2, 'Dalia María Teresa Ojeda', 3),
  (3, 'Timoteo Porfirio Gaona Meléndez', 4),
  (4, 'Estela Aparicio Mata', 3),
  (5, 'Gabriel Barraza', 1),
  (6, 'Raquel Ignacio Galindo', 2),
  (7, 'Leonardo Reynoso', 5),
  (8, 'Gabino Clara Gurule', 3),
  (9, 'Ing. Frida Viera', 2),
  (10, 'Rodolfo Ozuna', 4),
  (11, 'Estefanía Citlali Saucedo Salcido', 4),
  (12, 'Amanda Carmona Corral', 4),
  (13, 'Luisa Rubén Barela', 2),
  (14, 'Juana Ybarra', 3),
  (15, 'Óliver Heredia', 2),
  (16, 'Sr(a). Camila Terán', 2),
  (17, 'Tomás Jacinto Carrasco Lozada', 5),
  (18, 'Cristina Rendón', 5),
  (19, 'Frida Sanches Domínguez', 3),
  (20, 'Sr(a). Socorro Lugo', 5);

