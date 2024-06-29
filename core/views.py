
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Assuming you have a success page
    else:
        form = ContactForm()
    return render(request, 'leotech/index.html', {'form': form})



def contact_success(request):
    return render(request, 'leotech/contact_success.html')



