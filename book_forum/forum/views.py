from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Page views
def book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    book.views += 1
    book.save()
    form = CreateBook_commentForm
    context = {'form':form,
               'book':book,
               'title': f'Книга {book.title}'
            }
    return render(request, template_name='book/book.html', context=context)

@login_required(login_url=reverse_lazy('home'))
def books(request):
    created_book = request.user.user_book.all()
    liked_book = request.user.liked_book.all()
    disliked_book = request.user.disliked_book.all()
    context = {
        'created_book':created_book,
        'liked_book':liked_book,
        'disliked_book':disliked_book,
        'title': f'Книги'
    }
    return render(request, template_name='book/books.html', context=context)

def discussion(request, book_slug, discussion_slug):
    book = get_object_or_404(Book, slug=book_slug)
    discussion = get_object_or_404(Discussion, Q(slug=discussion_slug) & Q(book = book))
    form = CreateDiscussion_commentForm
    answerform = AnswerDiscussion_commentForm

    context = {'form':form,
               'answerform':answerform,
               'book':book,
               'discussion':discussion,
               'title': f'Обговорення {discussion.title}'
            }
    return render(request, template_name='book/discussion.html', context=context)

@login_required(login_url=reverse_lazy('home'))
def discussions(request):
    created_discussion = request.user.user_discussion.all()
    liked_discussion = request.user.liked_discussion.all()
    disliked_discussion = request.user.disliked_discussion.all()
    context = {
        'created_discussion':created_discussion,
        'liked_discussion':liked_discussion,
        'disliked_discussion':disliked_discussion,
        'title': f'Обговорення'
    }
    return render(request, template_name='book/discussions.html', context=context)

@login_required(login_url=reverse_lazy('home'))
def add_book(request):
    if request.method == "POST":
        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            category = form.cleaned_data['category']
            form.cleaned_data.pop("category", None)
            book = Book.objects.create(**form.cleaned_data, user = request.user)
            book.category.set(category)
            return redirect(book.get_absolute_url())
        return redirect(add_book)
    else:
        form = CreateBookForm
        context = {'form':form,
                   'title': f'Додати книгу'
                   }
        return render(request, template_name='book/add_book.html', context=context)

@login_required(login_url=reverse_lazy('home'))
def add_discussion_comment(request,book_slug,discussion_slug):
    if request.method == "POST":
        book = get_object_or_404(Book, slug=book_slug)
        discussion = get_object_or_404(Discussion, Q(slug=discussion_slug) & Q(book=book))
        form = CreateDiscussion_commentForm(request.POST)
        if form.is_valid():
            Discussion_comment.objects.create(**form.cleaned_data, user = request.user, discussion = discussion)
            return redirect(reverse_lazy('discussion', kwargs = {'book_slug':book_slug, 'discussion_slug':discussion_slug}))
        return redirect(reverse_lazy('discussion', kwargs={'book_slug': book_slug, 'discussion_slug': discussion_slug}))

@login_required(login_url=reverse_lazy('home'))
def add_book_comment(request,book_slug):
    if request.method == "POST":
        book = get_object_or_404(Book, slug=book_slug)
        form = CreateDiscussion_commentForm(request.POST)
        if form.is_valid():
            Book_comment.objects.create(**form.cleaned_data, user = request.user, book = book)
            return redirect(reverse_lazy('book', kwargs = {'book_slug':book_slug}))
        return redirect(reverse_lazy('book', kwargs={'book_slug': book_slug}))

@login_required(login_url=reverse_lazy('home'))
def answer_discussion_comment(request,book_slug,discussion_slug):
    if request.method == "POST":
        book = get_object_or_404(Book, slug=book_slug)
        print(request.POST.get('answer'), request.POST.get('content'))
        answer =  get_object_or_404(Discussion_comment, id = request.POST.get('answer'))
        discussion = get_object_or_404(Discussion, Q(slug=discussion_slug) & Q(book=book))
        content = request.POST.get('content')
        form = AnswerDiscussion_commentForm(request.POST)
        if form.is_valid():
            Discussion_comment.objects.create(content = content, user = request.user, discussion = discussion, answer = answer)
            return redirect(reverse_lazy('discussion', kwargs={'book_slug': book_slug, 'discussion_slug': discussion_slug}))
        return redirect(reverse_lazy('discussion', kwargs={'book_slug': book_slug, 'discussion_slug': discussion_slug}))

@login_required(login_url=reverse_lazy('home'))
def add_discussion(request):
    if request.method == "POST":
        form = CreateDiscussionForm(request.POST)
        if form.is_valid():
            discussion = Discussion.objects.create(**form.cleaned_data, user = request.user)
            return redirect(discussion.get_absolute_url())
        return redirect(add_discussion)
    else:
        form = CreateDiscussionForm()
        return render(request, template_name='book/add_discussion.html', context={"form":form,'title': f'Додати обговорення'})

@login_required(login_url=reverse_lazy('home'))
def add_concrete_discussion(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    form = CreateDiscussionForm(initial={'book': book})
    return render(request, template_name='book/add_discussion.html', context={"form":form,'title':'Додати обговорення'})


#ajax views


#book ajax

@login_required(login_url=reverse_lazy('home'))
def like_book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    if book in request.user.disliked_book.all():
        request.user.disliked_book.remove(book)
        request.user.liked_book.add(book)
    else:
        request.user.liked_book.add(book)
    return HttpResponse("ok")

@login_required(login_url=reverse_lazy('home'))
def dislike_book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    if book in request.user.liked_book.all():
        request.user.liked_book.remove(book)
        request.user.disliked_book.add(book)
    else:
        request.user.disliked_book.add(book)
    return HttpResponse("ok")



#discussion ajax
@login_required(login_url=reverse_lazy('home'))
def like_discussion(request, book_slug, discussion_slug):
    discussion = get_object_or_404(Discussion, slug=discussion_slug)

    if discussion in request.user.disliked_discussion.all():
        request.user.disliked_discussion.remove(discussion)
        request.user.liked_discussion.add(discussion)
        print(discussion, 'in')
    else:
        request.user.liked_discussion.add(discussion)
    print(discussion, 'out',request.user.disliked_discussion.all(),  request.user.liked_discussion.all())
    return HttpResponse("ok")

@login_required(login_url=reverse_lazy('home'))
def dislike_discussion(request, book_slug, discussion_slug):
    discussion = get_object_or_404(Discussion, slug=discussion_slug)
    print(discussion)
    if discussion in request.user.liked_discussion.all():
        request.user.liked_discussion.remove(discussion)
        request.user.disliked_discussion.add(discussion)
    else:
        request.user.disliked_discussion.add(discussion)
    return HttpResponse("ok")

