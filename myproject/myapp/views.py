from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UserProfile
from .forms import UserProfileForm

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_created')
    else:
        form = UserProfileForm()
    return render(request, 'myapp/create_profile.html', {'form': form})

def profile_created(request):
    return render(request, 'myapp/profile_created.html')



def diagnosis_view(request):
    return render(request, 'myapp/diagnosis.html')

def match_profile(request, student_id):
    profile = get_object_or_404(UserProfile, student_id=student_id)
    return render(request, 'myapp/profile.html', {'profile': profile})

# アップロードされたファイルを処理する関数を追加します
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
