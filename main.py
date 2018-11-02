# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from image_reworker import rework_picture_from_url

def send_msg(id, text, session):
    if text == '':
        return
    session.messages.send(user_id=id, message=text)

def main():
    with open('token.txt', 'r') as f:
        api_token = f.read().strip()

    vk_session = vk_api.VkApi(token=api_token)
    api = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, '173227835')
    print('Слушаем')
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            for attachment in event.obj.attachments:
                if attachment['type'] == 'photo':
                     rework_picture_from_url(vk_session, attachment['photo']['sizes'][3]['url'], event.obj.from_id)
            send_msg(event.obj.from_id, event.obj.text, api)


if __name__ == '__main__':
    main()
