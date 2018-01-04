#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']

    style_fields = {"detail": "ueditor"}


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course__name', 'name', 'add_time']
    search_fields = ['course', 'name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson__name', 'name', 'add_time']
    search_fields = ['lesson', 'name']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    list_filter = ['course__name', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
