from django.shortcuts import render


def theme(request):
    context = {}
    return render(request, 'base.html', context)
