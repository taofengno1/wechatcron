#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import itchat, time

itchat.auto_login()

def task():
  chatroomList = itchat.get_chatrooms(False);
  for m in chatroomList:
    NickName = m['NickName'].encode('utf-8')
    if NickName == u'测试'.encode('utf-8'):
      text = u'中文群发测试'.encode('utf-8')
      itchat.send(text, m['UserName'])

sched = BlockingScheduler()
sched.add_job(task, 'cron', month='1-12', day='1-31', hour=14, minute=32)
sched.start()
