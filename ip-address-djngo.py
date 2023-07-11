from django.shortcuts import render

def index(request):
    ip_address = request.META.get('REMOTE_ADDR')
    return render(request, 'index.html', {'ip_address': ip_address})
