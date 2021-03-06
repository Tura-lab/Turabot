from telegram.ext import Updater, CommandHandler
import logging
import os, sys, re
import string
import random
import requests
from functools import partial
import time
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from telegram.ext import MessageHandler, Filters

TOKEN = '957266795:AAHewWLVfyyAYhHMAOPP9zukcT9AENWwrqc'



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,level=logging.INFO)

def start(update, context):

	context.bot.send_message(chat_id=update.message.chat_id, text="Hello!! Search anything and this bot will send you the image \n Thank You!!" , timeout = 5.0)


def send(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text= "searching for " + str(update.message.text))
    
    USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    headers = { 'User-Agent': USER_AGENT }
    
    query = update.message.text
    query_key = query.replace(' ','+')
    
    tgt_url = 'https://www.google.com.sg/search?q={}&tbm=isch&tbs=sbd:0'.format(query_key)
    
    r = requests.get(tgt_url, headers = headers)
    
    urllist = [n for n in re.findall('"ou":"([a-zA-Z0-9_./:-]+.(?:jpg|jpeg|png))",', r.text)]
    if len(urllist)==0:
    	context.bot.send_message(chat_id=update.message.chat_id, text= "Sorry...I could not find any picturs..\nPlease try again..")
    else:
    	num=random.randint(0,len(urllist))
    	chat_id=update.message.chat_id
    	pic=urllist[num]
    	context.bot.send_photo(chat_id, pic)
 

def main():
	
	updater = Updater(token = '957266795:AAHewWLVfyyAYhHMAOPP9zukcT9AENWwrqc', use_context=True)


	dispatcher = updater.dispatcher
	send_handler = MessageHandler(Filters.text, send)
	dispatcher.add_handler(send_handler)


	start_handler = CommandHandler('start', start)
	dispatcher.add_handler(start_handler)
	updater.start_polling()
	updater.idle()

	
if __name__=="__main__":
	main()
