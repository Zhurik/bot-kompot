# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def send_msg(id, text, session):
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
            print(event.obj.text)
            send_msg(event.obj.from_id, event.obj.text, api)


if __name__ == '__main__':
    main()
