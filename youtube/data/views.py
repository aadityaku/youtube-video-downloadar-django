from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from pytube import * 

def index(request):
    if request.method == "POST":
        url=request.POST['url']
        video=YouTube(url)
        stream=video.streams.get_highest_resolution()
        stream.download(r'C:\Users\aadit\Desktop\new')
        messages.info(request,"Video dowanload..")
        return render(request,"index.html")
    return render(request,"index.html")