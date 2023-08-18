from django.http import JsonResponse

def api_home(request, *arg, **kwarg):
    return JsonResponse({"message": "Json answer, we come in peace"})