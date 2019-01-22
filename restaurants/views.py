from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    'my_list': [
    {
    'restaurant_name':'cupcake',
    'food_type':'bakery'

    },
    {
    'restaurant_name':'pizza',
    'food_type':'italy'
    }


    ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { 
    'my_object' : {
    'restaurant_name': 'Melenzane',
    'food_type':'italiano'
    }

    }
    return render(request, 'detail.html', context)
