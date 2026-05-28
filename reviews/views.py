from django.shortcuts import render

from .models import Review

# Create your views here.
def reviews(request):
    reviews = Review.objects.select_related('game', 'user').order_by('-created_at')

    return render(
        request,
        'pages/reviews.html',
        context={
            'reviews': reviews,
        }
    )
