from django.utils.text import slugify
from selenium import webdriver
import random, string, os

def random_string_generator(size, chars=string.ascii_lowercase + string.digits):
    return str(''.join(random.choice(chars) for _ in range(size)))

def unique_slug_generator(instance, new_tag=None):

    if new_tag is not None:
        tag = new_tag
    else:
        tag = slugify(instance.tag)

    qs_exists = (instance.__class__).objects.filter(tag=tag).exists()
    #checking if there is any other tag with same name
    if qs_exists:
        #if exists then regenerate unique url
        new_tag = (tag+"-"+random_string_generator(size=4))
        return unique_slug_generator(instance, new_tag=new_tag)
    return tag

def send_whatsapp_message(message):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DRIVER_PATH = os.path.join(BASE_DIR, 'static/static/driver/chromedriver.exe'),
    driver = webdriver.Chrome(DRIVER_PATH)

    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')

    name = 'Event Group'
    
    input('Enter anything after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')

    msg_box.send_keys(message)
    button = driver.find_element_by_class_name('_2lkdt')
    button.click()
