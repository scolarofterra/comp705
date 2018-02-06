from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    context = {} #an empty dictionary
    return render(request, 'home.html', context)
def resume(request):
    '''
    Renders resume page
    '''
    context = {} #an empty dictionary
    return render(request, 'resume.html', context)
def contact(request):
    '''
    Renders home page
    '''
    context = {} #an empty dictionary
    return render(request, 'contact.html', context)
def portfolio(request):
    '''
    Renders resume page
    '''
    context = {} #an empty dictionary
    return render(request, 'portfolio.html', context)