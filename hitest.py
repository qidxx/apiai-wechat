#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os.path
import sys
import werobot
import jsonobject

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


robot = werobot.WeRoBot(token='2333')


CLIENT_ACCESS_TOKEN = ''

class JSONObject:
	def __init__(self, d):
		self.__dict__ = d



@robot.handler

def main(message):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'zh-CN'  # optional, default value equal 'en'

    request.session_id = "123456"

    request.query = message.content

    response = request.getresponse()
#    data = json.loads(response.read().decode('utf-8'))
#    print (data['code'])
#    print (response.read())
    jsonData = response.read()
    data = json.loads(jsonData, object_hook=JSONObject)
#    print jsonData
#    datatext = 'hello,text'
#    data = json.loads(response, object_hook=JSONObject)
    return data.result.fulfillment.speech

robot.config['HOST'] = '106.14.19.134'
robot.config['PORT'] = 80


robot.run()
