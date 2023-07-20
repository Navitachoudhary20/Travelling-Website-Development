from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('registration', views.Auth,name = 'Auth'),
    path('successful',views.successful,name = 'successful'),
    path('about',views.about,name = 'about'),
    path('contact_us',views.contact_us,name = 'contact_us'),
    path('login_or_signup',views.login_or_signup,name = 'login_or_signup'),
    path('home',views.home,name = 'home'),
    path('',views.index,name = 'index'),
]
# from django.urls import path 
# from Travelling import views 
# urlpatterns = [ 
#   # path('admin/', admin.site.urls), 
#   path('register', views.register,name='register'), 
#   #path('show',views.show), 
#   path('success',views.success),
# ]