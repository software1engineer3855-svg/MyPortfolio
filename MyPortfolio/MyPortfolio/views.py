from django.shortcuts import render
from dashboard.models import Hero,About_Me,Services,Education,lenguage,project,testimonial,touch
def homeP(request):
    return render(request, "index.html", {
    "hero": Hero.objects.last(),
    "about": About_Me.objects.last(),
    "service": Services.objects.all(),
    "education":Education.objects.all(),
    "language":lenguage.objects.all(),
    "project":project.objects.all(),
    "testim":testimonial.objects.all(),
    "touch":touch.objects.last(),
})

    