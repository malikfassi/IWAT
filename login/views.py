
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from login.models import UtilisateurForm

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        form = UtilisateurForm(request.POST)
        if(form.is_valid()):
            user = authenticate(username = form.profilBase.username, password=form.profilBase.password)
            if user is not none:
                state = 'logged in'
    else:
        form = UtilisateurForm()

    return render_to_response('login.html',{'message':state, 'form':form})

def main_page(request):
    return render_to_response('index.html')
 
def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')