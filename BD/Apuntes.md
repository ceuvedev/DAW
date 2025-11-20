## Tema 3 Diseño de BB.DD. El modelo relacional

### Introducción

El objetivo del modelo relacional es obtener un conjunto de relaciones sin redundancia y que cumplan las necesidades requeridas.

Para eso sirve el modelo relacional, trasformando el esquema ER a tablas.

### 2 Conceptos básicos del modelo relacional

#### Modelos y esquemas

En la fase de diseño transformamos el **esquema conceptual** a un **esquema lógico**

[imagen](/BD/imagenes/modeloesquema.png)

Diferencias entre modelo y esquema:
    Modelo: es una herramienta para representar datos
    Esquema: es la representación de esos datos

#### Elementos del modelo relacional

En la tabla se ven los distintos tipos de elementos y lo que equivale  según  la fase en la que está

||Fase Analisis|Fase Diseño|Implementación|
|---|---|---|---|
|Model|ER|Relacional|Físico|
|Objetos|Entidades y relaciones|Relaciones|Tablas|
|Características|Atributos|Campos|Columnas|
|Datos|Ocurrencias|Registros/Tuplas|Filas|

El modelo relacional representa una BD como un conjunto de relaciones.

**Las claves** sirven para en el modelo relacional no haya ocurrencias duplicadas. Hay dos tipos de claves: claves candidatas y claves externas.
Es un atributo (o más de uno) de la tabla que cumplen 2 condiciones:  
    Unicidad: No puede haver dos tuplas de relacion con el mismo valor de atributo
    Minimalismo: No sobre ningún atributo de la clave
    