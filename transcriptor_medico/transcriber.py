import whisper

# Cargar el modelo una vez
model = whisper.load_model("large")  # Cambiar a "base", "small", "medium" si el PC no puede con "large"

def transcribe_audio(file_path: str, language: str = "es") -> str:
    """
    Transcribe un archivo de audio usando Whisper.
    :param file_path: Ruta al archivo de audio
    :param language: Idioma del audio (ej. 'es' para español)
    :return: Texto transcrito
    """
    result = model.transcribe(file_path, language=language)
    return result["text"]
