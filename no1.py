import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

my_profile = {
    "name" : "Ahmad Luthfi Mahar",
    "age" : 22,
    "address" : "Jln Rawa Kuning RT003/02, Cakung, Jakarta Timur",
    "hobbies" : ['Swimming, Reading book'],
    "is_married" : False,
    "list_school" : [{'SDN 17 Pagi Jakarta       year_in : 2002, year_out : 2008, major : null'},
                   {'MTsN 20 Jakarta           year_in : 2008, year_out : 2011, major : null'},
                   {'SMAN 89 Jakarta           year_in : 2011, year_out : 2014, major : Science'},
                   {'University of Indonesia   year_in : 2015, year_out : 2019, major : Material of Physics'}],
    "skills" : [{'skill name : python, level : beginner'},
              {'skill name : kotlin, level : beginner'},
              {'skill name : machine learning, level : beginner'}],
    "interest_in_coding"  : True
}
print(json.dumps(my_profile, cls=ComplexEncoder))