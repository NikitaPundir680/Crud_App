from django.test import TestCase

# Create your tests here.
# models.py
from django.db import models

class Employee(models.Model):
    empcode = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    # Other fields...

class Comment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'


# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Comment, Employee
from .forms import CommentForm

def comments_view(request, empcode):
    employee = get_object_or_404(Employee, empcode=empcode)
    comments = Comment.objects.filter(employee=employee)

    form = CommentForm()

    return render(request, 'comments.html', {
        'comments': comments,
        'form': form,
        'empcode': empcode
    })

def add_comment(request, empcode):
    employee = get_object_or_404(Employee, empcode=empcode)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.employee = employee
            comment.save()
            return redirect(reverse('comments_view', kwargs={'empcode': empcode}))
    return redirect(reverse('comments_view', kwargs={'empcode': empcode}))

def read_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    return render(request, 'read_comment.html', {'comment': comment})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(reverse('comments_view', kwargs={'empcode': comment.employee.empcode}))
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    empcode = comment.employee.empcode
    comment.delete()
    return redirect(reverse('comments_view', kwargs={'empcode': empcode}))


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('comments/<str:empcode>/', views.comments_view, name='comments_view'),
    path('add_comment/<str:empcode>/', views.add_comment, name='add_comment'),
    path('read_comment/<int:comment_id>/', views.read_comment, name='read_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]

<form method="post" action="{% url 'add_comment' empcode %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Save Comment</button>
</form>
