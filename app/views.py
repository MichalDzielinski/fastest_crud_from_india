from django.shortcuts import render, redirect
from .models import Book
from .forms import  BookCreate
from django.http import HttpResponse

def index(request):
    shelf = Book.objects.all()
    context = {'shelf': shelf}
    return render(request, 'library.html', context)

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong """)
    else:
        return render(request, 'upload_form.html', {'upload_form': upload})
