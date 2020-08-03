from django.shortcuts import render,HttpResponse
from home.models import CarModels, BrandNames
from home.customwork import dynamic_parts, append_service_csv, parts_table_html, rating, rank_html
import os

static_path = os.path.join(os.getcwd(), 'static')
carprofile_path = os.path.join(static_path, 'carprofiles')

no_of_parts = 5  # this will be changed for each car
info = [] # dealership car name contact details etc

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
    print(carprofile_path)
    titlename = 'Home' # for webpage title
    return render(request,'home.html',{'titlename':titlename, 'all_brands':all_brands})

def car_detail(request, username):
    titlename = username # for webpage title
    car = CarModels.objects.filter(car_brand_name=username) # single selected car
    html_table = parts_table_html(car[0], carprofile_path)
    rate = rating(car[0], carprofile_path)
    return render(request,'car_detail.html', {'titlename':titlename, 'all_brands':all_brands, 'car':car[0], 'html_table':html_table, 'rate':rate})

def navsearch(request):
    if request.method == "POST":
        carsearch = request.POST.get('carsearch')
        rended = car_detail(request, (carsearch.lower()).title())
    return rended
    return HttpResponse(f'{carsearch.capitalize()}')

def rank(request):
    html_par = rank_html(carprofile_path)
    
    return render(request, 'rank.html', {'all_brands':all_brands, 'html_par':html_par})

def comp_ask(request):
    all_cars = CarModels.objects.all()
    return render(request, 'comp_ask.html', {'all_brands':all_brands, 'all_cars':all_cars})


def comp_done(request):
    car1 = ''
    car2 = ''
    if request.method == "POST":
        car1 = request.POST.get('car1')
        car2 = request.POST.get('car2')
    car1select = CarModels.objects.filter(car_brand_name=car1)
    car2select = CarModels.objects.filter(car_brand_name=car2)
    return render(request, 'comp_done.html', {'all_brands':all_brands, 'car1':car1select[0], 'car2':car2select[0]})

# servicing below
# level 4
def final_submit(request):
    k = 1
    parts_dict = {}
    if request.method =="POST":
        while k != no_of_parts+1:      # only run till no of parts
            parts_dict[k] = request.POST.get(f'{k}') # dynamically store input according a car`s no. of parts
            k += 1
        feedback = request.POST.get('feedback')
        append_service_csv(info, parts_dict, feedback, carprofile_path)
        print('done')
    return render(request, 'successfull.html', {'all_brands':all_brands})

# level 3
def semi_submit(request):
    if request.method =="POST":
        global info  #
        info.clear() #
        selected_dealer = request.POST.get('selected_dealer')
        info.append(selected_dealer) #
        selected_car = request.POST.get('selected_car')
        info.append(selected_car)    # car name =  info[1]
        emp_name = request.POST.get('name_employee')
        info.append(emp_name)        #
        email = request.POST.get('email')
        info.append(email)           #
        phone_num = request.POST.get('phone')
        info.append(phone_num)       #
        car_sele = CarModels.objects.filter(car_brand_name=selected_car) # used to select one car
        global no_of_parts
        html_parts, no_of_parts = dynamic_parts(car_sele[0].car_brand_name,carprofile_path) # func will return custom input form and no. of parts from unique text file
    titlename = 'Service Info'
    return render(request, 'parts_list.html', {'titlename':titlename, 'all_brands':all_brands, 'html_parts':html_parts})

# level 2
def service_loc(request):
    if request.method =="POST":
        selected_brand = request.POST.get('brandselect') # from level 1
    titlename = selected_brand+' Dealership'
    car2s = CarModels.objects.filter(car_brand_name__startswith=selected_brand)  # for car models in CarModels model
    dealers = BrandNames.objects.filter(brand_cap=selected_brand)   # for dealers in brands model
    return render(request, 'service_loc.html', {'titlename':titlename, 'all_brands':all_brands, 'selected_brand':selected_brand, 'dealers':dealers[0], 'car2s':car2s})

# level 1
def brand_select(request):
    titlename = 'Update'
    return render(request, 'select_brand.html',{'titlename':titlename, 'all_brands':all_brands})

