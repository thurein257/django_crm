from django.contrib import admin
from django.urls import path,re_path
from blog.views import record,add_record,data_update,login_user,logout,register,edit,delete,handling_404


urlpatterns = [
    path('', record),
    path('admin/', admin.site.urls),
    path('add_record/',add_record),
    path('data_update/<int:user_id>/', data_update),
    path('edit/<int:user_id>/',edit),
    path('delete/<int:user_id>/',delete),
    path('login/', login_user, name='login'),
    path('register/', register),
    path('logout/', logout, name='logout'),
    re_path(r'^.*/$', handling_404)
]
