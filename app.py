from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('8wFacFsGNdnNJNLijxay336uu51vdtWRbHb8xH0bCquvIowvaIAJsUrEr/HAY3hLoQie+PMYUSxeUIPtm2jRlSeqTmnVNOaxEyI9iVp+R+3P1q2JzrdDfCoO+351rjjZb5GBzFXWq3gRzM4SUEscqQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('338567064a38b3ff17884a5ac3096e5f')



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text

    News1_Business_Easy ='Apple is a big American company. It is a computer company. It has a lot of money. In August, it has $1 trillion. However, business is smaller now. This news is a shock to business people. Apple’s boss says that the business is smaller because people in China do not buy many new iPhones. The Chinese economy is not growing as fast as before. Some people say that the business is smaller because Apple products are expensive. !\nAre you ready to play the game?(If you ready please text "Yes11")'
    News1_Business_Normal = 'It is said that Apple will make less money than before, and this is a shock to business people. Apple’s boss said that this is because people are buying fewer iPhones in China. After a lot of growth, China’s economy is slowing down. The Chinese are more careful with their money, so people buy less. In fact, car companies and coffee companies also have fewer sales than before. Other experts even say that Apple products are expensive. Apple’s boss also mentioned that people do not upgrade their iPhones as often as they did in the past. ! \nAre you ready to play the game?(If you ready please text "Yes21")' 
    News1_Business_Challenging = 'Apple announced a reduced revenue outlook recently which came as a shock to the stock market. Apple’s CEO Tim Cook said that slow sales in China could cause the drop in value. After a lot of growth, experts say that China is facing an economic slowdown and 2018 is projected to have China’s slowest growth since 1990. With Chinese consumers more careful about how they spend their money, Apple is not the only company to face the consequences. Western car companies and Starbucks, for example, are finding it harder to sell in China. Other analysts blame the situation on Apple’s expensive pricing strategy. The frequency with which people upgrade their iPhones is lower, as well. \nAre you ready to play the game?(If you ready please text "Yes31")'
    News2_Technology_Easy = 'This news is from Norway. It is about electric cars. In 2013, only 5.5% of new cars are electric. In 2018, it is 33%. This is a world record. People in Norway have a plan. They want to have all new cars be electric in 2025. This is a big plan. The government wants to help people buy electric cars. For example, if you buy an electric car in Norway, you do not have to pay for parking. \nAre you ready to play the game?(If you ready please text "Yes41")'
    News2_Technology_Normal ='Norway has a plan for 2025. It wants all new cars which people buy there to be electric. It looks like the plan is working. In 2018, the country set a world record for electric car sales when one third of all new cars were 100 percent electric. Five years ago, only 5.5 percent of new cars were electric. Norway’s 2025 plan is very ambitious, but the government offers help if you buy a new electric car. You can have free parking and you do not have to pay some taxes. !\nAre you ready to play the game?(If you ready please text "Yes51")'
    News2_Technology_Challenging = 'By 2025, Norway has a plan for all new cars to have zero emissions, and it is possible to achieve this goal. In 2018, almost one third of all new vehicles sold in Norway were already 100 percent electric. People reported it to be a world record for yearly vehicle sales. This shows a growing trend in Norway where electric vehicle sales were only 5.5 percent five years ago. Norway’s 2025 plan is very ambitious, but the government is trying to convince people to make the switch by offering a lot of incentives like free parking and not having to pay some taxes. ! \nAre you ready to play the game?(If you ready please text "Yes61")'
    if text == 'profile':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile API without user ID"))
    elif text == 'bye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
    elif text == 'Hello' or text == 'hello':
        buttons_template = ButtonsTemplate(
            title='News', text='Do you want to read today’s news?', actions=[
            PostbackAction(label='Yes', data='ping', text='Yes'),
            PostbackAction(label='No', data='ping', text='bye')
        ])
        template_message = TemplateSendMessage(alt_text='Buttons alt text',template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'Yes':
        buttons_template = ButtonsTemplate(
        title='Category', text='Which kinds of News do you prefer to read?', actions=[
            PostbackAction(label='A. Business_商業', data='ping', text='Business'),
            PostbackAction(label='B. Technology_科技', data='ping', text='Technology')
        ])
        template_message = TemplateSendMessage(alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'Business':
        buttons_template = ButtonsTemplate(
        title='Level', text='Which kinds of News do you prefer to read?', actions=[
            PostbackAction(label='A. Easy_簡單', data='ping', text='N1E'),
            PostbackAction(label='B. Normal_普通', data='ping', text='N1N'),
            PostbackAction(label='C. Challenging_挑戰', data='ping', text='N1C'),
        ])
        template_message = TemplateSendMessage(alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'N1E':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=News1_Business_Easy.strip()))
    elif text == 'Yes11' or text == 'yes11':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Question 11. 新聞提到哪⼀個品牌︖\nA11. Asus\nB11. Apple\nC11. Acer\n\nPlease show me the right answer! A11, B11, or C11?'))
    elif text == 'a11' or text == 'A11' or text == 'c11' or text == 'C11':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'b11' or text == 'B11':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQuestion 12.新聞中，這品牌的⽼闆說了什麼︖\nA12. 在中國，⼈們破壞他們的⼯廠。\nB12. 在中國，⼈們開始瘋狂搶購他們的產品。\nC12. 在中國，⼈們漸漸不買他們的產品。\n\nPlease show me the right answer! A12, B12, or C12?'))
    elif text == 'a12' or text == 'A12' or text == 'b12' or text == 'B12':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'c12' or text == 'C12':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQuestion 13.新聞中，造成這家品牌業績不佳的可能原因是︖\nA13. 這家品牌的產品賣太貴了。\nB13. 這家品牌的產品功能太差。\nC13. 這家品牌發的廣告不夠多。\n\nPlease show me the right answer! A13, B13, or C13?'))
    elif text == 'c13' or text == 'C13' or text == 'b13' or text == 'B13':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'a13' or text == 'A13':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! You got today’s easter egg! Please enter "EG1" to get today’s easter egg!'))
    elif text == 'EG1' or text == 'eg1':
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/RL86CjW.png',
            preview_image_url='https://i.imgur.com/RL86CjW.png'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'N1N':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=News1_Business_Normal.strip()))
    elif text == 'Yes21' or text == 'yes21':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Q21. Which of the following brand is mentioned in the news?\nA21. Apple\nB21. Asus\nC21. Acer\n\nPlease show me the right answer! A21, B21, or C21?'))
    elif text == 'b21' or text == 'B21' or text == 'c21' or text == 'C21':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'a21' or text == 'A21':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ22. What could be the reason that the company will make less money than before?\nA22. People in China consider their products bad.\nB22. The sales of their product is not as expected.\nC22. Their new products are not allowed to be imported in China.\n\nPlease show me the right answer! A22, B22, or C22?'))
    elif text == 'a22' or text == 'A22' or text == 'c22' or text == 'C22':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'b22' or text == 'B22':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ23. Which of the following is NOT the main reason that lead to the company’s situation?\nA23. China’s economic growth is slowing down.\nB23. People in China consider their products expensive.\nC23. Car companies and coffee companies are taking over their market.\n\nPlease show me the right answer! A23, B23, or C23?'))
    elif text == 'a23' or text == 'A23' or text == 'b23' or text == 'B23':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'c23' or text == 'C23':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! You got today’s easter egg! Please enter "EG2" to get today’s easter egg!'))
    elif text == 'EG2' or text == 'eg2':
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ftA2M9S.png',
            preview_image_url='https://i.imgur.com/ftA2M9S.png'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'N1C':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=News1_Business_Challenging.strip()))
    elif text == 'Yes31' or text == 'yes31':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Q31. What could be inferred from the news?\nA31. China’s economic growth is getting well.\nB31. People in China will not use smartphones anymore.\nC31. People in China becomes reserved when purchasing.\n\nPlease show me the right answer! A31, B31, or C31?'))
    elif text == 'b31' or text == 'B31' or text == 'a31' or text == 'A31':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'c21' or text == 'C21':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ32. What does the word “consequence” mean in the news?\nA32. the result\nB32. the reason\nC32. the building\n\nPlease show me the right answer! A32, B32, or C32?'))
    elif text == 'b32' or text == 'B32' or text == 'c32' or text == 'C32':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'a32' or text == 'A32':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ33. Which of the following business may also be the victims of China’s economic slowdown?\nA33. Education industry\nB33. Coffee industry\nC33. Housing Property\n\nPlease show me the right answer! A33, B33, or C33?'))
    elif text == 'a33' or text == 'A33' or text == 'c33' or text == 'C33':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'b33' or text == 'B33':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! You got today’s easter egg! Please enter "EG3" to get today’s easter egg!'))
    elif text == 'EG3' or text == 'eg3':
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/OguVCAa.png',
            preview_image_url='https://i.imgur.com/OguVCAa.png'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'Technology':
        buttons_template = ButtonsTemplate(
        title='Level', text='Which kinds of News do you prefer to read?', actions=[
            PostbackAction(label='A. Easy_簡單', data='ping', text='N2E'),
            PostbackAction(label='B. Normal_普通', data='ping', text='N2N'),
            PostbackAction(label='C. Challenging_挑戰', data='ping', text='N2C'),
        ])
        template_message = TemplateSendMessage(alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'N2E':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=News2_Technology_Easy.strip()))
    elif text == 'Yes41' or text == 'yes41':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Q41. 新聞中提到的是哪⼀個國家︖\nA41. 挪威\nB41. 瑞典\nC41. 芬蘭\n\nPlease show me the right answer! A41, B41, or C41?'))
    elif text == 'b41' or text == 'B41' or text == 'c41' or text == 'C41':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'a41' or text == 'A41':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ42. 這個國家預計在2025年達成什麼⽬標︖\nA42. 非核家園\nB42. 全⾯機器⼈代⼯\nC42. 新⾞輛皆為電動⾞\n\nPlease show me the right answer! A42, B42, or C42?'))
    elif text == 'a42' or text == 'A42' or text == 'b42' or text == 'B42':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'c42' or text == 'C42':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ43. 為了⿎勵民眾達成這個⽬標，政府採取什麼措施︖\nA43. ⿎勵民眾搭乘⼤眾運輸。\nB43. 民眾使⽤政府⿎勵的交通⼯具能免費停⾞。\nC43. ⼤量減少⼆氧化碳排放。\n\nPlease show me the right answer! A43, B43, or C43?'))
    elif text == 'c43' or text == 'C43' or text == 'a43' or text == 'A43':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'b43' or text == 'B43':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! You got today’s easter egg! Please enter "EG4" to get today’s easter egg!'))
    elif text == 'EG4' or text == 'eg4':
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/WwbIMsF.png',
            preview_image_url='https://i.imgur.com/WwbIMsF.png'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'N2N':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=News2_Technology_Normal.strip()))
    elif text == 'Yes51' or text == 'yes51':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Q51. What will happen in 2025 Norway?\nA51. People rely much on public transportation.\nB51. Robots have take over the government.\nC51. On the road are all electric cars.\n\nPlease show me the right answer! A51, B51, or C51?'))
    elif text == 'b51' or text == 'B51' or text == 'a51' or text == 'A51':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'c51' or text == 'C51':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ52. In 2018, what was the world record the Norwegians have achieved?\nA52. The government will help you buy a new car.\nB52. About one third of the new car sold are electric cars.\nC52. The Norwegians have given up the plan of electric cars.\n\nPlease show me the right answer! A52, B52, or C52?'))
    elif text == 'a52' or text == 'A52' or text == 'c52' or text == 'C52':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'b52' or text == 'B52':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ53. Which of the following is NOT mentioned as advantages of buying an electric car?\nA53. Housing price discount.\nB53. Free parking.\nC53. Tax reduction.\n\nPlease show me the right answer! A53, B53, or C53?'))
    elif text == 'c53' or text == 'C53' or text == 'b53' or text == 'B53':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'a53' or text == 'A53':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! You got today’s easter egg! Please enter "EG5" to get today’s easter egg!'))
    elif text == 'EG5' or text == 'eg5':
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ZBAInyI.png',
            preview_image_url='https://i.imgur.com/ZBAInyI.png'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'N2C':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=News2_Technology_Challenging.strip()))
    elif text == 'Yes61' or text == 'yes61':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Q61. In 2018, if there were 12 cars on the roads, how many of them were electric cars?\nA61. Only 1 car was electric car.\nB61. About 4 cars were electric cars.\nC61. All of the cars were electric cars.\n\nPlease show me the right answer! A61, B61, or C61?'))
    elif text == 'c61' or text == 'C61' or text == 'a61' or text == 'A61':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'b61' or text == 'B61':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ62. What could be inferred from the news?\nA62. Norwegians prefer to buy electric cars nowadays.\nB62. Norwegians do not like electric cars.\nC62. Norwegians are not allowed to buy electric cars.\n\nPlease show me the right answer! A62, B62, or C62?'))
    elif text == 'b62' or text == 'B62' or text == 'c62' or text == 'C62':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'a62' or text == 'A62':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! Let’s move on!\n\nQ63. What does the word “convince” mean in the news?\nA63. to discourage\nB63. to warn\nC63. to persuade\n\nPlease show me the right answer! A63, B63, or C63?'))
    elif text == 'a63' or text == 'A63' or text == 'b63' or text == 'B63':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Let’s think again!'))
    elif text == 'c63' or text == 'C63':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Great! You got today’s easter egg! Please enter "EG6" to get today’s easter egg!'))
    elif text == 'EG6' or text == 'eg6':
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/bAkjYLi.png',
            preview_image_url='https://i.imgur.com/bAkjYLi.png'
        )
        line_bot_api.reply_message(event.reply_token, message)
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Please type "Hello" to start to read News!'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
