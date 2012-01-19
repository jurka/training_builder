# -*- coding: utf-8 -*-

from models import Task, Exercise, Day, Program
from django.contrib import admin

admin.site.register(Exercise)
admin.site.register(Program)
admin.site.register(Day)
admin.site.register(Task)
