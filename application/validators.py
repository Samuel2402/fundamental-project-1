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

print('============================ after_validation ================================')

   

