#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.corpus import wordnet as wn
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Steps
WORD, POS, ACTION = range(3)
userWord = ""
userPos = ""
userAction = ""
posKeyboard = [['Noun', 'Verb', 'Adjective'],
               ['Adjective-Sattelite', 'Adverb']]
actionKeyboard = [['Synonym', 'Antonym'], ['Definition', 'Example']]


def start(bot, update):
    reply_markup = ReplyKeyboardRemove()
    update.message.reply_text(
        "Welcome, please type your word.", reply_markup=reply_markup)
    return WORD


def word(bot, update):
    user = update.message.from_user
    global userWord
    userWord = update.message.text
    if wn.synsets(userWord):
        logger.info("%s said %s" % (user.first_name, update.message.text))
        reply_markup = ReplyKeyboardMarkup(posKeyboard, True)
        update.message.reply_text(
            'Choose part of speech', reply_markup=reply_markup)
        return POS

    else:
        logger.info("%s said %s" % (user.first_name, update.message.text))
        reply_markup = ReplyKeyboardRemove()
        update.message.reply_text(
            'Unknown word. Please enter a known word', reply_markup=reply_markup)
        return WORD


def pos(bot, update):
    user = update.message.from_user
    global userPos
    if update.message.text == "Noun":
        userPos = 'n'
        wordWithPos = '{}.{}.01'.format(userWord, userPos)
        try:
            wn.synset(wordWithPos)
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(actionKeyboard, True)
            update.message.reply_text(
                "What do you want to do?", reply_markup=reply_markup)
            return ACTION
        except:
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(posKeyboard, True)
            update.message.reply_text(
                "Enter valid part of speech for this word.", reply_markup=reply_markup)
            return POS

    elif update.message.text == "Verb":
        userPos = 'v'
        wordWithPos = '{}.{}.01'.format(userWord, userPos)
        try:
            wn.synset(wordWithPos)
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(actionKeyboard, True)
            update.message.reply_text(
                "What do you want to do?", reply_markup=reply_markup)
            return ACTION
        except:
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(posKeyboard, True)
            update.message.reply_text(
                "Enter valid part of speech for this word.", reply_markup=reply_markup)
            return POS

    elif update.message.text == "Adjective":
        userPos = 'a'
        wordWithPos = '{}.{}.01'.format(userWord, userPos)
        try:
            wn.synset(wordWithPos)
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(actionKeyboard, True)
            update.message.reply_text(
                "What do you want to do?", reply_markup=reply_markup)
            return ACTION
        except:
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(posKeyboard, True)
            update.message.reply_text(
                "Enter valid part of speech for this word.", reply_markup=reply_markup)
            return POS

    elif update.message.text == "Adjective-Sattelite":
        userPos = 's'
        wordWithPos = '{}.{}.01'.format(userWord, userPos)
        try:
            wn.synset(wordWithPos)
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(actionKeyboard, True)
            update.message.reply_text(
                "What do you want to do?", reply_markup=reply_markup)
            return ACTION
        except:
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(posKeyboard, True)
            update.message.reply_text(
                "Enter valid part of speech for this word.", reply_markup=reply_markup)
            return POS

    elif update.message.text == "Adverb":
        userPos = 'r'
        wordWithPos = '{}.{}.01'.format(userWord, userPos)
        try:
            wn.synset(wordWithPos)
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(actionKeyboard, True)
            update.message.reply_text(
                "What do you want to do?", reply_markup=reply_markup)
            return ACTION
        except:
            logger.info("%s said %s" % (user.first_name, update.message.text))
            reply_markup = ReplyKeyboardMarkup(posKeyboard, True)
            update.message.reply_text(
                "Enter valid part of speech for this word.", reply_markup=reply_markup)
            return POS

    else:
        logger.info("%s said %s" % (user.first_name, update.message.text))
        reply_markup = ReplyKeyboardMarkup(posKeyboard, True)
        update.message.reply_text(
            "Enter valid part of speech", reply_markup=reply_markup)
        return POS


def action(bot, update):
    user = update.message.from_user
    global userAction
    wordWithPos = '{}.{}.01'.format(userWord, userPos)
    syns = wn.synsets(userWord, pos=userPos)
    synsList = []
    antsList = []
    custom_keyboard = [['Synonym', 'Antonym'],
                       ['Definition', 'Example'], ['New Word']]
    for syn in syns:
        for l in syn.lemmas():
            synsList.append(l.name())
            if l.antonyms():
                antsList.append(l.antonyms()[0].name())

    if update.message.text == "Synonym":
        userAction = 'Synonym'
        logger.info("%s said %s" % (user.first_name, update.message.text))
        reply_markup = ReplyKeyboardMarkup(custom_keyboard, True)
        if synsList:
            update.message.reply_text(synsList, reply_markup=reply_markup)
            return ACTION
        else:
            update.message.reply_text(
                "There isn't any synonym for this word.", reply_markup=reply_markup)
            return ACTION

    elif update.message.text == "Antonym":
        userAction = 'Antonym'
        logger.info("%s said %s" % (user.first_name, update.message.text))
        reply_markup = ReplyKeyboardMarkup(custom_keyboard, True)
        if antsList:
            update.message.reply_text(antsList, reply_markup=reply_markup)
            return ACTION
        else:
            update.message.reply_text(
                "There isn't any antonym for this word.", reply_markup=reply_markup)
            return ACTION

    elif update.message.text == "Definition":
        userAction = "Definition"
        logger.info("%s said %s" % (user.first_name, update.message.text))
        definition = wn.synset(wordWithPos).definition()
        reply_markup = ReplyKeyboardMarkup(custom_keyboard, True)
        if definition:
            update.message.reply_text(definition, reply_markup=reply_markup)
            return ACTION
        else:
            update.message.reply_text(
                "There isn't any definition for this word.", reply_markup=reply_markup)
            return ACTION

    elif update.message.text == "Example":
        userAction = "Example"
        logger.info("%s said %s" % (user.first_name, update.message.text))
        reply_markup = ReplyKeyboardMarkup(custom_keyboard, True)
        examples = wn.synset(wordWithPos).examples()
        if examples:
            update.message.reply_text(examples, reply_markup=reply_markup)
            return ACTION
        else:
            update.message.reply_text(
                "There isn't any example for this word.", reply_markup=reply_markup)
            return ACTION

    else:
        logger.info("%s said %s" % (user.first_name, update.message.text))
        reply_markup = ReplyKeyboardRemove()
        update.message.reply_text(
            "Please type your word.", reply_markup=reply_markup)
        return WORD


def anyText(bot, update):
    user = update.message.from_user
    logger.info("%s said %s" % (user.first_name, update.message.text))
    reply_markup = ReplyKeyboardRemove()
    update.message.reply_text('Please /start',
                              reply_markup=reply_markup)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Unknown Command")


def cancel(bot, update):
    user = update.message.from_user
    logger.info("%s canceled the bot." % user.first_name)
    reply_markup = ReplyKeyboardRemove()
    update.message.reply_text('Ok bye.', reply_markup=reply_markup)
    return ConversationHandler.END


def error(bot, update, error):
    logger.warn('Update: "%s", Error: "%s"' % (update, error))


def main():
    updater = Updater("Token")

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            WORD: [MessageHandler(Filters.text, word)],
            POS: [MessageHandler(Filters.text, pos)],
            ACTION: [MessageHandler(Filters.text, action)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)

    any_handler = MessageHandler(Filters.text, anyText)
    dp.add_handler(any_handler)

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
    updater.stop()


if __name__ == "__main__":
    main()
