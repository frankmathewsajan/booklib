from django.shortcuts import render, redirect
import requests
from ..models import Book, Genre
from django.contrib.auth.decorators import login_required

def index(request):
    if not request.user.is_authenticated: return redirect('welcome')
    books = get_books_by_multiple_genres(request.user.favorite_genres.all())
    try:
        g = []
        for book in books:
            if book['volumeInfo']['categories']:
                for i in book['volumeInfo']['categories']:
                    if i not in g:
                        g.append(i)
        for i in g:
            Genre.objects.get_or_create(genre=i) 
    except:
        pass                 
    return render(request, "library/index.html", {'books':books, 'genres': Genre.objects.all()})
    

def profile(request):
    if not request.user.is_authenticated: return redirect('welcome')
    return render(request, "library/profile.html", {
        'favorite_genres': request.user.favorite_genres.all()
    })


def welcome(request):
    return render(request, "library/welcome.html")


def choice(request):
    if request.method == 'POST':
        selected_genres = request.POST.getlist('genre') 
        if request.user.is_authenticated:
            request.user.favorite_genres.clear()
            for genre_name in selected_genres:
                genre, _ = Genre.objects.get_or_create(genre=genre_name)  
                request.user.favorite_genres.add(genre)

            request.user.save()  
            return redirect('profile') 
        else:
            return redirect('welcome') 

    return render(request, "library/choice.html", {
        'genres': Genre.objects.all()
    })


def get_books_by_genre(genre):
    api_url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': f'subject:{genre}',
        'maxResults': 6
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])  # Extract the list of books
    else:
        return None  # Handle errors
    
def get_books_by_multiple_genres(genres):
    all_results = []
    for genre in genres:
        results = get_books_by_genre(genre) 
        if results:
            all_results.extend(results)  

    return all_results[:12]   