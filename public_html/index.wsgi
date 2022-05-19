# import os
# import sys
# sys.path.append('/home/c/cj37708/gallery/public_html/venv/lib/python3.6/site-packages/')
# from flask import Flask
# app = Flask(__name__)
# application = app
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# if __name__ == '__main__':
#     app.run()

###########

# activate_this = 'ПУТЬ_ДО_ОКРУЖЕНИЯ/bin/activate_this.py'
# exec(open(activate_this).read())
 
# import sys
# sys.path.remove('/usr/lib/python3/dist-packages')
# sys.path.insert(0, 'ПУТЬ_ДО_ПРОЕКТА')
# sys.path.insert(1, 'ПУТЬ_ДО_ПАКЕТОВ_PYTHON')
 
# from ИМЯ_МОДУЛЯ import app as application

import os
import sys

sys.path.append('/home/c/cj37708/gallery/public_html/venv/lib/python3.6/site-packages/')
sys.path.append('/home/c/cj37708/gallery/public_html/')
from main import app as application
