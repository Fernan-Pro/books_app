from django.urls import path
from .views import Start, Books, Create, Update, Delete

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', Start, name='home'),
    path('read', Books, name='books'),
    path('books/create', Create, name='create'),
    path('books/update', Update, name='update'),
    path('delete/<int:id>', Delete, name='delete'),
    path('books/update/<int:id>', Update, name='update'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)