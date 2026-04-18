import os
import yaml
from datetime import datetime
from src.utils import load_env_vars, set_model_name
from src.crew import build_content_engine_crew

def run_content_engine(topic=None):
    """
    Main function to run the content research and generation workflow.
    """
    # 1. Environment Setup
    load_env_vars()
    set_model_name(os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo"))
    
    # 2. Get Config
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    # 3. Use default topic if none provided
    if not topic:
        topic = config['domains'][0]
    
    print(f"\n--- Starting Content Engine for Topic: {topic} ---")
    
    # 4. Build and Kickoff Crew
    crew = build_content_engine_crew()
    result = crew.kickoff(inputs={"topic": topic})
    
    # 5. Handle Archiving
    if config.get('enable_archive'):
        archive_dir = config.get('archive_directory', 'posts_archive')
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{archive_dir}/post_{timestamp}_{topic.replace(' ', '_').lower()}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Content for: {topic}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(str(result))
            
        print(f"\nContent archived to: {filename}")
        
    return result

if __name__ == "__main__":
    # Test run with the first domain from config
    run_content_engine()
