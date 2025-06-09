# Base de datos
Esta evidencia se creo un diagrama entidad-relación no estructurado sobre el **maquillaje**, donde;
- **Hexágono**: relación (MAQUILLAJE)
- **Estadios**: para las entidades
- **Rectángulos**: para los atributos
- **Trapezoides**: para los dominios de cada uno de los atributo

```mermaid


  flowchart TD
    Maquillaje["Maquillaje"] --> Producto(["Producto"]) & Tono(["Tono"]) & Origen(["Origen"]) & Marca(["Marca"]) & Ingrediente(["Ingrediente"]) & Reseña(["Reseña"])
    Producto --> Labial["Labial"] & Base["Base"] & Ojos["Ojos"] & Primer["Primer"]
    Labial -- Tipos --> Gloss["Gloss"] & Barra["Barra"] & Tinta["Tinta"]
    Base -- Acabado --> Matte["Matte"] & SemiMatte["SemiMatte"] & Satinado["Satinado"]
    Ojos --> Sombras["Sombras"] & Rimel["Rimel"]
    Primer --> Tubo["Tubo"] & Spray["Spray"]
    Tono --> Neutro["Neutro"] & Calido["Calido"] & Frio["Frio"]
    Origen --> Pais["Pais"]
    Marca --> Lujo["Lujo"] & Semi["Semi"] & NoLujo["NoLujo"]
    Ingrediente --> Natural["Natural"] & Quimico["Quimico"]
    Reseña --> Usuario["Usuario"]
    Maquillaje@{ shape: hex}
    Gloss@{ shape: trap-b}
    Barra@{ shape: trap-b}
    Tinta@{ shape: trap-b}
    Matte@{ shape: trap-b}
    SemiMatte@{ shape: trap-b}
    Satinado@{ shape: trap-b}
    Sombras@{ shape: trap-b}
    Rimel@{ shape: trap-b}
    Tubo@{ shape: trap-b}
    Spray@{ shape: trap-b}
```

# Dominio de los atributos

| Dominio     | Atributo | Descripción                                   | Tipo de dato | Ejemplo de dominio                                             |
|-------------|----------|-----------------------------------------------|---------------|----------------------------------------------------------------|
| PRODUCTO    | LABIAL   | Tipo de labial                                | String        | {'Gloss', 'Barra', 'Tinta'}                                   |
|             | BASE     | Acabado de la base                            | String        | {'Matte', 'SemiMatte', 'Satinado'}                            |
|             | OJOS     | Producto para los ojos                        | String        | {'Sombras', 'Rimel'}                                          |
|             | PRIMER   | Tipo de presentación                          | String        | {'Tubo', 'Spray'}                                             |
| TONO        | NEUTRO   | Tipo de subtono                               | String        | {'Mute', 'Bright', 'Deep'}                                    |
|             | CÁLIDO   | Tipo de subtono                               | String        | {'Mute', 'Bright', 'Deep'}                                    |
|             | FRÍO     | Tipo de subtono                               | String        | {'Mute', 'Bright', 'Deep'}                                    |
| ORIGEN      | PAÍS     | País donde se creó                            | String        | {'Estados Unidos', 'México', 'Corea del Sur'}                |
| INGREDIENTE | NATURAL  | Tipo de ingrediente sin modificación          | String        | {'Leche de arroz', 'Centella Asiática', 'Aloe Vera'}         |
|             | QUÍMICO  | Tipo de ingrediente con modificación          | String        | {'Ceramida', 'Propaneidol', 'Panthenol'}                      |
| RESEÑA      | USUARIO  | Calificación que dio el usuario               | Float         | Valores positivos; 2.9, 4.5, 5                                |
