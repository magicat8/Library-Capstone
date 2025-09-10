from django.shortcuts import render
from .models import OtherProduct

def other_list(request):
    other = OtherProduct.objects.all()
    return render(request, 'other/other_list.html', {'other': other})
