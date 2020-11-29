# Modulo 2.- Comunicaciones inalámbricas

## Tema 1. Radio definida por software

¿Qué es una radio definida por software (SDR)? Es una radio en la cual alguna o varias de las funciones de la capa física son definidas mediante software: filtros, mezcladores, amplificadores, etc. Esto implica ventajas a la hora de ahorrar costes, configuración, versatilidad, etc.

En las SDR tenemos 3 etapas: 
- Muestreo, donde recibimos las señales analógicas
    - Se trata de tomar muestras de una forma rápida y precisa. La cantidad es la frecuencia de muestreo.
    - La frecuencia mínima de muestreo debe ser el doble del ancho de manda a muestrear (Nyquist-Shanonn)
    - Si se quisiera muestrear de 0-10 MHz se necesitaría un mínimo de 60 millones de muestras: 10MHz = 10 millones de ciclos x 2
    - Se supone que la máxima frecuencia a grabar es de 20000 Hz por lo que son 40000 Hz según Nyquist. Por eso el estándar es 44.1 KHz, suficiente para sonido de calidad (este estándar se usa en los CDs por ejemplo).
- Cuantificación donde digitalizamos estas señales
- Decodificación donde procesamos estas señales para que sigan unos estándares 

Orígenes de la tecnología SDR:
- En 1991 gracias a la agencia DARPA se creó un programa llamado SPEAKeasy donde se tenía como objetivo integrar este tipo de radio en el entorno militar. 
- Posteriormente en 1992 Joseph Mitola publicó en la IEEE un artículo llamado "Software Radio: Survey, Critical Analysis and Future Directions".
- En estos años las SDR tenían un hardware caro y complejo de usar y tenían anchos de banda muy limitados (150KHz, donde en la actualidad un low-cost serían 2MHz).
- Después de estos años, en los finales de los años 90 principios de los 2000 se empezó a usar por parte de las empresas y radioaficionados gracias al modelo "Flex Radio SDR-1000".
- A partir de 2011 se abarató el precio con los SDR low-cost. 

A la hora de tener nuestros primeros pasos en el mundo de las SDR debemos pensar en qué queremos hacer o para qué queremos utilizar las SDR:
- Recepción de señales en general
- Emisión de señales
- Recepción de una determinada banda
- Uso profesional

Podemos ver los distintos tipos de radios SDR en https://en.wikipedia.org/wiki/List_of_software-defined_radios y algunos ejemplos concretos de SDR son:
- SDRPlay RSP
- Airspy
- USRP B200/B210
- Para HF (onda corta) tenemos el conjunto Afredi + Chirio SDR Mini-Whip antena activa o el AirSpy HF (para recibir señales).
- El más recomendable para un principiante es el RTL-SDR que viene un usb + antena. 

Para utilizar un SDR se recomienda instalar SDR Sharp Software, para ello seguir los siguientes pasos:
- Tener instalado NET 4.6 y VISUAL C++ Runtime
- Bajar "sdrsharp.zip" de www.airspy.com
- Ejecutar "install-rtlsdr.bat"
- Ejecutar "zadig.exe" 
- Seleccionar Bulk-In, Interface (Interface 0), RTL2832UHIDIR o RTL2832U
- Pulsar en "Replace Driver"
- Aceptar advertencia Windows
- Configurar:
    - Source - RTL-SDR (USB)
    - Sample-Rate - 2.4 MSPS
    - RF Gain - 37.2 dB
- Para realizar la decodificación de ciertos modos deberemos recurrir a software específico como DSD+, Telive, MULTPSK, Sorcerer, etc.
- Para pasar el audio desde nuestro receptor SDR al software deberemos proporcionar algún sistema de audio-pipping como Free Virtual Cable. En algunos casos podría ser suficiente con usar nuestro Mixer y que el software adquiera el sonido directamente de nuestra tarjeta. 

## Tema 2. Amenazas no convencionales / Introducción Reversing

Normalmente cuando intentamos defender nuestras conexiones tendemos a centrarnos en las tecnologías IP, bluetooth, Wifi y solemos descuidar las radio-frecuencias. Por eso en este tema veremos la importancia de protegerlas siguiendo el siguiente esquema:

1. Smartcities
2. El coche hiperconectado
3. Infraestructuras críticas
4. Comunicaciones embarcadas
5. Sistemas GNSS
6. Satélites: ¿pueden ser objetivo de los cibercriminales?
7. Comunicaciones móviles (GSM)
8. Las comunicaciones en la lucha contra los "malos"

### Riesgos de una ciudad hiperconectada

La seguridad siempre se ha aplicado a sistemas TCP/IP, dejando de lado sistemas inalámbricos que no sean Wifi y/o Bluetooth, peroe hoy en día, con unos conocimientos básicos y algo de lectura en Internet, se pueden llevar a cabo ataques muy variados contra las comunicaciones radio.

¿Qué encontraríamos si nos ponemos a escuchar a nuestra ciudad? Se podrían producir los siguientes ataques:
- Ataques a la infraestructura física: Un atacante podría robar el dispositivo y realizar un ataque físico sobre el. Disponiendo del dispositivo, de tiempo y de las herramientas adecuadas un posible atacante podría tratar de leer las claves de comunicación de dicho dispositivo mediante las interfaces de debugging del dispositivo.
- También podría ocurrir, que si las "keys" no están almacenadas en un lugar seguro se puedan leer desde algún medio de almacenamiento.
- Construcciones de GW maliciosos: En algunas redes de comunicaciones los GWs pueden no requerir autenticación. Por esta razón un atacante podría suplantar la identidad de un GW existente y actuar en su nombre, permitiendo la recogida de los mensajes. Por otro lado, un GW malicioso podría enviar mensajes de confirmación de recepción cuando realmente el mensaje no ha llegado a su destino. 

Por ejemplo, los contadores de agua y luz realizan un conteo del consumo junto a un identificador del cliente y lo envían de manera telemática. Podríamos, por medio de una RDS con capacidad de enviar señales, enviar datos modificados sobre nuestro consumo, incapacitar el contador para que no pueda enviar señales o realizar una investigación sobre el consumo de una persona externa para saber cuando está en casa y demás aspectos sobre su vida cotidiana. Normalmente estos contadores envían la información a un dispositivo físico que puede estar situado en farolas, semáforos u otros sitios, los cuales pueden ser atacados físicamente.

En Octubre del 2016 ya ocurrió en Barcelona. Un grupo de ciberdelincuentes consiguieron controlar los semáforos de la ciudad. El incidente se pudo llevar a cabo porque los semáforos llevan incorporado wifi para poder enviar información y capturas de las cámaras mediante éste sistema inalámbrico. En una ciudad hiperconectada, existen también otros sistemas de información como el de los parkings que funcionan de forma inalámbrica. 

En la ciudad de Barcelona se instaló un sistema de alumbrado inteligente. La columna de alumbrado público, no sólo se encarga de proporcionar alumbrado en vía pública, sino que actúa también como soporte de elementos de comunicación e información (TIC) alojando en su interior:
- puntos de cobertura Wifi
- diversidad de sensores
- comunicación con el "back-end" mediante M2M (2G/3G)
En este caso también se podría utilizar estas comunicaciones telemáticas para ser capaces de alterar los valores que captan/transmiten.

### El coche hiperconectado

La incorporación de nuevos sistemas de comunicaciones inalámbricos han conseguido que dispongamos de coches mejor conectados, pero como contrapartida ha convertido a estos vehículos en un blanco para los ciberdelincuentes.

Al aumentar estos sistemas electrónicos (Jamming, Firmware OTA, USB SD ODB-II, Wifi, 3G/4G, Radio RDS / TMC, GPS, Sensores inalámbricos (TPMS), V2V - DSRC), también aumenta la superficie de exposición y por tanto también la probabilidad de que un ataque pueda llegar a materializarse. La incorporación de nuevos protocolos inalámbricos sumado al abaratamiento de los equipos SDR convierte a nuestro vehículo en un objetivo casi al alcance de cualquiera. 

Por ejemplo con el TMC el coche puede detectar atascos en la carretera y que el algoritmo del coche que calcula la ruta óptima cambie su ruta. De igual manera por medio del Wifi se podría atacar al coche y atacar a su centralita. Por medio del GPS igual. Incluso sabemos que estos coches se pueden actualizar de manera inalámbrica, donde un actor malicioso podría interceptar esta actualización e inyectar código malicioso tanto en el coche como en la centralita. Se pueden simular obstáculos que hagan que el coche frene de forma brusca hiriendo a los pasajeros. 

El TPMS es uno de esos elementos de seguridad activa que, siendo sencillos, nos ahorran problemas, ya que nos recuerdan la importancia de la presión del neumático. En sí, la función del sistema es esta: avisar al conductor de una pérdida de presión de inflado en los neumáticos.

El sistema TPMS monta un sensor colocado en cada rueda que mide la presión de inflado y transmite el dato a una centralita mediante comuniccaciones inalámbricas.

Estos aparatos tienen un ID único de 32 bits registrado en la centralita electrónica y normalmente transmiten los datos de forma inalámbrica en 433 Mhz con una modulación ASK.

Los posibles vectores de ataque pueden ser:
- Seguimiento de vehículos: Se podría configurar una red de sensores que se encargasen de realizar el seguimiento de uno o varios vehículos basándose en el ID.
- Suplantación de identidad: Se podrían enviar mensajes falsos que lograsen iluminar el tablero de mando de un vehículo consiguiendo que el conductor se detenga, o como se refleja en un casao documentado llegar a bloquear una centralita ECU al recibir mensajes TPMS erróneos.
- Desencadenar eventos. Se podrían desencadenar eventos desde la apertura de un garaje, hasta otros con fines maliciosos como la detonación de un artefacto explosivo ante la detección de un ID de TPMS.

### Comunicaciones inalámbricas en infraestructuras críticas

Un ejemplo de comunicaciones inalámbricas en infraestructuras críticas son las comunicaciones GSM-R en trenes de alta velocidad. 

El GSM-R (de GSM-Railway) es un sistema de comunicación digital inalámbrico desarrollado específicamente para la comunicación ferroviaria. Provee a los trenes de radiotelefonía y línea de datos. Según Adif significa: Group Special Mobile for Railways.
- Funciona a modo de baliza enviando continuamente la posición del tren al centro de control.
- Sirve también como sistema de radiotelefonía (llamadas) y envío de mensajes de Texto.
- En España GSM-R se utiliza en las líneas de alta velocidad.
- En España, su uso depende de la ubicación. No todas las "features" están implantadas en todas las líneas.
- GSM-R utiliza las frecuencias 876-880 Mhz (Uplink) y 921-925 Mhz (downlink) dentro de la banda de GSM-900. 
- Los servicios concretos que conseguimos por medio de su uso son:
    - Comunicación entre el controlador y el maquinista
    - Control de trenes
    - Control remoto
    - Comunicaciones ferroviarias auxiliares
    - Comunicaciones con estaciones
    - Comunicaciones de larga distancia
    - Numeración funcional (igual que GSM)
    - Llamadas de alta prioridad
    - Etc.

Este sistema se deriva del sistema GSM el cual ya se ha demostrado que tiene fallos de seguridad a partir de los cuales un actor malicioso podría atacar estas comunicaciones enviando información falsa, haciendo DoS, etc. 

Otro ejemplo de infraestructura crítica es las redes de transporte eléctrico. 

La tecnología TETRA es cada vez más usada en aplicaciones de telecontrol y tele medida. 
- Podemos encontrar básicamente dos implementaciones:
    - TETRA Packet DATA
    - TETRA SDS
- TETRA es una red de baja velocidad (poco ancho de banda).
- Existen protocolos optimizados para TETRA = DNP3
- Existen módems y routers preparados para DNP3.

Este estándar se suele usar para comunicaciones con walkies pero también se usan con radio-modems que envían y reciben telemetrías entre la información captada por PLCs y la estación base de TETRA, la cual lleva el mantenimiento y gestión del sistema. 

Un ejemplo mucho más cercano de ataque a estos sistemas de comunicación en la ciudad de Dallas con las sirenas de emergencia, las cuales comenzaron a sonar causando pánico cuando no había ningún peligro. Las sirenas utilizadas para advertir de peligros a los ciudadanos pueden ser activadas mediante tonos DTMF (tonos que suenan cuando pulsamos números en un teléfono) vía radio. Decodificar los tonos DTMF no es complicado hoy en día, incluso subiendo una muestra de audio a http://dialabc.com/sound/detect/ es posible decodificar estos tonos para posteriormente ser reproducidos por un equipo de radio o software. 

### Comunicaciones embarcadas

En la actualidad y cada vez más, las ayudas de los aparatos electrónicos en el puente suponen una fuente de información que nos aporta seguridad y conocimientos durante la travesía. 

Al igual que en otros entornos, la automatización de los procesos es cada vez mayor. Un barco puede llegar a tener:
- Sistemas Anticolisiones (AIS)
- Radar
- GPS
- Sistemas de monitorización (motor, viento, etc)
- Piloto automático
- Domótica interior
- Etc.

Pero por si esto no fuese suficiente, hoy en día los dispositivos no son modernos si no disponen de comunicaciones inalámbricas, por eso los fabricantes incorporan las comunicaciones Wireless a sus dispositivos.

Estos dispositivos no fueron fabricados bajo la premisa de la seguridad y nos encontramos con:
- Wifi con WPA-PSK
- Claves por defecto
- El radar actúa como AP y, por tanto, puedes concectarte como cliente.

Warning: La conexión canBUS que utilizan los barcos se convierten posteriormente por medio de una interfaz en conexión Wifi a la que podemos conectar nuestros dispositivos. No obstante, un atacante podría acceder a los sistemas de tu embarcación mediante una conexión Wifi consiguiendo en el peor de los casos manipular el piloto automático del barco.

No es ninguna novedad ver que cada vez conectamos más cosas a Internet. El IoT ya no es una palabra de moda, hoy en día casi todo está conectado de una forma u otra a Internet.

Un grupo de investigadores (Shodan) descubrió un dispositivo embarcado que estaba conectado a Internet y que además proporcionaba información sobre su posición.

Con estos datos crearon el proyecto "Ship Tracker" en el que, en tiempo real, muestran información de esos dispositivos (sistemas vSAT) sobre un mapa. 

El investigador francés @xorz publicaba en Twitter que con una simple búsqueda en Shodan era posible encontrar estos dispositivos con una configuración por defecto (la gran mayoría disponían de credenciales por defecto).

Estos dispositivos, están compuestos por una o varias antenas vSAT, una unidad encargada de realizar las funciones de un router para dotar de conectividad a internet a la embarcación. 

No sólo se consiguió localizar cientos de estos dispositivos en Internet mediante Shodan, sino que algunos investigadores consiguieron incluso acceder mediante TELNET o SSH a los dispositivos. Viendo que era posible, subir un nuevo firmware y/o cambiar la configuración de estos dispositivos.

### Sistemas GNSS (GPS | GLONASS | BEIDOU | QZSS | NAVIC)

La seguridad del sistema GPS ha sido reconocida como una de las amenazas de seguridad más seria de los últimos años, debido al uso intensivo y grado de dependencia, que hoy en día, se hace de este sistema de posicionamiento. En especial el uso que hacen de estas señales las aeronaves no tripuladas (UAV), y muchas otras aplicaciones de uso civil: seguimiento de flotas, logística, conducción autónoma, localización de personas, etc.

Estos sistemas cada vez reciben más ataques puesto que nuestra dependencia de ellos cada vez es mayor. Pasemos a analizar algunos de los ataques más frecuentes que reciben estos sistemas:
- La interferencia (jamming), en este caso el actor malicioso trata de degradar el servicio generando una señal que interfiera e imposibilite al receptor acceder a la señal legítima. Este tipo de ataque suele ser de baja tecnología y de fácil alcance (sobre todo en tiendas online chinas) aún siendo ilegal su venta y uso. Normalmente estos dispositivos se suelen usar en barcos o en camiones para conseguir no ser localizados por GPS. No obstante su uso por ejemplo cerca de aeropuertos pueden inhibir los sistemas de GPS de los aviones.
- Spoofing, cuando hablamos de spoofing nos referimos a la existencia de una señal generada por un actor malicioso que intenta sustituir la señal legítima tratando de engañar a nuestro receptor, para que este use esta señal. 
    - Un ejemplo de Spoofing puede ser engañar a nuestro teléfono para cambiar nuestra localización GPS para conseguir un pokemon en Pokemon Go. 
    - No obstante otro ejemplo sucedió el 22-06-2017 cuando apareció una alerta de seguridad indicando que en las proximidades de la costa de Novorossiysk (en el Mar Negro) un buque informó al Centro de Navegación de la Guardia Costera de EEUU que sus equipos de navegación eran incapaces de detectar la señal GPS. Además se pudo comprobar que más de 20 buques que se encontraban navegando por la misma zona tuvieron la misma incidencia con la señal de GPS. Tras varias investigaciones, expertos han podido concluir que ha sido un ataque de Spoofing a la señal de GPS.
    - En otra ocasión, en el 2018, y coincidiendo con el ejercicio TRIDENT JUNCTURE 2018 de la OTAN, medios como la BBC se hacían eco indicando que casi con total certeza Rusia podría haber estado alterando las señales GPS. Otros medios, sin embargo, van más allá apuntando directamente a Rusia como origen de estas interferencias, e indicando que este tipo de disrupciones en la señal, han sido deliberadamente ejecutadas para poner a prueba sus sistemas de Guerra Electrónica. Con implicaciones directas más allá de lo militar ya que pudieron verse afectados aviones, barcos y otros sistemas civiles. 

La mayoría de los escenarios que hemos observado tienen como objetivo la alteración del posicionamiento, dificultando obviamente la navegación.

No obstante, los sistemas GNSS no sólo prestan servicio de posicionamiento. Otras de sus funciones es proporcionar una fuente precisa y extraordinariamente estable de tiempo.

Un ejemplo de infraestructura crítica que tiene una alta dependencia de esta fuente de tiempo es la red eléctrica, pero no la única, también podemos citar las redes de distribución de TDT.

Las redes de TDT disponen de arquitecturas de distribución SFN (Single Frecuency Network), donde todos y cada uno de los transmisores y reemisores que componen la red SFN hacen uso de la misma frecuencia de emisión para transmitir un determinado paquete de canales de televisión.

Por el tipo de modulación empleada en las redes SFN, se requiere una cuidada sincronización de tiempo en todos los centros emisores y reemisores ya que, de no existir esa sincronización la emisión podría verse afectada y hay muchas posibilidades de que los centros entre sí se interfieran. 

La Bolsa de Londres también ha estado sujeta en repetidas ocasiones a interrupciones en el servicio GPS, esto afecta al sellado de tiempo en las transacciones económicas.

Para que podamos observar el impacto que puede suponer la degradación o interferencia del sistema GPS con respecto a las operaciones bancarias, en 2007 debido a un ejercicio de la marina de EEUU donde se experimentaba con la pérdida de la señal GPS, los ciudadanos del puerto de San Diego no pudieron retirar efectivo de los cajeros automáticos por la afectación al sellado de tiempo de las operaciones bancarias. 

Volviendo al tema de los vehículos autónomos, imaginemos que estamos circulando por la carretera con un Testa Model 3 con el Autopilot activado. Como el manejo lo lleva el propio coche, tu puedes despreocuparte y relajarte un poco -pero siempre con las manos al volante y atendiendo-. Pero tu tranquilidad se interrumpe cuando, de repente, el vehículo desacelera por si mismo. 

### Satélites, ¿pueden ser objetivo de cibercriminales?

Los satélites hoy en día juegan un papel clave a nivel mundial, no sólo porque proporcionan servicios de posicionamiento y tiempo, sino que también nos permiten transmitir información a todos los rincones del planeta.

Sirven de plataforma de observación de la tierra, además de ser fundamentales para el soporte a misiones tanto civiles como militares. 

Muchos expertos en asuntos internacionales apuntan a que los satélites se están convirtiendo en un punto frágil dentro de la cadena de seguridad mundial. En el documento "Ciberseguridad de los Activos Estratégicos de la OTAN" advierten del riesgo potencial al que nos enfrentamos. No conviene olvidar que, a pesar de que se encuentran a miles de kilómetros, las redes de satélites pueden ser vulnerables. 

¿Son posibles los ataques a satélites? Veamos algunos ejemplos:
- La madrugada del 27 de abril del 1986 tuvo lugar uno de los ataques más conocidos contra un sistema satélite. El "Captain Midnight" (Jonh R.MacDougall) descontento con la tarifa que se tenía que pagar para acceder a los servicios codificados de HBO decidió "secuestrar" la señal de esta cadena. 
- En 1998 varios atacantes tomaron el control del satélite germano-estadounidense ROSAT, consiguiendo modificar su configuración y alterando la posición de sus placas solares. Como consecuencia de esta modificación, el satélite giró sin control y su cámara de alta resolución quedó expuesta directamente a la radiación solar (quedando inutilizada). Investigaciones posteriores de la NASA determinaron que ciertos atacantes rusos habían burlado la seguridad del Goddard Space Flight Center y causado el incidente. 

Aunque la seguridad de los sistemas ha mejorado mucho en los últimos años, hoy en día, todo es susceptible de ser atacado. Y no debemos dejar de prestar atención a las comunicaciones inalámbricas.

### Comunicaciones móviles, un vector de ataque más para los cibercriminales

Actualmente existen alertas masivas en algunos países que avisan por medio de un pop-up a todos los dispositivos móviles de un determinado país de una determinada alerta. Se han dado casos en los que se envían mensajes a una gran parte de la población con falsos mensajes de avisos de bomba (lo cual causa un gran pánico) o mensajes de estafa o phising. 

### La importancia de las comunicaciones en la lucha contra los "malos"

Hoy en día los sistemas de comunicación inalámbrica son fundamentales para la coordinación y la comunicación. Por eso, la interceptación de las señales, puede ser un punto fundamental en la generación de inteligencia, sobre todo, en la lucha contra el terrorismo.

