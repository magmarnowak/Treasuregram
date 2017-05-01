from django.shortcuts import render

def index(request):
    name = 'Gold Nugget'
    value = 1000.00
    context = {'treasure_name': name,
                'treasure_val': value}

    return render(request, 'index.html', context)
