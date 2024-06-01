from django.shortcuts import render, HttpResponse
from home.models import contacts, login, Product


# Create your views here.
def home(request):
    # return HttpResponse("This is Home page & Iam baikuntah behara")
    return render(request, 'home.html')


def index(request):
    # return HttpResponse("This is Home page & Iam baikuntah behara")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')


def blog(request):
    # return HttpResponse("This is blog page")
    return render(request, 'blog.html')


def contact(request):
    context = {'success': False}

    if request.method == "POST":
        print("this is post ")
        email1 = request.POST['email']
        name = request.POST['password']
        # name1 = request.POST['Name']
        address1 = request.POST['address']
        address21 = request.POST['address2']
        city1 = request.POST['city']
        state1 = request.POST['state']
        Zip1 = request.POST['Zip']
        print(email1, name, address1, address21, city1, state1, Zip1)
        ins = contacts(email=email1, name=name, address=address1,
                       address2=address21, city=city1, state=state1, Zip=Zip1)
        ins.save()
        print("the data has been written to the contact db")
        context = {'success': True}
        # check=models.CharField(max_length=100)
    # return HttpResponse("This is contact page")

    return render(request, 'contact.html', context)


def index_php(request):
    # return HttpResponse("This is contact page")
    return render(request, 'index.php')


def signin(request):
    context = {'success': False}
    if request.method == "POST":

        email1 = request.POST['email']
        password1 = request.POST['password']
       #  print(email,password)
        ins = login(emails=email1, passwords=password1)
        ins.save()
        print("the data has been written to the  sign in db")
        context = {'success': True}
    return render(request, 'signin.html', context)

    # return HttpResponse("This is contact page")


def cart(request):
    # return HttpResponse("This is contact page")
    return render(request, 'cart.html')


def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = []
    return render(request, 'search.html', {'query': query, 'products': products})
def design(request):
    return render(request, 'design.html')
def pickndrop(request):
    return render(request, 'pickandrop.html')
def policy(request):
    return render(request,'policy.html')
def apoinment(request):
    return render(request,'apoinment.html')
def consltant(request):
    return render(request,'consltant.html')