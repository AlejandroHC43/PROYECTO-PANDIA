
# VARIABLES
default rol_jugador = ""

# PERSONAJES
define RISE = Character("RISE", color="#8be9fd")
define a = Character("REID", color="#c8ffc8")
define b = Character("VICTOR", color="#c4e80f")
define c = Character("CHRISTINA", color="#0c83d9")
define d = Character("JEREMY", color="#bc4055")

# IMÁGENES
image FONDO1 = "images/FONDO ESCENA 1.jpeg"
image FONDO2 = "images/FONDO ESCENA 2.jpeg"
image FONDO3 = "images/FONDO ESCENA 3.jpeg"
image Rise = "images/RISE.png"
image CHRISTINA = "images/CHRISTINA.png"
image REID = "images/REID WISEMAN.png"
image VICTOR = "images/VICTOR.png"
image JEREMY = "images/JEREMY.png"
image FondoAstronautas = "FONDO ASTRONAUTAS.jpeg"

# ESCENA 1
label start:

    scene FONDO1
    with fade

    show Rise

    RISE "Bienvenido, explorador. Me llamo RISE y seré tu asistente durante esta misión."

    RISE "Hoy no estamos ante un lanzamiento cualquiera. Cuatro astronautas están preparados para viajar alrededor de la Luna a bordo de la nave Orion."

    RISE "Pero llegar al espacio requiere mucho más que encender un cohete. Miles de sistemas, personas y procedimientos deben trabajar en perfecta coordinación."

    RISE "Tu función será apoyar al equipo de análisis de misión. Tendrás acceso a información meteorológica, indicadores de vuelo y comunicaciones de la tripulación."

    RISE "No estarás solo. Yo te ayudaré a interpretar los datos, pero las decisiones operativas reales corresponden a los especialistas y responsables de misión."

    menu:
        "¿Estás preparado?"

        "Sí, estoy listo para comenzar.":
            RISE "Excelente. Comencemos con los preparativos."

        "Necesito conocer primero los objetivos.":
            RISE "Nuestra misión consiste en comprobar que Orion y sus sistemas pueden transportar de manera segura a una tripulación alrededor de la Luna y de regreso a la Tierra."
            RISE "Comenzaremos con la preparación del lanzamiento y avanzaremos hasta alcanzar la órbita terrestre."

    RISE "Antes de adentrarnos de lleno en la misión, ¿qué rol deseas tener?"

    menu:
        "Elige tu especialidad:"

        "Ingeniero":
            $ rol_jugador = "Ingeniero"
            RISE "Experto en mecánica y sistemas. Capaz de reparar estructuras y resolver fallos críticos."

        "Piloto":
            $ rol_jugador = "Piloto"
            RISE "Maestro de los controles y los reflejos rápidos. Sobresale en navegación y control bajo presión."

        "Científico":
            $ rol_jugador = "Científico"
            RISE "Análisis, investigación y resolución de enigmas científicos y de telemetría."

    RISE "Configuración completada. ¡Que comience la misión!"

jump escena_2


# ESCENA 2
label escena_2:
    scene FondoAstronautas

    RISE "Antes de comenzar, quiero presentarte a quienes estarán a bordo."
    
    scene FONDO2

    show REID
    a "Soy Reid Wiseman, comandante de Artemis II. Nuestra prioridad es trabajar como equipo y asegurarnos de que cada procedimiento se cumpla correctamente."
    hide REID
    show VICTOR
    b "Victor Glover, piloto de Orion. Estaremos atentos a los sistemas de la nave y a las operaciones necesarias durante el vuelo."
    hide VICTOR
    show CHRISTINA
    c "Christina Koch, especialista de misión. Esta prueba nos permitirá evaluar sistemas esenciales para los futuros viajes tripulados."
    hide CHRISTINA
    show JEREMY
    d "Jeremy Hansen, especialista de misión. Esta misión representa la colaboración de personas y equipos de diferentes países para explorar más allá de la Tierra."
    hide JEREMY
    show Rise
    RISE "¡Ahora sí! Ya conoces a la tripulación. Recuerda que una misión espacial es el resultado del trabajo de muchísimas personas, tanto dentro como fuera de la nave."

jump escena_3

# Escena 3. El primer desafío: condiciones meteorológicas
label escena_3:

    scene FONDO3

    RISE "Atención, explorador. Antes del lanzamiento necesitamos revisar las condiciones atmosféricas."

    RISE "Los vientos en altura pueden generar fuerzas adicionales sobre el cohete durante el ascenso. Por eso, los equipos de NASA recopilan información meteorológica y actualizan los parámetros de vuelo."

    RISE "Existe un procedimiento llamado DOLILU: Day-of-Launch I-Load Update."

    RISE "Este procedimiento permite actualizar información del software de vuelo del SLS para considerar las condiciones ambientales del día del lanzamiento."

    # Desafío 1: Evaluación meteorológica
    menu:
        "Debemos decidir qué hacer:"

        "Continuar con los parámetros anteriores sin revisar los cambios.":
            RISE "Recuerda que las condiciones atmosféricas influyen en las cargas que experimenta el cohete durante el ascenso."
            RISE "No podemos ignorar esta información. Revisemos nuevamente el procedimiento."
            #jump escena_4

        "Incorporar los datos meteorológicos, actualizar DOLILU y verificar la trayectoria.":
            RISE "¡Excelente trabajo! Los datos meteorológicos deben integrarse en la actualización y los equipos deben verificar los resultados antes de continuar."
            RISE "Has completado tu primera tarea."
            #jump escena_4

        "Ignorar los vientos porque el cohete ya está preparado.":
            RISE "Recuerda que las condiciones atmosféricas influyen en las cargas que experimenta el cohete durante el ascenso."
            RISE "No podemos ignorar esta información. Revisemos nuevamente el procedimiento."
            #jump escena_4
return