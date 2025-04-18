Autor: Eddy Campos Jiménez
Fecha Creación: 14 abril 2025

-------------------------------------------------
Documento .env

API_KEY = 12345
MODELO = deepseek-r1

-------------------------------------------------
Descripción de las Tecnologías Utilizadas

Para la elaboración de este proyecto se utilizaron varias tecnologías, que permitieron completarlo satisfactoriamente y segun los requerimientos solicitados, a continuación se mencionan cada una de ellas.

*Python: lenguaje de programación base, con este se desarrolló en su totalidad el documento main
*FastAPI: para la creación de la API, framework que permitió crear una interfaz de manera rápida para que el usuario pueda interactuar con la IA y hacer las solicitudes
*Ollama: herramienta que ofrece modelos pre-entrenados de inteligencia artificial. En el proyecto se utilizó especificamente el modelo DeepSeek-r1
*PostMan: herramienta utilizada para realizar pruebas en la API
*Visual Studio Code: editor de código utilizado 

-------------------------------------------------
Instrucciones para la ejecución

Pasos para ejecutar el proyecto y poder realizar solicitudes, suponiendo que el entorno virtual ya ha sido creado y configurado correctamente

*1. Abrir una terminal de windows (dentro de la carpeta del proyecto) y activar el entorno virtual, escribiendo el comando '.\env\Scripts\activate'

*2. Ejecutar el servidor, escribiendo desde la terminal de windows 'uvicorn app.main:app --reload'. Para garantizar que se ejecutó correctamente verificar que muestre en la terminal un mensaje que diga 'Aplication startup complete'

*3. En una nueva terminal y considerando mantenerla abierta durante toda momento en que se vaya a trabajar con el proyecto, debemos correr el modelo de ollama, escribiendo 'ollama run deepseek-r1'. Si aparece '>>>' en la terminal, significa que el proceso de ejecución fue exitoso

*4. En el programa postman realizando una solicitud post HTTP a la url localhost ('http://localhost:8000/preguntar'), nos colocamos en la pestaña body y escribimos la consulta entre las comillas que se encuentran despues del input 'texto' y presionamos el boton de enviar, esperamos un momento y si todo funcionó correctamente la respuesta generada aparece en la sección 'Response' respectivamente

Si el entorno virtual aun no ha sido creado, ANTES de los pasos anteriores debes

*1. Crear el entorno virtual, abriendo una terminal de windows (dentro de la carpeta del proyecto) y escribir el comando 'python -m venv env' y activarlo respectivamente escribiendo el comando '.\env\Scripts\activate'

*2. Instalar las librerías escribiendo en la misma terminal el comando 'pip install fastapi uvicorn requests python-dotenv ollama'

-------------------------------------------------
Respuestas a las preguntas Claves

1.¿Que es Ollama?
    Es una herramienta de código abierto que permite ejecutar y gestionar modelos de inteligencia artificial, de gran tamaño, localmente, es decir desde nuestro computador, lo que ofrece la ventaja de que no es necesario depender de conexión a internet ni de ningun tipo de servicio en la nube, ofreciendole, por la misma razón, mucha privacidad a los usuarios.

2.¿Que es FastAPI?
    Es un framework que permite crear APIs con Python de una manera rápida y sencilla.

3.¿Que es el modelo Deepseek-r1?
    Es un modelo de razonamiento de código abierto desarrollado por la empresa china de IA Deepseek, que se ha convertido en una opción popular entre desarrolladores gracias a su capacidad de razonamiento en problemas, tareas o situaciones que requieran un mayor nivel de profundidad en el análisis y gracias a su eficiencia y accesibilidad, que permite una fácil implementación en cualquier tipo de hardware y/o proyecto.

4.Uso de peticiones con stream=True
    Parametro utilizado en las requests HTTP en python que permite controlar como se descargan los datos de la respuesta, bastante util para cuando se trabajan con archivos grandes o respuestas en tiempo real.
    Ejemplo: por defecto, cuando se utiliza 'response = requests.get(url)' se descarga todo el contenido y se almacena en 'response.content' o 'response.text'; pero en cambio, si se utiliza 'response = requests.get(url, stream=True)' el contenido se descarga a medida que se lee, permitiendo procesar datos en partes

5.¿Como garantizar la escalabilidad de una API que consume modelos de IA pesados?
    Si bien es un reto, en proyectos que consumen modelos de IA muy grandes, lograr escalabilidad, no es imposible por lo que, a continuación se mencionan algunas recomendaciones para poder alcanzarlo.

    *1. Separar la API del modelo: gracias a esta práctica se puede escalar y tarabajar cada una de ellas por separado. Logrando una arquitectura compuesta por la API, el servicio de inferencia y la cola de tareas, separadas

    *2. Optimización del modelo: utilizar, si es posible, versiones del modelo cuantizadas y/o modelos más ligeros. Además de que si el proyecto se va a correr de manera local, utilizar Ollama o vLLM

    *3. Caché inteligente: para evitar hacer la solicitud si ya existe alguna respuesta igual o similar

    *4. Balanceo de Carga: utilizar un 'load balancer' para que así cada instancia del servicio de IA pueda estar corriendo en contenedores como por ejemplo de Docker

    *5. Infraestructura elástica: en el caso de que se de el uso de la nube, utilizar contenedores que permitan el escalado automatico como por ejemplo AWS

    *6. Rate limiting y control de uso: esto permite proteger las APIs con autenticación y limites de uso, evitando la sobrecarga y abusos, esto implementando 'FastAPI-limiter' o 'NGINX limit_req'

6.¿Que parametros de Ollama (ej: num_ctx, temperature) afectan el rendimiento/calidad de respuestas?
    En este modelo, cualquier parámetro que se pase al ejecutar puede afectar positiva o negativamente el rendimiento y la calidad de las respuestas, por ello a continuación se mencionan algunos.

    *1. num_ctx (context length): este parametro define la cantidad de tokens que el modelo puede tener en memoria, es decir el contexto. Por ejemplo si se utiliza 'num_ctx = 4096', esto quiere decir que entre el input y el output pueden haber 4096 tokens. Lo que significa que, entre mayor cantidad de tokens, mayor comprensión de conversaciones extensas pero al mismo tiempo un mayor consumo de RAM/GPU

    *2. temperature: este parametro controla la aleatoriedad de las respuestas, en donde tenemos que los valores mas bajos son mas serios, mientras que los valores más altos, pueden ser mas variables y creativos
        -0.0: Totalmente determinista (preciso pero aburrido)
        -0.7: Balance entre coherencia y creatividad
        -1.0 o más: Muy creativo pero puede inventar cosas

    *3. top_p (nucleus sampling): este parametro controla la probabilidad acumulada de las opciones consideradas, en donde los valores bajos como por ejemplo 0.5 son más conservadores, mientras que los valores más altos como 0.9-1.0, tienden a ser más creativos 

    *4. top_k: este parametro controla la cantidad de tokens más probables que son considerados en cada paso, en donde los valores bajos tienden a dar respuestas más predecibles, mientras que los valores más altos mayor variedad pero a la vez mayor probabilidad de incoherencia y/o errores

    *5. repeat_penalty: este parametro penaliza tokens repetidos para evitar que se repita lo mismo una y otra vez, en donde por ejemplo un valor de 1.0 no tendría ninguna penalización, pero un valor de entre 1.1 - 1.5 tendría menor cantidad de repeticiones

    *6. num_gpu (o configuración del modelo con o sin GPU): aspecto importante a considerar ya que si el modelo es ejecutado en CPU será mas lento y menos eficiente que si se ejecuta en el GPU

    *7. num_predict: cantidad de tokens que puede generar la respuesta, en donde, menos tokens se traducen en una respuesta más rapida, mientras que mayor cantidad de tokens significa una información más completa pero más lenta de generar

7.¿Que estrategias usar para balancear carga entre multiples instancias de Ollama?
    En caso de que se vayan a correr varias instancias de Ollama es importante considerar ciertos aspectos para poder balancear la carga y poder lograr mayor flexibilidad, escalabilidad y eficiencia, a continuación se describen algunas de ellas.

    *1. Balanceador de carga clásico (NGINX, HAProxy): este método reparte las peticiones entrantes entre las instancias disponibles
    
    *2. Balanceo por lógica de aplicación (custom dispatcher): revisando, por medio de métricas en Redis o con un heartbeat simple, cual instancia de Ollama está menos ocupada y redirigiendo la petición a esta instancia, podemos balancear cargas

    *3. Colas de tareas (Celery, Redis Queue, etc.): para un procesamiento asíncrono las colas ofrecen la posibilidad de que multiples workers en Ollama se registren y tomen esas tareas segun la disponibilidad de las mismas, permitiendo tambien tener tareas en espera en dado caso de que tosas las instancias estén ocupadas, lo que lo convierte en una estrategia perfecta para tareas pesadas, generación larga o uso compartido entre varios usuarios

    *4. Instancias aisladas con Docker + Docker Swarm o Kubernetes: esta estrategia se basa en tener cada instancia de Ollama en su propio contenedor, permitiendo una escalabilidad horizontal según la carga de cada instancia

    *5. Auto-escalado basado en métricas: realizando un monitoreo constante del uso del CPU/RAM o de la latencia de cada instancia, se pueden tomar acciones según la variabilidad de las mismas, lanzando nuevas instancias si la carga sube o deteniendolas si bajan respectivamente

8.¿Que patrones de diseño (ej: CQRS, Singleton) son utiles para integrar modelos de IA en backend?
    Es importante conocer los patrones de diseño que existen disponibles, esto para poder escoger el correcto según el que mejor se adapte a nuestras necesidades, a continuación se mencionan algunos de ellos y sus caracteristicas

    *1. Singleton: este patrón se asegura que solo exista una instancia del modelo de IA en memoria, lo que es bastante util para ahorrar recursos y cuando quieres evitar que en cada request el modelo se recargue.

    *2. Command Query Responsibility Segregation (CQRS): este patrón se encarga de separar la lectura, es decir el Query, y escritura, es decir el Command, en componentes distintos, lo que lo convierte en un patrón bastante util cuando se hacen inferencias asíncronas o cuando se utlizan colas.

    *3. Factory Pattern: este patrón crea diferentes modelos de IA, según condiciones dinámicas, lo que lo convierte en un patrón util para servir varios modelos (multi-model API)

    *4. Strategy Pattern: este patrón de diseño define una familia de algoritmos o técnicas y las intercambia en tiempo de ejecución. Útil para cambiar modelo de IA, dependiendo de la disponiblidad, costos, contexto o cualquier otra variable.

    *5. Adapter Pattern: este patrón permite utilizar diferentes interfaces como si fueran iguales, lo que lo convierte en un patrón bastante útil, si se utilizan APIs diferentes, pero se quiere mantener una única lógica en el diseño del proyecto.

    *6. Builder Pattern: este patron de diseño permite construir objetos complejos paso a paso, como por ejemplo prompts o pipelines de IA.

    *7. Observer / Pub-Sub: este patron de diseño permite reaccionar a eventos, por ejemplo, cuando una interferencia termina, lo que lo convierte en un modelo ideal para sistemas asincronicos con colas.
