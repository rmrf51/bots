import vk_api
from vk_api import VkApi
import random
import requests
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from io import BytesIO
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})


def photo(user_id, width, height):
    write_msg(event.user_id, "https://picsum.photos/"+width+"/"+height,random.randint(1,212121212121))


# API-ключ 
token = "28d7c0d60ff6535fe416ea5eca9a138ce1a0f33e3d7b8b5a8e033efe677b69c0df8f077982d2c7580fed7"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk, 170719138)



def upload_photo(upload, url):
    img = requests.get(url).content
    f = BytesIO(img)

    response = upload.photo_messages(f)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.method('messages.send', {'user_id': peer_id, 'attachment': attachment, 'random_id': get_random_id()})




##############################
##############################
# keyboard ###################
##############################

def create_keyboard():
    keyboard = VkKeyboard(one_time=False)
    #False Если клавиатура должна оставаться откртой после нажатия на кнопку
    #True если она должна закрваться

    keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button('Синяя кнопка', color=VkKeyboardColor.PRIMARY)

    return keyboard


def create_empty_keyboard():
    keyboard = VkKeyboard(one_time=False)#vk_api.keyboard.VkKeyboard.get_empty_keyboard()

    return keyboard
    #Эта функция используется для закрытия клавиатуры



##############################
##############################




# Основной цикл
for event in longpoll.listen():
  
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text

            keyboard = create_keyboard()
            #empty_keyboard = create_empty_keyboard()
            
            # Каменная логика ответа
            if request.lower() == "привет":
                write_msg(event.user_id, "Привет, няшка!", random.randint(1,212121212121))
            elif request.lower()  == "пока":
                vk.method('messages.send', {'user_id': event.user_id, 'message': "Keyboard", 'random_id': random.randint(1,212121212121), 'keyboard': keyboard.get_keyboard()})
                write_msg(event.user_id, "Досвидули",random.randint(1,212121212121))
            elif request.lower() == "фото":
                write_msg(event.user_id, "Держи",random.randint(1,212121212121))
                #photo(event.user_id, '300', '300')
                upload = VkUpload(vk)
                send_photo(vk, event.user_id, *upload_photo(upload, "https://picsum.photos/300/300"))
            else:
                write_msg(event.user_id, "Отчислен(а)!!!!!",random.randint(1,212121212121))
            
