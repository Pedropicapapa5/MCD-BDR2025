-- Regresion lineal

DELIMITER $$

CREATE FUNCTION calcular_pendiente(
    tabla VARCHAR(64),
    columna_x VARCHAR(64),
    columna_y VARCHAR(64)
) RETURNS DECIMAL(10,5)
DETERMINISTIC
BEGIN
  SET @sql = CONCAT(
    'SELECT (SUM(x*y) - SUM(x)*SUM(y)/COUNT(*)) / (SUM(x*x) - (SUM(x)*SUM(x))/COUNT(*)) INTO @pendiente ',
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



-- Correlacion entre 2 conjuntos de datos

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
