from django.shortcuts import render,HttpResponse
from home.models import CarModels, BrandNames

# Create your views here.
all_brands = BrandNames.objects.all()   # for brand names in nav dropdown

def inter(request, brand_loc):
    cars = CarModels.objects.filter(car_brand_name__startswith=brand_loc) # brand_loc is name of brand and also used to create custom url like /Suzuki/Suzuki Ignis
    titlename = brand_loc # for webpage title
    return render(request,'inter.html',{'titlename':titlename, 'all_brands':all_brands, 'cars':cars, 'brand_loc':brand_loc})

def toyota(request):
    rended = inter(request, 'Toyota')
    return rended

def suzuki(request):
    rended = inter(request, 'Suzuki')
    return rended

def kia(request):
    rended = inter(request, 'Kia')
    return rended

def home(request):
    titlename = 'Home' # for webpage title
    return render(request,'home.html',{'titlename':titlename, 'all_brands':all_brands})

def car_detail(request, username):
    titlename = username # for webpage title
    car = CarModels.objects.filter(car_brand_name=username) # single selected car
    return render(request,'car_detail.html', {'titlename':titlename, 'all_brands':all_brands, 'car':car[0]})

def navsearch(request):
    if request.method == "POST":
        carsearch = request.POST.get('carsearch')
        rended = car_detail(request, (carsearch.lower()).title())
    return rended
    return HttpResponse(f'{carsearch.capitalize()}')



