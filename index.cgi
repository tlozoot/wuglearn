#! /usr/bin/env python
from wsgiref.handlers import CGIHandler
from server import app

CGIHandler().run(app)