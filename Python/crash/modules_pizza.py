import pizza
#When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program.”

pizza.make_pizza(12, 'pepperoni')
pizza.make_pizza(22, 'cheese', 'green pepper', 'onions')

###module_name.function_name()

###import specific function in the module: “from module_name import function_name”

#from pizza import make_pizza

###using as to give a function an alias (if the name of the funtion is too long we can change it name as short using the command)
###“from module_name import function_name as fn”

#from pizza import make_pizza as mp
#mp(12, 'pepperoni')
#mp(22, 'cheese', 'green pepper', 'onions')

###using as to give a module an alias
###“import module_name as mn”

#import pizza as p
#p.make_pizza(12, 'pepperoni')
#p.make_pizza(22, 'cheese', 'green pepper', 'onions')

### import all function in a module
###from module_name import *

#from pizza import *
#make_pizza(12, 'pepperoni')
#make_pizza(22, 'cheese', 'green pepper', 'onions')
