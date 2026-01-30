### Chan Voong Tran

### Proyecto intermodular

## Fase de diseño del sistema de reserva de citas


### Diagrama de casos de uso

#### Actores

* Cliente: Interactua con la interfaz para:
  * Gestionar su cita
  * Ver su ficha
  
* Administradores/Empleados de la tienda: 
  * Controlar y gestionar las citas 
  * Gestionar usuarios

#### Casos de uso principal

* Cliente:
  * Reservar cita
  * Modificacion de cita
  * Cancelar cita
  * Visualizar cita
  * Seguimiento de cita
  * Confirmación de cita
  * Visualizar ficha
* Administrador:
  * Administrar cita
  * Administrar agenda
  * Administrar ficha
  * Administrar usuarios

### Diagrama de componentes

@startuml
skinparam componentStyle rectangle

package "Aplicación Web (Frontend)" {
  [Interfaz de Usuario]
}

package "Servidor Backend\n(API REST)" {
  [Gestión de Usuarios]
  [Gestión de Citas]
  [Gestión de Horarios]
  [Autenticación]
}

package "Base de Datos" {
  [Usuarios]
  [Citas]
  [Horarios]
}

[Clientes] ..> UI: Utiliza
[Administradores] ..> UI: Utiliza
Frontend ..> Backend : HTTP / REST
Backend ..> DB : JDBC / ORM

@enduml


Interfaz de usuario: 
Sistema de gestión de citas
Base de datos
Modulos funcionales:
