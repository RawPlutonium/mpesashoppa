from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^other$',views.other, name='other'),
	url(r'^form_handle$',views.form_handle, name='form_handle'),
	url(r'^callbacks$', views.callbacks, name='callbacks'),
	]