from backend.settings import SERVICE_BRANDING
from django.contrib.auth.context_processors import auth
def environments(request):
    return {
        "SERVICE_BRANDING": SERVICE_BRANDING
    }