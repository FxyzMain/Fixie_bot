from memgpt import MemGPT
import json
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize MemGPT
client = MemGPT(
    auto_save=True
)

# Get the agent_id from .env
agent_id_str = os.getenv("AGENT_ID")
agent_id = uuid.UUID(agent_id_str)

my_message = "Who are you? Who am I?"
response = client.user_message(agent_id=agent_id, message=my_message)

# print(response)

formatted_response = json.dumps(response, indent=2)

print(formatted_response)