#!/usr/bin/env python

import sys, re, unicode_support_checker
from anki import Collection

def main():

    collection_path = '/Users/jiamingz/Documents/Anki/User 1/collection.anki2'
    deck_name = u'Language::English'
    model_name = u'English Word'
    fact = {
        'Word': 'Word1',
        'Sound': 'Sound1',
        'Image': 'Image',
        'Meaning': 'Meaning'
    }

    m = AnkiManager(collection_path, deck_name, model_name)
    m.add_node(**fact)
    m.save()
    m.close()

class AnkiManager:
    def __init__(self, collection_path, deck_name, model_name):
        self.collection = Collection(collection_path)
        self.select_deck(deck_name)
        self.select_model(model_name)

    def select_deck(self, deck_name):
        deck_manager = self.collection.decks
        deck_id = deck_manager.id(deck_name)
        deck_manager.select(deck_id)
    def select_model(self, model_name):
        model_manager = self.collection.models
        model = model_manager.byName(model_name)
        model_manager.setCurrent(model)

    def add_node(self, **argv):
        node = self.collection.newNote()
        for key in argv:
            node[key] = argv[key].decode('utf-8')
        print node.items()
        self.collection.addNote(node)

    def save(self):
        self.collection.save()

    def close(self):
        self.collection.close()

if __name__ == '__main__':
    main()
