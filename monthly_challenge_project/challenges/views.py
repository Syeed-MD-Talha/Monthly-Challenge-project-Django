from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


# Create your views here.z 

monthly_challenges = {
  "january": "Eat no meat for the entire month!",
  "february": "Walk for at least 20 minutes every day!",
  "march": "Learn Django for at least 20 minutes every day!",
  "april": "Eat no meat for the entire month!",
  "may": "Walk for at least 20 minutes every day!",
  "june": "Learn Django for at least 20 minutes every day!",
  "july": "Eat no meat for the entire month!",
  "august": "Walk for at least 20 minutes every day!",
  "september": "Learn Django for at least 20 minutes every day!",
  "october": "Eat no meat for the entire month!",
  "november": "Walk for at least 20 minutes every day!",
  "december": "Learn Django for at least 20 minutes every day!"
}


def index(request):
    month_list=list(monthly_challenges.keys())
    print(month_list)
    return render(request,'challenges/index.html',{'months':month_list})
    # months=list(monthly_challenges.keys())
    # lists=""
    
    # for month in months:
    #     redirect=reverse('challenge_path',args=[month])
    #     lists+=f"<h1><li><a href=\"{redirect}\">{month.capitalize()}</a></li></h1>"
    
    # return HttpResponse(f"<ul>{lists}</ul>")



def month_number(request, month):
    try:
        months=list(monthly_challenges.keys())
        redirect_path=reverse('challenge_path',args=[months[month]])
        print(redirect_path)
        return HttpResponseRedirect(redirect_path)
    except:
        redirect_path=reverse('challenge_path')
        return HttpResponseNotFound("<h1>Not a valid month name </h1>")


def month(request, month):
    print(month)
    context=monthly_challenges[month]
    return render(request,'challenges/challenge.html',{'month_text':context,'month_name':month})
    # try:
    #     context=monthly_challenges[month]
    #     return render(request,'challenges/challenge.html',{'month_text':context,'month_name':month})
    # except:
    #     return HttpResponseNotFound("<h1>Not a valid month name </h1>")
    

