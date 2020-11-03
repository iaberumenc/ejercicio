from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    var1 = "Variable 1"
    context = {
        "var1": var1,
    }
    return render(request, "index.html",context)

def list_items(request):
    var1 = "Variable 1"
    query = stock.objects.all()
    context = {
        "var1": var1,
        "query" : query,
    }
    return render(request, "list_items.html",context)
