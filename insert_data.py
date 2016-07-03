#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rethinkdb as r

r.connect( "localhost", 28015).repl()

conn = r.connect(db='wetimer')

r.table("message").insert({
    "content": "Dolor sit amet"
}).run(conn)