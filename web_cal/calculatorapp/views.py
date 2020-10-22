from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def home(request):
	#return render(request, 'home.html');

#def cal1(request):

    #val1 = int(request.POST['num1'])
    #val2 = int(request.POST['num2'])
    #res1 = val1 + val2
    #res2 = val1 * val2
    #res3 = val1 - val2
    #res4 = val1 / val2

    #op = request.POST['operator']

    #if (op == '+'):
        #return render(request, "home.html", {'result': res1})
    #elif (op == '*'):
        #return render(request, "result.html", {'result': res2})
    #elif (op == '-'):
        #return render(request, "result.html", {'result': res3})
    #elif (op == '/'):
        #if val2 != 0:   
            #return render(request, "result.html", {'result': res4})
        #else:
            #return render(request, "result.html", {'result': 'Division by zero is invalid'})





from calculatorapp.models import Calculations

# Create your views here.
def index(request):
    return render(request, 'index.html')



def equate(request):

    curr = float(request.POST['operand1'])
    ans = float(request.POST['operand2'])

    oper = request.POST['operator']
    #cal = Calculations(operand1=curr, operator=oper, operand2=ans)
    #cal.save()

    if (oper == '+'):
        ans1 = curr + ans
        #return render(request, "index.html", {'result': ans1})
    elif (oper == '*'):
        ans1 = curr * ans
        #return render(request, "index.html", {'result': ans1})
    elif (oper == '-'):
        ans1 = curr - ans
        #return render(request, "index.html", {'result': ans1})
    elif (oper == '/'):
        if ans != 0: 
            ans1 = curr / ans
            #return render(request, "index.html", {'result': ans1})
        else:
            ans1 ='Error'


    cal = Calculations(operand1=curr, operator=oper, operand2=ans, results=ans1)
    cal.save()

    return render(request, "index.html", {'result': ans1})


def history(request):
    #equate(request)
    #cal = Calculations(operand1=curr, operator=oper, operand2=ans, results=ans1)
   # cal.save()
    
    data = Calculations.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {'calculations': data})




#def equate(request):
    #curr = int(request.POST.get("curr",'0'))
    #ans = int(request.POST.get("ans",'0'))
    #oper = request.POST.get("oper")
    #cal = Calculations(operand1=ans, operator=oper, operand2=curr)
    #cal.save()
    #if request.POST:
        #if oper == '+':
            #ans = curr + ans
        #elif oper == '-':
            #ans = ans - curr
        #elif oper == '*':
            #ans = curr * ans
        #elif oper == '/':
            #if curr != 0:
                #ans = ans / curr
            #else:
                #ans = 'Division by zero is invalid'
    
    #return JsonResponse({'ans':ans}) 


                





