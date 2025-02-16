from django import forms
from .models import Category

class AuctionListingForm(forms.Form):
    title = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Give it a title'
        }
        )
    )
    description = forms.CharField(
        label='Description',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Tell more about the product',
            'rows': '3'
        }
        )
    )
    price = forms.DecimalField(
        label='Price',
        required=False,
        initial=0.00,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Estimated price (optional)',
            'min': '0.01',
            'max': '999999999.99',
            'step': '0.01'
        }
        )
    )
    starting_bid = forms.DecimalField(
        label='Starting Bid',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Starting bid',
            'min': '0.01',
            'max': '99999999999.99',
            'step': '0.01'
        }
        )
    )
    category = forms.ModelChoiceField(
            label='Category',
            required=False,
            queryset=Category.objects.all(),
            widget=forms.Select(attrs={
                'class' : 'form-control form-group',
                'placeholder' : "Category (optional)",
                'autocomplete' : 'on'
            })
        )
    image_url = forms.URLField(
        label='Image URL',
        required=False,
        initial='https://www.bahmansport.com/media/com_store/images/empty.png',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Image URL (optional)',
        }
        )
    )

    def clean_starting_bid(self):
        amount = float(self.cleaned_data.get('starting_bid'))
        if isinstance(amount, float) and amount > 0:
            return amount
        print(amount)
        raise forms.ValidationError('Should be a number larger than zero!')



class CommentForm(forms.Form):
    text = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control-md lead form-group',
            'rows': '3',
            'cols': '100'
        }
        )
    )

    def clean_comment(self):
        text = self.cleaned_data.get('text')
        if len(text) > 0:
            return text
        return self.errors
