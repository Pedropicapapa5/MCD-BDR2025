CREATE VIEW Vista_Productos_Marca AS
SELECT 
  P.ID_Producto,
  P.Tipo AS Tipo_Producto,
  P.Subtipo,
  M.Categoria AS Categoria_Marca
FROM Producto P
JOIN Marca M ON P.ID_Producto = M.ID_Marca;

CREATE VIEW Vista_Producto_Resenas AS
SELECT 
  P.ID_Producto,
  P.Tipo,
  R.Usuario,
  R.Calificacion
FROM Producto P
LEFT JOIN Reseña R ON P.ID_Producto = R.ID_Reseña;

CREATE VIEW Vista_Ingredientes_Productos AS
SELECT 
  I.ID_Ingrediente,
  I.Nombre,
  P.Tipo
FROM Producto P
RIGHT JOIN Ingrediente I ON P.ID_Producto = I.ID_Ingrediente;

CREATE VIEW Vista_Productos_Sobresalientes AS
SELECT 
  P.ID_Producto,
  P.Tipo,
  R.Calificacion
FROM Producto P
JOIN Reseña R ON P.ID_Producto = R.ID_Reseña
WHERE R.Calificacion > (
  SELECT AVG(Calificacion) FROM Reseña
);

CREATE TABLE Reseña_Eliminada (
  ID_Reseña INT,
  Usuario VARCHAR(50),
  Calificacion INT,
  FechaEliminacion DATETIME
);

DELIMITER $$

CREATE TRIGGER trg_reseña_delete
BEFORE DELETE ON Reseña
FOR EACH ROW
BEGIN
  INSERT INTO Reseña_Eliminada (ID_Reseña, Usuario, Calificacion, FechaEliminacion)
  VALUES (OLD.ID_Reseña, OLD.Usuario, OLD.Calificacion, NOW());
END$$

DELIMITER ;
