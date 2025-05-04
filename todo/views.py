from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from todo.models import TODO
from django.contrib.auth import authenticate,login,logout
from todo import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# The @login_required decorator ensures only logged-in users can access the dashboard.
# If a user is not logged in, they will be redirected to the login page.

def signup(request):
    if request.method=="POST":
        Uname=request.POST.get('uname')
        Email=request.POST.get('mail')
        Pass=request.POST.get('pwd')
        print('your details',Uname,Email,Pass)
        my_user=User.objects.create_user(Uname,Email,Pass)
        my_user.save()
        return redirect('/login')
    return render(request, "signup.html")


def user_login(request):
    if request.method=="POST":
         Uname=request.POST.get('uname')
         Pass=request.POST.get('pwd')
         print('your details',Uname,Pass)
         my_user=authenticate(username=Uname,password=Pass)
         if my_user is not None:
             login(request, my_user) 
            #  Without calling login(), request.user remains AnonymousUser, and @login_required prevents access to /todo/.
            # login() function, which actually logs the user in after authentication.
             return redirect('/todo')
         else:
             error_message = "incorrect username and password"
             return render(request, 'login.html', {'error_message': error_message})

    return render(request,"login.html")
@login_required(login_url='/login/')
def todo(request):
    if request.method == "POST":
        tsk = request.POST.get('task')
        if tsk:  # Avoid empty task creation
            new_task = models.TODO(Tittle=tsk, user=request.user)
            new_task.save()
            res=TODO.objects.filter(user=request.user).order_by('-date')
            return redirect('/todo')
            # return render(request,)
    res=TODO.objects.filter(user=request.user).order_by('-date')
    print(f"Current logged-in user: {request.user}")  # Debugging
    return render(request, 'todos.html',{'res':res} )

def user_logout(request):
    logout(request)
    return redirect('/login')

def updateTodo(request, sr_number):
     if request.method=="POST":
         new_title=request.POST.get('task')
         obj=TODO.objects.get(sr_number=sr_number)
         obj.Tittle=new_title
         obj.save()
         return redirect('/todo')
     task = TODO.objects.get(sr_number=sr_number)
     print('id',task.sr_number,'tittle',task.Tittle)
     res=task.Tittle
     
     return render(request,"update.html",{'res':res})

def deleteTodo(request,sr_number):
    # obj=TODO.objects.get(sr_number=sr_number)
    obj = get_object_or_404(TODO, sr_number=sr_number)
    
    if request.method == 'POST':  # If user confirms the deletion
        obj.delete()
        return redirect("/todo")
    
    return render(request, 'confirm.html', {'todo': obj})
