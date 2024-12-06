from telegram import Update 
from telegram.ext import Updater, CommandHandler, CallbackContext, filters, MessageHandler, ApplicationBuilder
import random

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Greetings! Shall we begin?\nUse /begin")

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Here's the deal: I'll provide you with a random number between 1 and 1000",'\n',
"And your job is to guess it. After each guessI'll give you hints to help you get closer and closer to the correct number.")

def begin(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Guess a number between 1 and 1000: ")
    user_guess=int(Update.message.text)
    if ValueError:
        update.message.reply_text="Please enter a valid number"
    guessing(update,user_guess)

def answer(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Let the game begin! use /begin")

def guessing(update:Update,user_guess):
    choosen_num=random.randint(1,1000)
    flag=True
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
    app = ApplicationBuilder().token("7717735224:AAExIHPzCqKYxFIXs1YPrIyAVwaPCUcZK8I").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("begin", begin))
    app.add_handler(MessageHandler(filters.Text() , answer))

    app.run_polling()

if __name__=='__main__':
    main()