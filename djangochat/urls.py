from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # dinh nghia mot duong dan truy cap vao giao dien admin
    path('admin/', admin.site.urls),
    # dinh nghia mot duong dan rong, cho phep dinh nghia cac duong dan rieng cho ung dung chat trong tep chat/urls.py
    path('', include('chat.urls'))
]
