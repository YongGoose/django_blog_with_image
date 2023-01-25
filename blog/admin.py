from django.contrib import admin
from .models import BLog #from 다음에 있는 마침표는 현재 디렉토리 또는 어플리케이션을 의미합니다.
# Register your models here.
admin.site.register(BLog)