from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    answer = 0
    if request.POST:
        try:
            answer = eval(request.POST['screen1'])
        except:
            error = 'Please input a valid mathematical statement'
            return render(request, 'calculator/index.html', {'error':error, 'answer':answer})
        else:
            return  render(request, 'calculator/index.html', {'answer':answer})
    return render(request, 'calculator/index.html', {'answer':answer})
