import logging
import csv
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from simplejson import dumps as json_encode
from time import sleep

from models import Program, Exercise, Day, Task

@login_required(login_url='/admin/login')
def programs_list(request):
    programs = Program.objects.all()
    return render_to_response('builder/programs.html', locals())


@login_required(login_url='/admin/login')
def edit_day(self, day_id):
    logging.error('edit_day')
    day = Day.objects.get(id=day_id)
    return render_to_response('builder/day_edit.html', locals())


@login_required(login_url='/admin/login')
def suggest(self):
    data = Exercise.objects.filter(title__contains=self.GET['term']).all()
    data = map(lambda x: {'label': x.title, 'id': x.id, 'value': x.title}, data)
    return HttpResponse(content=json_encode(data), mimetype='application/x-javascript')


@login_required(login_url='/admin/login')
def task_add(self, day_id):
    logging.error('task_add')
    logging.error(self.POST)

    params = {'warmup': [False],
              'order': ['0'],
              'super_set': ['0']}
    params.update(dict(self.POST))
    params = dict(params)

    for k, val in params.iteritems():
        params.update({k: val[0]})

    if params['super_set'] == '':
        params.update({'super_set': '0'})

    day = Day.objects.get(id=int(day_id))
    if params['order'] == '':
        params.update({'order':str(len(day.get_tasks()))})

    logging.error(params)

    Task.objects.create(**{
                         'day_id': day,
                         'excercise_type': Exercise.objects.get(id=int(params['task_id'])),
                         'super_set_number': int(params['super_set']),
                         'is_light_weight': bool(params['warmup']),
                         'order': int(params['order']),
                         'reps': params['reps'].replace('*', '&bull;')
                         })

    return redirect('/pr/day/' + str(int(day_id)), day_id=int(day_id))


@login_required(login_url='/admin/login')
def load_csv(self):
    reader = csv.reader(open('./base_ex.csv', 'rb'))

    i = True
    for row in reader:
        if i:
            i = False
            continue

        logging.error(row)

        c = Exercise()
        row = map(str, row)
        row = row + ([''] * 5)

        logging.error(row)

        c.title = row[0]
        c.description = row[1]
        c.image_link = row[2]
        c.link_to = row[3]
        c.video_link = row[4]

        c.save()

    return render_to_response('builder/load.html', locals())
    pass


@login_required(login_url='/admin/login')
def task_delete(self, day_id, task_id):
    logging.error('task_delete')
    task = Task.objects.get(id=task_id)
    logging.error(task)
    if task is not None:
        task.delete()
    return redirect('/pr/day/' + str(int(day_id)), day_id=int(day_id))


@login_required(login_url='/admin/login')
def task_reorder(request):
    logging.error(request.POST)
    order_f = request.POST.get(u'order')
    logging.error(order_f)

    pos = 1
    for i in order_f.split('+'):
        task_id = int(i[len('task_id_'):])
        logging.error(task_id)

        task = Task.objects.get(id=task_id)
        if Task:
            task.order = pos
            task.save()
        pos += 1

    sleep(1)

    return HttpResponse(content=json_encode({'res': 'OK'}), mimetype='application/x-javascript')


@login_required(login_url='/admin/login')
def task_ss_save(request):
    logging.error(request.POST)
    number = request.POST.get(u'number')
    task_id = request.POST.get(u'task_id')
    logging.error(number)
    logging.error(task_id)

    task = Task.objects.get(id=int(task_id))
    task.super_set_number = number
    task.save()

    sleep(0.5)

    return HttpResponse(content=json_encode({'res': 'OK'}), mimetype='application/x-javascript')


@login_required(login_url='/admin/login')
def build(request, pr_id):
    program = Program.objects.get(id=int(pr_id))
    return render_to_response('builder/pr_dump.html', locals())

