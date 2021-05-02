from django.shortcuts import render

def ComingSoon(request):
    return render(request, 'solid/index.html', name='comingsoon')