#!/usr/bin/env python
# coding=utf-8

import sys
sys.path.append('/Users/jonathan/wuglearn')
sys.path.append('/usr/local/Cellar/python/2.7/lib/python2.7/site-packages')

from lib import util
import logging
logging.basicConfig(filename='log/server.log', level=logging.DEBUG)

from flask import Flask, url_for, render_template
app = Flask(__name__)

try:
    import local_config
    config = util.hash_object(local_config)
except ImportError:
    config = {
        'host': 'localhost',
        'debug': True
    }

@app.route('/')
def root():
    return render_template('index.haml')

@app.route('/plurals/')
def exp():
    import learner
    argument_hash = {
        'constraints': learner.constraints,
        'constraint_names': learner.constraint_names,
        'word_list': learner.word_list,
        'wug_list': learner.wug_list
    }
    return render_template('experiment.haml', **argument_hash)

if __name__ == '__main__':
    app.run(**config)