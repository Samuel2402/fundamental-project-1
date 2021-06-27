from flask import Flask
from wtforms.validators import DataRequired, Length, ValidationError

print('=========================== before_validation ================================')

class decimal_places:
    def validate_most_expensive(self,message=None):
        if not message:
            message = "Please enter a valid price range in the form: 16.00"
        self.message = message   
    def __call__(self, form, field):
        if len(field.data.rsplit('.')[-1]) != 2:
            raise ValidationError(self.message)

class name_validator:
    def __call__(self, store):
        store_list =[tesco, mcdonalds] 
        for i in store_list:
            if store.data.lower != i:
                raise ValidationError("Please enter a valid store name")

print('============================ after_validation ================================')

   

