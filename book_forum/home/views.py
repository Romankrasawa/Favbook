from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name='home/home.html')

def search(request):
    return render(request, template_name='home/search.html')

def search_profiles(request):
    return render(request, template_name='home/search.html')

def search_books(request):
    return render(request, template_name='home/search.html')

def search_discussions(request):
    return render(request, template_name='home/search.html')

def news(request):
    return render(request, template_name='home/news.html')

# def error500(request):
#     return render(request, template_name='home/home.html')

# def error404(request):
#     return render(request, template_name='home/home.html')