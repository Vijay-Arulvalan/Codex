#9.1 (Exercise)
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_server = 0  #9.4

    def describe_restaurant(self):
        print("The Restaurant name is " + self.restaurant_name.title()+ ".")
        print("We have these type of cuisine " + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open ")

    def set_number_served(self, number): #9.4
        self.number_server = number

    def increment_number_served(self, inc):
        self.number_server += inc

    def read_served(self):
        print(str(self.number_server) + ' has been served')

restaurant = Restaurant('central_perk', 'non_veg')
print('Hi there we opened a new restaurant ' + restaurant.restaurant_name.title() + ' and we have ' + restaurant.cuisine_type.title() + '.')
restaurant.describe_restaurant()
restaurant.open_restaurant()

hotel = Restaurant('A2B', 'veg')
print('\nOne more ' + hotel.restaurant_name.title() + " and " + hotel.cuisine_type + '.')
hotel.describe_restaurant()
hotel.open_restaurant()
hotel.set_number_served(10) #9.4
hotel.read_served() #9.4
hotel.increment_number_served(40)#9.4
hotel.read_served()#9.4
