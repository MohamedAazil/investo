from django.urls import path
from .views import signup, register_idea, home,investor, chatbot, study, save_profile, investor_dashboard, investor_matches, edit_investor_profile
from .views import chat_view,login,profile_success

urlpatterns = [
    path('login/', login, name='login'),
    path('',signup,name='signup'),
    path('home/', home, name='home'),
    path('register/', register_idea, name='register'),
    path('chatbot/', chatbot, name='chatbot'),
    path('study/', study, name='study'),
    path('investor/',investor,name='investor'),
    path('investor_dashboard/', investor_dashboard, name='investor_dashboard'),
    path('investor_matches/', investor_matches, name='investor_matches'),
    path('edit-profile/', edit_investor_profile, name='edit_investor_profile'), 
    path('chat/<str:email>/', chat_view, name='chat'),
    path('save_profile/', save_profile, name='save_profile'),
    path('profile_success/',profile_success, name='profile_success'),
]