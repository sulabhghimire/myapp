from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from .models import UserProfile, Blog
from django.contrib.auth.decorators import login_required


def register(request):
    if not request.user.is_authenticated:
        if request.method  == 'POST':
            form = UserRegistrationForm(request.POST)
            form2 = ProfileForm(request.POST,request.FILES)
            if form.is_valid() and form2.is_valid():
                user = form.save()
                profile = form2.save(commit = False)
                profile.user = user
                profile.save()
                return redirect('login')
            
        form = UserRegistrationForm()
        form2 = ProfileForm()
        return render(request, 'myapp/register.html', {'form':form, 'form2' : form2})
    
    else:
        return redirect('home')

def bog_list(request):
    query_set = Blog.objects.all()

    context = {
    'posts' : query_set
    }

    return render(request, 'myapp/blogs.html', context)


@login_required
def blog_detail(request, pk):
    post = Blog.objects.get(id=pk)
    return render(request, 'myapp/blog_detail.html', {'post' : post})