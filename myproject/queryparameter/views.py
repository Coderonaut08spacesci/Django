from django.shortcuts import render
# Create your views here.
def setform(req):
    return render(req,"index.html")
def getform(req):
    first=req.GET['fname']
    last=req.GET['lname']
    emp={'fname':first,'lname':last}
    return render(req,"view.html",emp)
