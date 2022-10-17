from django.shortcuts import render

# Create your views here.


def home(request):  # deve obrigatóriamente receber um argumento request que será passado pelo path
    # return HttpResponse('HOME 1') -> função que retorna uma resposta http.
    return render(request, 'recipes/pages/home.html', status=200, context={
        'name': 'Cainan Luyles Gomes do Vale',
    })  # retorna uma página html


def recipe(request, id):  # deve obrigatóriamente receber um argumento request que será passado pelo path
    # return HttpResponse('HOME 1') -> função que retorna uma resposta http.
    return render(request, 'recipes/pages/recipe-view.html', status=200, context={
        'name': 'Cainan Luyles Gomes do Vale',
    })  # retorna uma página html
