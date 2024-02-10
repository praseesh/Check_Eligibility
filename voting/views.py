from django.shortcuts import render


def home(request):
    return render(request,'vote.html')

def eligibility(request):
    age=int(request.POST['age1'])
    print(age)
    if age < 18:
        return render(request,'ineligible.html',({'eligibility': age}))
    else:
        return render(request,'eligibile.html',({'eligibility': age}))


        


# (venv) P:\DJango\Entri\Eligibility>cd..\venv\scripts&&deactivate
# P:\DJango\Entri\venv\Scripts>activate
# (venv) P:\DJango\Entri\venv\Scripts>cd..\..\Eligibility
