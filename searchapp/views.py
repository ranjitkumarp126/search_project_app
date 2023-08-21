from django.shortcuts import render

# Create your views here.
def home(request):
    query = request.GET.get('q', '')  # Get the value of the search query
    context = {'query': query}
    return render(request, 'home.html', context)
