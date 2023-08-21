from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import k_washing, k_washing_state
from .forms import k_washingForm, k_washing_stateForm
from datetime import datetime

# Create your views here.
class k_washingList(ListView):
    model = k_washing
    fields = ['time','floor','direction', 'finish_time', "k_washing_state_list"]

    def get(self, request):
        if request.method == 'GET':
            form = k_washingForm(request.GET)
            #print(form.is_bound)
            #print(form.errors)
            if form.is_valid():
                print("is valid")
                # form.save()
                floor_ = form.cleaned_data.get('floor')
                direction_ = form.cleaned_data.get('direction')
                #print(floor_)
                #print(direction_)
                k_washing_list2 = k_washing.objects.filter(floor = floor_, direction = direction_, )
                now = datetime.now()
                time1=0
                time_first=0
                if k_washing_list2:
                    for i in k_washing_list2:
                        if i.finish_time:
                            hour = int(i.finish_time.split(':')[0])
                            minute= int(i.finish_time.split(':')[1])
                            i.time = hour*60+minute-now.hour*60-now.minute
                            time1+=i.time
                            if i.time<0:
                                i.delete()
                        else: i.finish_time = str(now.hour)+":"+str(now.minute)

                    #print("self.request.user: ")
                    #print(self.request.user)
                    #print(k_washing_list2[0].author)

                    if self.request.user == k_washing_list2[0].author:
                        k_washing_state_1 = k_washing_state.objects.filter(pk_1 = k_washing_list2[0].pk)
                        k_washing_state_1.state = 1                        
                        print(k_washing_state_1)

                k_washing_state_1 = k_washing_state.objects.all()
                for i in k_washing_state_1:
                    k_washing_state_ = k_washing.objects.filter(pk = i.pk_1)
                    print(i.pk_1)
                    print("dsafjsdlajfklasdjfklsd")
                    print(k_washing.objects.filter(pk = i.pk_1))
                    print(k_washing_state_)
                    i.time_first = k_washing_state_.time
                    if i.time_first<0: i.delete()


                minute_=(now.minute+time1)%60
                hour_=(now.hour+(time1+now.minute)//60)%24
                time_=str(hour_)+":"+str(minute_)

                messages.success(request, f"New account created")
                return render(
                    
                    request,
                    'k_washing/k_washing_list.html',
                    {
                        "k_washing_list2": k_washing_list2,
                        "k_washing_state_list":  k_washing_state.objects.filter(state = 1),
                        "floor_": floor_,
                        "direction_": direction_,
                        "time_": time_,
                        "time_first": time_first,
                    }
                )
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
            form.save()
            k_washing_list2 = k_washing.objects.filter(floor = form.instance.floor, direction = form.instance.direction, )
            time1=0
            for i in k_washing_list2:
                if not i.time: time1+=i.time
            print(form.instance.time)
            time1+=form.instance.time
            now = datetime.now()
            minute = (now.minute+time1)%60
            hour = int(now.hour+int(now.minute+time1)//60)
            form.instance.finish_time= str(hour%12) + ":" + str(minute)
            form.instance.author = current_user
            response = super(k_washingCreate, self).form_valid(form)

            floor = form.instance.floor
            direction = form.instance.direction
            time = form.instance.time
            pk = form.instance.pk
            print(floor)
            print(form)
            form = k_washing_stateForm()
            print(form)
            print("______")
            print(floor)
            print(form.is_bound)
            print(form.errors)
            if form.is_valid():
                floor_1 = form.cleaned_data.get('floor_1')
                direction_1 = form.cleaned_data.get('direction_1')
                time_first = form.cleaned_data.get('time_first')
                state = form.cleaned_data.get('state')
                pk_1 = form.cleaned_data.get('pk_1')

                k_washing_stateform = form.save()
                k_washing_stateform.floor_1 = floor
                k_washing_stateform.direction_1 = direction
                k_washing_stateform.time_first = time
                k_washing_stateform.state = 0
                print(k_washing_stateform.pk_1)
                k_washing_stateform.pk_1 = pk
                k_washing_stateform.save()


            return response
        else:
            return redirect('/k_washing/')

