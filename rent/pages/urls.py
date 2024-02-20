from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('', include('pages.urls')),
    path('user/', include('user.urls'))

]