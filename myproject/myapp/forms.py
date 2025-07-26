# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile




class UploadFileForm(forms.Form):
    file = forms.FileField()

# myapp/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'gender', 'student_id', 'password', 'age', 'profile', 'image_url']
# myapp/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    hobbies = forms.MultipleChoiceField(
        choices=[
            ('101', 'Mrs.GREEN APPLE'), ('102', 'back number'), ('103', 'RADWIMPS'),
            ('104', 'SEKAINOWARI'), ('105', 'Saucy Dog'), ('106', 'King Gnu'),
            ('107', 'ONE OK ROCK'), ('108', 'Vaundy'), ('109', 'クリープハイプ'),
            ('110', 'Official髭男dism'), ('111', '洋楽'), ('201', 'イタリア料理'),
            ('202', '中華料理'), ('203', '焼肉'), ('204', 'ラーメン'), ('205', 'スイーツ'),
            ('301', 'サッカー'), ('302', '野球'), ('303', 'バレーボール'), ('304', 'フットサル'),
            ('305', 'バドミントン'), ('306', 'テニス'), ('307', '卓球'), ('308', '陸上'),
            ('309', 'バスケットボール'), ('310', '水泳'), ('311', 'ゴルフ'), ('312', '自転車'),
            ('313', 'ボーリング'), ('400', '映画鑑賞'), ('500', '筋トレ'), ('600', 'カフェ巡り'),
            ('700', 'ディズニー'), ('800', 'ジブリ'), ('900', 'Netflix'), ('1000', 'カラオケ'),
            ('1100', '旅行'), ('1200', 'フェス'), ('1301', '電話派'), ('1302', 'LINE派'),
            ('1303', 'インスタ派'), ('1304', 'X (Twitter)派')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = UserProfile
        fields = ['name', 'gender', 'student_id', 'password', 'age', 'profile', 'image_url', 'hobbies']

