FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Set the environment variables for Streamlit
ENV STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ENABLE_CORS=false \
    STREAMLIT_SERVER_HEADLESS=true
    # BASE_URL= your_base_url
    # DEEPSEEK_API_KEY= your_deepseek_api_key

# Command to run the application
CMD ["streamlit", "run", "app/app.py"]