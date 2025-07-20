# Procedimientos y funciones

En esta evidencia, crearemos dos funciones almacenadas (STORED FUNCTIONS) en SQL para trabajar con:
- Regresión lineal simple
- Coeficiente de correlación entre 2 conjuntos de datos

## Función para Regresión Lineal (pendiente β1 y ordenada β0)

Esta función calcula la pendiente de la recta de regresión lineal entre dos columnas *x* y *y*.

    DELIMITER $$
    
    CREATE FUNCTION calcular_pendiente(
        tabla VARCHAR(64),
        columna_x VARCHAR(64),
        columna_y VARCHAR(64)
    ) RETURNS DECIMAL(10,5)
    DETERMINISTIC
    BEGIN
      SET @sql = CONCAT(
        'SELECT (SUM(x*y) - SUM(x)*SUM(y)/COUNT(*)) / (SUM(x*x) - (SUM(x)*SUM(x))/COUNT(*)) INTO     @pendiente ',
        'FROM (SELECT ',
        columna_x, ' AS x, ',
        columna_y, ' AS y FROM ', tabla, ') AS datos'
      );
    
      PREPARE stmt FROM @sql;
      EXECUTE stmt;
      DEALLOCATE PREPARE stmt;
    
      RETURN @pendiente;
    END$$
    
    DELIMITER ;



### Uso

En el caso de la base de datos de maquillaje se utilizaría así:

    SELECT calcular_pendiente('Reseña', 'ID_Reseña', 'Calificacion');

    - Esto te da la pendiente de la regresión lineal entre *ID_Reseña* y *Calificación*.

*Nota*: solo se calcula la pendiente (β1), para obtener la ordenada al origen (β0) se necesitaría extender la función.


## Función para Correlación entre 2 conjuntos de datos

Esta función calcula el coeficiente de correlación r, que mide la relación lineal entre dos variables.

    DELIMITER $$
    
    CREATE FUNCTION calcular_correlacion(
        tabla VARCHAR(64),
        columna_x VARCHAR(64),
        columna_y VARCHAR(64)
    ) RETURNS DECIMAL(10,5)
    DETERMINISTIC
    BEGIN
      SET @sql = CONCAT(
        'SELECT (SUM((x - avg_x)*(y - avg_y))) / SQRT(SUM(POW(x - avg_x,2)) * SUM(POW(y - avg_y,2))) INTO @correlacion ',
        'FROM (',
        'SELECT ',
        columna_x, ' AS x, ',
        columna_y, ' AS y, ',
        '(SELECT AVG(', columna_x, ') FROM ', tabla, ') AS avg_x, ',
        '(SELECT AVG(', columna_y, ') FROM ', tabla, ') AS avg_y ',
        'FROM ', tabla,
        ') AS datos'
      );
    
      PREPARE stmt FROM @sql;
      EXECUTE stmt;
      DEALLOCATE PREPARE stmt;
    
      RETURN @correlacion;
    END$$
    
    DELIMITER ;


### Uso

En el caso de la base de datos de maquillaje se utilizaría así:

    SELECT calcular_correlacion('Reseña', 'ID_Reseña', 'Calificacion');

- Esto te devuelve el valor r, que:
    1. Es cercano a 1 si hay una fuerte correlación positiva.
    2. Cercano a -1 si es negativa.
    3. Cercano a 0 si no hay relación lineal.
