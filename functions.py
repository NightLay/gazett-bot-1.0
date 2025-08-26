
from telebot import types
from config import cnfg, bot, texts, rehost_texts, BOT_LINK, OUR_AD



def work_menu(user_id):

    if user_id != cnfg.MY_ID:
        butn_text = '◀️ написать письмо 📬/◀️ моё портфолио 👤/◀️ позвать друга 👥'
        bot.send_message(user_id, "Я бот помошник редакции \nКаждый читатель здесь на несколько шагов ближе к нам", reply_markup=reply_btn_create(3, butn_text))
    else:
        butn_text = '◀️ читатели 👥/◀️ сообщение всем 📬/◀️ код-пароль-ссылка #️⃣/⏹️ К РЕХОСТУ ТОВЬСЬ ❗️'
        bot.send_message(cnfg.MY_ID, 'Здравия желаю!', reply_markup=reply_btn_create(4, butn_text))



def find_user_num(id_to_seek):
    user_num = 0
    for i in range (0, len(cnfg.users)):
        if cnfg.users[i] == id_to_seek:
            user_num = i
            break
    return(user_num)



def chatting(msg_text, sender_id, sender_name, recipient_id):

    if msg_text == '◀️ написать письмо 📬' and cnfg.MESSAGE_FLAG == False:

        bot.send_message(sender_id, texts[cnfg.TEXT_NUM], reply_markup=reply_btn_create(1, '◀️ отмена ❌'))
        cnfg.MESSAGE_FLAG = True

    elif cnfg.MESSAGE_FLAG == True and msg_text == '◀️ отмена ❌':
        
        bot.send_message(sender_id, "Возвращаю на главный экран")
        bot.send_message(recipient_id, 'Ваше сообщение прочитано 📭\n' + sender_name)

        cnfg.MESSAGE_FLAG = False
        work_menu(sender_id)

    elif cnfg.MESSAGE_FLAG == True:

        btn_text = str(sender_id) + '|' + str(recipient_id)+ '/' +str(sender_id * -1) + '|' + str(recipient_id)
        bot.send_message(recipient_id, texts[cnfg.TEXT_NUM + 2] + msg_text + '\nС уважением, ' + sender_name, reply_markup=inline_btn_create(2, 'ответить ✉️/прочитано 📭', btn_text))
        bot.send_message(sender_id, "Сообщение отправлено ✅")

        cnfg.MESSAGE_FLAG = False
        work_menu(sender_id)



def login(msg_text, user_num):

    if cnfg.QUESTION_NUM == 0:

        cnfg.QUESTION_NUM += 1
        cnfg.names[user_num] = msg_text
        bot.send_message(cnfg.users[user_num], 'Приятно познакомиться, ' + msg_text)
        bot.send_message(cnfg.users[user_num], 'Укажи свой пол', reply_markup=reply_btn_create(2, '◀️ М 🙎‍♂️/◀️ Ж 🙍‍♀️'))

    elif cnfg.QUESTION_NUM == 1:
        if msg_text == '◀️ М 🙎‍♂️':
            cnfg.sexes[user_num] = '♂ М 🙎‍♂️'
        elif msg_text == '◀️ Ж 🙍‍♀️':
            cnfg.sexes[user_num] = '♀ Ж 🙍‍♀️'
        else:
            cnfg.sexes[user_num] = msg_text
        cnfg.QUESTION_NUM += 1
        bot.send_message(cnfg.users[user_num], 'Укажи дату рождения (можно просто месяц и число)', reply_markup=reply_btn_create(1, '-- -- ----'))

    elif cnfg.QUESTION_NUM == 2:

        cnfg.QUESTION_NUM += 1
        cnfg.birthdays[user_num] = msg_text
        bot.send_message(cnfg.users[user_num], 'Вы зарегестрированы! Добро пожаловать!')
        send_chennel_link(cnfg.users[user_num])
        work_menu(cnfg.users[user_num])



def shearling_everyone(msg_text, caht_id):

    if msg_text == '◀️ сообщение всем 📬':
        cnfg.SHEARLING_FLAG = True
        bot.send_message(caht_id, 'Вы выбрали сделать рассылку всем читателям', reply_markup=reply_btn_create(1, '◀️ отменить перессылку ❌'))

    elif cnfg.SHEARLING_FLAG == True and msg_text == '◀️ отменить перессылку ❌':
        bot.send_message(caht_id, 'Вы возвращены в меню')
        work_menu(caht_id)
        cnfg.SHEARLING_FLAG = False

    elif cnfg.SHEARLING_FLAG == True:
        for i in range(0, len(cnfg.users)):
            btn_text = str(cnfg.MY_ID) + '|' + str(cnfg.users[i]) + '/' + str((cnfg.MY_ID) * -1) + '|' + str(cnfg.users[i])
            bot.send_message(cnfg.users[i], 'ВНИМАНИЕ ВНИМАНИЕ!\nСРОЧНОЕ СООБЩЕНИЕ ДЛЯ ВСЕХ ЧИТАТЕЛЕЙ КАНАЛА!\n\n' + msg_text + '\nС уважением, Редакция канала', \
                        reply_markup=inline_btn_create(2, 'ответить ✉️/прочитано 📭', btn_text))

        cnfg.SHEARLING_FLAG = False
        work_menu(caht_id)



def plan_rehost(msg_text, chat_id):

    if msg_text == '⏹️ К РЕХОСТУ ТОВЬСЬ ❗️':
        cnfg.START_REHOST_FLAG = True
        bot.send_message(chat_id, rehost_texts[0])
        bot.send_message(chat_id, '⏹️users: ' + str(cnfg.users) + '\n⏹️names: ' + str(cnfg.names) + '\n⏹️sexes: ' + str(cnfg.sexes) + '\n⏹️birthdays: ' + str(cnfg.birthdays) + \
                    '\n⏹️usernames: ' + str(cnfg.usernames) + '\n⏹️black_list:' + str(cnfg.black_list))
        bot.send_message(chat_id, 'MY_ID = ' + str(cnfg.MY_ID) + '\nCODE = ' + cnfg.CODE + '\nPASSWORD = ' + cnfg.PASSWORD + '\nCHENEL_LINK = ' + cnfg.CHENEL_LINK)
        btn_text = '◀️ продолжить ➡️/◀️ отмена ❌'
        bot.send_message(chat_id, rehost_texts[2], reply_markup=reply_btn_create(2, btn_text))

    elif cnfg.START_REHOST_FLAG == True and msg_text == '◀️ продолжить ➡️':
        for i in range(0, len(cnfg.users)):
            bot.send_message(cnfg.users[i], rehost_texts[3])
        cnfg.REHOST_FLAG = True

    elif cnfg.START_REHOST_FLAG == True and msg_text == '◀️ отмена ❌':
        bot.send_message(chat_id,  rehost_texts[1])
        work_menu(chat_id)



def send_bot_link(user_id):
    global BOT_LINK, OUR_AD

    bot.send_message(user_id, 'Сейчас пришлём тебе сообщение-рекламу нашей канала, под ней будет ссылка на этого бота' \
                + 'Перешлите это сообщение тому, кто хочет вступить в ряды наших читателей, он пройдёт решистрацию и он сможет вступить в канал')
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='бот канала', url=BOT_LINK)
    markup.add(btn)
    bot.send_message(user_id, OUR_AD + '\n————————————————————\n\nМЫ ЖДЁМ ТЕБЯ! ЗАХОДИ (но сначала в бота, так надо)', reply_markup=markup)


def send_chennel_link(user_id):
    global OUR_AD
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='наша газета', url=cnfg.CHENEL_LINK)
    markup.add(btn)
    bot.send_message(user_id, OUR_AD + '\n————————————————————', reply_markup=markup)


def portfolio_check(message, user_num):
    bot.send_message(message.chat.id, '◀️ Имя: ' + cnfg.names[user_num] + '\n◀️ Пол: ' + cnfg.sexes[user_num] + '\n◀️ Дата рождения: ' + cnfg.birthdays[user_num], \
                reply_markup=reply_btn_create(2, '◀️ перепройти регистрацию 📝/◀️ назад в меню ⬅️'))


def change(new, change_val):
    if change_val == cnfg.CODE:
        cnfg.CODE = new
    elif change_val == cnfg.PASSWORD:
        cnfg.PASSWORD = new
    elif change_val == cnfg.CHENEL_LINK:
        cnfg.CHENEL_LINK = new
    bot.send_message(cnfg.MY_ID, 'Изменения успешно применяны')


def reply_btn_create(btn_cnt, btn_text):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, btn_cnt):
        markup.add(types.KeyboardButton(btn_text.split('/')[i]))
    return markup

def inline_btn_create(btn_cnt, btn_text, btn_clbc):
    markup = types.InlineKeyboardMarkup()
    for i in range(0, btn_cnt):
        btn = types.InlineKeyboardButton(text=btn_text.split('/')[i], callback_data=btn_clbc.split('/')[i])
        markup.add(btn)

    return markup
