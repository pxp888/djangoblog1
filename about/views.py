from django.shortcuts import render
from .models import AboutPost
from django.http import HttpResponse

# Create your views here.

def about_page(request):
    queryset = AboutPost.objects.all()
    try:
        about = queryset[0]
    except Exception as e:
        print(e)
        return render(request, "about/about.html", )

    return render(request, "about/about.html", {"about": about} )

