"""Configuration module for Agentic RAG system"""

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for RAG system"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Model Configuration
    LLM_MODEL = "openai:gpt-4o"
    
    # Document Processing
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    
    # Default URLs
    DEFAULT_URLS = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
    ]
    
    @classmethod
    def get_llm(cls):
        """Initialize and return the LLM model."""
        # ensure the OpenAI key is available to the SDK
        os.environ["OPENAI_API_KEY"] = cls.OPENAI_API_KEY

        # fix broken SSL_CERT_FILE settings that point to missing files
        # (Anaconda on Windows often sets this to a path that doesn't exist)
        cert_file = os.environ.get("SSL_CERT_FILE")
        if cert_file and not os.path.isfile(cert_file):
            print(f"Warning: SSL_CERT_FILE '{cert_file}' does not exist; unsetting.")
            del os.environ["SSL_CERT_FILE"]
        return init_chat_model(cls.LLM_MODEL)