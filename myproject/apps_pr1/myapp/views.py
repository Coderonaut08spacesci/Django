from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

from django.shortcuts import render

def index_view(request):
    # Django automatically looks inside your app's "templates" folder, 
    # so you just specify the path relative to that folder.
    return render(request, 'myapp/form.html')


def home(request): 
    html="<h1 style='background-color:lightyellow;color:red;text-align:center'>The Cold Coffee</h1>" 
    crt=datetime.now().hour 
    if crt>1 and crt<=12: 
        html+="<h4>Good morning user</h4>" 
    elif crt>12 and crt<=17: 
        html+="<h4>Good afternoon user</h4>" 
    elif crt>17 and crt<=24: 
        html+="<h4>Good evening user</h4>" 
    else: 
        html+="<h4>Good to see you at this time</h4>" 
    html+="""<p>Today's Special</p> 
    <ol type='I'> 
    <li>Espresso</li> 
    <li>Americano</li> 
    <li>Latte</li> 
    <li>Matcha Latte</li> 
    </ol>""" 
    return HttpResponse(html)

def books_section(request):
    html="""<body style='background-color:lightgreen;'><h1 style="background-color:yellow;text-align:center">Top 3 Mystery Thrillers</h1> 
    <br>
    <h5 style='text-align:right;color:red'>...Read a thriller while sipping your hot latte...</h5>
    """ 
    books={1:{'authname':'Freida McFadden', 
              'bookname':'The Housemaid', 
              'price':350}, 
           2:{'authname':'Freida McFadden', 
              'bookname':'The Tenant', 
              'price':250}, 
           3:{'authname':'Blake Pierce', 
              'bookname':'Once Lost', 
              'price':400} 
           } 
    for key,value in books.items(): 
        html+=f""" 
            <ul><li style='color:blue;'>{key}.Book name: {value['bookname']}</li> 
            <li style='color:yellow;'>Author: {value['authname']}</li> 
            <li style='color:red;'>Price: {value['price']}</li> 
            </ul> 
            </body>
            """ 
    return HttpResponse(html)
def bookspage(req):
    books= {1:{'authname':'Freida McFadden', 
              'pic':'1.jpg',
              'bookname':"The Housemaid", 
              'price':350,
              }, 
           2:{'authname':'Freida McFadden',
              'pic':'2.jpg',
              'bookname':'The Tenant', 
              'price':250}, 
           3:{'authname':'Blake Pierce', 
              'pic':'3.jpg',
              'bookname':'Once Lost', 
              'price':400} 
              } 
    return render(req,'myapp/booklist.html',{'books':books})

def table(request): 
    emp={'fname':'John','lname':'Doe','dept':'Hr','Salary':25000} 
    op="""<h1>Employee Details</h1> 
          <table border=1> 
          <tr> 
              <td>Firstname</td> 
              <td>Lastname</td> 
              <td>Deptment</td> 
              <td>Salary</td> 
          </tr> 
     """ 
    op+=f"""<tr> 
              <td>{emp['fname']}</td> 
              <td>{emp['lname']}</td> 
              <td>{emp['dept']}</td> 
              <td>{emp['Salary']}</td> 
          </tr> 
          </table> 
    """ 
    return HttpResponse(op)


