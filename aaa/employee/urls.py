
from django.urls import path
from .views import home, records_view, read_comment, edit_comment, delete_comment

urlpatterns = [
    path('', home, name='home'),
    path('records/', records_view, name='records'),
    path('records/read/<int:comment_id>/', read_comment, name='read_comment'),
    path('records/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('records/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]

