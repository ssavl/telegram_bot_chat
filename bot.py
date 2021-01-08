from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import random
from config import token, questions
from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove






def main_keybord():
    return ReplyKeyboardMarkup(
         [
         ['Следующий вопрос'],
         ['Поддержать проект 💸'],
         ]
    )


def donation():
    update.message.reply_text('😂')


def talk_to_me(update, context):
    user_text = str(update.message.text).lower()
    quest = random.choice(questions)
    print(user_text)
    if user_text == 'следующий вопрос':
        update.message.reply_text(quest)
    if user_text == 'вопрос':
        update.message.reply_text(quest)
    if user_text == 'поддержать проект 💸':
        update.message.reply_text(f'💳 Qiwi кошелек для оплаты Никнейм: BATOL249       💳 Яндекс кошелек (ЮMoney)'
                                  '4100116346136331', reply_markup=main_keybord())
    if user_text != 'qwerty' or 'следующий вопрос' or 'вопрос' or 'поддержать проект 💸':
        update.message.reply_text('Чтобы получить вопрос просто напиши "Следующий вопрос"')


def talk_talk_talk(update, context):
    user_text = str(update.message.text).lower()
    if user_text == 'qwerty':
        update.message.reply_text('quest')

# else:
    #     update.message.reply_text('Чтобы получить вопрос просто напиши "Следующий вопрос"')
    #     pass


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text(f'😁 Привет! Я - бот игры chat, я умею задавать разные интересные вопросы. '
                              'Просто напиши мне "Вопрос" и увидишь все сам 💁🏼‍♀️', reply_markup=main_keybord())


def main():
    mybot = Updater(token, use_context=True)
    md = mybot.dispatcher
    md.add_handler(CommandHandler("start", greet_user))
    # md.add_handler(MessageHandler(Filters.text, talk_talk_talk))
    md.add_handler(MessageHandler(Filters.text, talk_to_me))
    md.add_handler(CommandHandler("time", donation))
    print('starting...')
    mybot.start_polling()
    mybot.idle()



if __name__ == "__main__":
    main()
