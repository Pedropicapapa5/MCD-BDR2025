# Composición, vistas y disparadores

En esta evidencia, se crearon vistas y un disparador para la base de datos del *maquillaje*, a continuación se presentan los tipos incluidos:

## Vistas
Una vista (**VIEW**) en SQL es como una consulta guardada. No guarda datos nuevos, solo una forma útil de consultar datos de forma rápida y repetitiva.

- **JOIN** (Producto + Marca):  Aquí uniremos la tabla *Producto* con *Marca* usando los campos *ID_Producto = ID_Marca*. queremos ver fácilmente qué tipo de producto pertenece a qué categoría de marca.  Para poder correr JOIN queremos qué el tipo de producto pertenezca a la categoría de marca.

      CREATE VIEW Vista_Productos_Marca AS
      SELECT 
        P.ID_Producto,
        P.Tipo AS Tipo_Producto,
        P.Subtipo,
        M.Categoria AS Categoria_Marca
      FROM Producto P
      JOIN Marca M ON P.ID_Producto = M.ID_Marca;

- **LEFT JOIN** (Productos y sus reseñas): Une los productos con sus reseñas, pero usando LEFT JOIN, lo que muestra todos los productos, incluso si no tienen reseña.

      CREATE VIEW Vista_Producto_Resenas AS
      SELECT 
        P.ID_Producto,
        P.Tipo,
        R.Usuario,
        R.Calificacion
      FROM Producto P
      LEFT JOIN Reseña R ON P.ID_Producto = R.ID_Reseña;

- **RIGHT JOIN**: Se usa cuando quieres revisar los ingredientes registrados, incluso si no se han utilizado aún. Este RIGHT JOIN es solo para ejemplificar, pero usualmente tendrías una tabla intermedia como Producto_Ingrediente para esta relación.

      CREATE VIEW Vista_Ingredientes_Productos AS
      SELECT 
        I.ID_Ingrediente,
        I.Nombre,
        P.Tipo
      FROM Producto P
      RIGHT JOIN Ingrediente I ON P.ID_Producto = I.ID_Ingrediente;

- **Subconsulta** (Productos con calificación mayor al promedio): Aqui usaremos **SELECT AVG** que es una subconsulta que usaremos para identificar productos que tienen buenas reseñas comparadas con la media.

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


## Disparador
Un disparador (**TRIGGER**) es un bloque de código que se ejecuta automáticamente cuando ocurre una acción: *INSERT*, *UPDATE* o *DELETE*.

- Trigger antes de eliminar reseñas

      CREATE TABLE Reseña_Eliminada (
        ID_Reseña INT,
        Usuario VARCHAR(50),
        Calificacion INT,
        FechaEliminacion DATETIME
      );
*Nota*: Esta tabla guardará las reseñas eliminadas, como si fuera un "historial".
      DELIMITER $$
      
      CREATE TRIGGER trg_reseña_delete
      BEFORE DELETE ON Reseña
      FOR EACH ROW
      BEGIN
        INSERT INTO Reseña_Eliminada (ID_Reseña, Usuario, Calificacion, FechaEliminacion)
        VALUES (OLD.ID_Reseña, OLD.Usuario, OLD.Calificacion, NOW());
      END$$
      
      DELIMITER ;

### ¿Qué hace este trigger?

- Se activa antes de que se borre una reseña.

- Copia la información de la reseña eliminada a la tabla Reseña_Eliminada.

- Agrega además la fecha y hora exacta en que fue borrada.

### ¿Para qué sirve?

- Para tener control y seguimiento de los cambios.

- Evita pérdida total de información por eliminaciones.
