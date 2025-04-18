# Importar las librerías necesarias
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Leer valores desde el entorno
MODELO = os.getenv("MODELO")

# Crea una instancia de FastAPI
app = FastAPI()

# Modelo de datos para recibir la pregunta
class Pregunta(BaseModel):
    texto: str

# Declara un endpoint HTTP tipo POST
@app.post("/preguntar")

# Definicion de la función asíncrona que recibe un objeto del tipo 'Pregunta'
async def preguntar(pregunta: Pregunta):
    try:
        # Creación del cuerpo (payload) que se va a enviar a la API de Ollama
        payload = {
            "model": MODELO,            # El nombre del modelo  
            "prompt": pregunta.texto,   # El texto que el usuario envía como pregunta
            "stream": False             # Desactiva el modo streaming para que devuelva la respuesta completa
        }

        # Envia una solicitud POST al servidor local de Ollama
        respuesta_ollama = requests.post(
            "http://localhost:11434/api/generate",  # Ruta de la API de generación de texto
            json=payload,                           # Le pasa el cuerpo (payload) en formato JSON
            timeout=200                             # Tiempo maximo de espera antes de que cancele la solicitud
        )

        # Si la respuesta tiene un código de error (404, 500, etc), lanza una excepción
        respuesta_ollama.raise_for_status()

        # Convierte la respuesta de Ollama en formato JSON (diccionario de Python)
        data = respuesta_ollama.json()

        # Verifica si la clave 'response' está presente en la respuesta
        if "response" not in data:
            raise HTTPException(
                status_code=500, 
                detail=f"Respuesta inesperada de Ollama: {data}") 
                # Lanza un error si el formato no es el esperado

        # Todo salió bien devuelve la respuesta del modelo en un diccionario
        return {"respuesta": data["response"]}

    # Si hubo un problema al conectar con Ollama (timeout, conexión fallida, etc)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con el modelo IA: {str(e)}")
        # Muestra el mensaje de error



