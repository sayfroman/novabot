{\rtf1\ansi\ansicpg1251\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import telebot\
import random\
import os\
from datetime import datetime\
\
# \uc0\u1058 \u1086 \u1082 \u1077 \u1085  \u1073 \u1086 \u1090 \u1072  (\u1074 \u1089 \u1090 \u1072 \u1074 \u1100 \u1090 \u1077  \u1074 \u1072 \u1096 )\
TOKEN = os.getenv("TOKEN")\
bot = telebot.TeleBot(TOKEN)\
\
# \uc0\u1057 \u1087 \u1080 \u1089 \u1086 \u1082  \u1092 \u1080 \u1083 \u1080 \u1072 \u1083 \u1086 \u1074  \u1080  \u1090 \u1088 \u1077 \u1085 \u1077 \u1088 \u1086 \u1074  (\u1087 \u1088 \u1080 \u1084 \u1077 \u1088 )\
TRAINERS = \{\
    123456789: \{"branch": "\uc0\u1060 \u1080 \u1083 \u1080 \u1072 \u1083  1", "start_time": "10:00", "end_time": "11:00"\},\
    987654321: \{"branch": "\uc0\u1060 \u1080 \u1083 \u1080 \u1072 \u1083  2", "start_time": "12:00", "end_time": "13:00"\},\
\}\
\
# \uc0\u1042 \u1072 \u1088 \u1080 \u1072 \u1085 \u1090 \u1099  \u1089 \u1086 \u1086 \u1073 \u1097 \u1077 \u1085 \u1080 \u1081 \
START_MESSAGES = ["\uc0\u1059 \u1074 \u1072 \u1078 \u1072 \u1077 \u1084 \u1099 \u1077  \u1088 \u1086 \u1076 \u1080 \u1090 \u1077 \u1083 \u1080 , \u1090 \u1088 \u1077 \u1085 \u1080 \u1088 \u1086 \u1074 \u1082 \u1072  \u1085 \u1072 \u1095 \u1072 \u1083 \u1072 \u1089 \u1100 ", "\u1058 \u1088 \u1077 \u1085 \u1080 \u1088 \u1086 \u1074 \u1082 \u1072  \u1085 \u1072 \u1095 \u1072 \u1083 \u1072 \u1089 \u1100 ! \u1044 \u1077 \u1090 \u1080  \u1074  \u1079 \u1072 \u1083 \u1077 ", "\u1053 \u1072 \u1095 \u1080 \u1085 \u1072 \u1077 \u1084 ! \u1046 \u1077 \u1083 \u1072 \u1077 \u1084  \u1093 \u1086 \u1088 \u1086 \u1096 \u1077 \u1081  \u1090 \u1088 \u1077 \u1085 \u1080 \u1088 \u1086 \u1074 \u1082 \u1080 "]\
END_MESSAGES = ["\uc0\u1058 \u1088 \u1077 \u1085 \u1080 \u1088 \u1086 \u1074 \u1082 \u1072  \u1086 \u1082 \u1086 \u1085 \u1095 \u1077 \u1085 \u1072 , \u1076 \u1077 \u1090 \u1080  \u1089 \u1074 \u1086 \u1073 \u1086 \u1076 \u1085 \u1099 ", "\u1057 \u1087 \u1072 \u1089 \u1080 \u1073 \u1086  \u1079 \u1072  \u1079 \u1072 \u1085 \u1103 \u1090 \u1080 \u1077 ! \u1044 \u1086  \u1074 \u1089 \u1090 \u1088 \u1077 \u1095 \u1080  \u1085 \u1072  \u1089 \u1083 \u1077 \u1076 \u1091 \u1102 \u1097 \u1077 \u1081  \u1090 \u1088 \u1077 \u1085 \u1080 \u1088 \u1086 \u1074 \u1082 \u1077 ", "\u1058 \u1088 \u1077 \u1085 \u1080 \u1088 \u1086 \u1074 \u1082 \u1072  \u1079 \u1072 \u1074 \u1077 \u1088 \u1096 \u1077 \u1085 \u1072 , \u1074 \u1089 \u1077 \u1084  \u1093 \u1086 \u1088 \u1086 \u1096 \u1077 \u1075 \u1086  \u1074 \u1077 \u1095 \u1077 \u1088 \u1072 "]\
\
# \uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1095 \u1080 \u1082  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076  /start\
@bot.message_handler(commands=['start'])\
def send_welcome(message):\
    bot.reply_to(message, "\uc0\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 ! \u1054 \u1090 \u1087 \u1088 \u1072 \u1074 \u1100 \u1090 \u1077  \u1092 \u1086 \u1090 \u1086  \u1090 \u1088 \u1077 \u1085 \u1080 \u1088 \u1086 \u1074 \u1082 \u1080 .")\
\
# \uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1095 \u1080 \u1082  \u1092 \u1086 \u1090 \u1086 \
@bot.message_handler(content_types=['photo'])\
def handle_photo(message):\
    trainer_id = message.from_user.id\
    \
    if trainer_id not in TRAINERS:\
        bot.reply_to(message, "\uc0\u1042 \u1099  \u1085 \u1077  \u1079 \u1072 \u1088 \u1077 \u1075 \u1080 \u1089 \u1090 \u1088 \u1080 \u1088 \u1086 \u1074 \u1072 \u1085 \u1099  \u1082 \u1072 \u1082  \u1090 \u1088 \u1077 \u1085 \u1077 \u1088 .")\
        return\
    \
    now = datetime.now().strftime("%H:%M")\
    trainer_info = TRAINERS[trainer_id]\
    \
    if now >= trainer_info["start_time"] and now <= trainer_info["end_time"]:\
        text = random.choice(START_MESSAGES if now == trainer_info["start_time"] else END_MESSAGES)\
        bot.send_message(message.chat.id, f"\{trainer_info['branch']\}: \{text\}")\
        bot.send_photo(message.chat.id, message.photo[-1].file_id)\
    else:\
        bot.reply_to(message, "\uc0\u1060 \u1086 \u1090 \u1086  \u1086 \u1090 \u1087 \u1088 \u1072 \u1074 \u1083 \u1077 \u1085 \u1086  \u1089  \u1086 \u1087 \u1086 \u1079 \u1076 \u1072 \u1085 \u1080 \u1077 \u1084 . \u1064 \u1090 \u1088 \u1072 \u1092  \u1073 \u1091 \u1076 \u1077 \u1090  \u1085 \u1072 \u1095 \u1080 \u1089 \u1083 \u1077 \u1085 .")\
\
# \uc0\u1047 \u1072 \u1087 \u1091 \u1089 \u1082  \u1073 \u1086 \u1090 \u1072 \
bot.polling(none_stop=True)}