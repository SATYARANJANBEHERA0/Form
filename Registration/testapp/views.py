from django.shortcuts import render
from testapp.models import Student
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
# Create your views here.
# def home_page_view(request):
#     return render(request, 'testapp/home.html')
def logout_view(request):
    return render(request,'testapp/logout.html')

# signup form
def signup_view(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'testapp/signup.html',{'form':form})


# retrive view
def retrieve_view(request):
    student_list = Student.objects.all()
    return render(request,'testapp/home.html',{'student_list':student_list})


    # update
def update_view(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance = employee)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})
