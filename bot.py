import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ChatJoinRequestHandler,
    ContextTypes,
)

# Bot Token সরাসরি লিখে দিচ্ছি
BOT_TOKEN = "8267045848:AAHzQaA_Xw3JhUbpvIey1OX7F8s92SIHWjo"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot চালু আছে! আমাকে Group/Channel এ অ্যাড করুন।")

# Auto Approve + Welcome Message
async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_request = update.chat_join_request
    user = chat_request.from_user

    # Auto approve
    await chat_request.approve()

    # Welcome message
    try:
        await context.bot.send_message(
            chat_id=chat_request.chat.id,
            text=f"স্বাগতম {user.first_name}! 🎉 আপনি সফলভাবে গ্রুপ/চ্যানেলে যোগ দিলেন।"
        )
    except Exception as e:
        print("Error sending welcome:", e)

# Main function
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Command handler
    app.add_handler(CommandHandler("start", start))

    # Join request handler
    app.add_handler(ChatJoinRequestHandler(approve))

    print("🤖 Bot চালু হচ্ছে...")
    app.run_polling()

if __name__ == "__main__":
    main()
