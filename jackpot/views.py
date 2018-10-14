from django.shortcuts import render
from .forms import GameJackpotForm
from .models import GameJackpot

def home(request, pk=None, *args, **kwargs):
    try:
        f = GameJackpot.objects.get(pk=pk)
        if request.method == 'POST':
            form = GameJackpotForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('jackpot:home', pk=pk)
        else:
            form = GameJackpotForm()
        return render(request, 'jackpot/index.html', {'form': form, 'f': f,})
    except GameJackpot.DoesNotExist :
        f = None
        context = {
            'f': f,
        }
        return render(request, 'jackpot/index.html', context)