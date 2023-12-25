import i18n
import os


pytest_plugins = ['common_fixtures', 'data_fixtures']

i18n.load_path.append(os.path.join(os.path.dirname(__file__), 'helpers/translations'))
i18n.set('locale', os.environ["TEST_LANG"])