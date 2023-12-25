import i18n
import os


class CustomTranslator:
    def __init__(self):
        self.locale = i18n.config.get('locale')
        i18n.resource_loader.load_directory(os.path.join(os.path.dirname(__file__), 'translations'), self.locale)

    def get_translator(self, key):
        return i18n.translations.container[self.locale][key]
