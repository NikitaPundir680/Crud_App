# from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
# from .models import Comment, Employee
# from .forms import CommentForm
# from django.http import JsonResponse


# def home(request):
#     empcode = request.GET.get('empcode')
#     selected_employee = None
#     if empcode:
#         selected_employee = get_object_or_404(Employee, empcode=empcode)
#     employees = Employee.objects.all().order_by('empcode')
    
#     context = {
#         'employees': employees,
#         'selected_employee': selected_employee
#     }
#     return render(request, 'home.html', context)

# def records(request):
#     empcode = request.GET.get('empcode')
#     selected_employee = get_object_or_404(Employee, empcode=empcode)
#     comments = Comment.objects.all().order_by('created_at')
#     form = CommentForm()
    
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.save()
#             return redirect(f'/home/records/?empcode={empcode}')

#     if request.method == 'GET' and request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#         comment_id = request.GET.get('empcode')
#         action = request.GET.get('action')
#         comment = get_object_or_404(Comment, empcode=comment_id)
#         return JsonResponse({'text': comment.text})
    
#     return render(request, 'records.html', {
#         'comments': comments,
#         'form': form,
#         'selected_employee': selected_employee,
#     })

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Employee, Comment
from .forms import CommentForm
from django.http import JsonResponse
from django.urls import reverse


def home(request):
    empcode = request.GET.get('empcode')
    selected_employee = None
    if empcode:
        selected_employee = get_object_or_404(Employee, empcode=empcode)
    employees = Employee.objects.all().order_by('empcode')
    
    context = {
        'employees': employees,
        'selected_employee': selected_employee
    }
    return render(request, 'home.html', context)


def records_view(request):
    empcode = request.GET.get('empcode')
    employee = get_object_or_404(Employee, empcode=empcode)
    comments = Comment.objects.filter(employee=employee)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.employee = employee
            comment.save()
            return redirect(f'{reverse("records")}?empcode={empcode}')
    else:
        form = CommentForm()

    return render(request, 'records.html', {'employee': employee, 'comments': comments, 'form': form})

def read_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    return JsonResponse({'text':comment.text})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("records")}?empcode={comment.employee.empcode}')
    return JsonResponse({'text':comment.text}) 

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    empcode = comment.employee.empcode
    comment.delete()
    return redirect(f'{reverse("records")}?empcode={empcode}')
