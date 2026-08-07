from django.shortcuts import render
# Create your views here.
def demo(req):
    return render(req,"index.html")
def showdata(req):
    first=req.POST['fname']
    last=req.POST['lname']
    dict={'fn':first,'ln':last}
    return render(req,"show.html",dict)