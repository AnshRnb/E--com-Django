from django.shortcuts import render

# Create your views here.

from .models import Student



def base(req):
    return render (req, 'base.html')


def registration(req):
    return render (req, 'registration.html')

def login(req):
    return render (req, 'login.html')





def home(req):
    return render (req, 'home.html')

def home1(request,pk):
    userdata = Student.objects.get(id=pk)
    userdata = {
                     "id":userdata.id,
                    "name":userdata.stu_name,
                    # "contact":userdata.stu_contact,
                    # "dis":userdata.stu_dis,
                    # "dob":userdata.stu_dob,
                    "email":userdata.stu_email,
                    # "image":userdata.stu_image,
                    # "file":userdata.stu_document,
                    # "education":userdata.stu_edu,
                    "password":userdata.stu_password,
                }
    return render(request,'home.html',{'userdata':userdata})






def about(req):
    return render (req, 'about.html')

def about1(request,pk):
    userdata = Student.objects.get(id=pk)
    userdata = {
                     "id":userdata.id,
                    "name":userdata.stu_name,
                    # "contact":userdata.stu_contact,
                    # "dis":userdata.stu_dis,
                    # "dob":userdata.stu_dob,
                    "email":userdata.stu_email,
                    # "image":userdata.stu_image,
                    # "file":userdata.stu_document,
                    # "education":userdata.stu_edu,
                    "password":userdata.stu_password,
                }
    return render(request,'about.html',{'userdata':userdata})




def contact(req):
    return render (req, 'contact.html')

def contact1(request,pk):
    userdata = Student.objects.get(id=pk)
    userdata = {
                     "id":userdata.id,
                    "name":userdata.stu_name,
                    # "contact":userdata.stu_contact,
                    # "dis":userdata.stu_dis,
                    # "dob":userdata.stu_dob,
                    "email":userdata.stu_email,
                    # "image":userdata.stu_image,
                    # "file":userdata.stu_document,
                    # "education":userdata.stu_edu,
                    "password":userdata.stu_password,
                }
    return render(request,'contact.html',{'userdata':userdata})





def product(req):
    return render (req, 'product.html')

def product1(request,pk):
    userdata = Student.objects.get(id=pk)
    userdata = {
                    "id":userdata.id,
                    "name":userdata.stu_name,
                    # "contact":userdata.stu_contact,
                    # "dis":userdata.stu_dis,
                    # "dob":userdata.stu_dob,
                    "email":userdata.stu_email,
                    # "image":userdata.stu_image,
                    # "file":userdata.stu_document,
                    # "education":userdata.stu_edu,
                    "password":userdata.stu_password,
                }
    return render(request,'product.html',{'userdata':userdata})






def finalregis(req):
    n=req.POST.get('username')
    e=req.POST.get('email')
    # d=req.POST.get('detail')
    # p=req.POST.get('phone')
    # dob=req.POST.get('dob')
    # s=req.POST.getlist('subscribe')
    # g=req.POST.get('gender')
    pa=req.POST.get('password')
    cp=req.POST.get('cpassword')
    # pc=req.FILES.get('profile-pic')
    # r=req.FILES.get('resume')

    # print(n,e,d,p,dob,s,g,pa,cp,pc,r)


    # return render(req, 'finalregis.html')

    # data={'name':n,'email':e,'details':d,'phone':p,'dob':dob,'subs':s,'profilepic':pc,'resume':r}

    # return render(req, 'finalregis.html', {'data' : data})

    user = Student.objects.filter(stu_email=e)
    if user: 
        msg='email exits alreday: '
        return render(req, 'registration.html', {'error' : msg})
    else:
        if pa == cp:

              Student.objects.create(stu_name=n,
                          stu_email=e,
                        #   stu_dis=d,
                        #   stu_contact=p,
                        #   stu_dob=dob,
                        #   stu_edu=s,
                        #   stu_gender=g,
                          stu_password=pa,
                        #   stu_image=pc,
                        #   stu_document=r)
              )
              msg = 'registration Done'
              return render (req, 'login.html', {'error' : msg})
        else:
             msg = 'your password not matched with confirm password'
             return render (req, 'registration.html', {'error' : msg})




def logindata(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        passw = req.POST.get('password')
        user =  Student.objects.filter(stu_email = email)
        if user:
            userdata = Student.objects.get(stu_email = email)
            print(userdata.stu_name)
            print(userdata.stu_email)
            pass1 =  userdata.stu_password
            if passw == pass1:
                msg = 'successfull login :) '

                userdata = {
                    "id":userdata.id,
                    "name":userdata.stu_name,
                    # "contact":userdata.stu_contact,
                    # "dis":userdata.stu_dis,
                    # "dob":userdata.stu_dob,
                    "email":userdata.stu_email,
                    # "image":userdata.stu_image,
                    # "file":userdata.stu_document,
                    # "education":userdata.stu_edu,
                    "password":userdata.stu_password,
                }
                return render(req, 'home.html', {'userdata' : userdata})
            else:
                 msg = "email and passw does't exits "
                 return render (req, 'login.html', {'error' : msg})
            
        else:
             msg = "user and email does't exits or register"
             return render (req, 'registration.html', {'error' : msg})

    else:
         
         return render (req, 'registration.html', {'error' : msg})
           
  
   
