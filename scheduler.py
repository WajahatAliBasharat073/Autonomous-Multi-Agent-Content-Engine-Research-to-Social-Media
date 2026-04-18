import time
import yaml
import random
from main import run_content_engine

def daily_scheduler():
    """
    Very simple scheduler to run the engine daily.
    For production, better use GitHub Actions, Cron, or Airflow.
    """
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    domains = config.get('domains', ['Artificial Intelligence'])
    
    print("--- Autonomous Content Engine Scheduler Started ---")
    
    while True:
        # Pick a random topic from the list each day to keep things fresh
        topic = random.choice(domains)
        
        try:
            run_content_engine(topic=topic)
        except Exception as e:
            print(f"Error during execution: {e}")
        
        # Wait for 24 hours (86400 seconds)
        print("\nWaiting 24 hours for the next update...")
        time.sleep(86400)

if __name__ == "__main__":
    daily_scheduler()
