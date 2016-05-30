#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.scheduler import Scheduler
import itchat, time

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

sched.add_cron_job(task, month='1-12', day='1-31', hour=21, minute=5)

itchat.run()