from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <body style="background: linear-gradient(to right, #4facfe, #00f2fe); 
                     font-family: Arial; text-align: center; color: white; padding-top: 100px;">
            <h1 style="font-size: 50px;">🚀 CI/CD Pipeline Active in your laptop!</h1>
            <p style="font-size: 20px;">
                Deployed from <b>feature-update-view</b> via GitHub Actions.
            </p>
        </body>
    """)