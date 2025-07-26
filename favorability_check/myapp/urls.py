from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/<int:user_id>/', views.profile_view, name='view_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('diagnosis/', views.diagnosis_view, name='diagnosis'),  # diagnosisビューは診断の結果を表示する
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
