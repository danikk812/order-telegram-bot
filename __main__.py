from datetime import date
import telebot
from telebot import types
import gspread
import re

bot_token = '5168334430:AAEnD0lZzV630lsp7j1Q96BJMEYvs0FMTQI'
googlesheet_id = '1NVPV33NVPoPFR8NwXsN4KxqbpHAqqiTphqga1YtemFA'
bot = telebot.TeleBot(bot_token)
gc = gspread.service_account()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Здравствуйте! Для дальнейшего общения с Вами напишите пожалуйста ФИО")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    global surname, name, faz, theme, number, t, addit

    if message.text == 'Разработка решений' or message.text == 'Дизайн/UX/UI/Mobile' or \
            message.text == 'Разработка CRM и ERP' or message.text == 'Анализ, поддержка' or \
            message.text == '📩 Оставить заявку':

        if message.text == 'Разработка решений':
            keyboard = types.InlineKeyboardMarkup()
            key_a = types.InlineKeyboardButton(text='Создание сайтов на 1С-Битрикс', callback_data='a')
            key_b = types.InlineKeyboardButton(text='Создание интернет-магазинов', callback_data='b')
            key_c = types.InlineKeyboardButton(text='Обмен данными с 1С интернет-магазинов', callback_data='c')
            key_d = types.InlineKeyboardButton(text='Мобильные адаптивные сайты', callback_data='d')
            key_e = types.InlineKeyboardButton(text='Мобильные приложения', callback_data='e')
            key_j = types.InlineKeyboardButton(text='Готовые сайты и магазины', callback_data='j')
            key_h = types.InlineKeyboardButton(text='Разработка сайтов на wordpress', callback_data='h')
            key_k = types.InlineKeyboardButton(text='Разработка python/Django', callback_data='k')
            key_l = types.InlineKeyboardButton(text='Гранты Европейского банка', callback_data='l')
            keyboard.add(key_a)
            keyboard.add(key_b)
            keyboard.add(key_c)
            keyboard.add(key_d)
            keyboard.add(key_e)
            keyboard.add(key_j)
            keyboard.add(key_h)
            keyboard.add(key_k)
            keyboard.add(key_l)
            bot.send_message(message.from_user.id, text='Что делаем?', reply_markup=keyboard)
            theme = message.text

        elif message.text == 'Дизайн/UX/UI/Mobile':
            keyboard = types.InlineKeyboardMarkup()
            key_a = types.InlineKeyboardButton(text='Дизайн-концепции сайтов', callback_data='aa')
            key_b = types.InlineKeyboardButton(text='Дизайн интернет-магазинов', callback_data='bb')
            key_c = types.InlineKeyboardButton(text='Разработка графики', callback_data='cc')
            key_d = types.InlineKeyboardButton(text='Прототипы UX, UI, mobile', callback_data='dd')
            key_e = types.InlineKeyboardButton(text='Креативные дизайн решения', callback_data='ee')
            key_j = types.InlineKeyboardButton(text='Дизайн контента корпоративных сайтов', callback_data='jj')
            key_h = types.InlineKeyboardButton(text='Дизайн мобильных приложений', callback_data='hh')
            key_k = types.InlineKeyboardButton(text='Адаптивный дизайн сайтов', callback_data='kk')
            key_l = types.InlineKeyboardButton(text='Адаптивная верстка HTML5', callback_data='ll')
            key_m = types.InlineKeyboardButton(text='Фирменный стиль и логотипы', callback_data='mm')
            keyboard.add(key_a)
            keyboard.add(key_b)
            keyboard.add(key_c)
            keyboard.add(key_d)
            keyboard.add(key_e)
            keyboard.add(key_j)
            keyboard.add(key_h)
            keyboard.add(key_k)
            keyboard.add(key_l)
            keyboard.add(key_m)
            bot.send_message(message.from_user.id, text='Что будем смотреть?', reply_markup=keyboard)
            theme = message.text

        elif message.text == "Разработка CRM и ERP":
            keyboard = types.InlineKeyboardMarkup()
            key_a = types.InlineKeyboardButton(text='Разработка и кастомизация Odoo', callback_data='aaa')
            key_b = types.InlineKeyboardButton(text='Разработка модулей Odoo', callback_data='bbb')
            key_c = types.InlineKeyboardButton(text='Автоматизация бизнес-процессов', callback_data='ccc')
            key_d = types.InlineKeyboardButton(text='Внедрение Odoo ecommerce', callback_data='ddd')
            key_e = types.InlineKeyboardButton(text='Разработка приложений Bitrix24', callback_data='eee')
            key_j = types.InlineKeyboardButton(text='Автоматизация процессов с Bitrix24', callback_data='jjj')
            key_h = types.InlineKeyboardButton(text='Корпоративный портал Bitrix24', callback_data='hhh')
            key_k = types.InlineKeyboardButton(text='Кастомизация CRM Bitrix24', callback_data='kkk')
            keyboard.add(key_a)
            keyboard.add(key_b)
            keyboard.add(key_c)
            keyboard.add(key_d)
            keyboard.add(key_e)
            keyboard.add(key_j)
            keyboard.add(key_h)
            keyboard.add(key_k)
            bot.send_message(message.from_user.id, text='Что добавим?', reply_markup=keyboard)
            theme = message.text

        elif message.text == "Анализ, поддержка":
            keyboard = types.InlineKeyboardMarkup()
            key_a = types.InlineKeyboardButton(text='Наполнение каталога продукцией', callback_data='aaaa')
            key_b = types.InlineKeyboardButton(text='QA тестирование и аудит сайта', callback_data='bbbb')
            key_c = types.InlineKeyboardButton(text='Техническая поддержка и доработка Bitrix', callback_data='cccc')
            key_d = types.InlineKeyboardButton(text='Техническая поддержка X4.cms', callback_data='dddd')
            key_e = types.InlineKeyboardButton(text='Техническая поддержка Django', callback_data='eeee')
            key_j = types.InlineKeyboardButton(text='Техническая поддержка wordpress', callback_data='jjjj')
            key_h = types.InlineKeyboardButton(text='Техническая поддержка woocommerce', callback_data='hhhh')
            keyboard.add(key_a)
            keyboard.add(key_b)
            keyboard.add(key_c)
            keyboard.add(key_d)
            keyboard.add(key_e)
            keyboard.add(key_j)
            keyboard.add(key_h)
            sent = bot.send_message(message.from_user.id, text='Что добавим?', reply_markup=keyboard)
            theme = message.text

        elif message.text == '📩 Оставить заявку':
            t = message.text
            bot.send_message(message.chat.id, text='Что бы Вы хотели узнать? Напишите нам!')
        else:
            theme = message.text
            bot.send_message(message.chat.id, text='Спасибо за уточнение! Оставьте пожалуйста Ваш номер телефона '
                                                   'для дальнейшей связи с Вами в формате +************')
    elif message.text[0] == '+':
        a = None

        while a == None:
            a = re.match(r'^(\+375|80)(29|25|44|33)(\d{3})(\d{2})(\d{2})$', message.text)
        number = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Выход')
        markup.add(back)
        bot.send_message(message.chat.id, text='Спасибо! \nНажмите пожалуйста кнопку выход для записи данных и если '
                                               'желаете начать переписку заново - нажмите /start', reply_markup=markup)

    elif message.text == 'Хочу заказать эту услугу':
        bot.send_message(message.chat.id, text='Оставьте пожалуйста Ваш номер телефона '
                                               'для дальнейшей связи с Вами в формате +************')

    elif message.text == 'Выход':
        today = date.today().strftime("%d.%m.%Y")
        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([today, surname + ' ' + name + ' ' + faz, theme, addit, number])

    elif t == '📩 Оставить заявку':
        theme = message.text
        t = ''
        bot.send_message(message.chat.id, text='Спасибо за уточнение! Оставьте пожалуйста Ваш номер телефона для'
                                               ' дальнейшей связи с Вами в формате +************')

    else:
        try:
            surname, name, faz = message.text.split(" ", 2)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            b1 = types.KeyboardButton('Разработка решений')
            b2 = types.KeyboardButton('Дизайн/UX/UI/Mobile')
            b3 = types.KeyboardButton('Разработка CRM и ERP')
            b4 = types.KeyboardButton('Анализ, поддержка')
            b5 = types.KeyboardButton('📩 Оставить заявку')
            markup.add(b1)
            markup.add(b2)
            markup.add(b3)
            markup.add(b4)
            markup.add(b5)
            bot.send_message(message.chat.id, text=f'Приятно познакомиться, {name} {faz}! Что бы вы хотели заказать?',
                             reply_markup=markup)

        except:
            bot.send_message(message.chat.id, text='Некорректный ввод')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global addit
    if call.data == "a":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Создание сайтов на 1С-Битрикс"

    elif call.data == "b":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Создание интернет-магазинов"

    elif call.data == "c":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Обмен данными с 1С интернет-магазинов"

    elif call.data == "d":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Мобильные адаптивные сайты"

    elif call.data == "e":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Мобильные приложения"

    elif call.data == "j":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Готовые сайты и магазины"

    elif call.data == "h":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Разработка сайтов на wordpress"

    elif call.data == "k":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Разработка python/Django"

    elif call.data == "l":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Гранты Европейского банка"

    elif call.data == "aa":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Дизайн-концепции сайтов"

    elif call.data == "bb":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Дизайн интернет-магазинов"

    elif call.data == "cc":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Разработка графики"

    elif call.data == "dd":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Прототипы UX, UI, mobile"

    elif call.data == "ee":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Креативные дизайн решения"

    elif call.data == "jj":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Дизайн контента корпоративных сайтов"

    elif call.data == "hh":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Дизайн мобильных приложений"

    elif call.data == "kk":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Адаптивный дизайн сайтов"

    elif call.data == "ll":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Адаптивная верстка HTML5"

    elif call.data == "mm":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Фирменный стиль и логотипы"

    elif call.data == "aaa":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Разработка и кастомизация Odoo"

    elif call.data == "bbb":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Разработка модулей Odoo"

    elif call.data == "ccc":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Автоматизация бизнес-процессов"

    elif call.data == "ddd":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Внедрение Odoo ecommerce"

    elif call.data == "eee":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Разработка приложений Bitrix24"

    elif call.data == "jjj":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Автоматизация процессов с Bitrix24"

    elif call.data == "hhh":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Корпоративный портал Bitrix24"

    elif call.data == "kkk":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Кастомизация CRM Bitrix24"

    elif call.data == "aaaa":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Наполнение каталога продукцией"

    elif call.data == "bbbb":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "QA тестирование и аудит сайта"

    elif call.data == "cccc":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Техническая поддержка и доработка Bitrix"

    elif call.data == "dddd":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Техническая поддержка X4.cms"

    elif call.data == "eeee":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Техническая поддержка Django"

    elif call.data == "jjjj":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Техническая поддержка wordpress"

    elif call.data == "hhhh":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу заказать эту услугу")
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Оставьте заявку на звонок:)", reply_markup=markup)
        addit = "Техническая поддержка woocommerce"

    else:
        bot.send_message(call.message.chat.id, text="На такую комманду я не запрограммирован..")


addit = ''
t = ''
name = ''
surname = ''
faz = ''
theme = ''
number = ''


bot.polling()