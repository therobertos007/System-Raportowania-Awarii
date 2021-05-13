from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def register(request):
    """Rejestracja nowego użytkownika."""
    if request.method != 'POST':
        #Wyświetlenie pustego formularza rejestracji
        form = UserCreationForm()
    else:
        #Przetworzenie wypełnionego formularza
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Zalogowanie użytkownika i -> homepage
            login(request, new_user)
            return redirect('learning_2:index')

    #Wyświetlenie pustego lub błędnego formularza
    context = {'form': form}
    return render(request, 'users/register.html', context)
