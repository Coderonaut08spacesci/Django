from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home1(req):
    return render(req,"index1.html")
def menudets(req,mid):
    menu={1:{'name':'Ramen', 
             'pic':'https://www.sidechef.com/recipe/051f5aff-8625-4616-8aa5-1581890442df.jpg', 
             'desc':'A Japanese noodle soup consisting of wheat noodles, a rich savory broth, and various toppings.', 
             'price':150, }, 
          2:{'name':'Sushi', 
             'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBb8aCSnC_klMtTbT_8iHG85JmZg_quc5IUryUHtF9XtzVvu_Cbp6tqMGA&s=10', 
             'desc':'Rice seasoned with sweetened vinegar and often topped or filled with a variety of ingredients such as seafood (both raw and cooked) and vegetables.', 
             'price':200,}, 
          3:{'name':'Matcha Latte', 
             'pic':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqAMHgwNHUEX-gjjlJOVmFeVI2QedglEv7j2ivTxkmrg&s=10', 
             'desc':'a creamy drink made from finely ground green tea powder, hot water, and steamed milk or a plant-based milk substitute.', 
             'price':80,}, 
          } 
    html=f""" 
         <h1>{menu[mid]['name']}</h1> 
         <img src='{menu[mid]['pic']} height='30%' width='30%'> 
         <p><i>{menu[mid]['desc']}</i></p> 
         <p><i>Price: Rs.{menu[mid]['price']}/-</i></p> 
    """ 
    return HttpResponse(html) 
    