from lib.fields.FieldItem import FieldItemValidation
from lib.fields import FieldClass, FieldItem
from lib.fields.FieldClass import FieldClass


class Fields(FieldClass):
    name = FieldItem.StringField(default="hello")
    resume = FieldItem.FileField().validation(FieldItemValidation('file_size').value(
        4444)).validation(FieldItemValidation('file_type').value(['application/pdf', 'image/*']))
