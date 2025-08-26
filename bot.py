from telegram import Update
from telegram.ext import Application, CommandHandler, ChatMemberHandler, ContextTypes

# তোমার টোকেন
TOKEN = "8267045848:AAFx5FQhCirhZtypTFs_oVjzLyJ3QlUQm14"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is running!")

# যখন নতুন কেউ join করবে তখন auto approve হবে
async def approve_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_member = update.chat_member
    if chat_member.new_chat_member.status == "member":
        await context.bot.approve_chat_join_request(
            chat_id=chat_member.chat.id,
            user_id=chat_member.from_user.id
        )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatMember
