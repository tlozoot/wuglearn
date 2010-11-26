#! /usr/bin/env python
# coding=utf-8

from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.haml')

@app.route('/exp/<experiment>/')
def exp(experiment):
  return "Hello, " +  experiment

if __name__ == '__main__':
  app.run(debug=True)