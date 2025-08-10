# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", auth_views.LoginView.as_view(template_name="tracker/login.html"), name="login"),
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
#     # Redirect /accounts/login/ to /login/ to avoid 404s
#     # Include your main app urls (tracker)
#     path('tracker/', include('tracker.urls')),
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
]
