from telegram.ext import Application, CommandHandler, ChatMemberHandler

# /start কমান্ডের জন্য ফাংশন
async def start(update, context):
    await update.message.reply_text("✅ হ্যালো! বট এখন চালু আছে।")

# যখন নতুন মেম্বার গ্রুপে জয়েন করবে
async def approve_member(update, context):
    member = update.chat_member
    if member.new_chat_member.status == "member":  # নতুন ইউজার এলো
        try:
            await context.bot.approve_chat_join_request(update.chat_member.chat.id, member.new_chat_member.user.id)
            print(f"✅ Auto approved: {member.new_chat_member.user.first_name}")
        except Exception as e:
            print(f"⚠️ Error approving: {e}")

# তোমার Bot Token
TOKEN = "8267045848:AAFx5FQhCirhZtypTFs_oVjzLyJ3QlUQm14"

# Application তৈরি
app = Application.builder().token(TOKEN).build()

# /start কমান্ড হ্যান্ডলার
app.add_handler(CommandHandler("start", start))

# Auto Approve হ্যান্ডলার
app.add_handler(ChatMemberHandler(approve_member, ChatMemberHandler.CHAT_MEMBER))

print("🚀 Bot চালু হচ্ছে...")
app.run_polling()
