import os
import re
import json


class BaseConfig(object):
    PORT = os.environ.get('PORT', 5000)
    ROOT_PATH = re.split('\Wmain', os.getcwd())[0]
    SERVER_VERBOSE_LOGS = False
    SMTP_EMAIL_ID = os.environ.get('SMTP_PASSWORD', 'gaurav.mishra.cx@gmail.com')
    SMTP_SERVER_ID = 'smtp.gmail.com'
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', 'default')
    WEAK_CHECKING = True
    SECURITY_PASSWORD_SALT = b'salty'
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    MAIL_EXPIRATION = 50000000
    DEBUG = True
    MAIL_FLAG = True
    TESTING = True
    SMTP_PASSWORD = 'weserve$123'
    BASE_URL = 'http://localhost:5000/'
    DB_URI = os.environ.get('SMTP_PASSWORD', 'default')
    SERVER_VERBOSE_LOGS = True


config = {
    "development": "ws_main.unity.configuration.DevelopmentConfig",
    "default": "ws_main.unity.configuration.DevelopmentConfig"
}


def configure_app(app, mode='FILE'):
    if mode == 'FILE':
        app.config.from_file(filename=f'{os.path.dirname(app.root_path)}/.env.json', load=json.load)
    else:
        print(os.getenv('FLASK_CONFIGURATION', 'default'))
        config_name = os.getenv('FLASK_CONFIGURATION', 'deployment')
        app.config.from_object(config[config_name])

    # print(app.config)
