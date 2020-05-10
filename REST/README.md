# REST

Para la ejecución del webservice Rest debemos instalar los siguientes programas y paquetes


# Instalación

La ejecucion del webservice al momento de ser subido al repositorio de github estaba corriendo con Python 3.8.2 y Node.js 14.2.0, por lo ques estos 2 deben estar instalados y adheridos al path de windows.
Luego en la consola de windows se deben ejecutar los siguientes comandos con pip para instalar distintas librerias y paquetes.

```

pip install django
pip install djangorestframework
pip install django-cors-headers

```

Luego con npm de Node.js ejecutamos los siguientes comandos.

```

npm install bootsrap-vue
npm install axios
npm install sweetalert


```

# Ejecución

Para que el webservice corra, debemos ejecutar primero el servidor con el siguiente comando en la carpeta donde se encuentra el server, en este caso Trabajo_Redes\REST\

```

python manage.py runserver

```

Para levantar el cliente entramos a la carpeta del cliente Trabajo_Redes\REST\cliente\ en este caso, y ejecutamos el siguiente comando

```

npm run dev

```
