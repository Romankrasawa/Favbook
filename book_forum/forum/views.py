from django.shortcuts import render

# Page views
def book(request, book_id):
    return render(request, template_name='book/book.html')

def books(request):
    return render(request, template_name='book/books.html')

def discussion(request, book_id, discussion_id):
    return render(request, template_name='book/discussion.html')

def discussions(request):
    return render(request, template_name='book/discussions.html')    

def category(request):
    return render(request, template_name='book/category.html')

def add_book(request):
    return render(request, template_name='book/add_book.html')

def add_discussion(request, book_id):
    return render(request, template_name='book/add_discussion.html')

def change_book(request, book_id):
    return render(request, template_name='book/change_book.html')

def change_discussion(request, book_id, discussion_id):
    return render(request, template_name='book/change_discussion.html')


#ajax views


#book ajax
def change_book_title(request):
    return render(request, template_name='home/news.html')

def change_book_description(request):
    return render(request, template_name='home/news.html')

def change_book_cover(request):
    return render(request, template_name='home/news.html')

def change_book_background_image(request):
    return render(request, template_name='home/news.html')

def change_book_genre(request):
    return render(request, template_name='home/news.html')

def change_book_similar(request):
    return render(request, template_name='home/news.html')

def add_book_rating(request):
    return render(request, template_name='home/news.html')

def delete_book(request):
    return render(request, template_name='home/news.html')


#discussion ajax
def change_discussion_title(request):
    return render(request, template_name='home/news.html')

def change_discussion_description(request):
    return render(request, template_name='home/news.html')

def change_discussion_status(request):
    return render(request, template_name='home/news.html')

def delete_discussion(request):
    return render(request, template_name='home/news.html')


#comment ajax    
def add_comment(request):
    return render(request, template_name='home/news.html')

def delete_comment(request):
    return render(request, template_name='home/news.html')

def show_comments(request):
    return render(request, template_name='home/news.html')
