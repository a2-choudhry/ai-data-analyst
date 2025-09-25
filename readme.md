AI Data Analyst

AI Data Analyst is an AI-powered assistant that reads and analyzes data from user-provided speech and images, generating actionable insights in both text and audio form. The system combines advanced multimodal AI capabilities with a seamless Gradio interface and is fully containerized with Docker for easy deployment.

Features

Speech-to-text: Capture user voice input and convert it to text using OpenAI's Whisper model.
Image analysis: Upload images and receive insights using the "Meta Llama3 Vision 90B" multimodal LLM.
AI-generated analytical responses: Provides text-based insights as a virtual data analyst.
Audio playback: Realistic TTS responses via ElevenLabs or gTTS for dynamic voice feedback.
Downloadable output: Save text responses as files for later reference.
Docker-ready: Containerized setup allows easy deployment on any system.

Getting Started
Clone the Repository
git clone https://github.com/yourusername/ai-data-analyst.git
cd ai-data-analyst

Environment Setup

Create a .env file and add your API keys:

GROQ_API_KEY=your_groq_api_key
ELEVEN_API_KEY=your_elevenlabs_api_key


Install dependencies:

pip install -r requirements.txt

Build and Run with Docker

Build the Docker image:

docker build -t ai-data-analyst .


Run the container:

docker run -p 7860:7860 ai-data-analyst

The app will be accessible at: http://127.0.0.1:7860/

🛠 Technology Stack

Gradio: Web-based interface for multimodal interaction.

OpenAI Whisper: Accurate speech-to-text conversion.

Meta Llama3 Vision 90B: Multimodal LLM for text and image understanding.

ElevenLabs & gTTS: Realistic text-to-speech conversion.

Docker: Containerization for easy deployment across systems.

📄 Usage

Launch the app.

Speak your query into the microphone.

Optionally upload an image for multimodal analysis.

Receive AI insights in text and audio format.

Download your results if needed.
