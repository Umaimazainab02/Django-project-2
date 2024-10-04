
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, "home.html")


def about(request):
    teacher_list = [
        {
            "name": "Ahmad",
            "contact": "030588857"
        },
        {
            "name": "Abdullah",
            "contact": "0307665325"
        },
        {
            "name": "Alii",
            "contact": "0308888889999"
        }
    ]   
    return render(request, "about.html", {'data': teacher_list})


def contact(request):
    pass