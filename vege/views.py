from django.shortcuts import render , redirect
from vege.models import * 
from django.http import HttpResponse



# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        x = data.get('receipe_name')
        y = data.get('receipe_description')
        z = request.FILES.get('receipe_image')

        #   # Create a model instance
        # recipe = Receipe()
        # recipe.receipe_name = receipe_name
        # recipe.receipe_description = receipe_description

        # # Save to the database
        # recipe.save()

        Receipe.objects.create(receipe_name = x  ,receipe_description =  y  , receipe_image = z)

        print(x)
        print(y)
        print(z)

        return redirect('/receipes')

    queryset = Receipe.objects.all()

    # print('hello')
    # print(request.GET.get('Search'))
    
    if request.GET.get('Search'):
        print(request.GET.get('Search'))
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('Search'))


    context = {'receipes' : queryset}



    return render(request , 'receipes.html' , context)


def update_receipe(request , id):
    # import pdb;pdb.set_trace()
    print('Request',request)
    queryset = Receipe.objects.get(id = id)
    print ('Queryset' , queryset)


    if request.method == "POST":
        # import pdb;pdb.set_trace()
        data = request.POST

        print('Data',data)

        x = data.get('receipe_name')
        y = data.get('receipe_description')
        z = request.FILES.get('receipe_image')

        queryset.receipe_name = x
        queryset.receipe_description = y

        if z :
            queryset.receipe_image = z
        print('post_queryset', queryset )    
        queryset.save()

        return redirect('/receipes')

    context = {'receipe' : queryset}
    print('context' , context)
    

    return render(request , 'update_receipe.html' , context)   



def delete_receipe(request , id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')

