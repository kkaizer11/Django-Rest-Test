from django.http import JsonResponse

def api_home(request, *arg, **kwarg):
    body = request.body
    print(body)
    return JsonResponse({"message": "Json answer, we come in peace"})