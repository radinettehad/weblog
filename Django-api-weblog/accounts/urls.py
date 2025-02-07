from django.urls import path
from .views import signup, login_user, profile,logout_user

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
]