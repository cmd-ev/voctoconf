from django.shortcuts import render, redirect
from partners.models import Partner
from django.conf import settings

# landingpage
def index(request):
    context = {}
    context['venue_partners'] = Partner.objects.filter(hide=False, bbb__isnull=False).order_by("order")
    context['venueless_partners'] = Partner.objects.filter(hide=False, bbb__isnull=True).order_by("order") # lul :3
    context['page_live'] = settings.PAGE_LIVE or (request.GET.get("preview") is not None)

    if settings.PAGE_LIVE:
        return redirect('eventoverview')
    return render(request, "index.html", context)
