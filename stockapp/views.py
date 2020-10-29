from django.shortcuts import render

# Create your views here.
def index(request):
    var1 = "Variable 1"
    context = {
        "var1": var1,
    }
    return render(request, "index.html",context)