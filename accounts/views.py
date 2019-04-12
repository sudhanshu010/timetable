from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import LoginForm,AdminLoginForm, SignupForm
# Create your views here.

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage



User = get_user_model()


@login_required
def Admin_home(request):
    return render(request,"accounts/admin_home.html")


@login_required
def Faculty_home(request):
    # send_mail('Hello','Kushal Vijay','kushvijay38@gmail',
    #           ['vijaykushal8118@gmail.com'],
    #           fail_silently=False)
    return render(request,"accounts/faculty_home.html")


def Login_View(request):
    form =  LoginForm(request.POST or None)
    print('yes')
    context = {'next': request.GET.get('next','')}
    print(context)

    if form.is_valid():
        redir = request.POST['next']
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,
                            username=username,
                            password=password)
        if user:
            login(request,user)
            print(request.user.username)
            if redir:
                return redirect(redir)
            return redirect("/faculty_home")
        else:
            print("Error1")
    return render(request,"accounts/login.html",context)

def Admin_Login_View(request):
    form =  AdminLoginForm(request.POST or None)

    context = {'next': request.GET.get('next','')}
    if form.is_valid():
        redir = request.POST['next']
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:

            login(request,user)
            if redir:
                return redirect(redir)
            messages.info(request,"Successfully Logged In")
            return redirect("/admin_home")  #To be changed ,where we need to be redirected after the process
        else:
            print("Error2")
    return render(request,"accounts/login.html")

# def FRegister_View(request):
#     form =  RegisForm(request.POST or None)
#
#     if form.is_valid():
#
#         username = form.cleaned_data.get("username")
#         email    = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         new_user = User.objects.create_user(username,email,password)
#         return redirect("/login")
#
#     return render(request,"accounts/facultyregister.html")


def FRegister_View(request):
    print(1)
    if request.method == 'POST':
        print(2)
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            print(3)
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            # form = SignupForm()
            return render(request, 'accounts/facultyregister.html', {'form': form})
    else:
        return render(request, 'accounts/facultyregister.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def ARegister_View(request):
    print(1)
    if request.method == 'POST':
        print(2)
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            print(3)
            user = form.save(commit=False)
            user.is_active = False
            user.is_staff = True
            # user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'accounts/facultyregister.html', {'form': form})

def Logout_view(request):

    logout(request)
    messages.info(request,"Succefully Logged Out")
    return redirect("/")


