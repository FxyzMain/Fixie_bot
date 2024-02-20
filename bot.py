from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext, filters
from memgpt import MemGPT
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

# Initialize MemGPT
client = MemGPT(
    auto_save=True
)


# Telegram Bot API token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
agent_id_str = os.getenv("AGENT_ID")
agent_id = uuid.UUID(agent_id_str)

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to the MemGPT chatbot! Send /help for instructions.")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("You can chat with me directly.")

async def message_handler(update: Update, context: CallbackContext):
    message_text = update.message.text
    
    # Use MemGPT to generate a response
    response = client.user_message(agent_id=agent_id, message=message_text)

    if response:
        for r in response:
            print("Individual Response:", r)
            if "assistant_message" in r:
                await update.message.reply_text(r["assistant_message"])
            elif "error" in r:
                print("Error:", r["error"])
                await update.message.reply_text("Error processing the message.")
    else:
        await update.message.reply_text("No response from MemGPT.")





def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler))

    application.run_polling()

if __name__ == "__main__":
    main()

