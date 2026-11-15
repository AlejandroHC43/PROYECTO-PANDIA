
# VARIABLES
default rol_jugador = ""

# PERSONAJES
define RISE = Character("RISE", color="#8be9fd")
define a = Character("REID", color="#c8ffc8")
define b = Character("VICTOR", color="#c4e80f")
define c = Character("CHRISTINA", color="#0c83d9")
define d = Character("JEREMY", color="#bc4055")
define CM = Character("Control de misión", color="#bc4055")

# IMÁGENES
image FONDO2 = "images/FONDO ESCENA 2.jpeg"
image FONDO3 = "images/FONDO ESCENA 3.jpeg"
image CHRISTINA = "images/CHRISTINA.png"
image VICTOR = "images/VICTOR.png"
image JEREMY = "images/JEREMY.png"
image FondoAstronautas = "FONDO ASTRONAUTAS.jpeg"
image 1 = "1.png"
image 2 = "2.png"
image 3 = "3.png"
image 5 = "5 (2).JPG"
image R1 = "Reid 1.png"
image V1 = "Victor 1.png"
image C1 = "Christina 1.png"
image J1 = "Jeremy 1 (1).png"
image 6 = "6.png"
image 7 = "7.png"
image 8 = "8.png"
image 9 = "9.jpg"
image 10 = "10.png"
image 11 = "11.png"
image 12 = "12.png"
image 13 = "13.png"
image 14 = "14.png"
image 15 = "15.png"
image 16 = "16.png"
image 17 = "17.jpg"
image 18 = "18.png"
image 19 = "19.png"
image 20 = "20.png"
image 21 = "21 (1).png"
image 22 = "22.png"
image 23 = "23.png"
image 24 = "24.png"
image 25 = "25.png"
image 26 = "26.png"
image 27 = "27.png"
image 28 = "28.png"
image 29 = "29.png"
image 30 = "30.png"
image 31 = "31.png"
image 32 = "32.png"
image 33 = "33.png"
image 34 = "34.png"

# ESCENA 1
label start:
    $ renpy.music.set_volume(1.0, delay=0, channel="music")
    play music "audio/Pandia.mp3" loop fadein 2.0

    scene 1
    with fade

    RISE "Bienvenido, explorador. Me llamo RISE y seré tu asistente durante esta misión."

    scene 2

    RISE "Hoy no estamos ante un lanzamiento cualquiera. Cuatro astronautas están preparados para viajar alrededor de la Luna a bordo de la nave Orion."

    RISE "Pero llegar al espacio requiere mucho más que encender un cohete. Miles de sistemas, personas y procedimientos deben trabajar en perfecta coordinación."

    scene 3

    RISE "Tu función será apoyar al equipo de análisis de misión. Tendrás acceso a información meteorológica, indicadores de vuelo y comunicaciones de la tripulación."

    RISE "No estarás solo. Yo te ayudaré a interpretar los datos, pero las decisiones operativas reales corresponden a los especialistas y responsables de misión."

    scene 5

    menu:
        "¿Estás preparado?"

        "Sí, estoy listo para comenzar.":
            scene 3
            RISE "Excelente. Comencemos con los preparativos."

        "Necesito conocer primero los objetivos.":
            scene 3
            RISE "Nuestra misión consiste en comprobar que Orion y sus sistemas pueden transportar de manera segura a una tripulación alrededor de la Luna y de regreso a la Tierra."
            RISE "Comenzaremos con la preparación del lanzamiento y avanzaremos hasta alcanzar la órbita terrestre."

    RISE "Antes de adentrarnos de lleno en la misión, ¿qué rol deseas tener?"
    scene 5
    menu:
        "Elige tu especialidad:"

        "Ingeniero":
            $ rol_jugador = "Ingeniero"
            scene 3
            RISE "Experto en mecánica y sistemas. Capaz de reparar estructuras y resolver fallos críticos."

        "Piloto":
            $ rol_jugador = "Piloto"
            scene 3
            RISE "Maestro de los controles y los reflejos rápidos. Sobresale en navegación y control bajo presión."

        "Científico":
            $ rol_jugador = "Científico"
            scene 3
            RISE "Análisis, investigación y resolución de enigmas científicos y de telemetría."

    RISE "Configuración completada. ¡Que comience la misión!"

jump escena_2


# ESCENA 2
label escena_2:
    scene FondoAstronautas

    RISE "Antes de comenzar, quiero presentarte a quienes estarán a bordo."
    
    scene R1

    a "Soy Reid Wiseman, comandante de Artemis II. Nuestra prioridad es trabajar como equipo y asegurarnos de que cada procedimiento se cumpla correctamente."
    
    scene V1
    b "Victor Glover, piloto de Orion. Estaremos atentos a los sistemas de la nave y a las operaciones necesarias durante el vuelo."
    
    scene C1
    c "Christina Koch, especialista de misión. Esta prueba nos permitirá evaluar sistemas esenciales para los futuros viajes tripulados."
    
    scene J1
    d "Jeremy Hansen, especialista de misión. Esta misión representa la colaboración de personas y equipos de diferentes países para explorar más allá de la Tierra."
    
    scene 6
    RISE "¡Ahora sí! Ya conoces a la tripulación. Recuerda que una misión espacial es el resultado del trabajo de muchísimas personas, tanto dentro como fuera de la nave."

jump escena_3

# Escena 3. El primer desafío: condiciones meteorológicas
label escena_3:

    scene 7 

    RISE "Atención, explorador. Antes del lanzamiento necesitamos revisar las condiciones atmosféricas."

    RISE "Los vientos en altura pueden generar fuerzas adicionales sobre el cohete durante el ascenso. Por eso, los equipos de NASA recopilan información meteorológica y actualizan los parámetros de vuelo."

    scene 8

    RISE "Existe un procedimiento llamado DOLILU: Day-of-Launch I-Load Update."

    RISE "Este procedimiento permite actualizar información del software de vuelo del SLS para considerar las condiciones ambientales del día del lanzamiento."

    # Desafío 1: Evaluación meteorológica

    scene 9

    menu:
            "Debemos decidir qué hacer"

            "Continuar con los parámetros anteriores sin revisar los cambios.":
                scene 8
                RISE "Recuerda que las condiciones atmosféricas influyen en las cargas que experimenta el cohete durante el ascenso."
                RISE "No podemos ignorar esta información. Revisemos nuevamente el procedimiento."
                jump escena_4

            "Incorporar los datos meteorológicos, actualizar DOLILU y verificar la trayectoria.":
                scene 8
                RISE "¡Excelente trabajo! Los datos meteorológicos deben integrarse en la actualización y los equipos deben verificar los resultados antes de continuar."
                RISE "Has completado tu primera tarea."
                jump escena_4

            "Ignorar los vientos porque el cohete ya está preparado.":
                scene 8
                RISE "Recuerda que las condiciones atmosféricas influyen en las cargas que experimenta el cohete durante el ascenso."
                RISE "No podemos ignorar esta información. Revisemos nuevamente el procedimiento."
                jump escena_4

# Escena 4. La verificación final
label escena_4:

    scene 3

    RISE "Los parámetros actualizados deben comprobarse antes de su utilización."

    RISE "Los equipos de NASA realizan verificaciones independientes de la trayectoria y de las cargas estructurales mediante simulaciones por computadora."

    RISE "La actualización se carha aproximadamente una hora antes del lanzamiento y debe realizarse a más tardar 40 minutos antes."

    #Desafío 2: Validación de datos

    scene 5

    menu:
        "Tenemos tres opciones para continuar. ¿Cuál debemos seguir?"

        "Cargar los datos y continuar sin realizar verificaciones adicionales.": 
         scene 3
         RISE "¡No tan rápido! Antes de continuar, recuerda que los datos de una misión deben ser confiables y corresponder a las condiciones actuales. No es recomendable avanzar sin comporbar la información ni utilizar parámetros de otras misiones sin validarlos." 
        #jump escena_5

        "Verificar los resultados de trayectoria y cargas, confirmar la correcta.":
         scene 3
         RISE "¡Correcto! La información debe verificarse antes de continuar. En una misión espacial, la comunicación entre los equipos es tan importante como los propios datos."

        "Utilizar los parámetros de un lanzamiento anterior.":
         scene 3
         RISE "No"
        #jump escena_5

    RISE "La preparación continúa. Vamos a comunicarnos con la tripulación"

#Escena 5. Comunicación con Orión
label escena_5:

    scene 10

    "Artemis II, comprobación de comunicaciones."

    scene 11

    a "Aquí Artemis II. Comunicaciones recibidas correctamente."

    scene 12

    b "Los sistemas de la nave están siendo revisados."

    scene 13

    c "La tripulación continúa con las comprobaciones previas al lanzamiento."

    scene 14

    d "Estamos preparados para comenzar esta aventura."

    scene 15

    RISE "Explorador, hemos llegado a uno de los momentos más importantes. La secuencia de lanzamiento está próxima a comenzar."

    scene 16

    RISE "Recuerda: durante el ascenso, el equipo de Tierra continuará supervisando el comportamiento del vehículo. Tu función será interpretar la información de nuestra simulación."

#Escena 6. La cuenta regresiva.
label escena_6:

    scene 17
    with fade

    RISE "Fecha: 1 de abril de 2026."

    RISE "Ubicación: Centro Espacial Kennedy, Florida."

    RISE "Vehículo: Space Launch System."

    RISE "Nave espacial: Orion."

    RISE "Tripulación: cuatro astronautas."

    RISE "¡Despegue!"

#Escena 7. El ascenso y la separación de propulsores
label escena_7:

    scene 18

    RISE "El SLS continúa su ascenso. Durante esta fase, el vehículo debe superar las fuerzas aerodinámicas y mantener su trayectoria."

    RISE "Aproximadamente dos minutos después del despegue, los propulsores sólidos completan su función y se sparan del vehículo."

    scene 19

    b "La nave continúa su trayectoria."

    scene 20

    a "Seguimos atentos a los indicadores."

    scene 18

    RISE "La separación de los propulsores es una de las etapas importantes del ascenso. Debemos continuar supervisando la información de vuelo."

#Escena 9. Llegada al espacio
label scena_9:

    scene 21

    RISE "¡Lo conseguimos! Orion ha alcanzado el espacio."

    RISE "Despues de llegar al espacio, la nave despliega sus paneles solares, que permiten recibir energía del sol."

    scene 22

    c "Comienza una nueva etapa. Necesitamos continuar con la comprovación de los sistemas de la nave."

    scene 23

    b "Prepararemos las siguientes operaciones de vuelo."

    scene 24

    d "La tierra se ve increible desde aquí-"

    scene 25

    a "Seguimos trabaajando. Nuestro viaje apenas comienza."

#Escena 10. Cierre del capitulo
label scene_10:
   
   scene 27
   
   RISE "¡Felicidades, explorador! Has completado la primera etapa de nuestra aventura."

   RISE "Hoy aprendiste que un lanzamiento espacial no depende únicamente del cohete. También requiere análisis meteorológico, simulaciones, comunicación y coordinación entre cientos de especialidades."
   
   RISE "Pero todavía tenemos un largo camino por recorrer."

   RISE "Nuestra siguiente misión comprobar los sistemas de Orion mientras permanecen en órbita terrestre."

#Capitulo 02 - ORBITA TERRESTRE
#Escena 11. Despertar en órbita
    
scene 26
default estado_soporte = "pendiente."
default estado_energia = "pendiente."
default estado_navegacion = "pendiente."

screen interfaz_objetivos():
        frame:
            xalign 0.03
            yalign 0.04
            padding (20, 15)
            background Solid("#0b132bCC")  

            vbox:
                spacing 8

                text "{b}{color=#8be9fd}OBJETIVO ACTUAL: COMPROBACIÓN DE SISTEMAS{/color}{/b}" size 20

                # Mostrar estados leyendo variables en tiempo real
                text "- Soporte vital: [estado_soporte]" size 18
                text "- Energía: [estado_energia]" size 18
                text "- Navegación: [estado_navegacion]" size 18
  
"UBICACIÓN: ORION · ÓRBITA TERRESTRE · DÍA DE VUELO 1"
 #poner sonido del viaje
RISE "Buenos días, explorador. ¿Puedes ver eso?"
RISE "Después de abandonar la Tierra, nos encontramos orbitando nuestro planeta."
RISE "Puede parecer que lo más difícil ya terminó, pero todavía tenemos mucho trabajo por delante."
RISE "Antes de continuar nuestro viaje hacia la Luna, necesitamos comprobar que todos los sistemas de Orion funcionan correctamente."
scene 28
a "Es un buen momento para revisar la nave. Tenemos que asegurarnos de que todo esté preparado para las siguientes operaciones."
scene 29
b "Durante esta fase estaremos trabajando con los sistemas de la nave y evaluando sus capacidades."
scene 30
c "El soporte vital, la energía y la navegación son fundamentales. Necesitamos entender cómo responde cada sistema."
scene 31
d "Y no olvidemos que estamos haciendo esto para preparar futuras misiones de exploración."
scene 27
RISE "Explorador, tenemos tres tareas principales. Vamos a comenzar con el sistema que nos permite mantener un ambiente habitable dentro de Orion."

# Escena 12 Sistema de soporte vital
label escena_12:
scene 13
c "El soporte vital es uno de los sistemas más importantes de la nave."
c "No se trata solamente de suministrar oxígeno. También debemos mantener condiciones adecuadas de presión, temperatura y calidad del aire."
scene 15
RISE "Exactamente. El sistema de soporte vital y control ambiental ayuda a mantener condiciones habitables para la tripulación."
RISE "Entre los parámetros que debemos observar están la concentración de oxígeno, el dióxido de carbono, la presión de cabina, la temperatura y la humedad."
scene 11
a "Necesitamos revisar los indicadores y asegurarnos de que no existan lecturas fuera de los límites establecidos."

# Desafío 1 — Una lectura fuera de lo esperado (ANOMALÍA SIMULADA)
scene 15
RISE "Explorador, tenemos una situación hipotética de entrenamiento."
RISE "El sensor A y el sensor B están mostrando lecturas diferentes relacionadas con el dióxido de carbono de la cabina."
RISE "No sabemos todavía si existe un problema real en el sistema o si estamos ante una discrepancia de medición."
    
scene 13
c "Antes de tomar cualquier decisión, necesitamos revisar la información disponible."
        
menu:
    "¿Qué debemos hacer?"

    "Desactivar inmediatamente todo el sistema de soporte vital.":
     scene 15
     RISE "Cuidado, explorador. No debemos desactivar sistemas esenciales ni ignorar una posible discrepancia."
     RISE "Primero necesitamos validar la información y seguir los procedimientos establecidos."
    #jump escena_3
        
    "Comparar las lecturas, revisar los indicadores relacionados y comunicar la discrepancia al equipo responsable.":
    # Actualiza automáticamente la interfaz de objetivos en tiempo real
     $ estado_soporte = "{color=#47ea98}completado.{/color}"
     scene 15
     RISE "¡Muy bien! No debemos asumir que una lectura diferente significa necesariamente que el sistema ha fallado."
     RISE "Comparar los datos y consultar los indicadores relacionados permite que el equipo responsable determine si existe una anomalía real."
     scene 13
     c "En una nave espacial, interpretar correctamente la información es tan importante como disponer de buenos sistemas."

    "Ignorar la lectura diferente porque uno de los sensores parece normal.":
     scene 15
     RISE "Cuidado, explorador. No debemos ignorar una posible discrepancia en los sensores."
     RISE "Primero necesitamos validar la información y seguir los procedimientos establecidos."

    # Transición final de la tarea
    "SOPORTE VITAL REVISADO"
    
RISE "Primera tarea completada. Continuemos con el suministro de energía."

#Escena 13. Sistema de energía eléctrica
label escena_13:

    scene 32
    b "Estos paneles solares son fundamentales para el funcionamiento de la nave."
    scene 33
    RISE "Los paneles solares permiten convertir la energía del Sol en energía eléctrica para los sistemas de Orion."
    RISE "La nave también cuenta con almacenamiento de energía para mantener el suministro cuando sea necesario."
    scene 34
    a "Necesitamos comprobar que la generación y distribución de energía sean adecuadas."
    scene 33
    RISE "Vamos a revisar los indicadores de generación, almacenamiento y consumo eléctrico."

#Escena 4. Sistemas de navegación
label scene_4:

    scene 32

    b "Para viajar alrededor de la Luna necesitamos conocer nuestra posición y orientación con precición."
   
    scene 33
    RISE "Los sistemas de navegación permiten determinar dónde se encuentra Orion y cómo esta orientada respecto a su trayectoria."

    RISE "También ayudan a proporcionar información necesaria para las maniobras de la nave."
    scene 36
    d "No basta con saber que estamos en el espacio. Necesitamos conocer exactamente cómo nos esta moviendo."
    scene 33
    RISE "Correcto. Vamos a revisar la información de navegación."

    RISE "Tenemos información de navegación procedente de diferentes fuentes. Necesitamos comprobar que los datos sean coherentes."

    #Desafío 3: Discrepancia de navegación 

    RISE "Atención, explorador. En nuestro escenario de entrenamiento, dos estimaciones de orientación presentan una discrepancia."
    
    RISE "Todavía no sabemos si existe una desviación real o si debemos revisar la información de los instrumentos."

    scene 32
    b "Antes de realizar cualquier corrección necesitamos verificar los datos."
    scene 36
    menu: 
        "¿Que debemos hacer?"

        "Modificar inmediatamente la orientacion de Orion.":
         scene 33
         RISE "¡Cuidado, explorador! Una diferencia entre las lecturas no significa necesariamente que Orion esté fuera de su trayectoria. Realizar una corrección sin comprobar los datos o desactivar instrumentos podría eliminar informacion importante para evaluar la situación."
         #jump escena_5

        "Comparar las fuentes de navegación, revisar la calidad de los datos y discrepancia al equipo responsable.":
         scene 33
         RISE "¡Correcto! Antes de realizar cualquier maniobra necesitamos validar la información."
         scene 32
         b "La precisión es fundamental. Cada maniobra requiere información confiable."
         #jump escena_5

        "Desactivar los instrumentos que presentan diferencias.":
         scene 33
         RISE "¡Cuidado, explorador! Una diferencia entre las lecturas no significa necesariamente que Orion esté fuera de su trayectoria. Realizar una corrección sin comprobar los datos o desactivar instrumentos podría eliminar información importante para evaluar la situación."
         #jump escena_5
    scene 33
    RISE "¡Excelente trabajo! Hemos completado las tres tareas princpales."

#Escena 15. Comunicación con Tierra
label escena_15:

    scene 37
    CM "Artemis II, aquí Houston. Solicitamos actualización del estado de los sistemas."
    scene 38
    a "Houston, aquí Artemis II. Hemos completado las comprobaciones previstas para esta etapa."
    scene 39
    b "Los datos de navegación han sido revisados."
    scene 40
    c "También hemos realizado la evaluación de los indicadores ambientales."
    scene 41
    d "La tripulación continúa con las actividades de misión."
    RISE "Explorador, hemos conseguido algo importante. Conocemos mejor el comportamiento de los sistemas de Orion."

#Escena 16. Resumen de la misión
label escena_16:
    scene 27
    RISE "Antes de continuar, vamos a revisar lo que aprendimos."
    "Soporte vital: mantiene condiciones habitables."
    "Energía: permite alimentar los sistemas de la nave."
    "Navegación: permite determinar posición, orientación y trayectoria."
    RISE "Recuerda algo, explorador: una anomalía no siempre significa que un sistema haya fallado. Por eso debemos comparar la información, identificar posibles inconsistencias y seguir los procedimientos adecuados."
    scene 30
    c "Cada comprobación nos ayuda a comprender mejor cómo funciona Orion."
    scene 28
    a "El trabajo todavía no termina."
    scene 29
    b "Pronto tendremos que prepararnos para nuestra siguiente maniobra."
    scene 31
    d "La Luna está cada vez más cerca."
    scene 27
    RISE "¡Capítulo completado!"

# Capítulo 03 — TRANSLUNAR INYECCIÓN
# Escena 1. El siguiente destino: la Luna

screen panel_navegacion():
    frame:
        xalign 0.75
        yalign 0.15
        padding (25, 20)
        background Solid("#1c2541CC")  

        vbox:
            spacing 10

            text "{b}{color=#ffde59}PANEL TL-INJECTION · NAVEGACIÓN{/color}{/b}" size 18
            
            # Datos simulados de telemetría espacial
            text "• Vector Orbital: Estable (CI-88)" size 15
            text "• Delta-V Requerido: 3.15 km/s" size 15
            text "• Margen de Inclinación: 0.04°" size 15
            text "• Estado TLI: [estado_navegacion]" size 15

label escena_3_1:
    show screen interfaz_objetivos
    
    RISE "¡Bienvenido de nuevo, explorador! Hemos completado nuestras primeras comprobaciones en órbita terrestre."
    RISE "Pero nuestra misión está lejos de terminar. Ha llegado el momento de prepararnos para viajar hacia la Luna."
    scene 28
    a "Antes de abandonar nuestra órbita actual, necesitamos asegurarnos de que la nave esté preparada para la siguiente maniobra."
    scene 29
    b "Realizaremos una maniobra conocida como inyección translunar, o TLI por sus siglas en inglés."
    scene 27
    RISE "La inyección translunar consiste en encender el sistema de propulsión para modificar nuestra trayectoria y dirigirnos hacia la Luna."
    scene 31
    d "Lo impresionante es que no se trata simplemente de apuntar hacia la Luna y acelerar. Necesitamos una trayectoria cuidadosamente calculada."
    scene 27
    RISE "Y tú nos ayudarás a comprender cómo verificarla. ¡Vamos a comenzar!"

    
    show screen panel_navegacion
    scene 42
    menu:
        "Verificar vector orbital y parámetros de Delta-V":
            $ estado_navegacion = "{color=#47ea98}completado.{/color}"
            
            hide screen panel_navegacion
            scene 27
            RISE "¡Parámetros confirmados! La trayectoria hacia la Luna es óptima."

#Escena 2. Validación de la trayectoria
label escena_3_2:

    b "Antes de ejecutar una maniobra necesitamos contar con información confiable sobre la trayectoria y el estado de la nave."
    RISE "En esta simulación revisaremos tres indicadores: posición estimada, orientación y parámetros de maniobra."

    RISE "Todos deben ser coherentes con la solución de navegación aprobada."

    RISE "Explorador, la consola indica que los parámetros de la maniobra aún necesitan ser validación."

    #Desafío 1 - preparación de la TLI
    
    menu: 
        "¿Que debemos hacer?"

        "Ejecutar la maniobra sin verificar los parametros.":
         RISE "¡Cuidado, explorador! No debemos realizar una maniobra sin verificar primero los parámetros de navegación. Cada decisión debe basarse en información confiable y en el plan de vuelo aprobado. ¡Inténtalo nuevamente!"

        "Comparar los parámetros con la solución aprobada y confirmar las verificaciones.":
         RISE "¡Excelente! Antes de una maniobra es fundamental confirmar que los datos de navegación y los parametros de ejecución sean coherentes con el plan aprobado."

        "Modificar la orientación de Orion sin consultar los datos.":
         RISE "¡Cuidado, explorador! No debemos realizar una maniobra sin verificar primero los parámetros de navegación. Cada decisión debe basarse en información confiable y en el plan de vuelo aprobado. ¡Inténtalo nuevamente!"

#Escena 3. Una desviación inesperada
label escena_3_3:
    show screen panel_navegacion
    
    RISE "Atención, explorador. Nuestro simulador ha detectado una discrepancia."
    RISE "La trayectoria estimada presenta una pequeña diferencia respecto a la trayectoria planificada."
    b "Antes de realizar una corrección necesitamos determinar si se trata de una desviación real o de una discrepancia en la información de la navegación"
    a "Debemos evaluar los datos y mantener comunicación con el equipo de Tierra."
    RISE "Explorador, necesitamos tu análisis."

    #Desafío 2 - desviación simulada
    
    menu: 
        "¿Qué decisión debemos tomar?"

        "Encender inmediatamente los propulsores para corregir la trayectoria.":
         RISE "¡Cuidado, explorador! No debemos modificar la trayectoria sin verificar primero la información, ni ignorar una posible desviación. Es fundamental analizar los datos y comunicar cualquier discrepancia al equipo de Tierra antes de continuar. ¡Inténtalo nuevamente!"

        "Ignorar la discrepancia y continuar con el encendido.":
         RISE "¡Cuidado, explorador! No debemos modificar la trayectoria sin verificar primero la información, ni ignorar una posible desviación. Es fundamental analizar los datos y comunicar cualquier discrepancia al equipo de Tierra antes de continuar. ¡Inténtalo nuevamente!"

        "Comparar las mediciones, comunicar la discrepancia y esperar la evaluación autorizada.":
         RISE "«¡Excelente trabajo, explorador! Antes de realizar cualquier corrección debemos verificar la información, comparar las mediciones y comunicar la discrepancia al equipo de Tierra. En una misión espacial, cada decisión debe estar respaldada por datos confiables y una evaluación autorizada."

    RISE "La comparación ha permitido identificar una inconsistencia en uno de los datos de nuestro ejercicio."
    RISE "El equipo de simulación ha validado nuevamente la solución de navegación. No es necesaria una corrección adicional en este escenario ficticio."
    b "Excelente. Ahora contamos con información verificada para continuar con la preparación."
    a "Sigamos con el procedimiento."

# Escena 4. La inyección translunar
label escena_3_4:

RISE "¡Excelente trabajo, explorador! Los parámetros de navegación han sido verificados."

RISE "¡Estamos listos para continuar con una de las maniobras más importantes de nuestra misión."

CM "Artemis II, Houston. Los equipos han completado la evaluación. Autorización de la maniobra confirmada."

a "Recibido, Houston. Preparándonos para la inyección traslunar."

b "La orientación está verificada. Preparados para el incendio"

RISE "Exploraodr, durante esta maniobra el motor principal del módulo de servicio europeo de Orion aumentará nuestra velocidad para abandonar la órbita terrestre."

RISE "¡Comenza la inyección traslunar!"

c "Continuamos monitoreando el comportamiento de los sistemas."

d "Cada segundo de esta maniobra nos acerca más a nuestro destino."

CM "Artemis II, Houston. Maniobra completada. Los datos de navegación confirman la trayectoria de salida."

# Escena 5. Rumbo a la Luna
label escena_3_5:

RISE "Explorador, mira por la ventana."

RISE "La Tierra comienza a quedar atrás. Hemos abandonado nuestra órbita y nuestro siguiente destino es la Luna."

d "Es increíble pensar en todo lo que hemos recorrido para llegar hasta aquí."

c "Y todavía nos esperan muchas oportunidades para aprender sobre nuestra nave y el espacio que nos rodea."

a "Hemos completado una etapa fundamental. Ahora debemos concentrarnos en lo que viene."

RISE "¡Felicidades, explorador! Gracias a tus decisiones hemos completado las verificaciones de navegación de nuestro simulador."

RISE "Hoy aprendiste que viajar a la Luna requiere cálculos precisos, información confiable y una gran coordinación entre los astronautas y el equipo de Tierra."

RISE "Pero nuestra aventura todavía no termina."

RISE "Nuestro siguiente desafío será explorar uno de los lugares más fascinantes del escpacio: el lado oculto de la Luna."

RISE "Explorador, hemos llegado al momento más esperado de la misión."

RISE "Frente a nosotros se encuentra el Space Launch System, listo para llevar a la tripulación de Artemis II al espacio."

a "Artemis II lista para el lanzamiento."

CM "Inicio de secuencia terminal."

b "Todos los sistemas verificados."

RISE "Explorador, comienza la cuenta regresiva."

"T-3"
"T-2"
"T-1"

RISE "¡Ignición!"

"El SLS enciende sus motores y una enorme columna de humo y fuego envuelve la plataforma."

RISE "¡Despegue confirmado!"

d "Estamos en camino."

RISE "El SLS comienza su ascenso, superando la gravedad terrestre."

c "Todos atentos a los indicadores."

a "Seguimos con el procedimiento."

RISE "La mision ha comenzado. Próxima etapa: ascenso y separación de propulsores."

RISE "¡Explorador, estamos de regreso! Después de nuestro viaje alrededor de la Luna, nos aproxima nuevamente a la Tierra."

a "estamos llegando a una de las fases más importantes de nuestra misión: el regreso atmosférico."

b " Necesitamos comprobar nuestra trayectoria y asegurarnos de que la nave esté preparada para entrar en la atmosfera."

RISE "Durante esta etapa, supervisaremos la velocidad, la orientación u la trayectoria."

#Desafio 1. Verificación de reingreso 

RISE "Explorador, nuestra consola de entretenimiento muestra una discrepancia entre dos estimaciones de orientación."

menu:
    "ignorar la diferencia y continuar.":
     RISE "No."

    "Comparar los datos, comprobar la información de navegación y comunicar la discrepancia al euqipo responsable.":
     RISE "¡Correcto! Antes del reingreso debemos contar con información de navegación confiable. Una maniobra incorrecta podria comprometer la seguridad de la nave."

    "Modificar inmediatamente la orientación sin verificar los instrumentos.":
     RISE "No."

c "Y todabía nos esperan muchas oportunidades para aprender sobre nuestra nave y el espacio que nos rodea."
b "Durante el trayecto continuaremos supervisando nuestra trayectoria. Si es necesario, los equipos podrán planificar maniobras de corrección."
a "Hemos completado una etapa fundamental. Ahora debemos concentrarnos en lo que viene."

RISE "¡Felicidades explorador! Gracias a tus desiciones hemos completado las verificaciones de navegación de nuestro simulador."
RISE "Hoy aprendiste que viajar a la luna requiere cálculos precisos, información confiable y una gras coordinación entre los astronautas y el equipo de tierra."
RISE "Pero nuestra aventura todabía no termina."

RISE "Nuestro siguiente desafío será explorar uno delos lugares más fascinantes del espacio: el lado oculto de la luna."

#Etapa 2. Reingreso atmosférico y desaceleración.

RISE "¡Comienza el reingreso! Orion viaja a una velocidad extraordinaria y debe reducirla para regresar de forma segura."

c "El escudo térmico protege la cápsula de las temperaturas extremas que se generan durante el reingreso."
d "La nave experimentará una desaceleración considerable. Todos debemos permanecer asegurados."

RISE "Explorador, oberva los indicadores. La velocidad está disminuyendo y debemos reconocer las etapas que permitirán completar el descenso."

#Desafio 2. Secuencia de aceleración
label escena_2_2:
    RISE "¿Cuál es el orden correcto de las principales fases de descenso?"

    menu:  
        "Paracaidas, reingreso atmosferico, amerizaje.":
         RISE "Recuerda que primero la cápsula debe atravesar la atmósfera, despues reducir su velocidad y finalmente abrir sus paracaidas antes de tocar el océano."

        "Reingreso atmosférico, desaceleración aerodinámica, despliegue de paracaídas.":
         RISE "La atmosfera contribuye primero a reducir la velocidad. Despues, el sistema de paracaidas permite completar el descenso hacia el océano."

        "Reingreso atmosférico, amerizaje, despliegue de paracaídas.":
         RISE "Recuerda que primero la cápsula debe atravesar la atmósfera, despues reducir su velocidad y finalmente abrir sus paracaidas antes de tocar el océano."

RISE "¡Paracaídas desplegados! La cápsula continúa reduciendo su velocidad."
b "Seguimos descendiendo hacia la zona de amerizaje."
a "Preparados para el contacto con el agua."

#Etapa 3. Amerizaje y regreso a casa ¿
  
RISE "¡Explorador, estamos a punto de completar nuestra misión!."

RISE "¡Amerizaje confirmado! Orion ha regresado a la Tierra."

"Orion, Huston. Iniciamos la coordinación de las operaciones de recuperación."

 #Desafio 3. Confirmación del amerizaje.
label escena3__1:
 RISE "La cápsula se encuentra en el océano. Antes de dar por terminada nuestra simulación, necesitamos verificar su estado."
 RISE "¿Qué información debemos confirmar?"
menu: 

        "Únicamente que la cápsula haya tocado el agua.":
         RISE "Recuerda, el amerizaje no termina la misión; primero debemos verificar que todo esté seguro."

        "El estado de la tripulación, las condiciones de la cápsula y la comunicación con los equipos de recuperación.":
         RISE "¡Exelenete! El regreso no termina con el contacto con el océano. Los equipos deben confirmar el estado de la tripulación y coordinar su recuperación."

        "Que los motores continúen encendidos.":
         RISE "Recuerda, el amerizaje no termina la misión; primero debemos verificar que todo esté seguro."

a "Huston, aquí Artemis II. Hemos regresado."
b "Ha sido un viaje extraordinario."
c "Todo lo que aprendimos ayudará a preparar las proximas misiones."
d "Nuestro viaje termina aquí, pero la exploración continúa."

RISE "¡Lo logramos, explorador! Hemos completado nuestro viaje alrededor de la luna y regresado a casa."
RISE "Desde el alnzamiento hasta el amerizaje, cada etapa nos enseñó que la exploración espacial requiere precición, conocimiento y trabajo en equipo."
RISE "Y recuerda: este es solo el comienzo de una nueva era de exploración."

"MISIÓN COMPLETADA."











return