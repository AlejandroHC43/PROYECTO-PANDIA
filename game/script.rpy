
# Declarar variables
default rol_jugador = ""

# Definir personajes
define RISE = Character("RISE", color="#8be9fd")

# Definir imágenes
image FONDO1 = "images/FONDO ESCENA 1.jpeg"


# Inicio del juego
label start:

    scene FONDO1
    with fade

    RISE "Bienvenido, explorador. Me llamo RISE y seré tu asistente durante esta misión."

    RISE "Hoy no estamos ante un lanzamiento cualquiera. Cuatro astronautas están preparados para viajar alrededor de la Luna a bordo de la nave Orion."

    RISE "Pero llegar al espacio requiere mucho más que encender un cohete. Miles de sistemas, personas y procedimientos deben trabajar en perfecta coordinación."

    RISE "Tu función será apoyar al equipo de análisis de misión. Tendrás acceso a información meteorológica, indicadores de vuelo y comunicaciones de la tripulación."

    RISE "No estarás solo. Yo te ayudaré a interpretar los datos, pero las decisiones operativas reales corresponden a los especialistas y responsables de misión."

    # Menú inicial de preparación
    menu:
        "¿Estás preparado?"

        "Sí, estoy listo para comenzar.":
            RISE "Excelente. Comencemos con los preparativos."

        "Necesito conocer primero los objetivos.":
            RISE "Nuestra misión consiste en comprobar que Orion y sus sistemas pueden transportar de manera segura a una tripulación alrededor de la Luna y de regreso a la Tierra."
            RISE "Comenzaremos con la preparación del lanzamiento y avanzaremos hasta alcanzar la órbita terrestre."

    # Selección de rol
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

return
