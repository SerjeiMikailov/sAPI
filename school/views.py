from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        student = {'id':1, 'name':'Fulano'}
        return JsonResponse(student)