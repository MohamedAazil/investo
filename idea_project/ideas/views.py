
from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm, InvestorProfileForm,LoginForm
from .models import VideoResource,SignupDetail,Message
from .forms import SignupForm, MessageForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                # Fetch the user from SignupDetail
                user = SignupDetail.objects.get(email=email)
                
                # Check if the password is correct
                if check_password(password, user.password):
                    # Log the user in
                    user_data = {
                        'email': email,
                        'name': user.name,
                        'category': user.category
                    }
                    request.session['user_data'] = user_data  # Store user data in session
                    
                    # Redirect based on the category
                    if user.category == 'entrepreneur':
                        return redirect('home')
                    elif user.category == 'investor':
                        return redirect('investor_dashboard')
                else:
                    messages.error(request, 'Invalid password')
            except SignupDetail.DoesNotExist:
                messages.error(request, 'User with this email does not exist')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the appropriate dashboard based on the category
            category = form.cleaned_data['category']
            if category == 'entrepreneur':
                return redirect('home')
            elif category == 'investor':
                return redirect('investor_dashboard')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'index.html')
def investor(request):
    return render(request,'investor.html')
def message(request):
    return render(request,'message.html')
def register_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Ensure 'success' is a valid URL name in your urls.py
    else:
        form = IdeaForm()
    return render(request, 'register.html', {'form': form})

def chatbot(request):
    return render(request, 'chatbot.html')

def study(request):
    videos = VideoResource.objects.all()
    return render(request, 'study.html', {'videos': videos})


def save_profile(request):
    if request.method == 'POST':
        form = InvestorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_success')  # Ensure 'profile_success' is a valid URL name in your urls.py
    else:
        form = InvestorProfileForm()
    return render(request, 'investor_profile.html', {'form': form})


def profile_success(request):
    return render(request, 'profile_success.html')


def investor_dashboard(request):
    return render(request, 'investor_dashboard.html')

def investor_matches(request):
    return render(request, 'investor_matches.html')

def investor_messages(request):
    return render(request, 'investor_messages.html')

def edit_investor_profile(request):
    if request.method == 'POST':
        form = InvestorProfileForm(request.POST, instance=request.user.investorprofile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()  # Save the many-to-many data for the form.
            return redirect('investor_dashboard')  # Ensure 'investor_dashboard' is a valid URL name in your urls.py
    else:
        form = InvestorProfileForm(instance=request.user.investorprofile)
    return render(request, 'investor_profile.html')

def get_signup_detail_for_user(user):
    # Ensure user is an instance of Django's User model
    if not user.is_authenticated:
        return None
    # Fetch SignupDetail related to the authenticated user
    return get_object_or_404(SignupDetail, email=user.email)


@login_required
def chat_view(request, email):
    recipient = get_object_or_404(SignupDetail, email=email)
    sender_email = request.session.get('user_data', {}).get('email')
    sender = get_object_or_404(SignupDetail, email=sender_email)
    
    messages = Message.objects.filter(
        (Q(sender=sender) & Q(receiver=recipient)) |
        (Q(sender=recipient) & Q(receiver=sender))
    ).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.receiver = recipient
            message.save()
            return redirect('chat', email=email)
    else:
        form = MessageForm()

    context = {
        'sender': sender,
        'recipient': recipient,
        'messages': messages,
        'form': form,
    }
    
    return render(request, 'chat.html', context)