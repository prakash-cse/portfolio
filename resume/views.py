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
            'path':'images/portfolio1.png',
            'link':'https://github.com/prakash-cse/portfolio'
        },
        
    ]

    return render(request,"projects.html",{"project_show":project_show})

def certificates(request):
    return render(request,"certificates.html")


def contact(request):
    return render(request,"contact.html")

def resume(request):
    """
    Handles resume viewing and downloading with consistent behavior across devices.
    Uses Content-Type and Content-Disposition headers to control browser behavior.
    """
    resume_path = "myapp/prakash_resume.pdf"
    
    # Check if file exists in static storage
    if not staticfiles_storage.exists(resume_path):
        return HttpResponse("Resume not found", status=404)
        
    try:
        # Get the full path to the file
        file_path = staticfiles_storage.path(resume_path)
        
        # Open and read the file
        with open(file_path, 'rb') as pdf_file:
            pdf_content = pdf_file.read()
        
        # Create response object
        response = HttpResponse(pdf_content, content_type='application/pdf')
        
        # Check if this is a download request
        if request.GET.get('download'):
            # Force download
            response['Content-Disposition'] = 'attachment; filename="prakash_resume.pdf"'
        else:
            # Force display in browser
            response['Content-Disposition'] = 'inline; filename="prakash_resume.pdf"'
            
        # Add headers to prevent caching
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        return response
        
    except Exception as e:
        return HttpResponse(f"Error accessing resume: {str(e)}", status=500)

