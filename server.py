#! /usr/bin/env python
# coding=utf-8

from lib import util

from flask import Flask, url_for, render_template
app = Flask(__name__)

try:
  import local_config
  config = util.hash_object(local_config)

except ImportError:
  config = {
    'host': '0.0.0.0',
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