[![Build Status](https://app.travis-ci.com/jval7/user-registration.svg?branch=main)](https://app.travis-ci.com/jval7/user-registration)
# Coink test
### Porfavor seguir los siguientes comandos para levantar la api:

### La api fue construida en flask y la base de datos con MYSQL, todo esta corriendo en docker. Para levantar los servicios utilizar:

``` shell  
$ docker-compose up
```
Esperar al menos 20 segundos a que la base de datos este funcionando
y luego dirigirse a localhost:5001

Una vez en la pagina web, veremos un menu en el lado izquierdo
con dos opciones:
- Registrar
- Lista de usuarios

En la primera opción aparecerá un formulario 
para registrar ususarios.

Una vez tenga varios usuarios registrados, dirigase
a la segunda opción y mire la lista de usuarios en 
la tabla paginada.

# Archivos Log
En la carpeta de la aplicacion encontrará
un archivo logs.txt donde se guardaran los eventos
relacionados con los usuarios. para ingresar a ella 
siga los siguientes comandos

``` shell  
$ docker exec -it coink_app_coink_1  bash 

```

asegurese que el nombre del contenedor sea igual al
del comando, en caso contrario modifique al nombre actual.

aparecerá algo como esto:
``` shell  
$ root@cf82acde76c3:/app#
```
ingrese el siguiente comando:
``` shell  
$ cat logs.txt 
```
por último, verá algo como esto:
``` shell
User created at: 22/01/2022 14:37:25 : 
{'name': 'jhon valderrama', 'email': 'jhonjj1993@gmail.com', 'city': 'Cali Valle del cauca'}
User created at: 22/01/2022 14:37:43 :
{'name': 'Gabriela munoz', 'email': 'grabiela@gmail.com', 'city': 'Santander'}
```
