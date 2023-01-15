from django.urls import path,include
from . import views
app_name='Home'
urlpatterns = [
    #path('admin/', admin.site.urls),
   
    path('',view=views.HomePage,name="home"),
    path('json',view=views.datas,name='json'),


]