from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import k_washing
from .forms import k_washingForm

# Create your views here.
class k_washingList(ListView):
    model = k_washing
    fields = ['floor','direction']

    def get(self, request):
        if request.method == 'GET':
            print("safjkfjlsdfjkllsd")
            form = k_washingForm(request.GET)
            print(form.is_bound)
            print(form.errors)
            if form.is_valid():
                print("is valid")
                # form.save()
                floor_ = form.cleaned_data.get('floor')
                direction_ = form.cleaned_data.get('direction')
                print(floor_)
                print(direction_)
                return render(request, 'k_washing/k_washing_list.html', {"k_washing_list2": k_washing.objects.filter(floor = floor_, direction = direction_)})
        else:
            form = k_washingForm()
        return render(request, 'k_washing/k_washing_list.html')


    
class k_washingCreate(LoginRequiredMixin, CreateView):
    model = k_washing
    fields = ['floor','direction', 'time', 'content']
    form = k_washingForm()

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(k_washingCreate, self).form_valid(form)

            return response
        else:
            return redirect('/k_washing/')

