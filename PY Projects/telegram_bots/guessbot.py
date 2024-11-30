from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler
import random

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Greetings! Shall we begin?\nUse command 'begin'")

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Here's the deal: I'll provide you with a random number between 1 and 1000",'\n',
"and your job is to guess it. After each guessI'll give you hints to help you get closer and closer to the correct number.")

def begin(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Guess a number between 1 and 1000: ")

def answer(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(guessing())

def guessing():
    choosen_num=random.randint(1,1000)
    flag=True
    user_guess=Update.message.text
    while flag:
        if user_guess<(choosen_num-200):
            print("much higher")
        elif (user_guess-200)>choosen_num:
            print("much lower")
        elif user_guess<choosen_num:
            print("higher")
        elif user_guess>choosen_num:
            print("lower")
        elif user_guess==choosen_num:
            print("prost <3")
            flag=False

def main():
    updater = Updater("7717735224:AAExIHPzCqKYxFIXs1YPrIyAVwaPCUcZK8I")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("begin", begin))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer))

    updater.start_polling()
    updater.idle()