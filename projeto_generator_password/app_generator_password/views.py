from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'generators/home.html')

def passwords(request):

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0987654321"
    symbols = "!@#$%&*?"

    to_generate = lower_case + upper_case + numbers + symbols

    length_password = int(request.GET.get('number_characters'))

    if length_password == 0:
        password = "There are no passwords with 0 characters.. Please try again!"
    elif length_password < 0:
        password = "There are no passwords with negative characters. Please try again!"
    elif length_password < 70:
        password = "".join(random.sample(to_generate, length_password))
    else:
        password = "The password is too long. Please try again!"

    return render(request, 'generators/password.html', {"senha": password})