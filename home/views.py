

# Create your views here.
from django.shortcuts import render
import datetime
import re
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
#DataFlair #Views #TemplateInheritance
# Create your views here.
def home(request,*args,**kwargs):
    
    return render(request, 'root.html')
#def home(request):
  #  return render(request, 'base.html')

def portfolio(request,*args,**kwargs):
    
    return render(request, 'portfolio-details.html')

def other(request,*args,**kwargs):
    context = {
    'k1': 'Welcome to the Second page',
    
    }

    return render(request, 'inner-page.html', context)

def about(request):
    time = datetime.datetime.now()
    return render(request, 'inner-page.html',{})
def cgpa(request):
    
    return render(request, 'cgpa.html',{})

def gpa(request,*args,**kwargs):
   
    va1= request.POST['nums1']
    val2=int( request.POST['nums2'])
    val3=request.POST['nums3']
    val4= int(request.POST['nums4'])
    val5= request.POST['nums5']
    val6= int(request.POST['nums6'])
    val7= request.POST['nums7']
    val8= int(request.POST['nums8'])
    val9= request.POST['nums9']
    val10=int(request.POST['nums10'])
    val11= request.POST['nums11']
    val12=int( request.POST['nums12'])
    va13= request.POST['nums13']
    val14=int(request.POST['nums14'])
    val15=request.POST['nums15']
    val16= int(request.POST['nums16'])
    val17= request.POST['nums17']
    val18= int(request.POST['nums18'])
    val19= request.POST['nums19']
    val20= int(request.POST['nums20'])
    
    va1=va1.capitalize()
    val3=val3.capitalize()
    val5=val5.capitalize()
    val7=val7.capitalize()
    val9=val9.capitalize()
    val11=val11.capitalize()
    va13=va13.capitalize()
    val15= val15.capitalize()
    val17=val17.capitalize()
    val19= val19.capitalize()
    A=5
    B=4
    C=3
    D=2
    E=1
    F=0
    comment=None
    point=0
    
   
    if  va1=='A' :
        point+=(A*val2 ) 
    elif va1=='B' :
         point+=(B*val2 )
    elif va1 =='C' :
         point+=(C*val2 )

    elif va1 =='D' :
        point+=(D*val2 )

    elif va1 =='E' :
         point+=(E*val2 )  
    else  :
        point+=(F*val2 )
    
    if  val3=='A' :
        point+=(A*val4 ) 
    elif val3=='B' :
         point+=(B*val4 )
    elif val3 =='C' :
         point+=(C*val4 )

    elif val3=='D' :
        point+=(D*val4 )

    elif val3=='E' :
         point+=(E*val4 )  
    else  :
        point+=(F*val4 )
    
    if  val5=='A' :
        point+=(A*val6 ) 
    elif val5=='B' :
         point+=(B*val6 )
    elif val5 =='C' :
         point+=(C*val6 )

    elif val5 =='D' :
        point+=(D*val6 )

    elif val5 =='E' :
         point+=(E*val6 )  
    else  :
        point+=(F*val6 )

    if  val7=='A' :
        point+=(A*val8 ) 
    elif val7=='B' :
         point+=(B*val8 )
    elif val7 =='C' :
         point+=(C*val8 )

    elif val7 =='D' :
        point+=(D*val8 )

    elif val7 =='E' :
         point+=(E*val8 )  
    else  :
        point+=(F*val8 )

    if  val9=='A' :
        point+=(A*val10 ) 
    elif val9=='B' :
         point+=(B*val10 )
    elif val9 =='C' :
         point+=(C*val10 )

    elif val9 =='D' :
        point+=(D*val10 )

    elif val9 =='E' :
         point+=(E*val10 )  
    else  :
        point+=(F*val10 )

    if  val11=='A' :
        point+=(A*val12 ) 
    elif val11=='B' :
         point+=(B*val12 )
    elif val11 =='C' :
         point+=(C*val12 )

    elif val11 =='D' :
        point+=(D*val12 )

    elif val11 =='E' :
         point+=(E*val12 )  
    else  :
        point+=(F*val12 )
    

    if  va13=='A' :
        point+=(A*val14 ) 
    elif va13=='B' :
         point+=(B*val14 )
    elif va13 =='C' :
         point+=(C*val14 )

    elif va13 =='D' :
        point+=(D*val14 )

    elif va13 =='E' :
         point+=(E*val14 )  
    else  :
        point+=(F*val14 )

    if  val15=='A' :
        point+=(A*val16 ) 
    elif val15=='B' :
         point+=(B*val16 )
    elif val15 =='C' :
         point+=(C*val16 )

    elif val15 =='D' :
        point+=(D*val16 )

    elif val15 =='E' :
         point+=(E*val16 )  
    else  :
        point+=(F*val16 )


    if  val17=='A' :
        point+=(A*val18 ) 
    elif val17=='B' :
         point+=(B*val18 )
    elif val17 =='C' :
         point+=(C*val18 )

    elif val17 =='D' :
        point+=(D*val18 )

    elif val17 =='E' :
         point+=(E*val18 )  
    else  :
        point+=(F*val18 )
    
    if  val19=='A' :
        point+=(A*val20 ) 
    elif val19=='B' :
         point+=(B*val20 )
    elif val19 =='C' :
         point+=(C*val20 )

    elif val19 =='D' :
        point+=(D*val20 )

    elif val19 =='E' :
         point+=(E*val20 )  
    else  :
        point+=(F*val20 )
    

    
    totalUnit= val2+val4+val6+val8+val10+val12+val14+val16+val18+val20
    sumTotal=point/totalUnit
    
    
    caculated_grade= ('%.2f' %sumTotal)
    Semestal_unit=totalUnit
    Semester_point=point
    caculated_class= comment
    return render(request, 'calc.html', {'result':caculated_grade,'su':Semestal_unit,'sp':Semester_point,'result2':caculated_class})


 

def add(request,*args,**kwargs):
    

    val1=int( request.POST['num1'])
    val2= int(request.POST['num2'])
    val3=int( request.POST['num3'])
    val4= int(request.POST['num4'])
    val5=int( request.POST['num5'])
    val6= int(request.POST['num6'])
    
    
          
        # if birth date is greater then given birth_month  
        # then donot count this month and add 30 to the date so  
        # as to subtract the date and get the remaining days  
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
          
    if (val1 > val4): 
            val5 = val5 - 1
            val4 = val4 + month[val2-1]  
                      
                      
        # if birth month exceeds given month, then  
        # donot count this year and add 12 to the  
        # month so that we can subtract and find out  
        # the difference  
    if (val2 > val5): 
             val6 = val6 - 1
             val2 = val2 + 12
                      
        # calculate day, month, year  
    calculated_day = val4 - val1  
    calculated_month = val5 - val2  
    calculated_year = val6 - val3 
  
        # calculated day, month, year write back 
        # to the respective entry boxes 
  
        # insert method inserting the   
        # value in the text entry box. 
          

    return render(request, 'resul.html',{'result1':calculated_day,'result2':calculated_month,'result3':calculated_year})



def contact(request,*args,**kwargs):
    return render(request, 'cal.html')

def service(request,*args,**kwargs):
    if request.method== 'POST':
        
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail(
        subject, 
        message,
         email,
         
        recipient_list=['oyedotuna@gmail.com'], 
        fail_silently=False, 
        auth_user=None, 
        auth_password=None, 
        connection=None, 
        html_message=None)
        return render(request, 'contact.html',{'email':email})
    else:
        return render(request, 'contact.html',{})

    


   