from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
# from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import  authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from post.models import Post
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .models import *

#login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                messages.error(request, 'Invalid credientials')
                return render(request,"Users/login.html",{'form':form})
    else:
        form = LoginForm()
    return render(request, "Users/login.html", {'form': form})

#register

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        print(form.__dict__) 
        # print('\n\n\n\n',,'\n\n\n\n')
        # form.dob='2024-01-20'
        if form.is_valid():
            try:
                data = form.cleaned_data
                user = RegisterUser.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password=data['password'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    dob=data['dob'],
                    gender=data['gender'],
                    avatar=data['avatar'],
                    custom_avatar=data['custom_avatar'],
                    phone=data['phone']
                ) 
                user.save()
                messages.success(request, 'User created successfully! Please log in.')
                return redirect('login')
            except Exception as e:
                # Log the error or handle it as needed
                messages.error(request, f'Error creating user: {str(e)}')
        else:
            # This will show the form errors in the console or logs
            print("Form errors:", form.errors)
            messages.error(request, 'Form is not valid. Please correct the errors below.',)
    else:
        form = UserRegisterForm
    return render(request, 'Users/register.html', {'form': form})

    

#logout
@login_required
def logout_user(request):
    logout(request)
    form = LoginForm()
    return redirect('login')


# profile edit   
@login_required
def edit_profile(request, id):
    user = get_object_or_404(RegisterUser, id=id)  
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)  
        if form.is_valid():
            form.save()
            return redirect('home')  
        else:
            return render(request,'Users/edit_profile.html',{'form':form})
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'Users/edit_profile.html', {'form': form})


#forgot password
# def forgot_password(request):
#     if request.method == 'POST':
#         form = ForgotPasswordForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             try:
#                 user = RegisterUser.objects.get(email=data['email'])
#                 user.set_password(data['password'])
#                 user.save()
#                 messages.success(request, 'Your password has been updated successfully.')
#                 return redirect('login')
#             except ObjectDoesNotExist:
#                 form.add_error('email', 'No user found with this email address.')
#     else:
#         form = ForgotPasswordForm()

#     return render(request, 'Users/forgot_password.html', {'form': form})

@login_required
def home(request):
    current_user=request.user
    posts=Post.objects.filter(user=current_user)
    return render(request, 'Users/base3.html',{'posts':posts})

def search_user(request):
    # Extract the search term from the query parameters
    name = request.GET.get('search', '').strip()
    users = RegisterUser.objects.none()  # Initialize with an empty QuerySet

    if name:
        # Perform search in username and first_name fields
        users = RegisterUser.objects.filter(username__icontains=name) | RegisterUser.objects.filter(first_name__icontains=name)
        if not users.exists():
            messages.error(request, "No users found with the given search criteria.")
    
    print(f"Search query: {users}")
    print(f"Number of users found: {users.count()}")
    return render(request, 'Users/search_result.html', {'users': users})
 


def profile(request, id):
    user = get_object_or_404(RegisterUser, id=id)
    posts = Post.objects.filter(user=user)
    print(user.__dict__)
    return render(request, 'Users/profile.html', {'user': user, 'posts': posts})




class PasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


from django.urls import reverse

@login_required
def follow(request, user_id):
    user_to_follow = get_object_or_404(RegisterUser, id=user_id)
    re_user=get_object_or_404(RegisterUser,username=request.user)
    follow_obj = Follow.objects.filter(user=user_to_follow, follower=re_user).exists()

    if user_to_follow != re_user:
        if follow_obj:
            # Unfollow: Delete the follow relation and update counts
            Follow.objects.filter(user=user_to_follow, follower=re_user).delete()
            user_to_follow.followers_count -= 1
            re_user.following_count -= 1
        else:
            # Follow: Create the follow relation and update counts
            Follow.objects.create(user=user_to_follow, follower=re_user)
            user_to_follow.followers_count += 1
            re_user.following_count += 1
        
        # Save the updated counts
        user_to_follow.save()
        re_user.save()
    
    return redirect(reverse('profile', kwargs={'id': user_id}))