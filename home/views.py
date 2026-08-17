from django.shortcuts import render, get_object_or_404
from .models import Opportunity

def index(request):
    opportunities = Opportunity.objects.all()


    return render(request, "home/index.html", {
        "opportunities": opportunities
    })

def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)

    return render(request, "home/opportunity_detail.html", {
        "opportunity" : opportunity
    })

# Create your views here.
