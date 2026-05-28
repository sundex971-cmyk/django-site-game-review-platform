from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.Select(
                choices=[(value, f'{value}/10') for value in range(10, 0, -1)]
            ),
            'text': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'What stood out: gameplay, story, visuals, replay value...',
            }),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 1 or rating > 10:
            raise forms.ValidationError('Rating must be between 1 and 10.')

        return rating
