import time, datetime

import RPi.GPIO as GPIO

import telepot

from telepot.loop import MessageLoop

led = 18

now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

 #LED

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 0) #Off initially

def action(msg):

    chat_id = msg['chat']['id']

    command = msg['text']

    print ('Received: %s' % command)

    if 'prende la' in command:

        message = "Luz "

        if 'luz' in command:

            message = message + "."

            GPIO.output(led, 1)

            telegram_bot.sendMessage (chat_id, message)

 

    if 'apaga la' in command:

        message = "Oscuridad "

        if 'luz' in command:

            message = message + ". "

            GPIO.output(led, 0)        

        telegram_bot.sendMessage (chat_id, message)
        
    if 'centella la' in command:

        message = "la planilla va a subir"

        if 'luz' in command:

            message = message + ". "

            while True:
            
               if "ap" in command:
                   break 
               time.sleep(5)
               GPIO.output(18, True)
               time.sleep(1)
               GPIO.output(18, False)
               time.sleep(1)    
               
               

        telegram_bot.sendMessage (chat_id, message)
    

telegram_bot = telepot.Bot('1149772657:AAHoVSU8AL0TU_Y25to4JApgyGJNEwxWiJM')

print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()

print ('Up and Running....')

while 1:

    time.sleep(10)
