from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^form_save.html$', views.form_save, name="form_save"),
    url(r'^next.html$', views.next, name="next"),

]
