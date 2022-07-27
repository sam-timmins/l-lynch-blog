from django.shortcuts import render


def contact(request):
    """ contact page """


    context = {

    }

    return render(request, 'contact/contact.html', context)