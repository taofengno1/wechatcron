#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rethinkdb as r

r.connect( "localhost", 28015).repl()

conn = r.connect(db='wetimer')

r.table('message').get_all().run(conn)

query = r.table('message').get_all()
for row in query.run(conn):
    print(row)