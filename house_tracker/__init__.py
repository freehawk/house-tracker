
import os
import sys
import importlib

from flask import Flask

version = '0.6.0'

root_path = os.path.dirname(os.path.abspath(__file__))

app = None

def get_application():
    from .utils import admin
    
    global app
    if app is None:
        app = Flask(__name__)
        admin.setup(app)
    return app

def run():
    sys.argv = sys.argv[1:]
    module = importlib.import_module('.'+sys.argv[0],
                                     'house_tracker.commands')
    module.run()