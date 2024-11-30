from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
import random
import requests
from bs4 import BeautifulSoup


async def greeting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'سلام {update.effective_user.first_name}')


async def faal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    random_number = random.randint(1, 495)
    url = 'https://ganjoor.net/hafez/ghazal/sh' + str(random_number)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with the specified class
        elements = soup.find_all(class_='b')

        text = 'غزل شماره ' + str(random_number) + '\n\n'
        # Print the text of each element
        for element in elements:
            text = text + element.text + '\n\n'
        await update.message.reply_text(text)
    else:
        await update.message.reply_text('مشکلی پیش آمده است.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


app = (
    ApplicationBuilder().token("8169939101:AAGCnWHlAmgjQlw3zi5KyFFbqeUznglMMvc").build()
)

app.add_handler(CommandHandler("hello", greeting))
app.add_handler(CommandHandler("faal", faal))
app.add_handler(MessageHandler(filters.Text(), echo))


app.run_polling()
