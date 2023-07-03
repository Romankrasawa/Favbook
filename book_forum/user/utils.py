from .forms import *


def registerForm(request):
    data = request.session.get("register_form", None)
    print(data)
    if data != None:
        form = RegisterUserForm(data, request=request)
    else:
        form = RegisterUserForm()
    return {"registerform": form}


def logInForm(request):
    form = LoginUserForm
    return {"loginform": form}
