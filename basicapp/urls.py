from django.conf.urls import url
from basicapp import views

# template urls!
app_name='basicapp'

urlpatterns = [
	url('user_login/',views.user_login,name='user_login'),
	url('register/',views.register),
]