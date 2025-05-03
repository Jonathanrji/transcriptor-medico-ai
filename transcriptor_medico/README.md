# 🩺 Transcriptor Médico AI

**Transcriptor Médico AI** es una aplicación desarrollada en Python que permite a doctores y personal clínico transcribir audios médicos automáticamente y generar un informe clínico estructurado utilizando modelos de lenguaje de última generación (LLMs).

---

## 🎯 Objetivo

Reducir errores humanos en la transcripción médica y agilizar el flujo de trabajo clínico, permitiendo que un audio dictado por el médico sea transcrito y analizado de forma automática para generar un informe con secciones como **Hallazgos** e **Impresión**.

---

## ⚙️ Tecnologías utilizadas

- 🧠 [Whisper](https://github.com/openai/whisper) – para transcripción de audio
- 🤖 [Ollama](https://ollama.com) – para ejecutar modelos LLM localmente
- 🌐 [Streamlit](https://streamlit.io) – para la interfaz web
- 🐍 Python 3.11+ con entorno gestionado por [`uv`](https://github.com/astral-sh/uv)

---

## 🛠️ Instalación rápida

1. Clona el repositorio:

```bash
git clone https://github.com/jonathanrji/transcriptor-medico-ai.git
cd transcriptor-medico-ai

2. Crea y activa el entorno virtual con uv:

uv venv
.\.venv\Scripts\Activate.ps1  # en Windows

3. Instala las dependencias:

uv pip install -r requirements.txt

4. Asegúrate de tener FFmpeg instalado (en Windows se recomienda usar choco install ffmpeg).

5. Inicia el servidor de modelos LLM de Ollama:

ollama serve

6. Ejecuta la app:

streamlit run app.py

 ## 🧪 Cómo usar 

Sube un audio (.mp3, .wav, .m4a) donde un médico dicte un análisis (por ejemplo, una radiografía).

La app transcribirá el audio usando Whisper.

Revisa y edita la transcripción si es necesario.

Selecciona un modelo LLM para analizar (Gemma 3, LLaMA 3, DeepSeek).

Haz clic en "Generar análisis médico".

Visualiza el informe generado con secciones estructuradas.

Descarga el informe en .txt si lo deseas.


## 🧠 Modelos compatibles (vía Ollama)
Modelo - Descripción
gemma3:12b-it-qat	Preciso, especializado en lenguaje técnico y clínico
llama3:latest	Balance entre velocidad y coherencia
deepseek-r1:latest	Ideal para razonamiento médico y análisis detallado



✅ Estado del proyecto
✅ Funcionalidad completa
✅ Modelos LLM dinámicos
✅ Transcripción optimizada
✅ UI limpia con Streamlit
🔜 Posible integración de grabación por micrófono

📄 Licencia
MIT License © 2025 - Jonathan Rojas, Carlos Rodríguez

✨ Autores
Desarrollado por [Jonathan Rojas, Carlos Rodríguez]
Especialización en Inteligencia Artificial – Universidad Autónoma de Occidente
