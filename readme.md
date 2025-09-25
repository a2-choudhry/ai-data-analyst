# AI Data Analyst

AI Data Analyst is an AI-powered assistant that reads and analyzes data from user-provided speech and images, generating actionable insights in both text and audio form. The system combines advanced multimodal AI capabilities with a seamless Gradio interface and is fully containerized with Docker for easy deployment.

**Features**

- Speech-to-text (via microphone input)
- Image upload support
- AI-generated analytical responses
- Audio playback of results
- Option to download responses.

#Technical architecture
![image alt](https://github.com/a2-choudhry/ai-data-analyst/blob/f388699698289107d3a93d1d5e1214688a94d5ad/diagram.JPG)

🐳 **Run with Docker**

```bash
# Clone the repository
git clone https://github.com/a2-choudhry/ai-data-analyst.git
cd ai-data-analyst

# Build the Docker image
docker build -t ai-data-analyst .

# Run the container
docker run -p 7860:7860 ai-data-analyst


