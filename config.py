
import telebot
import os

token = "8049800117:AAF9nnxShWOhvlPrWWmzZ55ImrQJcwkM-hc"
bot = telebot.TeleBot(os.getenv('token'))


texts = ["Ты выбрал написать письмо\nМожешь написать всё что хочешь: вопросы, пожелания, предложения рекламы, анекдотов или тем для других рубрик", \
       "Напиши и отправь свой ответ", "ПРИШЛО СООБЩЕНИЕ!\n\n", "ВАМ ПРИШЁЛ ОТВЕТ!\n\n", "Напиши, почему ты хочешь, чтобы тебя разбанили", "Пришла оппеляция на бан"]

rehost_texts = ['ЕСТЬ🫡. Начинаю подготовку. Перед повторным запуском измените значения переменных и списков', 'Есть отменить рехост! Возвращаю в главное меню', \
            'Подготовка завершена! Бот готов к рехосту! Нажмите "отмена" если хотите перенести рехост', \
            'ВНИМАНИЕ ВНИМАНИЕ! ТЕХНИЧЕСКИЕ РАБОТЫ!\nОжидаемая продолжительность: не более 48 часов. На время команды не будут работать\nС уважением, Редакция канала']

BOT_LINK = 'https://t.me/maybe_this_try_will_normalbot'

OUR_AD = '———————РЁКЛАМА————————\n- ты какой-то странный \n- мне сказали, что у меня скитлстрянка\n- а это заразно?\n- не, не думаю'



class Config:
    def __init__(self):

        self.MY_ID = 0
        self.PERS_ID = 0
        self.MESSAGE_FLAG = False
        self.SHEARLING_FLAG = False
        self.COMMANDER_FLAG = False
        self.CHANGE_CODE_FLAG = False
        self.CHANGE_PASSWORD_FLAG = False
        self.CHANGE_LINK_FLAG = False
        self.START_REHOST_FLAG = False

        self.REHOST_FLAG = False

        self.TEXT_NUM = -1
        self.QUESTION_NUM = 3
        self.CHENEL_LINK = 'https://t.me/+qkPpUDqZH-M5MWQy'
        self.CODE = 'qws_==_1vaa.;wrbaasny0j@-nfo'
        self.PASSWORD = '11'

        self.users = []
        self.names = []
        self.sexes = []
        self.birthdays = []
        self.usernames = []
        self.black_list = []


cnfg = Config()
