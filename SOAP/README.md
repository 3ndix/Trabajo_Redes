# SOAP

Para la ejecucion del webservice SOAP debemos seguir los sguientes pasos

# Instalación

El primer paso es instalar el programa XAMPP en su version 7.2.30, luego descargamos la libreria NUSOAP, este archivo lo extraemos y pegamos la carpeta "lib" en donde se encuentra la carpeta SOAP. Es decir, dentro de esta carpeta (SOAP) deben quedar 2 archivos, sevicio.php y la carpeta lib.
Posterior a ello procedemos a copiar la carpeta SOAP, buscamos la ruta donde se encuentra XAMPP, la cual probablemente este en el disco C. Dentro de la carpeta xampp entramos a la carpeta htdocs y pegamos la carpeta SOAP.
Para consumir este servidor usaremos SOAP UI, por lo que debemos tenerlo instalado tambien.

# Ejecución

Ejecutamos el programa XAMPP y en la fila que dice Apache pulsamos el boton que dice Start. Luego accedemos a la siguiente url; http://localhost/SOAP/servicio.php.
Finalmente ejecutamos SOAP UI, pulsamos en NEW PROJECT, y pegamos el link antes mostrado, es desde aqui donde consumiremos el api

