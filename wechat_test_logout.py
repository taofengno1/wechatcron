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
      text = u'间隔5分钟发送一次测试'.encode('utf-8')
      itchat.send(text, m['UserName'])

sched.add_interval_job(task, minutes=5, start_date='2016-05-30 15:27')

itchat.run()