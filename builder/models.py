# -*- coding: utf-8 -*-
from django.db import models


class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_link = models.CharField(max_length=255, blank=True, null=True)
    link_to = models.CharField(max_length=255, blank=True, null=True)
    video_link = models.CharField(max_length=255, blank=True, null=True)
    for_women = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Program(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    for_women = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s (id:%s)" % (self.title, self.number)

    def get_days(self):
        return self.day_set.order_by('week_number', 'day_number').all()


class Day(models.Model):
    pr_id = models.ForeignKey(Program)
    day_number = models.IntegerField()
    week_number = models.IntegerField(default=1)

    def __unicode__(self):
        return u"%s, неделя %s, день %s" % (self.pr_id, self.week_number, self.day_number)

    def get_tasks(self):
        return self.task_set.order_by('order').all()


class Task(models.Model):
    day_id = models.ForeignKey(Day)
    excercise_type = models.ForeignKey(Exercise)
    super_set_number = models.IntegerField(null=True, blank=True, default=0)
    reps = models.CharField(null=True, blank=True, max_length=100)
    order = models.IntegerField(default=1, blank=False)
    is_light_weight = models.BooleanField(default=False)

    def is_super_set(self):
        return self.super_set_number is not 0

    def set_num(self):
        return self.super_set_number % 2 == 0

    def __unicode__(self):
        return "%s: %s" % (self.excercise_type.title, self.reps)
