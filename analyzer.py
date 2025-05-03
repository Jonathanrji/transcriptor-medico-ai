from ollama import chat

def analyze_transcription(transcript_text: str, model_name: str = "gemma3:12b-it-qat") -> str:
    """
    Envía la transcripción al modelo LLM en Ollama y obtiene un análisis médico estructurado.
    :param transcript_text: Texto transcrito del audio médico
    :param model_name: Nombre del modelo cargado en Ollama (por defecto: 'gemma3')
    :return: Informe estructurado con hallazgos e impresión
    """
    messages = [
        {
            "role": "system",
            "content": (
                "Eres un asistente médico experto. Tu tarea es analizar una transcripción dictada por un doctor "
                "y generar un informe clínico estructurado. Usa un tono profesional y lenguaje técnico apropiado."
            )
        },
        {
            "role": "user",
            "content": (
                f"Aquí está la transcripción dictada por el doctor:\n\n\"\"\"\n{transcript_text}\n\"\"\"\n\n"
                "Por favor, genera un informe médico bien redactado en español, con dos secciones tituladas:\n"
                "- Hallazgos\n- Impresión (Conclusión clínica)"
            )
        }
    ]

    response = chat(model=model_name, messages=messages)
    return response['message']['content']
