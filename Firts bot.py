import telebot
from telebot import types

name = ''
surname = ''
age = 0

bot = telebot.TeleBot('5052717622:AAE2Jsyz14xuUPFsGdp5a1dTAPnM6iwLAjk')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	x = 'крокоп', 'Крокоп', 'КРОКОП'
	if message.text in x:
			bot.reply_to(message, 'Мирко Крокоп Филипович - лучший ударник всех времен и народов')
	elif message.text == 'Азаза Аргунов':
		bot.reply_to(message, 'Добрый день, Азаза Аргунов!')
	elif message.text == '/reg':
		bot.send_message(message.from_user.id, 'Хай! Го знакомиться! Назови своё имя!')
		bot.register_next_step_handler(message,reg_name)

def reg_name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, 'А теперь напиши какая у тебя фамилия')
	bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
	global surname
	surname = message.text
	bot.send_message(message.from_user.id, 'Укажи свой возраст')
	bot.register_next_step_handler(message, reg_age)

def reg_age(message):
	global age
	age = message.text
	while age == 0:
		try:
			age = int(message.text)
		except Exception:
			bot.send_message(message.from_user.id, 'Вводи цифрами')

	keyboard = types.InlineKeyboardMarkup()
	key_yes = types.InlineKeyboardButton(text = 'да', callback_data= 'yes')
	keyboard.add(key_yes)
	key_no = types.InlineKeyboardButton(text = 'нет', callback_data= 'no')
	keyboard.add(key_no)
	question = 'Ещё раз глянь. Ты всё верно указал? Тебе ' + str(age) +'лет(года)? И зовут тебя '+ name+' '+ surname+ '?'
	bot.send_message(message.from_user.id, text= question, reply_markup=keyboard)


@bot.callback_query_handler(func= lambda call: True)
def callback_worker(call):
	if call.data == 'yes':
		bot.send_message(call.message.chat.id, 'Отлично. Всё прошло успешно')
	elif call.data == 'no':
		bot.send_message(call.message.chat.id, 'Жалко. Короче, попробуем еще раз')
		bot.send_message(call.message.chat.id, 'Хай, лох! Го знакомиться! Назови своё имя!')
		bot.register_next_step_handler(call.message.chat.id, reg_name)


#bot.reply_to(message, message.text)






bot.infinity_polling()
