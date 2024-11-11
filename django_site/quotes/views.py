from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from quotes.forms import AuthorForm, TagForm, QuoteForm
from quotes.models import Author, Tag, Quote

def main(request, page=1):
    quotes_list = Quote.objects.all()

    paginator = Paginator(quotes_list, 10)
    quotes = paginator.get_page(page)

    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]

    return render(request, 'quotes/main.html', {'quotes': quotes, 'top_tags': top_tags})

@login_required(login_url='users:login')
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        fullname = form.data.get('fullname')
        if Author.objects.filter(fullname=fullname).exists():
            messages.error(request, 'An author with this name already exists.')
        if form.is_valid():
            form.save()
            return redirect('quotes:main')
    else:
        form = AuthorForm()
    return render(request, 'quotes/author.html', {'form': AuthorForm()}) #change for FORM in 'form': ..., if not working

@login_required(login_url='users:login')
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})

@login_required(login_url='users:login')
def quote(request):
    authors = Author.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.author = form.cleaned_data['author']
            new_quote.save()
            form.save_m2m()
            return redirect('quotes:main')
    else:
        form = QuoteForm()
    return render(request, 'quotes/quote.html', {'form': form, 'authors': authors, 'tags': tags})

def detail_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})

def detail_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    return render(request, 'quotes/quote_detail.html', {'quote': quote})

def quotes_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    return render(request, 'quotes/quotes_by_tag.html', {'quotes': quotes, 'tag': tag})