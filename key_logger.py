from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = 'Enter your BOT_TOKEN HERE '
LOG_FILE = "Enter your LOG_FILE name here "

# Save every user message to a file
async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    user = update.effective_user.first_name
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{user}: {message}\n")
    await update.message.reply_text("Message received and logged!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, log_message))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
