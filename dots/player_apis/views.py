from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseServerError, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers
from .models import player_data
import json

"""
Methods in views.py
1. create_player (POST)
2. player_details (GET and PUT routes combined due to similar path.)
3. leaderboards (GET)
"""


# POST - Create Player 
@csrf_exempt
def create_player(request):
    if request.method == "POST":
        try:
            if len(request.body) == 0 or len(json.loads(request.body)) == 0:
                return HttpResponseBadRequest("Request body cannot be empty.")

            data = json.loads(request.body)

            details = player_data.objects.create(
                username=data['username']
            )

            return JsonResponse({
                "username": details.username,
                "player_id": details.id
            })
        except Exception as e:
            # System Log 
            print(f"ERROR : view.py : player_details : {e}")
            return HttpResponseServerError("Opps ! There seems to be an error on our side. Please contact support.")
    else:
        raise Http404("Please check the appropriate methods for this route.")

# GET / UPDATE Player Details
@csrf_exempt
def player_details(request,player_id):
    if request.method == "GET":
        try:
            details = player_data.objects.filter(id=player_id).first()
            if details is None:
                return HttpResponseNotFound("Player Not Found")
            return JsonResponse({
                "username": details.username,
                "player_id": details.id,
                "xp": details.xp,
                "gold": details.gold
            })
        except Exception as e:
            # System Log 
            print(f"ERROR : view.py : player_details : {e}")
            return HttpResponseServerError("Opps ! There seems to be an error on our side. Please contact support.")
    elif request.method == "PUT":
        try:
            if len(request.body) == 0 or len(json.loads(request.body)) == 0:
                return HttpResponseBadRequest("Request body cannot be empty.")

            data = json.loads(request.body)

            if player_data.objects.filter(id=player_id).first() is None:
                return HttpResponseNotFound("Player Not Found")

            player_data.objects.filter(id=player_id).update(
                username=data['username'],
                xp=data['xp'],
                gold=data['gold']
            )
            details = player_data.objects.filter(id=player_id).first()

            return JsonResponse({
                "username": details.username,
                "player_id": details.id,
                "xp": details.xp,
                "gold": details.gold
            })
        except Exception as e:
            # System Log 
            print(f"ERROR : view.py : player_details : {e}")
            return HttpResponseServerError("Opps ! There seems to be an error on our side. Please contact support.")
    else:
        raise Http404("Please check the appropriate methods for this route.")

# GET - Fetch Leaderboard
@csrf_exempt
def leaderboards(request):
    if request.method == "GET":
        try:
            sortby = request.GET.get("sortby")
            if sortby is not None and sortby not in ["gold", "xp"]:
                return HttpResponseBadRequest("sortby parameter must be either gold or xp.")
            else:
                # Default sortby is by "xp"
                sortby = "xp"

            size = int(request.GET.get("size")) if request.GET.get("size") else None

            details = player_data.objects.all().order_by(f"-{sortby}")[:size]

            
            details = model_to_dict_arr(details)

            return HttpResponse(json.dumps(details), content_type='application/json')
        except Exception as e:
            # System Log 
            print(f"ERROR : view.py : leaderboards : {e}")
            return HttpResponseServerError("Opps ! There seems to be an error on our side. Please contact support.")
    else:
        raise Http404("Please check the appropriate methods for this route.")


def model_to_dict_arr(arr):
    output = []
    for element in arr:
        output.append(model_to_dict(element))
    return output
