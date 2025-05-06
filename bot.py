from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from colorama import init, Fore

# Inisialisasi colorama
init(autoreset=True)

# Ganti dengan token bot yang kamu dapatkan dari BotFather
TOKEN = '8003231767:AAGewSQTTDGH64C1ADdW14OGWu4yqxmquY8'

# Fungsi untuk memeriksa member yang masuk
async def check_new_member(update: Update, context: CallbackContext):
    # Mendapatkan informasi member baru yang masuk
    for member in update.message.new_chat_members:
        # Pastikan member tidak memiliki username
        if not member.username:  
            # Mengirim pesan pemberitahuan dan meng-kick member
            await context.bot.kick_chat_member(chat_id=update.message.chat.id, user_id=member.id)
            await context.bot.send_message(
                chat_id=update.message.chat.id,
                text=f"User {member.full_name} telah dikeluarkan karena tidak memiliki username."
            )

# Fungsi untuk memulai bot (opsional)
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Bot telah aktif dan siap mengelola grup.')

def main():
    # Membuat Application dan menghubungkannya dengan bot token
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk pesan masuk dan memeriksa member baru
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, check_new_member))
    application.add_handler(CommandHandler("start", start))
    
    # Menjalankan bot
    application.run_polling()

    # Menampilkan pesan berhasil dijalankan berwarna hijau
    print(Fore.GREEN + "Bot berhasil dijalankan dan aktif!")

if __name__ == '__main__':
    main()
