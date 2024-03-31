from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

#Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    '''
    serializers.ModelSerializer is Used.
    Validations are auto Created, no need to create Manually.
    create() and update() function for POST and PUT is auto implemented.
    '''
    #Validator 3rd Type
    def start_with_n(value):
        if value[0].lower()!='n':
            raise serializers.ValidationError("Name Should start with N")
        return value
        
    # name = serializers.CharField(read_only = True)
    name = serializers.CharField(validators=[start_with_n])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name':{"read_only": True}, 'roll':{'read_only':True}}

    #Field Level Validator for Model Serializer
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError("Seat Full: Admissions Stopped for Course")
        return value
    
    #Object Level Validator for Model Serializer
    def validate(self, data):
        nm = data.get("name")
        ct = data.get("city")
        if nm.lower()=="nikhil" and ct.lower()!="prayagraj":
            raise serializers.ValidationError("For Nikhil, City must be Prayagraj")
        return data


# #Validators
# def start_with_n(value):
#     '''
#     These Validator are given as argument to field of serializer.
#     First Priority of Validator Check.
#     '''
#     if value[0].lower()!='n':
#         raise serializers.ValidationError("Name Should start with 'N")

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 100, validators=[start_with_n])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length = 100)

    
#     def create(self, validated_data):
#         '''
#         This Function is used for POST request handelling.
#         '''
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         '''
#         This Method is used for PUT request handelling.
#         '''
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
    
#     #Field Level Validation
#     def validate_roll(self, value):
#         '''
#         Used for Validating Single Field.
#         2nd Level Priority
#         When serializer.is_valid() is called in the view this function is triggered.
#         This Checks for the provided condition for the field.
#         If FALSE, raises a exception and (json_data = JSONRenderer().render(serializer.errors)) handles the Error in view
#         If True sends back the value to view.
#         '''
#         if value>=200:
#             raise serializers.ValidationError("Seat Full: Admissions Stopped for Course")
#         return value
    
#     #Object Level Validation
#     def validate(self, data):
#         '''
#         Used for Validating Multiple fields.
#         3rd level Priority.
#         Working is same as field validator
#         '''
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower()=="nikhil" and ct.lower()!='prayag':
#             raise serializers.ValidationError("City must be Prayag for Nikhil")
#         return data