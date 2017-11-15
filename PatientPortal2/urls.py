from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='patient_login'),
    url(r'^$', views.index, name='patient_login'),
    url(r'^login', views.logina, name='patient_login'),
    url(r'^signup', views.register, name='patient_register'),

]
