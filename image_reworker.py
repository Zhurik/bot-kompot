import vk_api
import requests
import os

vk_session = vk_api.VkApi(token='ac2c3229028488e89ba5a80eb5057e3653cb6bebc371f8964ac0ed5a0cc7c9940607ec7d1086eafc357a6')
pic_url = 'https://memepedia.ru/wp-content/uploads/2017/05/dick-butt-%D0%BE%D1%80%D0%B8%D0%B3%D0%B8%D0%BD%D0%B0%D0%BB-1.jpg'
user_id = 18841900

# def rework_picture_from_url(session, url, user, text, rework_function):
def rework_picture_from_url(session, url, user, text=''):
    # Получаем имя картинки
    name = url.rsplit('/', 1)[1]

    # Скачиваем ее и пишем на диск
    r = requests.get(url, allow_redirects=True)
    with open(name, 'wb+') as f:
        f.write(r.content)
    
    # Тут ее можно вполне себе обработать
    # rework_function(name)

    upload = vk_api.VkUpload(session)
    photo = upload.photo_messages(name)
    api = session.get_api()
    api.messages.send(user_id=user, message=text, attachment='photo' + str(photo[0]['owner_id']) + '_' + str(photo[0]['id']))
    os.remove(name)

# rework_picture_from_url(vk_session, pic_url, user_id)