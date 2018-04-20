from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    return render(request, 'index.html')
