#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMinxin(object):
    """
    验证用户是否登陆
    """

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMinxin, self).dispatch(request, *args, **kwargs)
