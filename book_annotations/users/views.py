from django.shortcuts import redirect, render
from users.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
