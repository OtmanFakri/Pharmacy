from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import add

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('add/',add,name="add"),
]