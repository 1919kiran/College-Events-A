from django.utils.text import slugify
import random, string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return str(''.join(random.choice(chars) for _ in range(size)))

def unique_slug_generator(instance, new_tag=None):

    if new_tag is not None:
        tag = new_tag
    else:
        tag = slugify(instance.tag)

    qs_exists = (instance.__class__).objects.filter(tag=tag).exists()
    if qs_exists:
        new_tag = (tag+"-"+random_string_generator(size=6))
        return unique_slug_generator(instance, new_tag=new_tag)
    return tag
