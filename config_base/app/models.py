from django.db.models import Model,CharField,EmailField

# Create your models here. 
class Employee(Model):  
    employee_id = CharField(max_length=20)  
    employee_name = CharField(max_length=100)  
    employee_email = EmailField()  
    employee_contact = CharField(max_length=15)  
    class Meta:
        db_table = "employee"  