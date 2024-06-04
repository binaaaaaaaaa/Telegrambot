import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from getnew import getnew3, getnew, getnewdecrypt

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    titles = getnew3()
    for title, link in titles:
        await update.message.reply_text(f'{title}\n{link}')
    titles = getnew()
    for title, link in titles:
        await update.message.reply_text(f'{title}\n{link}')
    titles = getnewdecrypt()
    for title, link in titles:
        await update.message.reply_text(f'{title}\n{link}')

def main():
    app = ApplicationBuilder().token("7429654937:AAEfzmEK6toY3AO3GuE5-ziR4FVWVsABhao").build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("news", news))
    app.run_polling()

if __name__ == "__main__":
    main()