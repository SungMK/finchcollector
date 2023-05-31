from django.shortcuts import render

# Create your views here.

finches = [
    {'name': 'House Finch'},
    {'name': 'American Goldfinch'},
    {'name': 'Common Chaffinch'},
    {'name': 'Brambling'},
    {'name': 'Evening Grosbeak'},
    {'name': 'Hawfinch'},
    {'name': 'Desert Finch'},
]
     
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
})