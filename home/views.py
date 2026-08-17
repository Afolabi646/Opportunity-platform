from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Opportunity

def index(request):
    query = request.GET.get("q", "")

    if query:
        opportunities = Opportunity.objects.filter(
            Q(title__icontains=query) |
            Q(organization__icontains=query) |
            Q(description__icontains=query) |
            Q(requirements__icontains=query) |
            Q(category__icontains=query) |
            Q(location__icontains=query) 
        )
    else:
        opportunities = Opportunity.objects.all()


    return render(request, "home/index.html", {
        "opportunities": opportunities,
        "query" : query
    })

def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)

    return render(request, "home/opportunity_detail.html", {
        "opportunity" : opportunity
    })

# Create your views here.
