from django.conf.urls import patterns, url
from ski_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^add_ski/$', views.add_ski, name ='add_ski'),
	url(r'^register/$',views.register, name='register'),
	url(r'^login/$',views.user_login, name='login'),
	url(r'^logout/$',views.user_logout, name='logout'),
	url(r'^search/$', views.search, name='search'),
	url(r'^(?P<category_name_url>\w+)/$',views.category, name='category'),
	url(r'^Skis/(?P<item_name_url>\w+)/$',views.item,name='item'),
	
	)