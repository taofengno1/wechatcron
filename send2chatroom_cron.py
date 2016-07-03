#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.scheduler import Scheduler
import itchat, time
import rethinkdb as r

r.connect( "localhost", 28015).repl()
itchat.auto_login()

sched = Scheduler()
sched.start()


def task():
  chatroomList = itchat.get_chatrooms(False);
  for m in chatroomList:
    NickName = m['NickName'].encode('utf-8')
    if NickName == u'测试'.encode('utf-8'):
      text = u'可以定时发送了'.encode('utf-8')
      itchat.send(text, m['UserName'])

sched.add_cron_job(task, month='1-12', day_of_week='0-6', hour=19, minute=20)

itchat.run()