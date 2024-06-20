class India():
    def capital(self):
        print("Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class BD():
    def capital(self):
        print("Dhaka is the capital of BD.")
 
    def language(self):
        print("Bangla is the primary language of BD.")
 
    def type(self):
        print("BD is a under-developed country.")
 
obj_ind = India()
obj_bd = BD()
for country in (obj_ind, obj_bd):
    country.capital()
    country.language()
    country.type()