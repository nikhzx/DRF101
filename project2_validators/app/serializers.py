from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

#This has Validators Implemented

# When working with Django REST Framework's ModelSerializer, validation occurs through a combination of automatic and customizable processes. Here's a breakdown of how different validation types are called:

# 1. Model-Level Validation:

# Django Model Constraints:
# The ModelSerializer automatically inherits validation rules defined in your Django model. This includes constraints like max_length, unique, null, and blank. If your model has these constraints, the serializer will enforce them.
# Model's clean() method:
# If your Django model has a clean() method, it will be called during the validation process. This allows you to perform custom model-level validation that involves multiple fields.

# 2. Serializer-Level Validation:

# Field-Level Validation:
    # validate_<field_name>() methods: You can define methods in your serializer class with the name validate_<field_name>, where <field_name> is the name of the field. These methods are called specifically to validate that individual field.
    # Built-in Validators: DRF provides built-in validators for various field types (e.g., EmailValidator, URLValidator). These are automatically applied based on the field type.
# Object-Level Validation:
    # validate() method: You can override the validate() method in your serializer class to perform validation that involves multiple fields or the entire object. This is useful for enforcing business logic that depends on the combined values of multiple fields.   
# Unique Validators:
    # DRF provides validators like UniqueValidator and UniqueTogetherValidator to enforce uniqueness constraints at the serializer level. These are useful for ensuring that data is unique within a table or across multiple fields.

# How the Process Works:
    # Incoming Data:
    # When data is sent to the API, the serializer receives it.
    # Field Validation:
    # The serializer first validates each individual field. This includes checking data types, applying built-in validators, and calling validate_<field_name>() methods.   
    # Object Validation:
    # If all field validations pass, the serializer then calls the validate() method to perform object-level validation.
    # Model Validation (if applicable):
    # If the data is being used to create or update a model instance, the model's clean() method is called.
    # Saving Data:
    # If all validations pass, the serializer proceeds to save the data to the database.
    

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
    def validate_roll(self, value): #Here naming should be as validate_fieldName
        if value>=200:
            raise serializers.ValidationError("Seat Full: Admissions Stopped for Course")
        return value
    
    #Object Level Validator for Model Serializer
    def validate(self, data): #validate func is overwritten for  Object Level Validation
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