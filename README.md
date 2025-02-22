# 🤖 Chatbot de Jaime Alonso Ruiz - DeepSeek API & Streamlit

🚀 **Chatbot interactivo basado en IA** que recita poemas clásicos (¡o lo que le pidas!). Utiliza **DeepSeek API** a través de **OpenRouter** y está implementado en **Streamlit**.

## ✨ Características
✅ Generación automática de poemas usando **DeepSeek-R1**  
✅ Historial de conversaciones en tiempo real con **Streamlit**  
✅ Interfaz web intuitiva y fácil de usar  
✅ Conexión con **OpenRouter** para evitar restricciones de pago  
✅ Código modular y adaptable a otros modelos de IA, con Docker  

## 🛠️ Tecnologías Utilizadas
- **Python** 🐍
- **Streamlit** 🎨 (Interfaz de usuario)
- **DeepSeek API** 🤖 (Modelo de IA)
- **OpenRouter** 🔗 (Acceso gratuito a la API)
- **Docker** 🐳 (Contenedorización del proyecto)
- **Logging y manejo de errores** 📜

## 🚀 Instalación y Ejecución
Sigue estos pasos para ejecutar el chatbot en tu equipo:

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/jaimealruiz/DeepSeek-R1-chatbot.git
cd DeepSeek-R1-chatbot/chatbot
```

### 2️⃣ Crear un Entorno Virtual (Opcional pero Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows
```

### 3️⃣ Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar la Clave API
Crea un archivo `.env` en la raíz del proyecto y agrega tu clave API:
```env
OPENROUTER_API_KEY="tu_clave_api_aquí"
BASE_URL="base_url_aquí"
```

### 5️⃣ Ejecutar la Aplicación
```bash
streamlit run chatbot.py
```
Esto abrirá la aplicación en tu navegador automáticamente. 🎉

### 6️⃣ Ejecutar con Docker (Opcional)
Si prefieres usar Docker, sigue estos pasos:

#### a) Construir la imagen Docker
```bash
docker build -t chatbot .
```

#### b) Ejecutar el contenedor
```bash
docker run -p 8501:8501 --env-file .env chatbot
```
Esto iniciará la aplicación en `http://localhost:8501`.

## 👥 Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, sigue estos pasos:
1. Haz un **fork** del repositorio.
2. Crea una nueva rama: `git checkout -b mi-nueva-funcionalidad`
3. Realiza cambios y haz commits: `git commit -m "Añadir nueva funcionalidad"`
4. Sube tus cambios: `git push origin mi-nueva-funcionalidad`
5. Crea un **pull request** 📬

## 📄 Licencia
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes utilizarlo y modificarlo libremente. Consulta el archivo `LICENSE` para más información.

---

✨ **¡Gracias por visitar este proyecto!** Si te gusta, ⭐ **dale una estrella en GitHub** y siéntete libre de contribuir. 🚀  
📩 **Contacto:** [LinkedIn](https://linkedin.com/in/jaimealonsoruiz)
