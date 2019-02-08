#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import requests
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        post_data = request.get_data()
        print(post_data)
        pasermsg(eval(post_data))
        return 'success'
    else:
        return 'weclome to use prometheus alertmanager BOB_TG webhook server!'


def pasermsg(msg):
    for data in msg['alerts']:
        # print('''
        # data['status']
        # data['labels']['alertname']
        # data['labels']['device']
        # data['labels']['fstype']
        # data['labels']['instance']
        # data['labels']['job']
        # data['annotations']['description']
        # data['annotations']['summary']
        # ''')
        status = data['status']
        alertname = data['labels']['alertname']
        device = data['labels']['device']
        fstype = data['labels']['fstype']
        instance = data['labels']['instance']
        job = data['labels']['job']
        description = data['annotations']['description']
        summary = data['annotations']['summary']
        sendmsgtotg(status, alertname, device, fstype, instance, job, description, summary)


def sendmsgtotg(status, alertname, device, fstype, instance, job, description, summary):
    tg_token = '723806405:AAF_x8-giga4HPntMHQCFOepA8D5pnXyiWE'
    chatid = '-369453715'
    request_url = 'https://api.telegram.org/bot{0}/sendMessage'.format(tg_token)
    msg = '''
    *{status}*
    alertname = {alertname}
    device = {device}
    fstype = {fstype}
    instance = {instance}
    job = {job}
    description = {description}
    summary = {summary}
    [BOB Alert Platform.](https://www.bobvip1.com)
    '''.format(status=status, alertname=alertname, device=device, fstype=fstype, instance=instance, job=job, description=description, summary=summary)
    payload = {'chat_id': chatid, 'text': msg, 'parse_mode': 'markdown'}
    req = requests.post(request_url, data=payload)
    print(req.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
