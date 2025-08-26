from telegram import Update
from telegram.ext import Application, CommandHandler, ChatJoinRequestHandler, ContextTypes
import os

# Bot Token (Render এ Environment Variable থেকে নেবে)
TOKEN = os.environ.get("8267045848:AAHzQaA_Xw3JhUbpvIey1OX7F8s92SIHWjo")

# /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot চালু আছে! আমাকে Group/Channel-এ Admin করে দাও।")

# Auto approve + Welcome message
async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_request = update.chat_join_request
    user = chat_request.from_user

    # Auto approve
    await chat_request.approve()

    # Welcome message পাঠানো
    try:
        await context.bot.send_message(
            chat_id=chat_request.chat.id,
            text=f"🎉 স্বাগতম {user.first_name}!\nতুমি সফলভাবে গ্রুপ/চ্যানেলে যোগ হয়েছো।"
        )
    except Exception as e:
        print("Error sending welcome:", e)

# Main Function
def main():
    app = Application.builder().token(TOKEN).build()

    # Command handler
    app.add_handler(CommandHandler("start", start))

    # Join request handler
    app.add_handler(ChatJoinRequestHandler(approve))

    print("🤖 Bot চালু হচ্ছে...")
    app.run_polling()

if __name__ == "__main__":
    main()
