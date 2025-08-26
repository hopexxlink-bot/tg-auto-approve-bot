from telegram.ext import Application, CommandHandler

# /start কমান্ডের জন্য ফাংশন
async def start(update, context):
    await update.message.reply_text("✅ হ্যালো! তোমার বট এখন ঠিকভাবে চলছে।")

# তোমার Bot Token
TOKEN = "8267045848:AAFx5FQhCirhZtypTFs_oVjzLyJ3QlUQm14"

# Bot চালু করার জন্য Application বানানো হলো
app = Application.builder().token(TOKEN).build()

# /start কমান্ড যোগ করা হলো
app.add_handler(CommandHandler("start", start))

print("🚀 Bot চলছে...")
app.run_polling()
