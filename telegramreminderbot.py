from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio  # Use asyncio instead of threading and time.sleep

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your bot. Send me a message, and I will set a reminder!')

async def set_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("Usage: /remind <time_in_seconds> <message>")
            return

        delay = int(args[0])
        message = " ".join(args[1:])

        chat_id = update.effective_chat.id
        await update.message.reply_text(f"Reminder set for {delay} seconds: {message}")

        # Use asyncio.sleep instead of time.sleep
        await asyncio.sleep(delay)  # Key change: await asyncio.sleep

        # Send the reminder
        await context.bot.send_message(chat_id=chat_id, text=f"⏰ Reminder: {message}")

    except ValueError:
        await update.message.reply_text("Invalid time. Please use a number for seconds.")

def main():
    TOKEN = "7893975968:AAGYs1KumPdCIVOWeXmu_DSNhYmTWAFGbGg"  # Replace with your actual token
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("remind", set_reminder))
    application.run_polling()

if __name__ == '__main__':
    main()