# Consultas

Ya que ah repasado las funciones para crear y editar nuestras bases de datos, tambien una pieza fundamental son también las consultas de nuestros datos, para este tipo tenemos varias opciones tales como:
- Conteo de frecuencias o media
- Mínimos y máximos
- Cuantiles
- Moda, etc.

En esta evidencia se tomaron las tablas de datos de *Producto*, *Tono*, *Origen*, *Marca*, *Ingrediente* y *Reseña*.

**Conteo de frecuencias**: ¿Cuántos productos hay por tipo? (Labial, Base, etc.)

    SELECT Tipo, COUNT(*) AS Frecuencia

    FROM Producto

    GROUP BY Tipo;

**Mínimos y máximos**: ¿Cuál es la calificación mínima y máxima de las reseñas?

    SELECT 

        MIN(Calificacion) AS Calificacion_Minima,

        MAX(Calificacion) AS Calificacion_Maxima

    FROM Reseña;

Otro ejemplo podría ser para saber cuántos productos tiene cada subtipo y ver el máximo:

    SELECT Subtipo, COUNT(*) AS Total

    FROM Producto

    GROUP BY Subtipo

    ORDER BY Total DESC;

**Cuantiles**: Para poder usar un cuantil diferente a la media se requiere obtener el percentil 25 (Q1) y percentil 75 (Q3) de las calificaciones:

    SELECT 

        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY Calificacion) AS Q1,

        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY Calificacion) AS Q3

    FROM Reseña;

**Moda**: ¿Cuál es la calificación que más se repite?

    SELECT Calificacion

    FROM Reseña

    GROUP BY Calificacion

    ORDER BY COUNT(*) DESC

    LIMIT 1;

Y otro ejemplo un poco más detallado podemos ver todas las calificaciones y su frecuencia para detectar la(s) moda(s):

    SELECT Calificacion, COUNT(*) AS Frecuencia

    FROM Reseña

    GROUP BY Calificacion

    ORDER BY Frecuencia DESC;
