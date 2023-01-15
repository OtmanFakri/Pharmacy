from django.shortcuts import render,redirect
from .Form import From_Pharmacie
from Pharmascie.models import Pharmacie
from Acount.models import Utilisateur2
# Create your views here.
from django.contrib import messages


def add(request):
    if  request.session.get('Login') == 'true':
        #form(initial={'idutil': "Dean Whitehead"})
        form = From_Pharmacie.From_Pharmacie(request.POST)
        if request.method == 'POST':
            create=Pharmacie.objects.create(
                nom_Pharmacie=request.POST.get("nom_Pharmacie"),adresse=request.POST.get("address"),Locality=request.POST.get("locality"),
                position_lat=request.POST.get("position_lat"),position_lng=request.POST.get("position_lng"),City_District_Town=request.POST.get("city"),
                PinCode=request.POST.get("postal_code"),tel=request.POST.get("NumberPhone"),state=request.POST.get("state"),
                sidegarde=1,idutil=Utilisateur2.objects.get(pk=request.session.get('user'))
            )
            messages.success(request, 'Form submission successful add Pharmaci')
            create.save()
            return redirect('/add',)

            print(create)
        else:
            form = From_Pharmacie.From_Pharmacie()
        return render(request,'index.html',{"form":form})
        
