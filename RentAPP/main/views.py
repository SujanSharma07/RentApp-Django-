from django.shortcuts import HttpResponse, render, redirect 
from main.models import Customers_model,RentRecords
from main.forms import Customers_form
# Create your views here.
from time import sleep

def mainpage(request):

  
    if request.method =='POST':    
        # Pass the form data to the form class 
        details = Customers_form(request.POST) 
  
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        if details.is_valid():   
       
            # Temporarily make an object to be add some 
            # logic into the data if there is such a need 
            # before writing to the database    
            customers_model = details.save(commit = False) 
         
            # Finally write the changes into database 
            customers_model.save()   
     
  
            # redirect it to some another page indicating data 
            # was inserted successfully 

            all = Customers_model.objects.all()
            all_fields = RentRecords._meta.fields

            Rent_Records ={}
            for record in all:
                data = RentRecords.objects.filter(info=record.username)
              #  print(data)
                Rent_Records[str(record.username)]=data
            print(Rent_Records)  

            for name,datas in Rent_Records.items():
                print(name)
                for data in datas:
                    print(data.status)
                print("_______________________________________")
            return render(request,"allentries.html",{'context':all,'columns':details.fields,'reports':Rent_Records,'rent_columns':all_fields})
                
        else: 
          
            return render(request, "home.html", {'form':details})  





    else:  
        '''
        
        for report in  RentRecords.objects.filter(username="Sujan Bhai"):
                  
          
            print(str(report.Total) +' at ' +str(report.time))
      
        records = RentRecords.objects.filter(info="Sujan Bhai")
        for record in records:
            print(record.status)  
            record.save()
        print("After changing")

        for record in records:
            record.status = "Paid"
        for record in records:
            print(record.status)  
              '''    
        context ={} 
        context['form']= Customers_form() 
        return render(request,template_name="home.html",context=context)


def record_(request):
    account_details = RentRecords.objects.filter()

    all_fields = RentRecords._meta.fields
  
   

    context = {

        "context":account_details,
        "columns":all_fields
    }
    return render(request,"account.html",context=context)