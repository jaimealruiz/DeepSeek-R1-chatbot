import streamlit as st
import logging
from openai import OpenAI

# Configura el cliente OpenAI con OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

logging.basicConfig(level=logging.INFO)

# Inicializar el historial de mensajes si no existe en el estado de la sesión
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Eres un asistente de IA especializado en generar resúmenes breves de libros y artículos de cultura empresarial. Responde siempre en español y mantén un tono amable y profesional."},
    ]

# Función para obtener una respuesta del modelo
def get_response(messages):
    try:
        # Realiza la solicitud a la API
        completion = client.chat.completions.create(
            extra_body={},
            model="deepseek/deepseek-r1:free",
            messages=messages
        )
        # Devuelve el contenido de la respuesta
        return completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Error en la API: {str(e)}")
        return "Lo siento, hubo un error al generar la respuesta."

# Aplicación principal
def main():
    st.title("Chatbot Resumen.es")
    st.info("¡Hola! Soy Resumen.es, tu asistente de IA para resúmenes breves de libros y artículos de cultura empresarial. ¿En qué libro o artículo estás interesado?")

    # Mostrar historial de mensajes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Entrada de usuario
    if prompt := st.chat_input("Escribe tu consulta aquí..."):
        # Agregar mensaje del usuario al historial
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Generar respuesta del asistente
        with st.chat_message("assistant"):
            with st.spinner("Generando respuesta..."):
                assistant_response = get_response(st.session_state.messages)
                st.write(assistant_response)
                # Agregar respuesta al historial
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    main()
