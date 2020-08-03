from django.db import models

# Create your models here.


features = '''1) Comfortable ride over all surfaces, noiseless suspension even over broken roads.<br>
2) Improved overall interior space with increased storage spaces, including 1-litre bottle holders on all doors.<br>
3) Largest-in-segment luggage compartment, well shaped too.<br>
4) Lots of space inside the cabin.<br>
*Disclaimer: Every car can have unique features and can be updated(open Admin then Car Models). Due to time constraints we are leaving this section empty as our main focus is analytics.'''

specification = '''Mileage (upto):-- kmpl<br>
Engine (upto): -- cc<br>
BHP: --<br>
Transmission: Automatic/manual<br>
Seats: --<br>
Boot Space: --L<br>
*Disclaimer: Every car can have unique specs and can be updated(open Admin then Car Models). Due to time constraints we are leaving this section empty as our main focus is analytics .'''

variants_table = '''<tr class="table-active">
						<td>
							1
						</td>
						<td>
							Variant 
						</td>
						<td>
							Rs.Latest Price
						</td>
						
					</tr>
					<tr class="table-success">
						<td>
							2
						</td>
						<td>
							Variant 
						</td>
						<td>
							Rs.25.15 Lakh*
						</td>
						
					</tr>
					<tr class="table-warning">
						<td>
							3
						</td>
						<td>
							Variant 
						</td>
						<td>
							Rs.Latest Price
						</td>
						
					</tr>
					<tr class="table-danger">
						<td>
							4
						</td>
						<td>
							Variant 
						</td>
						<td>
							Rs.Latest Price
						</td>
						
					</tr>
<tr class="table-active">
						<td>
							5
						</td>
						<td>
							Variant 
						</td>
						<td>
							Rs.Latest Price
						</td>
						
					</tr>
					<tr class="table-success">
						<td>
							6
						</td>
						<td>
							Variant 
						</td>
						<td>
							Rs.Latest Price
						</td>
						
					</tr>'''

branddesc = '''<option>Toyota ABC motors, Gurugram</option>
<option>Toyota KLF motors, Faridabad</option>
<option>Toyota Avenue motors, New Delhi</option>
<option>Toyota Plaza motors, Mumbai</option>'''

class CarModels(models.Model):
    car_brand_name = models.CharField(max_length=100, null='imp')
    price = models.CharField(max_length=150, default='starting at ₹lakhs')
    mileage = models.CharField(max_length=150, default='14kmpl')
    
    #short_desc = models.TextField(default=car_desc)
    feat = models.TextField(default=features)
    specs = models.TextField(default=specification)
    variants = models.TextField(default=variants_table)
    category = models.CharField(max_length=100, null='imp')

    def __str__(self):
        return self.car_brand_name

class BrandNames(models.Model):
    brand_cap = models.CharField(max_length=100)
    brand_desc = models.TextField(null='fd')
    dealership_loc = models.TextField(default=branddesc)
    
    
    def __str__(self):
        return self.brand_cap