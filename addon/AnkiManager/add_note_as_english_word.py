import requests, os, urllib, sys
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from anki_manager import AnkiManager

sys.path.append('/Library/Python/2.7/site-packages')
import xmltodict

THESAURUS_APP_KEY = 'a9b47f0e-456f-4aaa-a99a-e0573b1647e3'

COLLECTION_PATH = u'/Users/jiamingz/Documents/Anki/User 1/collection.anki2'
DECK_NAME       = u'Language::English'
MODEL_NAME      = u'English Word'

def main():

    words = raw_input('Please type a word or words seperated by comma: ')

    for word in words.split(','):

        word = word.strip()
        print 'Making a note for "%s"' % word

        meaning = get_word_meaning(word)
        sound   = get_word_sound(word)

        fields = { 'Word': word, 'Sound': sound, 'Meaning': meaning }
        print fields

        # anki_manager = AnkiManager(COLLECTION_PATH, DECK_NAME, MODEL_NAME)
        # anki_manager.add_node(fields, ['todo'])

    # anki_manager.save()
    # anki_manager.close()

def get_word_meaning(word):
    dict_url = 'http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/%s?key=%s' % (word, THESAURUS_APP_KEY)
    response = requests.get(dict_url)
    if response.ok:
        xmldict = xmltodict.parse(response.text)
        pass
    return 'meaning ...'

def get_word_sound(word):
    sound_url = 'http://dict.youdao.com/dictvoice?audio=%s&type=1' % word
    directory = 'tmp'
    filename = '%s.mp3' % word
    pathname = '%s/%s' % (directory, filename)
    if not does_file_exist(pathname):
        urllib.urlretrieve(sound_url, pathname)
    return filename

def does_file_exist(pathname):
    return os.path.isfile(pathname)


if __name__ == '__main__':
    main()
