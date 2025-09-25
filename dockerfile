# 1. Base image with Python
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements first for caching
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your app code into the container
COPY . .

# 6. Expose Gradio’s default port
EXPOSE 7860

# 7. Run your app
CMD ["python", "gradio_app.py"]
