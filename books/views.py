from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def Start(request):
    return render(request, 'start.html')

def Books(request):
    books = Book.objects.all()
    return render(request, 'crud/read.html', {'books': books}) 

def Create(request):
    forms = BookForm(request.POST or None, request.FILES or None)
    if forms.is_valid():
        forms.save()
        return redirect('books')
    return render(request, 'crud/create.html', {'forms': forms}) 

def Update(request, id):
    book = Book.objects.get(id=id)
    forms = BookForm(request.POST or None, request.FILES or None, instance=book)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('books')
    return render(request, 'crud/update.html', {'forms': forms}) 

def Delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')