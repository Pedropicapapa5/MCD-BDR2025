# Composición, vistas y disparadores

En esta evidencia, se crearon vistas para la base de datos del *maquillaje*, a continuación se presentan los tipos de vistas incluidos:

- Vista con **JOIN** (Producto + Marca):  Aquí uniremos la tabla *Producto* con *Marca* usando los campos *ID_Producto = ID_Marca*. queremos ver fácilmente qué tipo de producto pertenece a qué categoría de marca.  Para poder correr JOIN queremos qué el tipo de producto pertenezca a la categoría de marca.

      CREATE VIEW Vista_Productos_Marca AS
      SELECT 
        P.ID_Producto,
        P.Tipo AS Tipo_Producto,
        P.Subtipo,
        M.Categoria AS Categoria_Marca
      FROM Producto P
      JOIN Marca M ON P.ID_Producto = M.ID_Marca;


- Vista con **LEFT JOIN** (Productos y sus reseñas): Une los productos con sus reseñas, pero usando LEFT JOIN, lo que muestra todos los productos, incluso si no tienen reseña.
  
      CREATE VIEW Vista_Producto_Resenas AS
      SELECT 
        P.ID_Producto,
        P.Tipo,
        R.Usuario,
        R.Calificacion
      FROM Producto P
      LEFT JOIN Reseña R ON P.ID_Producto = R.ID_Reseña;

- Vista con **RIGHT JOIN**: Ingredientes mencionados, aunque no estén en productos (caso forzado para mostrar sintaxis)
