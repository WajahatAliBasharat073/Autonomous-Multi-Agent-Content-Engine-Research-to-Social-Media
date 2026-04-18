import os
from dotenv import load_dotenv

def load_env_vars():
    """
    Load environment variables from .env file.
    """
    load_dotenv()
    
    # Check for required API keys
    openai_key = os.getenv("OPENAI_API_KEY")
    serper_key = os.getenv("SERPER_API_KEY")
    
    if not openai_key:
        print("Warning: OPENAI_API_KEY not found in .env")
    if not serper_key:
        print("Warning: SERPER_API_KEY not found in .env")
        
    return openai_key, serper_key

def set_model_name(model_name="gpt-3.5-turbo"):
    """
    Set the default OpenAI model name.
    """
    os.environ["OPENAI_MODEL_NAME"] = model_name
