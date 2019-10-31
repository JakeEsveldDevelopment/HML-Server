from django.http import JsonResponse
from rest_framework.decorators import api_view
import json


@api_view(["GET"])
def getUser(request):
    user = request.user
    id = user.id
    username = user.username
    return JsonResponse({'id': id, "username": username}, safe=True)
