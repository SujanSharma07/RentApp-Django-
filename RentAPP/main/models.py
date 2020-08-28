from django.db import models
from django.utils.timezone import now
import os
import csv

      #check if dir exist if not create it
def check_dir(file_name,field_names):
  directory = os.path.dirname(file_name)
  if not os.path.exists(directory):
#    os.makedirs(directory)
   
    writer = csv.DictWriter(file_name, fieldnames=field_names)

    writer.writeheader()

def save_csv(file_name, records,field_names):
  check_dir(file_name,field_names)
  csv_file = open(file_name,'w+')
  csvWriter = csv.writer(csv_file,delimiter=',')
  count = 0
  data = {}
  for  field_name,record in zip(field_names,records):
    data[field_name]= record 
  print(data)  
  csvWriter.writerow(data)

 
class Customers_model(models.Model): 
        # fields of the model 


    Male = 'M'
    FeMale = 'F'
    Other = 'O'
    GENDER_CHOICES = ( 
    (Male, 'Male'), 
    (FeMale, 'Female'), 
    (Other,'Other')
    ) 
  
    # define a username filed with bound  max length it can have 
    username = models.CharField( max_length = 20, blank = False, primary_key=True,
                                 null = False,  error_messages={
               'required': 'Please enter your name'
                }) 
      
    # This is used to write a post 
    text = models.TextField(blank = False, null = False) 
      
    # Values for gender are restricted by giving choices 
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES,  
                              default = Male) 

    total = models.IntegerField(blank=False,null=False,default=1)                          
      
   # time = models.DateTimeField(auto_now_add = True,blank=True)
    time = models.DateTimeField(default=now, editable=False)
 

    email = models.EmailField(max_length = 254) 


 
 #   img = models.ImageField(upload_to = "media/images/",blank=False,null=False) 
   
        # renames the instances of the model 
        # with their title name 
    def __str__(self): 
        return self.username


# Create your models here.

class RentRecords(models.Model):

    info = models.ForeignKey(Customers_model, on_delete=models.CASCADE,null=True, blank=True)    
    time = models.DateTimeField(default=now, editable=False)

  #  time = models.DateTimeField(auto_now_add = True,blank=True) 
  #  info = models.ForeignKey(Customers_model, on_delete=models.CASCADE)  
    Previous_Balance = models.IntegerField(default=0)      
    Rent = models.IntegerField(default=0)
    Electricity_Units = models.IntegerField(help_text="Units",default=0)
    Electricity_Rate = models.IntegerField(default=15)
    Other = models.IntegerField(help_text="Waste Dumping and Water") 

    Total = models.IntegerField(help_text="Grand Total",default=1)

    STATUS_CHOICES = ( 
    ('Paid','Paid'), ('Unpaid','Unpaid'), ('Partial','Partial') 
    ) 
  
    # Values for gender are restricted by giving choices 
    status = models.CharField( max_length=18, choices = STATUS_CHOICES,  
                              default = 'Unpaid') 


   

  

    def save(self):
        # self.first_char for referencing to the current object
        self.Total = self.Previous_Balance + self.Rent + self.Electricity_Units * self.Electricity_Units + self.Other

        your_list = [self.Previous_Balance,self.Rent,self.Electricity_Units,self.Electricity_Rate,self.Other,self.Total,self.status,self.time]
        field_names = ['Previous_Balance', 'Rent','Electricity_Units','Electricity_Rate','Other','Total','Status','Time']

        directory = os.path.abspath(os.path.join(os.path.curdir))
        print(directory)
       # save_csv(directory+f"/data/{self.info}.csv",your_list,field_names)
        super().save(self)

    def __str__(self):
      return self.info.username  




