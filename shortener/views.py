from django.shortcuts import render, redirect
import random
from .models import *
from .forms import *
import string

# Create your views here.
def homePage(request):
    return render(request, 'base.html')


def urlShort(request):
    if request.method == 'POST':
        form = URLShortenerForm(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = form.cleaned_data["url"]
            new_url = URLShortener(url=url, slug=slug)
            new_url.save()
            # request.user.urlshort.add(new_url)
            return redirect('/')
    else:
        form = URLShortenerForm()
    data = URLShortener.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'index.html', context)


def urlRedirect(request, slugs):
    data = URLShortener.objects.get(slug=slugs)
    return redirect(data.url)