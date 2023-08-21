from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import k_washing
from .forms import k_washingForm
from datetime import datetime
from django.contrib import messages


# Create your views here.
class k_washingList(ListView):
    model = k_washing
    fields = ['time','floor','direction', 'finish_time', "state"]

    def get(self, request):
        if request.method == 'GET':
            form = k_washingForm(request.GET)
            #print(form.is_bound)
            #print(form.errors)
            if form.is_valid():
                #print("is valid")
                #form.save()
                #print(form.errors)
                floor_ = form.cleaned_data.get('floor')
                direction_ = form.cleaned_data.get('direction')
                #print(floor_)
                #print(direction_)
                k_washing_list2 = k_washing.objects.filter(floor = floor_, direction = direction_, )
                now = datetime.now()

                for i in k_washing_list2:
                    print("888")
                    print(i.time)

                time1=0
                state=0
                time_=""
                time_first=0
                if k_washing_list2:
                    for i in k_washing_list2:
                        if i.finish_time:
                            print("i.finish_time")
                            print(i.finish_time)
                        else: i.finish_time = str(now.hour)+":"+str(now.minute)

                    hour = int(k_washing_list2[len(k_washing_list2)-1].finish_time.split(':')[0])
                    minute = int(k_washing_list2[len(k_washing_list2)-1].finish_time.split(':')[1])
                    time1=hour*60+minute-now.hour*60-now.minute

                    minute_=(now.minute+time1)%60
                    hour_=(now.hour+(time1+now.minute)//60)%24
                    time_=str(hour_)+":"+str(minute_)

                #print("self.request.user: ")
                #print(self.request.user)
                #print(k_washing_list2[0].author)




                if k_washing_list2:
                    #print(k_washing_list2[0])
                    if self.request.user == k_washing_list2[0].author:
                        state = 1
                        if k_washing_list2[0].time<=0:
                            print("빨래가 다 되었습니다.")
                            messages.warning(request, '빨래가 다 되었습니다.')
                            #print(k_washing_list2[0])

                    hour = int(k_washing_list2[0].finish_time.split(':')[0])
                    minute= int(k_washing_list2[0].finish_time.split(':')[1])
                    k_washing_list2[0].time = hour*60+minute-now.hour*60-now.minute

                    if k_washing_list2[0].time <= 0: k_washing_list2[0].delete()

                    time_first = k_washing_list2[0].time
                else: state = 0

                return render(
                    request,
                    'k_washing/k_washing_list.html',
                    {
                        "k_washing_list2": k_washing_list2,
                        "floor_": floor_,
                        "direction_": direction_,
                        "time_": time_,
                        "state": state,
                        "time_first": time_first
                    }
                )
            else:
                #print("15456fsd86a4f89asd4f6515sd4fa561sdf") 
                print(form.errors)
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
                print("00")
                print(i.time)
                time1+=i.time
            now = datetime.now()
            minute = (now.minute+time1)%60
            hour = int(now.hour+int(now.minute+time1)//60)
            form.instance.finish_time= str(hour) + ":" + str(minute)
            form.instance.author = current_user 
            response = super(k_washingCreate, self).form_valid(form)

            return response
        else:
            return redirect('/k_washing/')
