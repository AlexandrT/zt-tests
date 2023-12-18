import os
import importlib


DEFAULT_ENV = 'dev'


def set_package():
    return 'zt-tests'


def set_env():
    env = os.environ.get('TEST_ENV')
    return DEFAULT_ENV if env is None else env


settings_module = f"{set_package()}.settings.{set_env()}"


class Settings:
    def __init__(self, settings_module):
        self.SETTINGS_MODULE = settings_module

        try:
            mod = importlib.import_module(self.SETTINGS_MODULE)
        except ModuleNotFoundError:
            mod = importlib.import_module(f"settings.{set_env()}", __package__)

        self._explicit_settings = set()
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)

                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)

    def is_overridden(self, setting):
        return setting in self._explicit_settings

    def __repr__(self):
        return f'<{self.__class__.__name__} "{self.SETTINGS_MODULE}">'


settings = Settings(settings_module)
