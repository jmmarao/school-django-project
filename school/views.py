from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        students = {'id': 1, "name": 'Iron Man'}
        return JsonResponse(students)