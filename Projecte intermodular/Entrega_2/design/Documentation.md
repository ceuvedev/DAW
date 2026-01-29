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

package "Gestion de usuarios" {
  [Cliente]
  [Administradores]
}

package "Servidor" {
  [Interfaz de usuario]
}

package "Cliente" {
  [Interfaz de usuario]
}

package "Cliente" {
  [Interfaz de usuario]
}