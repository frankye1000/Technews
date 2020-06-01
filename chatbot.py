import time
import requests
from bs4 import BeautifulSoup
from random import randint
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def ugly():
    uglys = ['https://i.imgur.com/9ybYuTv.png',
             'https://i.imgur.com/iwMkwW3.png',
             'https://pbs.twimg.com/media/CHq_LB7UsAE0iVZ.jpg']
    ugly = uglys[randint(0, len(uglys) - 1)]

    return ugly


def url():
    payload = {
        'from': 'from: /bbs/Beauty/index.html',
        'yes': 'yes'
    }
    rs = requests.session()
    res = rs.post('https://www.ptt.cc/ask/over18', data=payload)
    res = rs.get('https://www.ptt.cc/bbs/Beauty/index.html')
    soup = BeautifulSoup(res.text, 'html5lib')
    domain = 'https://www.ptt.cc'
    t = soup.select('div.r-ent > div.title > a')
    urls = [domain + a.get('href') for a in t]
    url = urls[randint(0, len(urls) - 5)]

    return url


def want(bot, update):
    a, b = randint(1, 100), randint(1, 100)
    update.message.reply_text('{} + {} = ?'.format(a, b),
                              reply_markup=InlineKeyboardMarkup([[
                                  InlineKeyboardButton(str(s), callback_data='{} {} {}'.format(a, b, s)) for s in
                                  range(a + b - randint(1, 3), a + b + randint(1, 3))
                              ]]))
    print(update.message.from_user.full_name)


def answer(bot, update):
    a, b, s = [int(x) for x in update.callback_query.data.split()]
    if a + b == s:
        update.callback_query.edit_message_text('你答對了！ 就大發慈悲給你這個小雞雞看正妹!')
        update.callback_query.edit_message_text(url())
    else:
        update.callback_query.edit_message_text('你答錯囉！ 我要逞罰你!')
        update.callback_query.edit_message_text(ugly())


updater = Updater('your token')

updater.dispatcher.add_handler(CommandHandler('want', want))
updater.dispatcher.add_handler(CallbackQueryHandler(answer))

updater.start_polling()
updater.idle()