from django.urls import path
from . import views

app_name='Acount'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login',view=views.login,name="login"),


    path('singup',view=views.signup,name="singup"),

    path('Logout',view=views.Lougout,name="Lougout"),

    #path('profile',view=views.profile,name="profile"),

    path('update/<int:id>/',view=views.update,name="profile")

]