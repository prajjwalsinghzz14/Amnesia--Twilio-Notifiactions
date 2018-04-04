from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    #url(r'^d/\d+/$',views.get, name='get'),
    url(r'^next.html$', views.next, name="next"),

]
