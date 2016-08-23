
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.load_user_page, name='load_user_page'),
	url(r'^sign_up/$', views.add_new_user_manager, name='add_new_user_manager'),
	url(r'^user/new/$', views.add_new_user, name='add_new_user'),
	# url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
	# url(r'^book/new/$', views.add_new_book, name='add_new_book'),
	# url(r'^book/(?P<pk>\d+)/add_name/$', views.add_new_name, name='add_new_name'),
]