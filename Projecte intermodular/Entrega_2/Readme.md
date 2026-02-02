### Chan Voong Tran

#### Proyecto intermodular 

#### 2da entrega


### Objetivo 

El objetivo de esta segunda entrega es de diseñar la arquitectura técnica de una aplicación de reserva de citas.

Se ha utilizado diagramas UML y unos bocemos UI/UX



### Diagrama UML casos de uso

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

![Diagrama casos de uso](design/diagramCasosUso.png)

### Diagrama UML de componentes


El diagrama de componentes muestra la estructura general del sistema y la relación entre sus principales módulos.
El sistema se divide en un frontend web, encargado de la interacción con el usuario, un backend que gestiona la lógica de negocio y una base de datos donde se almacenan las citas, los clientes y la ficha del cliente.
Adicionalmente, el backend puede comunicarse con un servicio de notificaciones para el envío de confirmaciones de citas.

![Diagrama de componentes](design/diagramaComponentesbrillo.png)