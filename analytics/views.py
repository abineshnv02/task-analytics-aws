from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>CI/CD Pipeline Active!</h1><p>Deployed from feature-update-view branch via GitHub Actions.</p>")