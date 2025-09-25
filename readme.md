AI Data Analyst

This project is an AI-powered Data Analyst assistant that accepts speech + image inputs and generates insights.
It is containerized with Docker for easy deployment.

✨ Features

🎙️ Speech-to-text (via microphone input)

🖼️ Image upload support

💬 AI-generated analytical responses

🔊 Audio playback of results

💾 Option to download responses.

🐳 Run with Docker
1. Clone this repo
git clone https://github.com/yourusername/ai-data-analyst.git
cd ai-data-analyst

2. Build the Docker image
docker build -t ai-data-analyst .

3. Run the container
docker run -p 7860:7860 ai-data-analyst


The app will be available at: http://127.0.0.1:7860/