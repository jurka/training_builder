from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^programs/', 'builder.views.programs_list', name='programs_list'),
    url(r'^day/(\d+)$', 'builder.views.edit_day', name='edit_day'),
    url(r'^suggest/exercise/', 'builder.views.suggest', name='suggest'),
    url(r'^add/(\d+)/task', 'builder.views.task_add', name='task_add'),
    url(r'^day/(\d+)/task/(\d+)/detele/', 'builder.views.task_delete', name='task_delete'),
    url(r'^load_db/', 'builder.views.load_csv', name='load_csv'),
    url(r'^task/re_order/', 'builder.views.task_reorder', name='task_reorder'),
    url(r'^task/save_ss/', 'builder.views.task_ss_save', name='task_ss_save'),
    url(r'^build_dump/(\d+)/', 'builder.views.build', name='build'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
