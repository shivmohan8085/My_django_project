from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    print("home page function is runnign now")
    return HttpResponse (" <b><h1>welcome my django project</b></h1>")

def success_page(request):
    print("success_page function is runnign now")
    return HttpResponse ("""
                         
                        <header>
                            <div class="container">
                                <h1>ZECDATA</h1>
                                <nav>
                                    <ul>
                                        <li><a href="/">Home Page</a></li>  
                                    </ul>
                                </nav>
                            </div>
                        </header>
                         <b><h1>Hay this is a Success page</b></h1>

                         <hr>
                         <p> this is demo of my dumy project</p> 
                         
                        """)

def courseDetails(request,name):
    return HttpResponse(name)


def home(request):
    if request.method == 'POST' :
        # name = request.POST['fname']    
        name = request.POST.get('fname')  
        print(name) 
    return render(request,"home.html")

def peopleDetails(request):
    # data = {
    #     'title':"peoples data",
    #     'languages':['PHP',' JAVA', 'PYHTON', 'C','C++'],
    #     "peoples": [
    #         {"name": "Shivmohan", "age": 22},
    #         {"name": "Aarav", "age": 18},
    #         {"name": "Saanvi", "age": 23},
    #         {"name": "Vivaan", "age": 21},
    #         {"name": "Anaya", "age": 19},
    #         {"name": "Ishaan", "age": 24},
    #         {"name": "Kiara", "age": 20},
    #         {"name": "Rohan", "age": 17},
    #         {"name": "Diya", "age": 25},
    #         {"name": "Arjun", "age": 22}
    #     ]
    #     }


    title = "peoples data"
    languages = ['PHP',' JAVA', 'PYHTON', 'C','C++']
    peoples = [
        {"name": "Shivmohan", "age": 22},
        {"name": "Aarav", "age": 18},
        {"name": "Saanvi", "age": 23},
        {"name": "Vivaan", "age": 21},
        {"name": "Anaya", "age": 19},
        {"name": "Ishaan", "age": 24},
        {"name": "Kiara", "age": 20},
        {"name": "Rohan", "age": 17},
        {"name": "Diya", "age": 25},
        {"name": "Arjun", "age": 22}
    ]

    data= {
        'title' : title,
        'languages': languages,
        'peoples' : peoples
    }

    return render(request,"zecdata.html",data)