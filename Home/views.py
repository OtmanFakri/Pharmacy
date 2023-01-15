from django.shortcuts import render
from Acount.models import Utilisateur2
from Pharmascie.models import Pharmacie
from django.http import JsonResponse

# Create your views here.
def HomePage(request):
    return render(request, 'bootleaf-master/index.html',{'login':request.session.get('Login'),
    "Username":Utilisateur2.objects.get(pk=request.session.get('user'))} )


def datas(requset):
  ListPhamarci=Pharmacie.objects.all()

  tt={
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 0,
      "properties": {
        "NAME": "45th Street Theater",
        "TEL": "(212) 352-3101",
        "URL": "http://www.theatermania.com/new-york/theaters/45th-street-theatre_2278/",
        "ADDRESS1": "354 West 45th Street",
        "ADDRES2": 'null',
        "CITY": "New York",
        "ZIP": 10036.0
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          -73.990618,
          40.759851
        ]
      }
    },
 ]
}
  for i in ListPhamarci:
    tt["features"]+={
      "type": "Feature",
      "id": i.id,
      "properties": {
        "NAME": i.nom_Pharmacie,
        "TEL": i.tel,
        "URL": "http://www.theatermania.com/new-york/theaters/45th-street-theatre_2278/",
        "ADDRESS1": i.adresse,
        "ADDRES2": 'null',
        "CITY": i.City_District_Town,
        "ZIP": 10036.0
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          float(i.position_lng),
          float(i.position_lat)
        ]
      }
    },
  
  return JsonResponse(tt)

