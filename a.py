import requests
x = 1
lang = []
sc = ''
count = [ 'PH', 'IT', 'GR', 'KR', 'ph']
google_voice_name = ['eu-ES-Standard-A', 'gl-ES-Standard-A', 'mr-IN-Standard-A', 'mr-IN-Standard-B', 'mr-IN-Standard-C', 'pa-IN-Standard-A', 'pa-IN-Standard-B', 'pa-IN-Standard-C', 'pa-IN-Standard-D', 'sv-SE-Standard-B', 'sv-SE-Standard-C', 'sv-SE-Standard-D', 'sv-SE-Standard-E', 'sv-SE-Standard-A', 'ta-IN-Standard-C', 'ta-IN-Standard-D', 'yue-HK-Standard-A', 'yue-HK-Standard-B', 'yue-HK-Standard-C', 'yue-HK-Standard-D', 'bn-IN-Standard-A', 'bn-IN-Standard-B', 'cmn-CN-Standard-C', 'cmn-CN-Standard-B', 'cmn-CN-Standard-A', 'cmn-CN-Standard-D', 'cmn-TW-Standard-A', 'cmn-TW-Standard-B', 'cmn-TW-Standard-C', 'es-US-Standard-A', 'es-US-Standard-B', 'es-US-Standard-C', 'gu-IN-Standard-A', 'gu-IN-Standard-B', 'ja-JP-Standard-A', 'ja-JP-Standard-B', 'ja-JP-Standard-C', 'ja-JP-Standard-D', 'kn-IN-Standard-A', 'kn-IN-Standard-B', 'ml-IN-Standard-A', 'ml-IN-Standard-B', 'nl-BE-Standard-A', 'nl-BE-Standard-B', 'ta-IN-Standard-A', 'ta-IN-Standard-B', 'af-ZA-Standard-A', 'ar-XA-Standard-A', 'ar-XA-Standard-B', 'ar-XA-Standard-C', 'ar-XA-Standard-D', 'bg-BG-Standard-A', 'cs-CZ-Standard-A', 'da-DK-Standard-C', 'da-DK-Standard-D', 'da-DK-Standard-E', 'da-DK-Standard-A', 'de-DE-Standard-A', 'de-DE-Standard-B', 'de-DE-Standard-C', 'de-DE-Standard-D', 'de-DE-Standard-E', 'de-DE-Standard-F', 'en-AU-Standard-A', 'en-AU-Standard-B', 'en-AU-Standard-C', 'en-AU-Standard-D', 'en-GB-Standard-A', 'en-GB-Standard-B', 'en-GB-Standard-C', 'en-GB-Standard-D', 'en-GB-Standard-F', 'en-IN-Standard-D', 'en-IN-Standard-A', 'en-IN-Standard-B', 'en-IN-Standard-C', 'en-US-Standard-A', 'en-US-Standard-B', 'en-US-Standard-C', 'en-US-Standard-D', 'en-US-Standard-E', 'en-US-Standard-F', 'en-US-Standard-G', 'en-US-Standard-H', 'en-US-Standard-I', 'en-US-Standard-J', 'es-ES-Standard-A', 'es-ES-Standard-C', 'es-ES-Standard-D', 'es-ES-Standard-B', 'fi-FI-Standard-A', 'fr-CA-Standard-A', 'fr-CA-Standard-B', 'fr-CA-Standard-C', 'fr-CA-Standard-D', 'fr-FR-Standard-A', 'fr-FR-Standard-B', 'fr-FR-Standard-C', 'fr-FR-Standard-D', 'fr-FR-Standard-E', 'he-IL-Standard-D', 'he-IL-Standard-A', 'he-IL-Standard-B', 'he-IL-Standard-C', 'hi-IN-Standard-D', 'hi-IN-Standard-A', 'hi-IN-Standard-B', 'hi-IN-Standard-C', 'hu-HU-Standard-A', 'is-IS-Standard-A', 'lt-LT-Standard-A', 'lv-LV-Standard-A', 'ms-MY-Standard-A', 'ms-MY-Standard-B', 'ms-MY-Standard-C', 'ms-MY-Standard-D', 'nb-NO-Standard-A', 'nb-NO-Standard-B', 'nb-NO-Standard-E', 'nb-NO-Standard-C', 'nb-NO-Standard-D', 'nl-NL-Standard-B', 'nl-NL-Standard-C', 'nl-NL-Standard-D', 'nl-NL-Standard-A', 'nl-NL-Standard-E', 'pt-BR-Standard-A', 'pt-BR-Standard-B', 'pt-BR-Standard-C', 'pt-PT-Standard-A', 'pt-PT-Standard-B', 'pt-PT-Standard-C', 'pt-PT-Standard-D', 'ro-RO-Standard-A', 'ru-RU-Standard-E', 'ru-RU-Standard-A', 'ru-RU-Standard-B', 'ru-RU-Standard-C', 'ru-RU-Standard-D', 'sk-SK-Standard-A', 'sr-RS-Standard-A', 'th-TH-Standard-A', 'uk-UA-Standard-A', 'vi-VN-Standard-A', 'vi-VN-Standard-B', 'vi-VN-Standard-C', 'vi-VN-Standard-D', 'pl-PL-Standard-A', 'pl-PL-Standard-B', 'pl-PL-Standard-C', 'pl-PL-Standard-E', 'pl-PL-Standard-D', 'tr-TR-Standard-B', 'tr-TR-Standard-C', 'tr-TR-Standard-D', 'tr-TR-Standard-A', 'tr-TR-Standard-E', 'id-ID-Standard-A', 'id-ID-Standard-B', 'id-ID-Standard-C', 'id-ID-Standard-D', 'fil-PH-Standard-A', 'fil-PH-Standard-B', 'fil-PH-Standard-C', 'fil-PH-Standard-D', 'ca-ES-Standard-A', 'it-IT-Standard-B', 'it-IT-Standard-C', 'it-IT-Standard-D', 'it-IT-Standard-A', 'el-GR-Standard-A', 'ko-KR-Standard-A', 'ko-KR-Standard-B', 'ko-KR-Standard-C', 'ko-KR-Standard-D', 'te-IN-Standard-A', 'te-IN-Standard-B', 'ar-XA-Wavenet-A', 'ar-XA-Wavenet-B', 'ar-XA-Wavenet-C', 'ar-XA-Wavenet-D', 'bn-IN-Wavenet-A', 'bn-IN-Wavenet-B', 'cmn-CN-Wavenet-A', 'cmn-CN-Wavenet-B', 'cmn-CN-Wavenet-C', 'cmn-CN-Wavenet-D', 'cmn-TW-Wavenet-A', 'cmn-TW-Wavenet-B', 'cmn-TW-Wavenet-C', 'cs-CZ-Wavenet-A', 'da-DK-Wavenet-C', 'da-DK-Wavenet-D', 'da-DK-Wavenet-E', 'da-DK-Wavenet-A', 'de-DE-Wavenet-F', 'de-DE-Wavenet-A', 'de-DE-Wavenet-B', 'de-DE-Wavenet-C', 'de-DE-Wavenet-D', 'de-DE-Wavenet-E', 'el-GR-Wavenet-A', 'en-AU-News-E', 'en-AU-News-F', 'en-AU-News-G', 'en-AU-Wavenet-A', 'en-AU-Wavenet-B', 'en-AU-Wavenet-C', 'en-AU-Wavenet-D', 'en-GB-News-G', 'en-GB-News-H', 'en-GB-News-I', 'en-GB-News-J', 'en-GB-News-K', 'en-GB-News-L', 'en-GB-News-M', 'en-GB-Wavenet-A', 'en-GB-Wavenet-B', 'en-GB-Wavenet-C', 'en-GB-Wavenet-D', 'en-GB-Wavenet-F', 'en-IN-Wavenet-D', 'en-IN-Wavenet-A', 'en-IN-Wavenet-B', 'en-IN-Wavenet-C', 'en-US-News-K', 'en-US-News-L', 'en-US-News-M', 'en-US-News-N', 'en-US-Wavenet-G', 'en-US-Wavenet-H', 'en-US-Wavenet-I', 'en-US-Wavenet-J', 'en-US-Wavenet-A', 'en-US-Wavenet-B', 'en-US-Wavenet-C', 'en-US-Wavenet-D', 'en-US-Wavenet-E', 'en-US-Wavenet-F', 'es-ES-Wavenet-C', 'es-ES-Wavenet-D', 'es-ES-Wavenet-B', 'es-US-Wavenet-A', 'es-US-Wavenet-B', 'es-US-Wavenet-C', 'es-US-News-G', 'es-US-News-F', 'es-US-News-E', 'es-US-News-D', 'fi-FI-Wavenet-A', 'fil-PH-Wavenet-A', 'fil-PH-Wavenet-B', 'fil-PH-Wavenet-C', 'fil-PH-Wavenet-D', 'fr-CA-Wavenet-A', 'fr-CA-Wavenet-B', 'fr-CA-Wavenet-C', 'fr-CA-Wavenet-D', 'fr-FR-Wavenet-E', 'fr-FR-Wavenet-A', 'fr-FR-Wavenet-B', 'fr-FR-Wavenet-C', 'fr-FR-Wavenet-D', 'gu-IN-Wavenet-A', 'gu-IN-Wavenet-B', 'he-IL-Wavenet-D', 'he-IL-Wavenet-A', 'he-IL-Wavenet-B', 'he-IL-Wavenet-C', 'hi-IN-Wavenet-D', 'hi-IN-Wavenet-A', 'hi-IN-Wavenet-B', 'hi-IN-Wavenet-C', 'hu-HU-Wavenet-A', 'id-ID-Wavenet-D', 'id-ID-Wavenet-A', 'id-ID-Wavenet-B', 'id-ID-Wavenet-C', 'it-IT-Wavenet-A', 'it-IT-Wavenet-B', 'it-IT-Wavenet-C', 'it-IT-Wavenet-D', 'ja-JP-Wavenet-B', 'ja-JP-Wavenet-C', 'ja-JP-Wavenet-D', 'ja-JP-Wavenet-A', 'kn-IN-Wavenet-A', 'kn-IN-Wavenet-B', 'ko-KR-Wavenet-A', 'ko-KR-Wavenet-B', 'ko-KR-Wavenet-C', 'ko-KR-Wavenet-D', 'ml-IN-Wavenet-A', 'ml-IN-Wavenet-B', 'ml-IN-Wavenet-C', 'ml-IN-Wavenet-D', 'mr-IN-Wavenet-A', 'mr-IN-Wavenet-B', 'mr-IN-Wavenet-C', 'ms-MY-Wavenet-A', 'ms-MY-Wavenet-B', 'ms-MY-Wavenet-C', 'ms-MY-Wavenet-D', 'nb-NO-Wavenet-A', 'nb-NO-Wavenet-B', 'nb-NO-Wavenet-C', 'nb-NO-Wavenet-D', 'nb-NO-Wavenet-E', 'nl-BE-Wavenet-A', 'nl-BE-Wavenet-B', 'nl-NL-Wavenet-B', 'nl-NL-Wavenet-C', 'nl-NL-Wavenet-D', 'nl-NL-Wavenet-A', 'nl-NL-Wavenet-E', 'pa-IN-Wavenet-A', 'pa-IN-Wavenet-B', 'pa-IN-Wavenet-C', 'pa-IN-Wavenet-D', 'pl-PL-Wavenet-A', 'pl-PL-Wavenet-B', 'pl-PL-Wavenet-C', 'pl-PL-Wavenet-E', 'pl-PL-Wavenet-D', 'pt-BR-Wavenet-A', 'pt-BR-Wavenet-B', 'pt-BR-Wavenet-C', 'pt-PT-Wavenet-A', 'pt-PT-Wavenet-B', 'pt-PT-Wavenet-C', 'pt-PT-Wavenet-D', 'ro-RO-Wavenet-A', 'ru-RU-Wavenet-E', 'ru-RU-Wavenet-A', 'ru-RU-Wavenet-B', 'ru-RU-Wavenet-C', 'ru-RU-Wavenet-D', 'sk-SK-Wavenet-A', 'sv-SE-Wavenet-B', 'sv-SE-Wavenet-D', 'sv-SE-Wavenet-C', 'sv-SE-Wavenet-E', 'sv-SE-Wavenet-A', 'ta-IN-Wavenet-A', 'ta-IN-Wavenet-B', 'ta-IN-Wavenet-C', 'ta-IN-Wavenet-D', 'tr-TR-Wavenet-B', 'tr-TR-Wavenet-C', 'tr-TR-Wavenet-D', 'tr-TR-Wavenet-E', 'tr-TR-Wavenet-A', 'uk-UA-Wavenet-A', 'vi-VN-Wavenet-A', 'vi-VN-Wavenet-B', 'vi-VN-Wavenet-C', 'vi-VN-Wavenet-D', 'en-US-Studio-M', 'en-US-Studio-O', 'es-US-Studio-B', 'da-DK-Neural2-D', 'da-DK-Neural2-F', 'de-DE-Neural2-B', 'de-DE-Neural2-C', 'de-DE-Neural2-D', 'de-DE-Neural2-F', 'de-DE-Polyglot-1', 'en-AU-Neural2-A', 'en-AU-Neural2-B', 'en-AU-Neural2-C', 'en-AU-Neural2-D', 'en-AU-Polyglot-1', 'en-GB-Neural2-A', 'en-GB-Neural2-B', 'en-GB-Neural2-C', 'en-GB-Neural2-D', 'en-GB-Neural2-F', 'en-US-Neural2-A', 'en-US-Neural2-C', 'en-US-Neural2-D', 'en-US-Neural2-E', 'en-US-Neural2-F', 'en-US-Neural2-G', 'en-US-Neural2-H', 'en-US-Neural2-I', 'en-US-Neural2-J', 'en-US-Polyglot-1', 'es-ES-Neural2-A', 'es-ES-Neural2-B', 'es-ES-Neural2-C', 'es-ES-Neural2-D', 'es-ES-Neural2-E', 'es-ES-Neural2-F', 'es-ES-Polyglot-1', 'es-US-Neural2-A', 'es-US-Neural2-B', 'es-US-Neural2-C', 'es-US-Polyglot-1', 'fil-ph-Neural2-D', 'fil-ph-Neural2-A', 'fr-CA-Neural2-A', 'fr-CA-Neural2-B', 'fr-CA-Neural2-C', 'fr-CA-Neural2-D', 'fr-FR-Neural2-A', 'fr-FR-Neural2-B', 'fr-FR-Neural2-C', 'fr-FR-Neural2-D', 'fr-FR-Neural2-E', 'fr-FR-Polyglot-1', 'hi-IN-Neural2-A', 'hi-IN-Neural2-B', 'hi-IN-Neural2-C', 'hi-IN-Neural2-D', 'it-IT-Neural2-A', 'it-IT-Neural2-C', 'ja-JP-Neural2-B', 'ja-JP-Neural2-C', 'ja-JP-Neural2-D', 'ko-KR-Neural2-A', 'ko-KR-Neural2-B', 'ko-KR-Neural2-C', 'pt-BR-Neural2-A', 'pt-BR-Neural2-B', 'pt-BR-Neural2-C', 'vi-VN-Neural2-A', 'vi-VN-Neural2-D', 'th-TH-Neural2-C'] 
print('updated_keyboard = telebot.types.InlineKeyboardMarkup()')
for voic in google_voice_name:
    #print(f'item{x} = types.InlineKeyboardButton("{voic}",callback_data="{voic}")')
    con =voic.split('-')[1]
    
    if 'ph' in voic:
        print(f'item{x} = types.InlineKeyboardButton("{voic}",callback_data="{voic}")')
        sc += f'item{x},'
        x+=1
print(f'updated_keyboard.add({sc})')
print(f"bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= ' Available Voice/Languages In KR')")
print("bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=updated_keyboard)")
