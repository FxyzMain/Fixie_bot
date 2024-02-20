# Fixie Bot

Fixie Bot is a simple chatbot powered by MemGPT that integrates with the Telegram messaging platform.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/lydacious/fixie_bot.git
    ```

2. Change into the project directory:

    ```bash
    cd fixie_bot
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run `create_agent.py` to generate a MemGPT agent:

    ```bash
    python create_agent.py
    ```

   Copy the generated agent ID.

5. Head into `.env` file in the project root:

   Replace `YOUR_TELEGRAM_BOT_TOKEN` with your Telegram Bot API token and `YOUR_AGENT_ID` with the agent ID obtained from running `create_agent.py`.

6. Now, you can run the bot using `bot.py`:

    ```bash
    python bot.py
    ```

   or test the bot's responses without Telegram using `test.py`:

    ```bash
    python test.py
    ```

## Testing Responses

To test the bot's responses without going through Telegram, run the `test.py` script after setting up the environment. This allows you to quickly evaluate the chatbot's behavior in a non-interactive manner.

## Customizing MemGPT Agents

Edit the parameters of the MemGPT agents within the `create_agent.py` script to customize their behavior. This script generates a new agent configuration and prints the corresponding agent ID.

Feel free to explore and modify the scripts according to your requirements!
