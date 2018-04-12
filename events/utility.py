from django.utils.text import slugify
import random, string

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
