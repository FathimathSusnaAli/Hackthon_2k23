from django.shortcuts import render ,redirect
import joblib
import os
import  pandas as pd
from .models import contact


def index(request):
    return render(request,'main/index.html')

def model(request):
    if request.POST:
        age = int(request.POST['age'])
        Medu = int(request.POST['Medu'])
        Fedu = int(request.POST['Fedu'])
        Mjob = int(request.POST['Mjob'])
        Fjob = int(request.POST['Fjob'])
        reason = int(request.POST['reason'])
        Studytime = int(request.POST['Studytime'])
        failures =int(request.POST['failures'])
        schoolsup = int(request.POST['schoolsup'])
        paid = int(request.POST['paid'])
        higher = int(request.POST['higher'])
        famrel = int(request.POST['famrel'])
        freetime = int(request.POST['freetime'])
        goout = int(request.POST['goout'])
        health = int(request.POST['health'])
        absence = int(request.POST['absence'])
        traveltime = int(request.POST['traveltime'])
        G1 = int(request.POST['G1'])/5
        
        model = joblib.load('D:\\HACKATHON(2)\\Hackathon\\SAA\\templates\\main\\best_G2_model.joblib')
        row = [[failures , absence , Fjob , freetime , health , Studytime , Medu , Mjob , goout , age , Fedu , reason , famrel , higher , schoolsup , paid , traveltime , G1]]
        df = pd.DataFrame({'higher': [higher], 'health': [health], 'goout': [goout], 'Fjob': [Fjob], 'age': [age], 'schoolsup': [schoolsup], 'Medu': [Medu], 'Fedu': [Fedu], 'freetime': [freetime], 'reason': [reason], 'studytime': [Studytime], 'failures': [failures], 'Mjob': [Mjob], 'paid': [paid], 'famrel': [famrel], 'G1': [G1], 'traveltime': [traveltime] , 'absences': [absence]})
        pred = model.predict(df)
        res = pred
        return render(request , 'main/model.html' , {'result' : res*5})
    return render(request , 'main/model.html')

def model2(request):
    if request.POST:
        age = int(request.POST['age'])
        Medu = int(request.POST['Medu'])
        Fedu = int(request.POST['Fedu'])
        Mjob = int(request.POST['Mjob'])
        Fjob = int(request.POST['Fjob'])
        reason = int(request.POST['reason'])
        Studytime = int(request.POST['Studytime'])
        failures =int(request.POST['failures'])
        schoolsup = int(request.POST['schoolsup'])
        paid = int(request.POST['paid'])
        higher = int(request.POST['higher'])
        famrel = int(request.POST['famrel'])
        freetime = int(request.POST['freetime'])
        goout = int(request.POST['goout'])
        health = int(request.POST['health'])
        absence = int(request.POST['absence'])
        traveltime = int(request.POST['traveltime'])
        G1 = int(request.POST['G1'])/5
        G2 = int(request.POST['G2'])/5
        
        model = joblib.load('D:\\HACKATHON(2)\\Hackathon\\SAA\\templates\\main\\best_G3_model.joblib')
        row = [[failures , absence , Fjob , freetime , health , Studytime , Medu , Mjob , goout , age , Fedu , reason , famrel , higher , schoolsup , paid , traveltime , G1 , G2]]
        df = pd.DataFrame({'higher': [higher], 'health': [health], 'goout': [goout], 'Fjob': [Fjob], 'age': [age], 'schoolsup': [schoolsup], 'Medu': [Medu], 'Fedu': [Fedu], 'freetime': [freetime], 'reason': [reason], 'studytime': [Studytime], 'failures': [failures], 'Mjob': [Mjob], 'paid': [paid], 'famrel': [famrel], 'G1': [G1], 'traveltime': [traveltime] , 'absences': [absence] , 'G2': [G2],})
        pred = model.predict(df)
        res = pred
        return render(request , 'main/model2.html' , {'result' : res*5})
    return render(request , 'main/model2.html')

def contacts(request):
    if request.POST:
        names = request.POST['name']
        emails = request.POST['email']
        subs = request.POST['sub']
        msgs = request.POST['msg']
        user_data = contact(name = names ,  email = emails , sub = subs , msg = msgs)
        user_data.save()
        return redirect(contacts)
    return render(request , 'main/contact.html')

def report(request):
    return render(request , 'main/report.html')


# Create your views here.
