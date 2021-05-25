from django.shortcuts import render


def renderContact(request):
    return render(request, "screens/contact.html")