from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! Your Analytics App is live on AWS!")