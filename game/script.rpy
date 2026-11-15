
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
            "Debemos decidir qué hacer"

            "Continuar con los parámetros anteriores sin revisar los cambios.":
                RISE "Recuerda que las condiciones atmosféricas influyen en las cargas que experimenta el cohete durante el ascenso."
                RISE "No podemos ignorar esta información. Revisemos nuevamente el procedimiento."
                jump escena_4

            "Incorporar los datos meteorológicos, actualizar DOLILU y verificar la trayectoria.":
                RISE "¡Excelente trabajo! Los datos meteorológicos deben integrarse en la actualización y los equipos deben verificar los resultados antes de continuar."
                RISE "Has completado tu primera tarea."
                jump escena_4

            "Ignorar los vientos porque el cohete ya está preparado.":
                RISE "Recuerda que las condiciones atmosféricas influyen en las cargas que experimenta el cohete durante el ascenso."
                RISE "No podemos ignorar esta información. Revisemos nuevamente el procedimiento."
                jump escena_4

# Escena 4. La verificación final
label escena_4:

    scene FONDO1

    RISE "Los parámetros actualizados deben comprobarse antes de su utilización."

    RISE "Los equipos de NASA realizan verificaciones independientes de la trayectoria y de las cargas estructurales mediante simulaciones por computadora."

    RISE "La actualización se carha aproximadamente una hora antes del lanzamiento y debe realizarse a más tardar 40 minutos antes."

    #Desafío 2: Validación de datos

    menu:
        "Tenemos tres opciones para continuar. ¿Cuál debemos seguir?:"

        "Cargar los datos y continuar sin realizar verificaciones adicionales.":
         RISE "¡No tan rápido! Antes de continuar, recuerda que los datos de una misión deben ser confiables y corresponder a las condiciones actuales. No es recomendable avanzar sin comporbar la información ni utilizar parámetros de otras misiones sin validarlos." 
        #jump escena_5

        "Verificar los resultados de trayectoria y cargas, confirmar la correcta.":
         RISE "¡Correcto! La información debe verificarse antes de continuar. En una misión espacial, la comunicación entre los equipos es tan importante como los propios datos."

        "Utilizar los parámetros de un lanzamiento anterior.":
         RISE "No"
        #jump escena_5

    RISE "La preparación continúa. Vamos a comunicarnos con la tripulación"

#Escena 5. Comunicación con Orión
label escena_5:

    scene FONDO2

    "Artemis II, comprobación de comunicaciones."

    a "Aquí Artemis II. Comunicaciones recibidas correctamente."

    b "Los sistemas de la nave están siendo revisados."

    c "La tripulación continúa con las comprobaciones previas al lanzamiento."

    d "Estamos preparados para comenzar esta aventura."

    RISE "Explorador, hemos llegado a uno de los momentos más importantes. La secuencia de lanzamiento está próxima a comenzar."

    RISE "Recuerda: durante el ascenso, el equipo de Tierra continuará supervisando el comportamiento del vehículo. Tu función será interpretar la información de nuestra simulación."

#Escena 6. La cuenta regresiva.
label escena_6:

    scene FONDO1

    RISE "Fecha: 1 de abril de 2026."

    RISE "Ubicación: Centro Espacial Kennedy, Florida."

    RISE "Vehículo: Space Launch System."

    RISE "Nave espacial: Orion."

    RISE "Tripulación: cuatro astronautas."

    RISE "¡Despegue!"

#Escena 7. El ascenso y la separación de propulsores
label escena_7

    scene FONDO2

    RISE "El SLS continúa su ascenso. Durante esta fase, el vehículo debe superar las fuerzas aerodinámicas y mantener su trayectoria."

    RISE "Aproximadamente dos minutos después del despegue, los propulsores sólidos completan su función y se sparan del vehículo."

    VICTOR "La nave continúa su trayectoria."

    REID "Seguimos atentos a los indicadores."

    RISE "La separación de los propulsores es una de las etapas importantes del ascenso. Debemos continuar supervisando la información de vuelo."

#Escena 8. Una anomalía durante el entrenamiento
label escena_8

    scene FONDO1

    RISE "Explorador, vamos a realizar un ejercicio de entrenamiento adicional."

    RISE "Se ha presentado una lectura de presión intermitente en nuestro escenario simulado. Necesitamos identificar la respuesta adecuada."

    #Desafío 3: Análisis de Telemetría

    menu:
        "¿Qué debemos hacer?"

        "Modificar manualmente la válvula para intentar corregir la lectura.":
            RISE "¡Espera!, una alerta no debe ignorarse, pero tampoco debemos intervenir directamente en un siste"
        #jump escena_9

        "Ignorar la alerta porque el vehículo continúa volando.":
         RISE "No."
        #jump escena_9

        "Comparar la información con otros indicadores, comunicar la anomalía al especialista responsable y seguir el procedimiento establecido.":
            RISE "Muy bien! Una lectura anormal no significa necesariamente que exista una falla real en el sistema."
            RISE "Debemos contrastar la información, comunicar la situación y permitir que los especialistas responsables evalúen los datos."
            RISE "En una misión espacioal, reaccionar rápidamente es importante, pero hacerlo sin información suficiente puede generar nuevos riesgos."

return