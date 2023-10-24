import os
import telebot
from telebot import types
import requests
import json
import logging
import random
from random_word import RandomWords
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from telegram.ext import filters
import sys
import time
import datetime
import re
import threading
#import asyncio
import requests
#import aiohttp
#import aiogram

#_______________________________________________

my_secret = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(my_secret, parse_mode=None)

print('bot started....')
s = time.perf_counter()
elapsed = time.perf_counter() - s

def main():
  # Enable logging
  logging.basicConfig(
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      level=logging.INFO)
  
  logger = logging.getLogger(__name__)
  # logging

  print(logger)
  print(logger.warning)
  print(logger.critical)
  print(logger.exception)
  
  currentDateTime = datetime.datetime.now()
  print(currentDateTime)
  

#___________________ ASYNC AWAIT____________________
  '''async def my_coroutine():
      await asyncio.sleep(15)
      result = datetime.datetime.now()
      print(datetime.datetime.now())
      return result 

  async def mainRoutine():
    
    await asyncio.gather( my_coroutine(),  my_coroutine(),  my_coroutine())

  # call my_async_function
  if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(mainRoutine())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
  
  for x in range(0, 1440):
      t = datetime.datetime.now()
      print(t)
      time.sleep(31)
      del t'''
#________________ASYNC AWAIT____________________
  
#_______________________________________________
  #Inline Keyboard
  @bot.message_handler(commands=['quiz'])
  def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    iron = InlineKeyboardButton(text='buried under my house', callback_data='buried')
    who = InlineKeyboardButton(text='in my room', callback_data='room')
    pops = InlineKeyboardButton(text='in the kitchen', callback_data='kitchen')
    
    markup.add(iron, who, pops)
    bot.send_message(message.chat.id, 'Where is it you thief?!?', reply_markup=markup)
  
  @bot.callback_query_handler(func=InlineKeyboardButton)
  def answer(callback):
      if callback.message:
        if callback.data == 'buried':
          bot.send_message(callback.message.chat.id, 'https://seeklogo.com/images/F/FBI_SHIELD-logo-2D02BDDAC8-seeklogo.com.png')
        elif callback.data == 'room':
          bot.send_message(callback.message.chat.id, "screw youse! ")
        else:
          bot.send_message(callback.message.chat.id, "celebrating pops birthday?")
        

  
  
#____________________________________________________________

  @bot.message_handler(commands=['start', 'hello'])
  def send_welcome(message):
    bot.reply_to(message, "shatap you dumb dweeb")



  
  '''@bot.message_handler(commands=['time'])
  def send_time(message):
    timeDateStr = 'Day: ' + str(timeDateDict['Day']) + " " + 'Time: ' + str(timeDateDict['Hour']) + ':' + str(timeDateDict['Minute']) + ' : ' + str(timeDateDict['Seconds']) 
    bot.reply_to(message, timeDateStr)'''
    
  
  
  @bot.message_handler(commands=['sniffer'])
  def sniffer(message):
    # waits for answer
    randomNum = 0
    randomNum = round(random.uniform(0, 3))
    time.sleep(32.2)
      
    if randomNum <= 1:
      newStr = "This chat is full of mountain sheep at the moment"      
    elif randomNum == 2:
      newStr = "Vern has been detected"           
    else:
      newStr = "various genre of sheep are currently flooding the chat"
  
    #print(randomInherit.run())
    bot.reply_to(message, newStr)
  
  
  @bot.message_handler(commands=["poor"])
  def poor(message):
    bot.reply_to(message, "spent all my life savings to visit Manhattan")
  
  
  @bot.message_handler(commands=["business"])
  def business(message):
    bot.reply_to(message, "this is the business we have chosen")
  
  
  @bot.message_handler(commands=["bridge"])
  def bridge(message):
    bot.reply_to(message, "I shall give me customer full satisfaction")
  
  
  @bot.message_handler(commands=["fifteendollars"])
  def fifteendollars(message):
    bot.reply_to(message,
                 "Alex is a cheap and doesn't clean up after himself")
  
  
  @bot.message_handler(commands=["me"])
  def text_filter2(message):
    bot.send_message(
        message.chat.id,
        "{name} is your friend".format(name=message.from_user.first_name))
  
  
  @bot.message_handler(commands=["grapefruit"])
  def photo(message):
    bot.send_message(
        message.chat.id,
        "https://ak1.ostkcdn.com/images/products/is/images/direct/7511aed92f9de24847683a0e76891e54c19f1ce3/Designart-%27Grapefruit-Infinity-Spiral%27-Modern-Duvet-Cover-Set.jpg"
    )
  
  
  @bot.message_handler(commands=["literallyhitler"])
  def photo(message):
    bot.send_message(message.chat.id, "https://www.hitler-archive.com/design/featured/th-block-44-goring.jpg"
    )
  
  
  @bot.message_handler(commands=["chance"])
  def chance(message):
    percent = str(round(random.uniform(0, 1) * 100))
    bot.send_message(message.chat.id, "There is a " + percent + "%" + " " + message.text)
  
  
  @bot.message_handler(commands=["troll"])
  def troll(message):
    response_API = requests.get('https://insult.mattbas.org/api/insult')
    print(response_API.status_code)
    data = response_API.text
    #print(data)
    #parse_json = json.loads(data)
    bot.reply_to(message, data)
  
  
  @bot.message_handler(commands=["paolotron"])
  def paolotron(message):
    response_API = requests.get(
        'https://evilinsult.com/generate_insult.php?lang=en&type=json')
    print(response_API.status_code)
    array = json.loads(response_API.text)
    #print(array)
    #print(array['insult'])
    #data = response_API.text
    #print(data)
    #parse_json = json.loads(data)
    word = message.text
    scramble = list(word)
    #print(scramble)
    random.shuffle(scramble)
    newphrase = ''.join(scramble)
    #print(newphrase)
    r = RandomWords()
    word_rand = r.get_random_word()
    word_rand2 = r.get_random_word()
  
    bot.reply_to(
        message, newphrase[:5] + "  " + word_rand + "  " + newphrase[5:10] +
        "  " + array['insult'] + " " + word_rand2 + " " + ": my friend ")

  
  
  @bot.message_handler(commands=["dart"])
  def dice(message):
    bot.send_dice(message.chat.id, "🎯")
  
  
  @bot.message_handler(commands=["dice"])
  def dice(message):
    bot.send_dice(message.chat.id)
  
  @bot.message_handler(commands=["ball"])
  def dice(message):
    bot.send_dice(message.chat.id, '⚽')
  
  @bot.message_handler(commands=["poll"])
  def poll(message):
    bot.send_poll(message.chat.id, "Who is the Fed here?", ["Russ", "Fedberg", "Ransom", "Alex"], 30)

  @bot.message_handler(commands=["poll2"])
  def poll2(message):
    bot.send_poll(message.chat.id, "If Vern was a dancer, what would be his stage name?", ["Mulch", "Mr. Furley", "Alex", "2Pack Shugur", "Aunt Bea"], 30)
  
  @bot.message_handler(commands=["nyx"])
  def nyx(message):
    bot.reply_to(message,
                 "Bruh, that lorf got rekt")
 

class Time:
  def __init__(self, hour, minute):
    self.hour = hour
    self.minute = minute

def goodNight():
  for x in range(0, 1440):
    time.sleep(31)
    updateTimeObj = datetime.datetime.now()
    night = Time(updateTimeObj.hour, updateTimeObj.minute)
    if (night.hour == 3 and night.minute == 3):
      bot.send_message(-1001369983015, "Good Night Peeps!")
    time.sleep(31)
    del night
    if x==1440:
      del x

def morning():
  for x in range(0, 1440):
    time.sleep(31)
    updateTimeObj = datetime.datetime.now()
    morning = Time(updateTimeObj.hour, updateTimeObj.minute)
    if (morning.hour == 13 and morning.minute == 0):
      bot.send_message(-1001369983015, "Good Morning fools!")
    time.sleep(31)
    del morning
    if x==1440:
      del x

def test():
  for x in range(0, 1440):
    time.sleep(5)
    updateTimeObj = datetime.datetime.now()
    test = Time(updateTimeObj.hour, updateTimeObj.minute)
    if (test.minute == 56):
      bot.send_message(-681387171, 'test')
    #print(test.minute)
    time.sleep(31)
    del test
    if x==1440:
      del x

def afternoon():
  for x in range(0, 1440):
    #time.sleep(29)
    updateTimeObj = datetime.datetime.now()
    afternoon = Time(updateTimeObj.hour, updateTimeObj.minute)
    if (afternoon.hour == 18 and afternoon.minute == 25):
      bot.send_message(-1001369983015, "test")
    time.sleep(29)
    del afternoon
    if x==1440:
      del x

def question():
  @bot.message_handler(regexp = r"^(//)([a-z0-9]*\s*)*\?")
  def question_me(message):
    ranMsgNumQ = random.randint(0, 7)
    #print(ranMsgNum)
    if ranMsgNumQ == 1:
      #bot.reply_to(message, message.text) echo function
      bot.reply_to(message, "I ask the questions 'round here'")
    elif ranMsgNumQ == 2:
      bot.reply_to(message, "Do I look like a quiz show?")
    elif ranMsgNumQ == 3:
      bot.reply_to(message, "stupid question")
    elif ranMsgNumQ == 4:
      bot.reply_to(message, "You don't ask me, I ask you!")
    elif ranMsgNumQ == 5:
      bot.reply_to(message, "Don't ask me about my business, Kaye")
    elif ranMsgNumQ == 6:
      bot.reply_to(message, "you think you're my interrogator or WHAT?!?!")
    elif ranMsgNumQ == 7:
      bot.reply_to(message, "I don't quizzing no mo', take your questions elsewhere")
    

def screaming():
  @bot.message_handler(regexp = r"^(//)([A-Z0-9]*\s*)*(!$)")
  def all_caps(message):
    ranMsgNumCaps = random.randint(0, 7)
    #print(ranMsgNum)
    if ranMsgNumCaps == 1:
      #bot.reply_to(message, message.text) echo function
      bot.reply_to(message, "what's up there Ms. ALL CAPS")
    elif ranMsgNumCaps == 2:
      bot.reply_to(message, "this ain't AKC & ROK where angry meant something")
    elif ranMsgNumCaps == 3:
      bot.reply_to(message, "quit yelling you freak!!!!!")
    elif ranMsgNumCaps == 4:
      bot.reply_to(message, "why are you screaming like a madman?!?!")
    elif ranMsgNumCaps == 5:
      bot.reply_to(message, "I CAN HEAR YOU !! my violent penguins and cats will mess you up!!")
    elif ranMsgNumCaps == 6:
      bot.reply_to(message, "you must be from a cave")
    elif ranMsgNumCaps == 7:
      bot.reply_to(message, "guaranteed you're from the animal kangdom")
   

def brett_response():
  @bot.message_handler(regexp=r'^(//)([a-z0-9]*\s*)*(\.$)')
  def respond_statement(message):
    ranMsgNum = random.randint(0, 24)
    #print(ranMsgNum)
    if ranMsgNum == 1:
      #bot.reply_to(message, message.text) echo function
      bot.reply_to(message, "dumb")
    elif ranMsgNum == 2:
      bot.reply_to(message, "fake")
    elif ranMsgNum == 3:
      bot.reply_to(message, "are youse talking to me ?")
    elif ranMsgNum == 4:
      bot.reply_to(message, "this!")
    elif ranMsgNum == 5:
      bot.reply_to(message, "whole thing that you said is fake!")
    elif ranMsgNum == 6:
      bot.reply_to(message, "I don't believe any of this nuthin' anymore")
    elif ranMsgNum == 7:
      bot.reply_to(message, "hah?")
    elif ranMsgNum == 8:
      bot.reply_to(message, "I just cannot")
    elif ranMsgNum == 9:
      bot.reply_to(message, "How do you say pina colada in Spanish?")
    elif ranMsgNum == 10:
      bot.reply_to(message, "penguins will mess you up")
    elif ranMsgNum == 11:
      bot.reply_to(message, "thanks for the kind words einstein")
    elif ranMsgNum == 12:
      bot.reply_to(message, "I have nowhere to go")
    elif ranMsgNum == 13:
      bot.reply_to(message, "well, i certainly have no problem with it")
    elif ranMsgNum == 14:
      bot.reply_to(message, "it's not like the old days, when we can do whatever we want")
    elif ranMsgNum == 15:
      bot.reply_to(message, "shatap")
    elif ranMsgNum == 16:
      bot.reply_to(message, "NO")
    elif ranMsgNum == 17:
      bot.reply_to(message, "THAT'S STUPID")
    elif ranMsgNum == 18:
      bot.reply_to(message, "this calls for cat memes")
    elif ranMsgNum == 19:
      bot.reply_to(message, "ypos")
    elif ranMsgNum == 20:
      bot.reply_to(message, "fall into line")
    elif ranMsgNum == 21:
      bot.reply_to(message, "pics or FAKE")
    elif ranMsgNum == 22:
      bot.reply_to(message, "always has been")
    elif ranMsgNum == 23:
      bot.reply_to(message, "which you are free to shut up about")
    elif ranMsgNum == 24:
      bot.reply_to(message, "always makes money for his partners")
   

# creating thread
t1 = threading.Thread(target=main)
t2 = threading.Thread(target=goodNight)
t3 = threading.Thread(target=morning)
t4 = threading.Thread(target=test)
t5 = threading.Thread(target=afternoon)
t6 = threading.Thread(target=question)
t7 = threading.Thread(target=screaming)
t8 = threading.Thread(target=brett_response)  

  
# starting thread 1
t1.start()
# starting thread 2
t2.start()
# starting thread 3
t3.start()
# starting thread 4
t4.start()
# starting thread 5
t5.start()
# starting thread 6
t6.start()
# starting thread 7
t7.start()
# starting thread 8  
t8.start()


# wait until thread 1 is completely executed
#t1.join()
# wait until thread 2 is completely executed
#t2.join()
# wait until thread 3 is completely executed
#t3.join()


#asyncio.run(bot.polling())
bot.infinity_polling()
