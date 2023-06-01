from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def home(request):
    return render(request, 'home.html')

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def admin_table(request):
    feedback_entries = Feedback.objects.all()
    return render(request, 'admin_table.html', {'feedback_entries' :feedback_entries})
def feedback_success(request):
    return render(request,'feedback_success.html')

# Create your views here.
