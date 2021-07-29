from django.shortcuts import render
from .form import ImageForm
from .models import Image

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'base.html', context)


def analysis(request):
    return render(request, 'about.html', {'title': 'Analysis'})

def index(request):
    
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"index.html",{"obj":obj})  
    else:
        form=ImageForm()    
    img=Image.objects.all()
    return render(request,"index.html",{"img":img,"form":form})
