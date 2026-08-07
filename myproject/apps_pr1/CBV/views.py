from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class cars(View):
    car={'Toyota': 2500000,
         'Chervolet': 3000000,
         'Fiat': 1500000,
         'Honda': 2000000
        }
    def get(self,req):
        html="""<body>
        <h1>Car Pricing Details</h1>
        <table border=1>
        <tr>
        <th>Brand</th>
        <th>Price</th>
        </tr>"""
        for brand,price in self.car.items():
            html+=f"""
            <tr>
            <td>{brand}</td>
            <td>{price}</td>
            </tr>"""
        html+="</table></body>"
        return HttpResponse(html)
class CarsView(View):
    car = {
        'Toyota': 2500000,
        'Chevrolet': 3000000,
        'Fiat': 1500000,
        'Honda': 2000000
    }

    def get(self, request):
        # Pass the dictionary context into the template render call
        context = {
            'cars': self.car
        }
        return render(request, 'carshop.html', context)
