import telebot
import random

bot_token = input(' Enter Your Token Bot TeleGram : » ')


bot = telebot.TeleBot(bot_token)
print(' \n\n      Running Bot /start ')
bot.set_my_commands([telebot.types.BotCommand("/start", "🤖 لبدء البوت"),telebot.types.BotCommand("/song", "لعرض الاغاني")])

@bot.message_handler(commands=['start'])
def start(message):
    t = '''
اهلا بك عزيزي في بوت الاغاني 
طريقه تشغيل البوت سهله جداا

فقط قم بضغط /song
سوف يعطيك اغنيه جديده
كل مره تقوم بلضغط عل /song
يعطيك اغنيه مختلفه 🔊🎶

تواصل @PY_87 ♡♡ @llxxx3

'''
    bot.send_message(message.chat.id, t)
    


songs = [
'https://t.me/llxxxv/105','https://t.me/PY_34/36?single', 'https://t.me/PY_34/37?single', 'https://t.me/PY_34/38?single', 'https://t.me/PY_34/38?single', 'https://t.me/PY_34/39?single', 'https://t.me/PY_34/40?single','https://t.me/PY_34/41?single', 'https://t.me/PY_34/42?single', 'https://t.me/PY_34/43?single', 'https://t.me/PY_34/44?single', 'https://t.me/PY_34/45?single', 'https://t.me/PY_34/46?single', 'https://t.me/PY_34/47?single', 'https://t.me/PY_34/48?single', 'https://t.me/PY_34/49?single', 'https://t.me/PY_34/50?single', 'https://t.me/PY_34/51?single', 'https://t.me/PY_34/51?single', 'https://t.me/PY_34/52?single', 'https://t.me/PY_34/53?single', 'https://t.me/PY_34/54?single', 'https://t.me/PY_34/55?single', 'https://t.me/PY_34/56?single', 'https://t.me/PY_34/57?single', 'https://t.me/PY_34/58?single', 'https://t.me/PY_34/59?single', 'https://t.me/PY_34/60?single', 'https://t.me/PY_34/61?single', 'https://t.me/PY_34/62?single'
]

@bot.message_handler(commands=['song'])
def send_random_song(message):
    
    random_song = random.choice(songs)
    te = '''
هذه اجمل الاغاني العراقيه 🎶
عنقريب سيتم اضافه لمزيد 🎵
__

حسناا اضغط /song مره اخرى لجلب اغنيه🎶 جديده 🎵
__

@PY_87 ♡♡ @llxxx3

'''
    bot.send_audio(message.chat.id, random_song,te)

bot.polling()