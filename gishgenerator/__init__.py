from random import choice
from pkgutil import get_data

animal_list = get_data('gishgenerator', 'data/animals.txt').split('\n')
animal_image_cache = {}

def generate_name():


    name1 = choice(animal_list)
    name2 = choice(animal_list)

    combined_name = name1[:-1] + name2[1:]

    print name1, "+", name2, "=", combined_name

    img1 = get_image_for_text(name1)
    img2 = get_image_for_text(name2)

    return combined_name, img1, img2


def get_image_for_text(text):
    import urllib2
    import json

    if text in animal_image_cache:
        return animal_image_cache[text]
    try:
        fetcher = urllib2.build_opener()
        f = fetcher.open("http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + text + "&start=0")
        data = json.load(f)
        animal_image = data['responseData']['results'][0]['unescapedUrl']
        animal_image_cache[text] = animal_image
        return animal_image
    except:
        return ''