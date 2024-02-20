from memgpt import MemGPT

# Initialize MemGPT
client = MemGPT(
    auto_save=True
)

# Create an AgentConfig
agent_config = {
    "name": "fixiet1",
    "persona": "anna_pa",
    "human": "basic",
}
agent_state = client.create_agent(agent_config=agent_config)

print("Please paste this string into agent_id in .env:" + str(agent_state.id))