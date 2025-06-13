  
#guia de uso

## 1 ejecutar el *brojker*
abre una terminal (*cmd*)
~~~ bash
python broker.py
~~~

se mostrara como resultado
~~~ bash
[BROKER]Escuchando ne 0.0.0.0:1400....
~~~
## 2. Ejecutar uno o mas suscriptores 
Abre una termninal y ejecuta un suscriptor 
o mas 

~~~bash
    python suscriber.py
~~~
Cuendo se te pida escribe el tema
(*topic*), por ejemplo:
~~~bash
Tema a suscribirse: deportes
~~~
El sistema mantendra la conexion abierta esperando mensajes del *broker*

## 3. Ejecutar uno o mas publicaodres 
En otra terminal:
~~~bash
python publisher.py
~~~
Envia un mensaje en este formato:
~~~bash
deportes:¡El america perdio 15-0!
~~~
Todos los *suscriptores* suscritos a *deportes*recibiran:
~~~bash
[deportes]¡El pumas gano 5-0!
~~~
