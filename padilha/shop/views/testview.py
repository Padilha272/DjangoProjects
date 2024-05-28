from django.shortcuts import render
from django.http import HttpResponse

def test_view(request):
    print("test_view called")  
    try:
        return render(request, 'shop/test.html')
    except Exception as e:
        return HttpResponse(f"Error: {e}")
