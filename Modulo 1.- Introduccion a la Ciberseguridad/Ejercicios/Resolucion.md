Ejercicio 1.- El equipo policial ha conseguido un volcado de memoria de un equipo en el que se introdujo un famoso ciberdelincuente. Se sabe que el ciberdelincuente estaba intentado descargarse archivos mediante una herramienta de certificación. Encuentra el nombre del archivo descargado (archivo "file_2.rar").
    - Este ejercicio hay varias formas de resolverlo:
        - La primera y más sencilla de ver es utilizando la opción cmdscan de volatility:
            - `volatility -f Desktop_Phineas.raw imageinfo` - Descubrimos que se trata de un sistema Windows que tiene como perfil "Win7SP1x64". Procedemos ahora a ver el árbol de procesos que se encontraban activos en el momento del volcado de memoria.
            - `volatility -f Desktop_Phineas.raw --profile=Win7SP1x64 cmdscan` - Descubrimos que utilizó un programa llamado "certutil.exe" y descargó un archivo pdf cuyo nombre es la flag.
        - La segunda y más compleja es por medio del árbol de procesos:
            - `volatility -f Desktop_Phineas.raw --profile=Win7SP1x64 pstree` - Vemos el árbol de procesos que se encontraban activos en el momento del volcado de memoria y nos fijamos en los procesos cuyo nombre es "GoogleCrashMan". Investigando sobre este proceso en Internet descubrimos que es un proceso regular de Google que se ejecuta cuando el navegador crashea pero también hay quien dice que se puede usar como malware. Puesto que hay dos procesos con el mismo nombre procedemos a descargar ambos y examinarlos a fondos. 
            - `volatility -f Desktop_Phineas.raw --profile=Win7SP1x64 memdump -p 1632 -D .`
            - `volatility -f Desktop_Phineas.raw --profile=Win7SP1x64 memdump -p 1644 -D .`
            - Convertimos ambos ficheros a texto para analizarlos con `strings -e l 1632.dmp > strings_1632_16bits.txt` `strings -e l 1644.dmp > strings_1644_16bits.txt`. 
            - Si investigamos a fondo el segundo archivo (relativo al proceso 1644) y usamos la herramienta de búsqueda con "file:" podemos encontrar la siguiente ruta de un archivo "file:C:/Users/Phineas_Fisher/4rCh1v0s_P0L1c14L3s.pdf"
    - Flag: "4rCh1v0s_P0L1c14L3s.pdf"


Ejercicio 2.- También se sabe que por lo visto el atacante dejo un mensaje de intrusión en el escritorio mediante una aplicación de dibujo (archivo "file_2.rar").
    - `volatility -f Desktop_Phineas.raw imageinfo` - Descubrimos que se trata de un sistema Windows que tiene como perfil "Win7SP1x64". Procedemos ahora a ver el árbol de procesos que se encontraban activos en el momento del volcado de memoria.
    - `volatility -f Desktop_Phineas.raw --profile=Win7SP1x64 pstree` - El enunciado nos dice que se usó una aplicación de dibujo y entre los procesos podemos ver "mspaint.exe" que se trata de la aplicación Paint de Windows. Procedemos a descargar la información asociada a ese proceso que tiene como pid 1072 en el directorio actual (.).
    - `volatility -f Desktop_Phineas.raw --profile=Win7SP1x64 memdump -p 1540 -D .`
    - Probamos a convertir el fichero descargado en texto por ver si podemos encontrar la flag con `strings -e l 1450.dmp > strings_1450_16bits.txt` pero no encontramos nada. No obstante el ejercicio nos dice que dejó un archivo con el mensaje en el escritorio. Intentamos buscar por la palabra "Desktop" y encontramos el siguiente archivo "\Device\HarddiskVolume1\Users\Phineas_Fisher\Desktop\DumpIt.exe" que también se encuentra como proceso en el árbol de procesos del volcado de memoria. De nuevo nos lo descargamos.
    - `volatility -f Desktop_Phineas.raw --profile=Win7SP1x64 memdump -p 1072 -D .`
    - (Opcional) De nuevo probamos a convertir el fichero descargado en texto por ver si podemos encontrar la flag con `strings -e l 1072.dmp > strings_1072_16bits.txt` pero esta vez no tenemos suerte.
    - Puesto que se trata de un volcado de memoria RAM el archivo descargado será un estado no definitivo de una imagen, tiene sentido entonces probar a abrir el archivo como si fuera una imagen. Para ello necesitaremos cambiar la extensión del archivo descargado (.dmp) a .data. Una vez hecho esto abriremos la imagen con Gimp, donde primero nos saldrá una ventana donde podremos modificar distintos parámetros como el Image Type, Offset, Width, Height y los colores. Probando distintas combinaciones de estos parámetros llegamos a obtener la flag.
        - Opciones seleccionadas:
            - Image Type: RGB Alpha
            - Offset: 129762802
            - Width: 1920
            - Height: 768
            - Palette Type: R,G,B (normal)
            - Offset: 0
        - Flag: "P1ntur4_al_0l3O" -> Por tanto la solución al ejercicio será modulo1{P1ntur4_al_0l3O}

Ejercicio 3.- Al parecer el equipo estaba conectando con algun centro de control remoto localiza la dirección. Encuentra el nombre del archivo descargado (archivo "file_2.rar").

Ejercicio 4.- Tenemos una imagen de una máquina virtual con el flag pero no sabemos recuperarlo. ¿Podrías ayudarnos? (archivo "module1.zip").

Descargar la carpeta que contiene los recursos para los ejercicios aquí - https://drive.google.com/drive/folders/1ArHNM30i8E6uZVjnjPf4yJdOh5lacNXS?usp=sharing



Win2008R2SP0x64, Win7SP1x64, Win7SP0x64, Win2008R2SP1x64


https://t.me/C1b3rWallAcademy