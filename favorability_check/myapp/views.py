from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, UserProfileForm, UploadFileForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
import subprocess
import os
from django.conf import settings
import logging

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

@login_required
def profile_view(request, user_id=None):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    users = User.objects.exclude(id=request.user.id)
    selected_user_profile = None

    if user_id:
        selected_user = get_object_or_404(User, id=user_id)
        selected_user_profile, created = UserProfile.objects.get_or_create(user=selected_user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'myapp/profile.html', {
        'form': form,
        'users': users,
        'selected_user_profile': selected_user_profile
    })

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')


def handle_uploaded_file(f):
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def run_c_analysis(file_path):
    # Cプログラムを呼び出し、ファイルを分析
    process = subprocess.Popen(['./diagnosis', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        return f"Error occurred: {error.decode('utf-8')}"
    return output.decode('utf-8')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            result = run_c_analysis(file_path)
            return render(request, 'myapp/result.html', {'result': result})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload.html', {'form': form})

import logging
import os
import subprocess
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SignUpForm, UploadFileForm, UserProfileForm
from .models import UserProfile

# ロガーの作成
logger = logging.getLogger(__name__)

# 他のビュー関数...

@login_required
def diagnosis_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            
            logger.debug(f"Uploaded file path: {file_path}")
            
            # 一時ディレクトリにファイルを保存
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # C言語のプログラムを呼び出して結果を取得
            try:
                executable_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../bin/diagnosis')
                logger.debug(f"Executable path: {executable_path}")
                
                result = subprocess.run(
                    [executable_path, file_path],  # 実行ファイルと入力ファイルを指定
                    capture_output=True,
                    text=True,
                    check=True,
                    encoding='utf-8',  # ここでエンコーディングを指定
                    errors='replace'  # エンコーディングエラー時に置換
                )
                diagnosis_result = result.stdout
                logger.debug(f"Diagnosis Result: {diagnosis_result}")
            except subprocess.CalledProcessError as e:
                diagnosis_result = f"Error: {e}"
                logger.error(f"Subprocess Error: {e}")
            except UnicodeDecodeError as e:
                diagnosis_result = f"Unicode Decode Error: {e}"
                logger.error(f"Unicode Decode Error: {e}")
            
            # 一時ファイルを削除
            os.remove(file_path)
            
            return render(request, 'myapp/diagnosis.html', {'diagnosis_result': diagnosis_result})
    else:
        form = UploadFileForm()
    
    return render(request, 'myapp/upload.html', {'form': form})

# 他のビュー関数...
