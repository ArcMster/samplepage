from django.shortcuts import render
from .models import Audios

# Create your views here.
def home(request):
    audio_files = Audios.objects.all()
    all_audio = []
    for i in audio_files:
        all_audio.append(i)

    return render(request,'home.html',{'audios': all_audio})