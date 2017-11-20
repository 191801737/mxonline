#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random
from django.core.mail import send_mail


from user.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def random_str(random_length=8):
    result = ''.join(random.sample(string.ascii_letters + string.digits, random_length))
    return result


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册激活链接'
        email_body = '请点击下面链接: http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '密码重置链接'
        email_body = '请点击下面链接: http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = '邮箱修改验证码'
        email_body = '邮箱验证码为:{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass