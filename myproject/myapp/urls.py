from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile_created/', views.profile_created, name='profile_created'),
    path('upload/', views.upload_file, name='upload_file'),
    path('diagnosis/', views.diagnosis_view, name='diagnosis'),
    path('profile/<int:student_id>/', views.match_profile, name='match_profile'),
    path('signup/', views.signup, name='signup'), 
    path('create-profile/', views.create_profile, name='create_profile'),
    path('match-profile/<int:student_id>/', views.match_profile, name='match_profile'),
    path('diagnosis/', views.diagnosis_view, name='diagnosis'),  # diagnosisビューは診断の結果を表示する
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

