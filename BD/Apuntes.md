# Apuntes de Bases de Datos SQL

## 1. ¿Qué es SQL?
SQL (Structured Query Language) es un lenguaje estándar para gestionar bases de datos relacionales. Permite crear, modificar, consultar y administrar datos.

## 2. Tipos de Sentencias SQL

### a) DDL (Data Definition Language)
- `CREATE`: Crea tablas, vistas, índices, etc.
- `ALTER`: Modifica la estructura de una tabla.
- `DROP`: Elimina tablas, vistas, etc.

```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100)
);
```

### b) DML (Data Manipulation Language)
- `INSERT`: Inserta datos.
- `UPDATE`: Modifica datos existentes.
- `DELETE`: Elimina datos.

```sql
INSERT INTO usuarios (id, nombre, email) VALUES (1, 'Ana', 'ana@email.com');
UPDATE usuarios SET nombre = 'Ana Gómez' WHERE id = 1;
DELETE FROM usuarios WHERE id = 1;
```

### c) DQL (Data Query Language)
- `SELECT`: Consulta datos.

```sql
SELECT nombre, email FROM usuarios WHERE id = 1;
```

### d) DCL (Data Control Language)
- `GRANT`: Concede permisos.
- `REVOKE`: Revoca permisos.

## 3. Cláusulas Importantes

- `WHERE`: Filtra registros.
- `ORDER BY`: Ordena resultados.
- `GROUP BY`: Agrupa resultados.
- `HAVING`: Filtra grupos.

## 4. Relaciones entre Tablas

- **Clave primaria (PRIMARY KEY):** Identifica de forma única cada registro.
- **Clave foránea (FOREIGN KEY):** Relaciona dos tablas.

```sql
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
```

## 5. Funciones de Agregación

- `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`

```sql
SELECT COUNT(*) FROM usuarios;
SELECT AVG(precio) FROM productos;
```

## 6. Joins (Uniones)

- `INNER JOIN`: Solo registros coincidentes.
- `LEFT JOIN`: Todos los de la izquierda y coincidentes de la derecha.
- `RIGHT JOIN`: Todos los de la derecha y coincidentes de la izquierda.

```sql
SELECT u.nombre, p.id
FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id;
```

## 7. Buenas Prácticas

- Usar nombres descriptivos para tablas y columnas.
- Normalizar la base de datos para evitar redundancias.
- Realizar copias de seguridad periódicas.

---

**Recuerda:** Practica con ejemplos y consulta la documentación oficial de tu gestor de base de datos (MySQL, PostgreSQL, SQL Server, etc.).

Modelo ER