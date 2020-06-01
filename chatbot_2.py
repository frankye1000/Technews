import requests
from datetime import date
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler


def CrawlUrl(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    t = soup.select("td.maintitle > h1.entry-title > a")
    newest5 = [i.get("href") for i in t[:5]]
    return newest5


def Commands(update, context):
    if update.message.text=='/component':
        newest5 = CrawlUrl("https://technews.tw/category/component/")
        for text in newest5:
            update.message.reply_text(text)
        update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/component/")


    if update.message.text=='/mobiledevice':
        newest5 = CrawlUrl("https://technews.tw/category/mobiledevice/")
        for text in newest5:
            update.message.reply_text(text)
        update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/mobiledevice/")


    if update.message.text=='/internet':
        newest5 = CrawlUrl("https://technews.tw/category/internet/")
        for text in newest5:
            update.message.reply_text(text)
        update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/internet/")


    if update.message.text=='/ai':
        newest5 = CrawlUrl("https://technews.tw/category/ai/")
        for text in newest5:
            update.message.reply_text(text)
        update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/ai/")


    if update.message.text=='/cuttingedge':
        newest5 = CrawlUrl("https://technews.tw/category/cutting-edge/")
        for text in newest5:
            update.message.reply_text(text)
        update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/cutting-edge/")


    if update.message.text=='/biotech':
        newest5 = CrawlUrl("https://technews.tw/category/biotech/")
        for text in newest5:
            update.message.reply_text(text)
        update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/biotech/")


    if update.message.text=='/finance':
        newest5 = CrawlUrl("https://finance.technews.tw/")
        for text in newest5:
            update.message.reply_text(text)
        update.message.reply_text("預知更多最新新聞，請參考:\nhttps://finance.technews.tw/")


def Broadcast(updater):
    title = "   {} 科技新報   \n".format(date.today())
    updater.bot.sendMessage(chat_id="1093911183", text=title)

    newest5 = CrawlUrl("https://technews.tw/")
    for text in newest5:
        updater.bot.sendMessage(chat_id="chatid", text=text)
        updater.bot.sendMessage(chat_id="chatid", text=text)


if __name__ == '__main__':
    token = "your token"
    updater = Updater(token=token, use_context=True)

    #commands
    updater.dispatcher.add_handler(CommandHandler("component", Commands))
    updater.dispatcher.add_handler(CommandHandler("mobiledevice", Commands))
    updater.dispatcher.add_handler(CommandHandler("internet", Commands))
    updater.dispatcher.add_handler(CommandHandler("ai", Commands))
    updater.dispatcher.add_handler(CommandHandler("cuttingedge", Commands))
    updater.dispatcher.add_handler(CommandHandler("biotech", Commands))
    updater.dispatcher.add_handler(CommandHandler("finance", Commands))

    #broadcast
    scheduler = BackgroundScheduler()
    scheduler.add_job(Broadcast, 'cron', day_of_week='1-6', hour=18, minute=00, args=(updater,))
    # scheduler.add_job(Broadcast, 'interval', seconds=30, args=(updater,))
    scheduler.start()

    updater.start_polling()
    updater.idle()
