from django.conf import settings

def add_conference_metadata(request):
    return {
        'conference_name': settings.CONFERENCE_NAME
    }
