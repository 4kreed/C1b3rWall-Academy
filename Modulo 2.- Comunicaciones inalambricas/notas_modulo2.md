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

## Tema 3.- Introducción Wi-Fi 6

En esta sección analizaremos los siguientes aspectos:
- Repasar la historia de la tecnología de red inalámbrica, comúnmente conocida como Wi-Fi.
- Analizar los avances que introduce la última actualización del estándar, conocida como Wi-Fi 6.
- Explorar de qué manera desplegar esta tecnología de manera eficiente, desde la perspectiva de un entorno de uso corporativo (no residencial). 

### ¿Qué es el Wi-Fi y cómo hemos llegado a la situación actual?

A día de hoy casi cualquier persona sabe de manera básica que es el Wi-Fi. Esta importancia del Wi-Fi (sobre todo frente a otras tecnología inalámbricas) en nuestras vidas se debe a los siguientes factores: 
- Crecimiento de Internet / Movilidad
- Estándares abiertos
- No dependemos de terceros para tener servicio (no es el caso de una línea de teléfono por ejemplo que necesitamos una asociación con una compañía de teléfono).
- No hay que pagar licencias (como si hay que pagar para usar radio-frecuencias).
- User-friendly

Veamos algunas características del Wi-Fi:
- Es una tecnología inalámbrica de red local (WLAN), que hace uso de bandas de radiofrecuencia no-licenciada (ISM).
- Nace en 1997, pero su uso real inicia en 1999.
- Se basa en contienda (CSMA/CA)
- Propone, originalmente, 2 formas de conexión de los usuarios. 

¿Qué es CSMA/CA?
- Es un sistema de comunicación en la que un usuario puede transmitir la información sin interferencias (colisiones). Es decir, el usuario sólo puede transmitir cuando lo pueda hacer sin interferencias.
- En este caso sería el espacio de radiofrecuencia, que se usará cuando nadie más lo esté utilizando.

¿Qué forma de conexión se utiliza en 802.11?
Existen dos formas de comunicación:
- La primera denominada ad hoc, en la que la comunicación se realiza entre iguales (peers) pero uno de los dispositivos toma el rol de "master" y "organiza" la comunicación entre los dispositivos en red. Un ejemplo de este tipo de comunicación es la llevada a cabo cuando usamos Bluetooth, donde un dispositivo se conecta con otro igual.
- La segunda es la comunicación basada en infraestructura. En esta comunicación sí tengo un elemento central al que se le denomina como Punto de Acceso (Access-Point, AP) y que actúa de "master" gestionando la comunicación en este entorno inalámbrico y que además sirve de unión entre los elementos inalámbricos y los que están conectados por medio de una red cableada.
- Esta segunda forma es la utilizada en el estándar 802.11

Otros conceptos básicos:
- Banda de frecuencia y canales
    - Actualmente se definen dos bandas de frecuencia, una la de 2.4 GHz y otra la de 5GHz. Estas bandas se dividen a su vez en lo que se conoce como canales que es donde tiene lugar la comunicación. 
    - Dentro de la banda de 2.4GHz en Europa se definen 13 canales donde todos ellos menos los canales 1,6 y 11 están superpuestos unos con otros. En EEUU por ejemplo solo definen 11 canales. 
    - Dentro de la banda de 5GHz se definen muchos más canales, por eso siempre será preferible usar esta sobre la otra, sin embargo, no todos los dispositivos (sobre todo los más antiguos) son capaces de operar con esta banda. Dentro de esta banda en función de la frecuencia podemos configurar las comunicaciones para que halla más o menos canales. Por ejemplo a 20 MHz podemos establecer 8 canales mientras que a 160 MHz sólo podemos establecer 1 canal.
- Método de modulación y acceso
    - La modulación consiste en la transformación de un contenido digital (un archivo) a una onda. Algunos tipos de modulación son BPSK, QPSK o xx-QAM.
    - Por otro lado el método de acceso determina cómo debemos estructurar nuestros paquetes y cómo enviamos estos a otro destinatario. Algunos métodos de acceso son DSSS, OFDM y OFDMA.  
    - Estos mecanismos se adaptan al entorno para favorecer el ancho de banda o el alcance de la señal.
- Antenas
    - Pueden ser omnidireccionales o directivas en función del arco que cubre.
    - Pueden ser discretas (una única antena) o un arreglo de varios elementos (MIMO) que se usa para soportar mayor variedad de dispositivos. 

¿Qué significa Wi-Fi?
- Primero veamos quién apodó este término. En concreto la entidad llamada "Wi-Fi Alliance" antaño llamada WECA (Wireless Ethernet Compatibility Alliance) la cual a diferencia del IEEE no es una entidad que desarrolla el estándar sino es una agrupación de empresas que se reune y la promociona. 
- Esta alianza lo primero que hizo fue ponerle el nombre Wi-Fi teniendo en cuenta que era una tecnología que se pensó para uso residencial (en los hogares). En este ambiente y en ese momento estaba muy arraigado el término Hi-Fi (High Fidelity) de los dispositivos de sonido. A partir del cual surgió el nombre Wi-Fi que no es unión de Wireless Fidelity sino que se pensó para que se asociara al concepto de Hi-Fi que tan famoso era en ese momento. Por tanto esta alianza lo que hace no es definir el estándar sino promover el estándar por medio de certificados que dan a los dispositivos que cumplen unas características mínimas necesarias para que se pueda comunicar por medio del estándar 802.11. 

A lo largo de los años el Wi-Fi ha tenido varias versiones:
- 11b / 1999 
- 11a / 1999 - salió a la vez que el anterior pero se aplicó años después. Incluía la posibilidad de usar la banda 5GHz (la 11b solo podía usar la banda 2.4GHz)
- 11g / 2003 - en la que hubo un aumento sustancial de velocidad
- 11n / 2009 / Wi-Fi 4 - se despliega muchísimo esta tecnología y se introducen conceptos como MIMO
- 11ac / 2014 / Wi-Fi 5 - actual

En las últimas versiones la alianza decidió renombrar estas versiones y seguir la tendencia del 3G, 4G, 5G, etc (aunque el Wi-Fi siempre ha ido una versión por delante de la telefonía móvil, es decir con el 5G tenemos Wi-Fi 6) con el objetivo de que fuesen más amigable. 


### ¿Qué es el Wi-Fi 6 y en qué nos puede beneficiar?

Esta claro que el Wi-Fi es muy popular pero ¿qué problemas tiene? 

Como hemos comentado el Wi-Fi se originó para un uso residencial donde en ese momento no había tablets, a los móviles le quedaban todavía algunos años y apenas había portátiles. Esto junto a su condición de contingencia (recordemos, se transmite cuando no haya interferencias), hace que conforme aumenta la cantidad de dispositivos conectados la calidad de servicio disminuye drásticamente.  

Además el Wi-Fi es "gratis" y cualquiera lo puede usar (al contrario de las bandas de radiofrecuencia). Eso hace que ya no es sólo que en mi casa haya muchos dispositivos sino que el hecho de que mi vecino utilice Wi-Fi me afecta también a mi. 

De esta manera nace el Wi-Fi 6 para satisfacer las necesidades del Wi-Fi del momento (a las que se le sumarían la necesidad de utilizar IoT, vídeo a alta resolución o incluso VR). 

Y para ello el Wi-Fi 6 no sólo se conforma con mejorar la velocidad de transmisión sino también aumentar el número de conexiones (IoT) y la latencia (es decir la velocidad a la que puedo enviar paquetes, video).

Si bajamos niveles de abstracción esto se consigue por medio de las siguientes tecnologías:
- Mayor ancho de banda - 1024-QAM, 8x8 MU-MIMO
- Mayor concurrencia - UL/DL OFDMA, UL/DL MU-MIMO
- Menos latencia - OFDMA Spatial Reuse
- Menos consumo energético - TWT 20MHz Only

Por ejemplo, hasta Wi-Fi 5 usabamos OFDM en donde en un intervalo de tiempo determinado todos los recursos se utilizan para transmitir a un único dispositivo. Con Wi-Fi 6 usamos OFDMA donde en un intervalo de tiempo determinado podemos transmitir a varios dispositivos, no simultáneamente sino primero a uno y luego a otro. Con lo cual se hace un reparto de tiempo y frecuencia entre los usuarios.

Otro cambio significativo fue la llegada del MU-MIMO (Multiuser - Multiple Input / Multiple Output), que se introdujo en el Wi-Fi 5. La idea es que si aumentamos el número de antenas podremos ofrecer servicio a mayor cantidad de usuarios, pues asignamos una antena a cada usuario. No obstante en Wi-Fi 5 esto sólo sucedía para la bajada (pero no la subida) de datos. Con Wi-Fi 6 no sólo se duplica la cantidad de antenas disponibles sino que se aporta también la posibilidad de que el servicio sea bidireccional, es decir, varios usuarios pueden enviar y recibir datos a la vez.

Por medio de pruebas se ha demostrado que el OFDMA que utiliza el Wi-Fi 6 es realmente ventajoso pero sólo cuando llegamos a un número de usuarios mayor de 10, mientras que si son menos usuarios obtenemos un rendimiento peor que con las generaciones anteriores. ¿Entonces si en mi casa tengo pocos dispositivos va a funcionar peor? No, la configuración se adaptará al número de dispositivos para utilizar unos métodos de modulación y acceso u otros.


### Mejores prácticas de diseño para redes Wi-Fi

Cuando nosotros diseñamos una red cableada sabemos perfectamente cómo y por dónde se van a comunicar los dispositivos (después de todo, nosotros establecemos el cableado), sin embargo, en las comunicaciones inalámbricas no es así. 

Por mucho que el Wi-Fi 6 alivien algunos problemas, las interferencias no desaparecen (sobre todo cuando aumentamos tanto el número de dispositivos). Además las barreras arquitectónicas continúan siendo un reto para la cobertura (paredes gruesas, etc.). Y conforme se va incorporando el Wi-Fi a entornos industriales las compañías deben comprometerse por contrato al cumplimiento de una serie de requisitos de calidad mínimos o disposiciones legales. 

Como hemos dicho los problemas del Wi-Fi se acentúan en una red Enterprise, donde se distinguen los siguientes elementos:
- Controlador: Es un elemento que orquesta los parámetros y políticas de un conjunto de AP, de manera que se facilita el ajuste RF, la autenticación de los usuarios o el roaming entre los AP. Puede ser físico o software, estar ubicado en local, en un sitio central o en la nube. 
- Gestión de Infraestructura: Es una suite de software que permite tener una visión global del estado de la red Wi-Fi, permitiendo la visualización de alarmas, topología, reportes, configuración, etc. Suele desplegarse en una ubicación central o en la nube.
- Gestión de Usuarios: Es una suite de software que permite tener, establecer y centralizar políticas relativas a la autenticación y autorización de los dispositivos de los clientes que se conectan a la red. Suele desplegarse en una ubicación central o en la nube. 

Factores de un buen diseño:
- El espacio físico: dónde se pueden instalar los AP y dónde estarán los usuarios de la red, es el primer elemento a controlar. Considerar que es necesario proporcionar conectividad y electricidad al AP. La seguridad de los instaladores también debe ser tomada en cuenta.
- Nivel de señal recibida (RSSI): es la "fuerza" de la señal recibida y que determinará la velocidad de conexión. Es importante saber las aplicaciones que se utilizarán y la distancia a la que estarán de los dispositivos.
- Nivel de ruido (SNR): es la medida de la "limpieza" del medio, simplificando, las interferencias que pueden generarse y afecten la comunicación entre AP y un dispositivo. Es importante saber las aplicaciones que se utilizarán y la densidad de dispositivos en servicio. 

Otras consideraciones a tener en cuenta en el diseño:
- Herramientas. A la hora de considerar el diseño podemos disponer de herramientas de análisis y optimización, destinadas a conocer la experiencia del usuario y no sólo el estado de la red. 
- Seguridad. Al igual que otros sistemas de comunicación, el Wi-Fi ha ido adaptando sus capacidades de seguridad a medida que la tecnología y las aplicaciones han evolucionado y surgen nuevas amenazas. La mejora más reciente es la incorporación de WPA3, que define los mecanismos de negociación de claves y cifrado entre la infraestructura y los dispositivos. El nivel de seguridad de una red Wi-Fi en 2020 es similar al de una conexión cableada. No obstante sí que debemos aplicar una serie de medidas de cara a la mejora de la seguridad:
    - Separar la comunicación de los distintos grupos de usuarios (corporativos, invitados, etc) por SSID, VLAN, etc. Cada grupo con sus políticas de seguridad particulares.
    - Utilizar mecanismos de autorización basados en perfil de usuario individual (como 802.1x o Personal PSK)
    - Migrar a mecanismos de cifrado mejorados, como WPA3, lo antes posible.
    - Activar mecanismos de monitorización activos en el dominio RF.
    - La seguridad debe ser general a toda la red y usuarios, en todo caso añadir políticas adicionales al usuario de acceso inalámbrico, no tratarlo de manera aislada. 

### Preguntas frecuentes

Si en una red hay dispositivos Wi-Fi 6 y dispositivos de generaciones anteriores, ¿todo el sistema red funcionará con los protocolos antiguos?

La negociación de la comunicación se realiza con cada dispositivo individualmente. Esta claro que el usuario del Wi-Fi 5 no se va a poder beneficiar de las ventajas del mismo.

¿Qué es mejor Wi-Fi 6 o 5G?

Aunque comparten algunos aspectos no comparten en teoría los mismos casos de uso sino que son complementarias.

¿Wi-Fi 7?

Se prevée que para 2023 tengamos este nuevo estándar, donde tendremos mayor ancho de banda y se espera que todas las aplicaciones se puedan integrar con el Wi-Fi de manera masiva.













