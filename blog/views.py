from django.shortcuts import render


# Create your views here.

posts = [{
    'author': 'Noah',
    'title': 'My first post',
    'content': 'First post content',
    'date_posted': 'August 23, 2021'
},
    {
        'author': 'Tina',
        'title': 'Another post',
        'content': 'Dummy example',
        'date_posted': 'August 23, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
