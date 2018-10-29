# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def main():
    with open('token.txt', 'r') as f:
        api_token = f.read().strip()

    vk_session = vk_api.VkApi(token=api_token)

    longpoll = VkBotLongPoll(vk_session, '173227835')
    print('Слушаем')
    for event in longpoll.listen():

        print(event.type)


if __name__ == '__main__':
    main()
