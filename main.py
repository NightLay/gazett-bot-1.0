

from config import cnfg, bot, texts
from functions import reply_btn_create, work_menu, find_user_num, login, chatting, portfolio_check, send_bot_link, shearling_everyone, change, plan_rehost, inline_btn_create



@bot.message_handler(commands=['start'])
def greeting(message):
    chat_id = message.chat.id

    if chat_id != cnfg.MY_ID:

        if not chat_id in cnfg.users:
            cnfg.users.append(chat_id)
            cnfg.names.append('-')
            cnfg.sexes.append('-')
            cnfg.birthdays.append('-')
            cnfg.usernames.append('@' + message.from_user.username)

            bot.send_message(cnfg.MY_ID, '@' + message.from_user.username + ' запустил(а) бота')
            bot.send_message(chat_id, 'Добро пожаловать в нашего бота', reply_markup=reply_btn_create(2, '◀️ зарегистрироваться 📝/◀️ войти без регистрации ❌'))
        else:
            bot.send_message(chat_id, 'Добро пожаловать в нашего бота')
            work_menu(chat_id)



@bot.message_handler(content_types=['text'])
def message_checking(message):
    chat_id = message.chat.id
    msg_text = message.text

    if chat_id != cnfg.MY_ID and cnfg.REHOST_FLAG == False and not chat_id in cnfg.black_list:
        user_num = find_user_num(chat_id)

        if msg_text == cnfg.CODE:
            cnfg.COMMANDER_FLAG = True
        elif cnfg.COMMANDER_FLAG == True and msg_text == cnfg.PASSWORD:
            cnfg.COMMANDER_FLAG = False
            cnfg.MY_ID = chat_id
            work_menu(chat_id)

        elif msg_text == '◀️ зарегистрироваться 📝' or msg_text == '◀️ перепройти регистрацию 📝':
            bot.send_message(chat_id, 'Напиши своё имя или никнейм', reply_markup=reply_btn_create(1, message.from_user.first_name))
            cnfg.QUESTION_NUM = 0
        elif msg_text == '◀️ войти без регистрации ❌':
            work_menu(chat_id)

        elif cnfg.QUESTION_NUM != 3:
            login(msg_text, user_num)

        elif msg_text == '◀️ написать письмо 📬' or cnfg.MESSAGE_FLAG == True:
            cnfg.TEXT_NUM = 0
            chatting(msg_text, cnfg.users[user_num], cnfg.names[user_num], cnfg.MY_ID)
            (user_num)

        elif msg_text == '◀️ моё портфолио 👤':
            portfolio_check(message, user_num)

        elif msg_text == '◀️ позвать друга 👥':
            send_bot_link(chat_id)

        elif msg_text == '◀️ назад в меню ⬅️':
            work_menu(chat_id)

        else:
            bot.send_message(chat_id, 'Команда не распознана, вы возвращены в меню')
            work_menu(chat_id)

    elif chat_id == cnfg.MY_ID and cnfg.REHOST_FLAG == False:

        if cnfg.MESSAGE_FLAG == True:
            chatting(msg_text, chat_id, 'Редакция канала', cnfg.PERS_ID)
        elif msg_text == '◀️ читатели 👥':

            for i in range(0, len(cnfg.users)):
                if not cnfg.users[i] in cnfg.black_list:
                    btn_text = 'написать/забанить'
                    btn_callback = str(cnfg.users[i]) + '|' + str(chat_id * (-1)) + '/block|' + str(cnfg.users[i])
                    bot.send_message(chat_id, '⏹️' + str(i) + '\n-ID: ' + str(cnfg.users[i]) + '\n-Имя: ' + cnfg.names[i] + '\n-Пол: ' + cnfg.sexes[i] + \
                                '\n-Дата рождения: ' + cnfg.birthdays[i] + '\n-Телеграм: ' + cnfg.usernames[i], reply_markup=inline_btn_create(2, btn_text, btn_callback))
                else:
                    btn_text = 'написать/разбанить'
                    btn_callback = str(cnfg.users[i]) + '|' + str(chat_id * (-1)) + '/unblock|' + str(cnfg.users[i])
                    bot.send_message(chat_id, '🚫БАН\n⏹️' + str(i) + '\n-ID: ' + str(cnfg.users[i]) + '\n-Имя: ' + cnfg.names[i] + '\n-Пол: ' + cnfg.sexes[i] + \
                                '\n-Дата рождения: ' + cnfg.birthdays[i] + '\n-Телеграм: ' + cnfg.usernames[i], reply_markup=inline_btn_create(2, btn_text, btn_callback))
            work_menu(chat_id)

        elif msg_text == '◀️ сообщение всем 📬' or cnfg.SHEARLING_FLAG == True:
            shearling_everyone(msg_text, chat_id)

        elif msg_text == '◀️ код-пароль-ссылка #️⃣':
            butn_text = '◀️ изменить код 🔄/◀️ сменить пароль 🔄/◀️ сменить ссылку 🔄/◀️ назад в меню ⬅️'
            bot.send_message(chat_id, 'Код: ' + cnfg.CODE + '\nПароль: ' + cnfg.PASSWORD + '\nСсылка: ' + cnfg.CHENEL_LINK, reply_markup=reply_btn_create(4, butn_text))

        elif msg_text == '◀️ изменить код 🔄':
            cnfg.CHANGE_CODE_FLAG = True
            bot.send_message(chat_id, 'Введите новый код')
        elif cnfg.CHANGE_CODE_FLAG == True:
            change(msg_text, cnfg.CODE)
            cnfg.CHANGE_CODE_FLAG = False
            work_menu(chat_id)

        elif msg_text == '◀️ сменить пароль 🔄':
            cnfg.CHANGE_PASSWORD_FLAG = True
            bot.send_message(chat_id, 'Введите новый пароль')
        elif cnfg.CHANGE_PASSWORD_FLAG == True:
            change(msg_text, cnfg.PASSWORD)
            cnfg.CHANGE_PASSWORD_FLAG = False
            work_menu(chat_id)

        elif msg_text == '◀️ сменить ссылку 🔄':
            cnfg.CHANGE_LINK_FLAG = True
            bot.send_message(chat_id, 'Введите новую ссылку')
        elif cnfg.CHANGE_LINK_FLAG == True:
            change(msg_text, cnfg.CHENEL_LINK)
            cnfg.CHANGE_LINK_FLAG = False
            work_menu(chat_id)

        elif msg_text == '◀️ назад в меню ⬅️':
            work_menu(chat_id)

        elif msg_text == '⏹️ К РЕХОСТУ ТОВЬСЬ ❗️' or cnfg.START_REHOST_FLAG == True:
            plan_rehost(msg_text, chat_id)

        else:
            bot.send_message(chat_id, 'Команда не распознана, вы возвращены в меню')
            work_menu(chat_id)
    else:
        bot.send_message(chat_id, 'Команда не распознана, вы возвращены в меню')
        work_menu(chat_id)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    if cnfg.REHOST_FLAG == False:
        if call.data.split('|')[0] != 'block' and call.data.split('|')[0] != 'unblock':

            user1_id = int(call.data.split('|')[0])
            user2_id = int(call.data.split('|')[1])

            if user1_id < 0:
                user_num = find_user_num(user2_id)
                bot.send_message(user1_id * -1, 'Ваше сообщение прочитано 📭\n' + cnfg.names[user_num])
                work_menu(user2_id)
            else:
                if user2_id < 0:
                    cnfg.TEXT_NUM = 0
                    user2_id *= -1
                else:
                    cnfg.TEXT_NUM = 1

                bot.send_message(user2_id, texts[cnfg.TEXT_NUM], reply_markup=reply_btn_create(1, '◀️ отмена ❌'))
                cnfg.MESSAGE_FLAG = True
                cnfg.PERS_ID = user1_id

        elif call.data.split('|')[0] == 'block':
            cnfg.black_list.append(int(call.data.split('|')[1]))

        elif call.data.split('|')[0] == 'unblock':
            cnfg.black_list.remove(int(call.data.split('|')[1])) 

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)



if __name__ == '__main__':
    bot.infinity_polling()
