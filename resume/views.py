from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    project_show=[
        {
            'title':'Personalized Grooming Website',
            'path':'images/grooming_website.png',
            'link':'https://github.com/prakash-cse/E-commerce_website'
        },

        {
            'title':'E-commerce Website',
            'path':'images/ecommerce_website.png',
            'link':'https://github.com/prakash-cse/shop_kart'
        },

        {
            'title':'Representation of Car Segmentation Website',
            'path':'images/car_segmentation.png',
            'link':'https://github.com/prakash-cse/Car_Representation_Website'
        },

        {
            'title':'Lakshmi Mahal Website',
            'path':'images/lakshmi_mahal.png',
            'link':'https://lakshmimahaldvk.com'
        },

        {
            'title':'Blog website',
            'path':'images/blog_website.png',
            'link':'https://github.com/prakash-cse/blog_website'
        },
        
        {
            'title':'TODOLIST',
            'path':'images/todolist.png',
            'link':'https://github.com/prakash-cse/todolist'
        },

        {
            'title':'Portfolio',
            'path':'images/portfolio.png',
            'link':'https://github.com/prakash-cse/Object_tracking_based_on_color'
        },
        
    ]

    return render(request,"projects.html",{"project_show":project_show})

def certificates(request):
    return render(request,"certificates.html")


def contact(request):
    return render(request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)