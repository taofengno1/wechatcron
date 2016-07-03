#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rethinkdb as r

r.connect( "localhost", 28015).repl()

r.db("wetimer").table_create("message").run()