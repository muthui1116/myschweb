from django.shortcuts import render


posts = [
    {
        'author': 'kyalo',
        'title': 'bio 3',
        'topic': 'reproduction',
        'sub_topic': 'female reproduction',
        'description': 'in femele reproduction ...',
        'created_date': '3 Jun, 2022',
    },
    {
        'author': 'muthui',
        'title': 'bio 3',
        'topic': 'reproduction',
        'sub_topic': 'male reproduction',
        'description': 'in male reproduction ...',
        'created_date': '4 Jun, 2022',
    },
]


def home(request):
    context = {
            'posts': posts,
        }
    return render(request, 'myschapp/home.html', context)


def about(request):
    return render(request, 'myschapp/about.html', {'title': 'About'})


