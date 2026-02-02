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


@startuml
left to right direction

actor Cliente
actor "Administrador" as Admin

rectangle "Sistema de Citas Óptica" {

  Cliente -- (Registrarse)
  Cliente -- (Iniciar sesión)
  Cliente -- (Reservar cita)
  Cliente -- (Ver citas)
  Cliente -- (Cancelar cita)
  Cliente -- (Ver ficha)

  Admin -- (Iniciar sesión)
  Admin -- (Ver agenda)
  Admin -- (Gestionar citas)
  Admin -- (Gestionar usuarios)
  Admin -- (Gestionar ficha de cliente)
  
 (Gestionar ficha de cliente) .> (Ver ficha) : <<include>>
 (Gestionar citas).> (Reservar cita) : <<include>>
 (Gestionar citas).> (Ver cita) : <<include>>
 (Gestionar citas).> (Cancelar cita) : <<include>>
}

@enduml

El diagrama de casos de uso representa las funcionalidades principales del sistema desde el punto de vista del usuario. El cliente puede registrarse, iniciar sesión y gestionar sus citas, mientras que el personal de la óptica dispone de funciones avanzadas como la gestión de citas, servicios y la ficha del cliente, donde se almacena la información relevante de cada cliente.


### Diagrama de componentes

@startuml

component "Sistema de citas para Ópticas" {
  [Interfaz de Usuario] as UI
  [Sistema de Gestión de citas] as Manager
  [Base de datos] as DB
}

component "Control de citas" {
      [Reservar cita]
      [Ver cita]
      [Cancelar cita]
      Manager --> [Reservar cita]
      Manager --> [Ver cita]
      Manager --> [Cancelar cita]
}

component "Gestión de Usuarios" {
    [Clientes]
    [Administradores]
    UI --> [Clientes]
    UI --> [Administradores]
}
component "Agenda" {
      [Reservar cita]
      [Ver cita]
      [Cancelar cita]
      Manager --> [Reservar cita]
      Manager --> [Ver cita]
      Manager --> [Cancelar cita]
}

component "Notificaciones" {
      [Enviar notificación]
      [Enviar recordatorios]
      [Alerta de cancelación]
      Manager --> [Enviar notificación]
      Manager --> [Enviar recordatorios]
      Manager --> [Alerta de cancelación]
}


component "Base de Datos" {
  [Usuarios]
  [Citas]
  [Fichas]
}

[Clientes] ..> UI: Utiliza
[Administradores] ..> UI: Utiliza
Frontend ..> Backend : HTTP / Peticiones
Backend ..> DB : Almacena/recupera

@enduml

Interfaz de usuario: 
Sistema de gestión de citas
Base de datos
Modulos funcionales:
