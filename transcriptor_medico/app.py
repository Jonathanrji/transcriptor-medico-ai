import streamlit as st
import tempfile
from transcriber import transcribe_audio
from analyzer import analyze_transcription

st.set_page_config(page_title="Transcriptor Médico AI", layout="centered", page_icon="🩺")
st.title("🩺 Transcriptor Médico Inteligente")
st.markdown("Sube un audio con el dictado del doctor y obtén una **transcripción automática** y un **informe clínico estructurado** usando inteligencia artificial.")

# --- Subida de audio ---
audio_file = st.file_uploader("📁 Sube un archivo de audio (MP3, WAV, M4A...)", type=["mp3", "wav", "m4a", "mp4"])

if audio_file:
    st.audio(audio_file)

    suffix = "." + audio_file.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    # Transcribir solo si aún no lo hicimos
    if "transcript" not in st.session_state:
        with st.spinner("🧠 Transcribiendo el audio con Whisper..."):
            try:
                transcript = transcribe_audio(tmp_path, language="es")
                st.session_state.transcript = transcript
                st.success("✅ Transcripción completada")
            except Exception as e:
                st.error("❌ Error al transcribir")
                st.exception(e)
                st.stop()
    else:
        transcript = st.session_state.transcript

    # --- Mostrar y permitir editar transcripción ---
    st.subheader("📝 Transcripción")
    transcript = st.text_area("Puedes editar el texto si es necesario:", transcript, height=200)
    st.session_state.transcript = transcript  # Guardar edición

    # --- Selección de modelo LLM ---
    st.subheader("🤖 Selecciona el modelo de lenguaje")
    model_descriptions = {
        "gemma3:12b-it-qat": "🧠 Gemma 3 (12B, fine-tuned): preciso, ideal para lenguaje técnico.",
        "llama3:latest": "⚡ LLaMA 3 (7B): rápido, balanceado para tareas generales.",
        "deepseek-r1:latest": "🔬 DeepSeek R1: excelente para razonamiento y detalle clínico."
    }
    model_option = st.selectbox(
        "Modelo a utilizar para el análisis:",
        options=list(model_descriptions.keys()),
        format_func=lambda m: model_descriptions[m]
    )

    # --- Botón para generar análisis ---
    if st.button("🔍 Generar análisis médico"):
        with st.spinner("📡 Analizando transcripción con modelo de lenguaje..."):
            try:
                analysis = analyze_transcription(st.session_state.transcript, model_name=model_option)
                st.session_state.analysis = analysis
                st.success("✅ Análisis generado")
            except Exception as e:
                st.error("❌ Error al generar análisis")
                st.exception(e)
                st.stop()

    # --- Mostrar análisis generado ---
    if "analysis" in st.session_state:
        st.subheader("📑 Informe Médico Generado")
        st.markdown(st.session_state.analysis)

        # Botón para descargar como .txt
        st.download_button(
            label="💾 Descargar informe (.txt)",
            data=st.session_state.analysis,
            file_name="informe_medico.txt",
            mime="text/plain"
        )
