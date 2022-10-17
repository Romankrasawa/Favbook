from .forms import *

def registerForm(request):
    form = RegisterUserForm
    return {'registerform':form}

def logInForm(request):
    form = LoginUserForm
    return {'loginform':form}
