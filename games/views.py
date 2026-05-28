from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Avg
from .models import Game
from reviews.forms import ReviewForm
# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def games(request):

    games = Game.objects.all()

    search_query = request.GET.get('search') or request.GET.get('q')
    genre_filter = request.GET.get('genre')

    if search_query:
        games = games.filter(
            name__icontains=search_query
        )

    if genre_filter:
        games = games.filter(
            genre__icontains=genre_filter
        )

    return render(
        request,
        'pages/games.html',
        context={
            'games': games,
            'search_query': search_query or '',
            'genre_filter': genre_filter or '',
        }
    )

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.select_related('user').order_by('-created_at')
    review_stats = reviews.aggregate(average_rating=Avg('rating'))
    average_rating = review_stats['average_rating']

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            review.save()
            return redirect('game_detail', game_id=game.id)
    else:
        form = ReviewForm()

    return render(
        request,
        'pages/detail.html',
        context={
            'game': game,
            'reviews': reviews,
            'average_rating': average_rating,
            'form': form,
        }
    )
