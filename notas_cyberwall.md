# CyberWall Academy

## Módulo 1.- Introducción a la Ciberseguridad

### Tema 1.- Uso de Recursos en Internet con OSINT. Eduardo Sanchez

OSINT significa Open Source Intelligence (en español Inteligencia de Fuentes Abiertas), y se trata de un conjunto de técnicas y herramientas para recopilar información pública, correlacionar los datos y procesarlos.

Pongamos como caso práctico que intentamos buscarnos a nosotros mismos por medio de nuestro nombre y apellido. Es probable que no nos encontremos a la primera, pero para ello podemos usar operadores de google para eliminar falsos positivos. 

Si por ejemplo nuestro nombre coincidiera con un tenista podemos buscar `"Nombre Apellido" -tenis`, de esta manera eliminamos la palabra clave tenis de los resultados. Con cada búsqueda que hagamos podemos añadir una palabra clave a la búsqueda, de esta manera la retroalimentamos y la vamos haciendo más precisa.

Supongamos ahora que en lugar de un nombre y apellido tenemos un correo electrónico. Para conseguir este correo podemos meternos en cualquier web, por ejemplo marca.com y por medio de la extensión de chrome `hunter` encontramos un correo. Una vez en posesión del correo se podría ejecutar cualquier técnica maliciosa.

Es posible que si hacemos varias búsquedas a una página con esta extensión en distintos momentos nos de un error a la hora de encontrar un correo. Es decir que este correo halla desaparecido. No obstante cuando nosotros buscamos por una web en google es posible que al lado del título veamos una flechita hacia abajo donde se desplegará las versiones que tenemos en caché de esa página. En caso de que esta flecha no esté disponible para la web que queremos podemos utilizar la web archive.org en la que podemos hacer búsquedas de dominios para saber cómo estaba la web para una fecha concreta y ahí buscar el correo. Esto nos permite ver que no basta con eliminar o cambiar o quitar de la web el contenido, ya que hay webs que recopilan la información como archive.org o cacheview.com.

Por otro lado tenemos la web pastebin.com que se usa para pegar trozos de código que luego podemos compartir. Si en google buscamos `site:pastebin.com gmail hacked` buscamos los correos electrónicos de esa página que han sido hackeados con correo y contraseña. Estos datos suelen producirse por fallos de seguridad en sitios web que luego la gente descubre.

Podemos intentar comprobar si nuestra cuenta ha sido atacada de alguna manera medidante la web `haveibeenpwned.com`. Es probable que aunque nuestra cuenta halla sido comprometida no se encuentre la contraseña fácilmente, no obstante podemos buscar por medio de la red tor el sitio web `pwndb2am4tzkvold.onion` nuestro correo.

Existen también herramientas desarrolladas como mailfy que busca si el correo que le pasemos se encuentra registrado en alguna red social con el comando `mailfy -m mycorreo@correo.com`. `h8mail -t mycorreo@correo.com` nos busca los diferentes leaks que halla podido tener un correo. 

Otra herramienta es `robtex.com`. Con esta web podemos buscar otras webs como marca.com y obtener un análisis con sus IPs, su ubicación, etc, y muy frecuentemente un contacto del responsable con el que podemos obtener nombre completo o incluso correo.

Podemos utilizar la herramienta `domaintools.com` y buscar a nombre de quién está la web marca.com. Sin embargo para dominios por ejemplo .es nos pide que vayamos a nic.es donde sí podemos buscar por un nombre que esté a cargo de una web.

No sólo existe el buscador de Google, por ejemplo existe Carrot2, el cual compartimenta la información, incluso a nivel visual. O shodan que busca dispositivos a partir de direcciones IP. También podemos registrarnos para intentar obtener más servicios y los haremos con un correo temporal generado por mailinator.com, pero vemos que no nos permite con este tipo de correos temporales. ¿Como podemos saltarnos esto? Usamos el propio shodan para obtener información. Primero obtenemos información con el comando `host mailinator.com` y nos da diferentes direcciones IP y varios correos. Uno de estos es mail.mailinator.com, si este correo lo introducimos en shodan vemos diferentes sitios que los están utilizando, el primero utiliza el dominio `lj1020-75.members.linode.com` el cual vamos a usar para registrarnos de tal forma que nuestro correo será mi-correo@lj1020-75.members.linode.com y vemos en mailinator que efectivamente podemos y nos llega el correo de confirmación. Una vez registrados podemos buscar direcciones IP para conocer los dispositivos que sirve un determinado dominio. Pero otro uso interesante de shodan es que podemos buscar qué dispositivos están utilizando escritorio remoto buscando `port:3389 country:es`. También podemos buscar por nombre o correo electrónico.

En google podemos buscar también por imágenes dándole botón derecho a una imagen de google y pinchando en buscar por imagen o bien buscando por imagen y adjuntando o subiendo una imagen nuestra.

También en pastebin podemos buscar números de teléfono de famosos con los que luego en páginas como ardilla.ai con el que podemos saber si ha sido portado (es decir, si se ha cambiado de número). Aun así se puede pedir a la operadora que lo dé de baja.

Con todas estas herramientas inevitablemente dejamos un rastro como nuestra IP con la cual podemos geolocalizarnos. Para evitarlo podemos usando una VPN una extensión de chrome como ultrasurf. 

### Tema 2.- Aprendiendo hacking con CTF - Parte 1

Dentro del mundo de los CTFs vamos a ver las diferentes disciplinas que tenemos:
- Criptografía
- Esteganografía
- Forense
- Redes
- Web
- Programming
- Reversing
- Exploiting
- OSINT
- Miscellaneous

Tipos de CTFs:
- Jeopardy: Una serie de retos de diferentes tipos (crypto, web, forense, etc.) que dan puntos cuando los resuelves según nivel de dificultad. Para ello hay que encontrar la FLAG (bandera). La resolución de unos retos libera otros. Gana el que más puntos tenga cuando se termine el tiempo de juego.
- Attack-Defense: Cada equipo tiene un servidor/red de equipos con vulnerabilidades que deben proteger. Tienes puntos de ataque y de defensa. Hay que conseguir acceso del equipo contrario.
- Mixted: Wargame, Hardware y otros.

Plataformas para montar nuestros propios CTF:
- Facebook CTF https://github.com/facebook/fbctf
- Mellivora CTF https://github.com/Nakiami/mellivora

Plataformas de entrenamiento:
- CTF Time https://ctftime.org/ Se van anunciando diferentes eventos donde hay CTF y Write Ups.
- Root Me https://www.root-me.org Sitio de entrenamiento con muchos retos de diferentes tipos y niveles.
- Hack Me https://hack.me/ Sitio donde cada uno puede colgar sus Apps Web vulnerables para fines educativos o de investigación.
- Hack The Box https://www.hackthebox.eu/ Sitio donde puedes hackear máquinas boot2root
- Atenea https://atenea.ccn-cert.cni.es/escuela/home



#### CTF - Criptografía

- Definición: Ciencia que se dedica a ocultar mensajes secretos. Cryptos -> Oculto + Logía -> Ciencia
- Criptografía: construcción de procedimientos criptográficos para cifrar información, de tal forma que lo escrito solamente sea legible para quien sepa descifrarlo.
- Criptoanálisis: ¿cómo obtener el mensaje original a partir de un criptograma? Hay que diferenciar entre cifrar y codificar.
- Codificar: No necesitamos una clave, es una manera diferente de representación. Ejemplo 10 = 2 en binario. 
    - Ejempos de codificación: ASCII, Binario, Hexadecimal, Base36, Base64, Morse...

- Reto Crypto: Decodificar el mensaje que se encuentra en https://pastebin.com/prRSPN5G. Como veremos es un mensaje que se encuentra codificado múltiples veces en base64. Para resolverlo lo ideal es crear un script que lo decodifique recursivamente. 

- Cifrado: Necesitamos hacer un criptoanálisis para descrifrar el mensaje.
- Hash: Resultado de un algoritmo matemático, el cual no es reversible. Los hashes (en función del algoritmo matemático), siempre tienen la misma longitud, y podemos identificar si una cadena es un hash o no en función de su chart set es decir, si hay un caracter que se escapa del conjunto de caracteres que utilizamos en formato hexadecimal entonces no es un hash. Los hashes no son reversibles es decir que a partir de un hash no podemos obtener la clave, no obstante hay mecanismos para crackearlo. Por ejemplo la web crackstation.net. Esto no significa que sea reversible sino que a partir de prueba y error en una base de datos muy grande podemos crackearlo.
- Ejemplo de algorimo de cifrado: Cifrado del César. En este algoritmo cada letra del diccionario se corresponde con la 3 siguiente (es decir, la A -> D, B -> E, etc. Esto se llama algoritmo de rotación +3).

- Reto Cifrado: Descifra el contenido de la cadena "emk{3Um4-juE4-Kntl} para ello se sugiere utilizar https://gchq.github.io/CyberChef. Tras probar con varios algoritmos y varias claves descubrimos que con el algoritmo vigenere y la clave ctf obtenemos el resultado que queremos.


- Por último solo recordar que no solo se pueden cifrar strings sino que se pueden cifrar archivos. Si tenemos en un archivo de texto un contenido cifrado y lo desciframos podemos obtener por ejemplo un mp4. Si a su vez este archivo lo abrimos con el comando strings podemos ver el contenido en string que sea reconocible. Y este texto a su vez puede estar cifrando la bandera (por ejemplo).


#### Esteganografía

- Definición: Steganos -> Dios Griego "cubierto" + Graphos -> Escritura
- Esteganografía: técnicas que ocultan mensajes u objetos dentro de otros, llamados portadores. Pretenden crear una comunicación encubierta.
- Watermarking: técnica de ocultación de información  (marcas de agua digitales) para identificación unívoca.

- Herramientas:
    - file: Identifica el tipo de fichero (lee la cabecera del fichero)
    - exiftool: Identifica el tipo de fichero (lee los metadatos del fichero)
    - strings: Obtiene cadenas en ficheros
    - ghex: Editor hexadecimal para buscar información.
    - binwalk:  Análisis de binarios, usar con --e para extracción de datos.
    - Openstego, DeepSound, StegExpose, Steghide - 

- Reto de Stego - https://c43s4rs.blogspot.com/2017/12/el-principio-de-los-c43s4rs.html - Aquí hay una imagen con fondo negro tal que si cambiamoms este negro por un gris descubrimos un mensaje oculto.

### Tema 2.- Aprendiendo hacking con CTF - Parte II - Hacking web

En esta charla se plantea un caso práctico de un formulario con un login formado por los campos usuarios y contraseña típicos. 

1. Si vemos el código fuente podemos ver que el usuario y contraseña se encuentran hardcodeados y al introducirlos nos da el flag de este pequeño CTF. 

2. En el código fuente podemos ver que se llama a la función `darFlag()`. Como sabemos podemos abrir la consola del navegador y hacer una llamada a la función que queremos. 

3. Cambiamos de caso (aunque la idea es la misma). Entramos a una página que nos pide una contraseña para acceder. Puesto que no la sabemos inspeccionamos el código fuente pero esta vez el código javascript se encuentra ofuscado. Para ello podemos acceder al depurador del navegador e inspeccionar el archivo (que aun así saldrá ofuscado) pero hay un botón para que lo formatee mejor. Al hacerlo vemos un listado de string que se usan en la web incluido el flag.

4. En los navegadores también disponemos de la pestaña red en la que podemos ver todas las peticiones. En el reto 3 vemos un mensaje en el que no somos administradores. En el código fuente no vemos js por ningún lado, pero si miramos la peticion get nos fijamos que en la cabecera se incluye un campo "admin: 0" que no es muy habitual. 

5. Si usamos la herramienta curl en la línea de comandos con el comando `curl <direccion_ip>` nos devuelve la web pero si le añadimos la opción -v nos muestra las cabeceras + el contenido. Si le añadimos la opción -X podemos aportar el método que utilizará la petición (-X GET/POST). Para este ejercicio nos basta con enviar o modificar una de las cabeceras con `curl -v -H "admin:1" <dir_ip>` vemos que el contenido que recibimos es distinto y se incluye el flag.

6. Proxy inverso. Cuando hacemos hacking web es necesario tener un proxy inverso, que podemos definir como un programa en nuestro ordenador que intercepta todas las peticiones que hace nuestro navegador, pararlas, evitarlas, etc. 

7. Por ejemplo podemos usar "BurpSuite". Para enlazarlo al navegador buscamos la pestaña proxy y lo configuramos. Una vez hecho en Burpsuite nos vamos a la pestaña proxy > HTTP y podemos ver todas las peticiones que ha hecho nuestro navegador y las respuestas. Un módulo interesante de esta herramienta es el Repeater. Podemos seleccionar una petición y con click derecho mandarla al Repeater donde podemos modificar de manera sencilla la petición y ver la respuesta de manera mucho más sencilla que desde curl.


### Tema 2.- Aprendiendo hacking con CTF - Parte III - Forense

- Tipos de retos en un CTF Forense:
    - Capturas de RAM : Fichero donde tengo extraído todo lo que hay en la memoria RAM.
    - Imagen de disco : Fichero donde tengo extraído todo lo que tengo en un disco duro.
    - Capturas de RAM + Imagen de disco

- En este apartado vamos a usar 2 herramientas:
    - FTK Imager - Es una herramienta que nos permite montar las imágenes de disco en modo lectura. https://accessdata.com/product-download
    - Volatility - Es una herramienta de análisis de capturas de RAM de los principales SO - https://www.volatilityfoundation.org/ , https://github.com/volatilityfoundation/volatility/wiki/Command-Reference

- Reto 1 - Nos han proporcionado la siguiente captura RAM para encontrar un mensaje que dicen que está oculto con el formato cft{FLAG}.
    Para eso primero obtenemos la versión del sistema operativo ya que las capturas de RAM difieren entre SO y versiones. Para ello introducimos el comando `volatility -f imagen imageninfo` en concreto para este caso `volatility -f reto1_taller.raw --profile=Win75P1x86 imageinfo`. En este caso el SO es un Windows x86. Seguidamente listamos el árbol de procesos con el comando `volatility -f imagen --profile=PERFIL pstree`, en este caso `volatility -f reto1_taller.raw --profile=Win75P1x86_23418 pstree`. Veremos una lista de procesos, nosotros queremos centrarnos en el proceso notepad y llevarnoslo (su contenido) a un archivo. Para ello tenemos el comando `volatility -f imagen --profile=PERFIL memdump -p PID -d DIRECTORIO_DUMPEO` en este caso `volatility -f reto1_taller.raw --profile=Win75P1x86 memdump -p 3112 -D .`. Esto nos genera un archivo .dmp que podemos abrir con el comando `strings FICHERO > strings.txt`, en este caso `strings 3112.dmp > strings_3112_8bits.txt`. Con esto hacemos un strings (8 bits por defecto) del proceso para intentar recuperar lo que tenía abierto el notepad. Sin embargo vemos que obtenemos como resultado una ruta a un archivo flag.txt pero no obtenemos el contenido de este archivo. Esto puede ser por dos motivos, el primero es que ese archivo no tenga contenido, o bien que la codificación del archivo no coincide con la por defecto de strings (8 bits o UTF-8). Para ver si es eso cambiamos la codificación con el comando `strings -e l FICHERO > strings_16bits.txt`, en concreto, `strings -e l 3112.dmp > strings_3112_16bits.txt`. En este caso obtendremos un archivo cuyo contenido está tanto en UNICODE como UTF-16. En esta ocasión si encontramos la flag ctf{H1dd3n_1nf0_16_b1ts}.


- Reto 2 - Averiguar la contraseña del usuario a partir de una captura de RAM.  
    Para eso repetimos los pasos `volatility -f MemoryDumpWH.raw imageinfo`, vemos que es un Windows y cogemos su profile. `volatility -f MemoryDumpWH.raw --profile=Win7SP1x86 pstree` para ver los procesos donde nos encontramos el lsass.exe que es proceso de seguridad de windows que realiza la autentificación del usuario. Es probable que ese proceso tenga los hashes de la contraseña del usuario. Cogemos este proceso y como en el caso anterior lo cargamos en memoria (con el comando `volatility -f imagen --profile=PERFIL memdump -p PID -d DIRECTORIO_DUMPEO`) y a continuación ejecutamos `volatility -f MemoryDumpWH.raw --profile=Win7SP1x86 hashdump` que cogerá el proceso y comprueba si tiene cargado en el proceso los hashes de las contraseña de los usuarios de Windows. Windows por defecto tiene 2 usuarios, Administrador e invitado. Separados por : tendremos los hashes, en concreto nos dan 2 hashes. Windows funciona con hashes NTLM que lo que hacen es separar la contraseña de 16 caracteres en dos partes de 8. Si nos fijamos vemos que el hash que hay hashes comunes entre usuarios, esto nos indica que esa parte de la cadena es una cadena vacía.  Vemos que la segunda parte del hash del usuario del que queremos saber su contraseña no esta vacía (porque es distinta al resto) lo cual nos indica que la longitud de la contraseña es de menos de 8 caracteres ya que las contraseñas Windows como máximo son de 16 caracteres. Por tanto nos cogemos el hash que tiene contenido y nos lo llevamos a un archivo con `echo <pass> > pass.txt`. El hash lo copiamos y nos lo llevamos a crackstation que comprueba si tiene el hash en su base de datos que efectivamente lo tiene y equivale a la palabra test.

- Reto 3 - Creemos que el usuario ha ejecutado alguna serie de comando para eliminar un fichero. Tu misión será averiguar el nombre del fichero eliminado.
    Windows por defecto no guarda el historial de comando que tu ejecutas pero sí se guarda si ese proceso está en la memoria RAM por medio del proceso cmd.exe. Si analizamos la captura de RAM vemos que está ese proceso (con `volatility -f MemoryDumpWH.raw --profile=Win7SP1x86 pstree`) y analizamos que comandos ha ejecutado con el comando `volatility -f MemoryDumpWH.raw --profile=Win7SP1x86 cmdscan` gracias al cual se nos muestra el historial de comandos y podemos ver que el fichero eliminado se llama `F1ch3r0_D3l3t33333.txt`.

- Reto 4 - Creemos que el usuario ha navegado por la Deep Web. Necesitamos averiguar la wiki de listado de .onion que ha visitado.
    Vemos en el árbol de procesos si se encuentra el navegador tor. Vemos que no lo encontramos en la captura de RAM. Pasamos a analizar la captura de disco con el software AccessData > File > Add .. item > Añadimos el fichero de imagen, y se nos habrá montado en modo lectura el disco. Navegando por la partición NFS de Windows buscamos la carpeta del navegador Tor, que por defecto se instala en el escritorio. El navegador Tor no guarda un historial de navegación, entonces cómo sabemos por dónde ha navegado el usuario? Navegamos por las carpetas del navegador Tor (que está basado en Firefox y tiene una estructura muy similar) hasta que encontramos archivos sqlite en concreto el favicon.sqlite, donde se almacenan los iconos de las webs por las que has navegado junto con sus urls. Este fichero nos lo exportamos a nuestro equipo y lo abrimos con el software sqlite browser (por ejemplo) y procedemos a ver si hay algún onion en los iconos y vemos que tenemos almacenada la url de un onion del cual obtenemos la flag de este reto.

- Reto 5 - Se cree que el usuario se ha estado comunicando mediante correo electrónico con un tercero pero ha intentado borrar pruebas. Nuestro objetivo es averiguar la información sensible que se ha estado enviando. 
    Analizando la captura de RAM y no vemos por ningún lado algún cliente de correo electrónico (thunderbird, office, etc). Procedemos a mirar en la imagen de disco si tiene instalado algún cliente de correo electrónico en Archivos de Programa y no encontramos nada. A lo mejor el usuario no lo tiene instalado en este momento pero sí lo ha tenido instalado en el pasado, ¿dónde podemos encontrarlo? se suele almacenar en la ruta Usuario > AppData > logs y nos encontramos con ThunderBird, accedemos a los Profiles > perfil por defecto de ThunderBird > Mail > Local Folders > messages.mbox donde nos encontramos el correo electrónico y nos interesa el cuerpo del correo, de donde obtenemos un codigo. Este código lo utilizamos en cyberchef donde desciframos el mensaje. Aparentemente al mensaje le han hecho una rotación, probamos con varios algoritmos de rotación y con el ROT47 obtenemos el flag del reto.

- Reto 6 - En el disco duro clonado nos encontramos restos de un famoso gestor de contraseñas. A lo mejor nos puede ser de utilidad. Tu misión será averiguar la contraseña de la base de datos. 
    En memoria RAM no tiene ningún gestor de contraseñas (se suele utilizar el keypass). Comprobamos en disco si lo tiene instalado y efectivamente lo tiene instalado. Vamos a buscar donde tiene almacenada la bd del gestor de contraseñas. Keypass por defecto la almacena en la carpeta Documents del usuario donde vemos que se encuentra el fichero passwords.kbdx. Exportamos el fichero y procedemos a sacar el hash de la contraseña. Antes de eso comprobamos con el comando `file passwords.kdbx` que se trata de una base de datos de contraseñas, una vez que sabemos esto vamos a ejecutar un programa que nos saca de la base de datos el hash de la contraseña, para ello ejecutamos `python2 keepass2john.py passwords.kdbx > outputfile.hash`. Si le hacemos un cat a ese archivo vemos que nos ha extraido con el formato `passwords:hash` el hash de la contraseña de la base de datos de keypass. Procedemos a quitarle la cadena passwords: para quedarnos solo con el hash y una vez tenemos el hash solo utilizamos `hashcat -m 13400 -a 0 -w 1 pass.hash rockyou.txt --force --show` para crackear el hash. Con el parámetro 13400 le indicamos que es el tipo de hash que utiliza keypass y con -a 0 -w 1 le indicamos parámetros de velocidad, por último le pasaremos un diccionario de palabras. Al hacerlo nos muestra al final del hash la contraseña. Con esta contraseña procedemos a abrir el fichero sqlite del keypass donde encontramos una contraseña almacenada, le indicamos que nos la copie al portapapeles y tendríamos la flag del reto.