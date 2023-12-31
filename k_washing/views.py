from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import k_washing
from .forms import k_washingForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json

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
                print("is valid")
                #form.save()
                print(form.errors)
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

                time_past=0
                hour_past=0
                minute_past=0

                n=0

                if k_washing_list2:
                    for i in k_washing_list2:
                        if n == 0:
                            minute_past = int(i.finish_time.split(':')[1])
                            hour_past = int(i.finish_time.split(':')[0])
                            time_past = i.time
                            print('첫 time_:')
                            print(time_)
                            n=1
                        elif i.finish_time:
                            minute_=(minute_past+time_past)%60
                            hour_=(hour_past+(minute_past+time_past)//60)%24
                            time_=str(hour_)+":"+str(minute_)

                            print('time_:')
                            print(time_)

                            
                            if time_ != i.finish_time:
                                print("i.finish_time")
                                print(i.finish_time)
                                i.finish_time = time_
                                minute_past = int(i.finish_time.split(':')[1])
                                hour_past = int(i.finish_time.split(':')[0])
                                time_past = i.time
                                i.save()
                                              
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
                state = 0
                print("k_washing_list2")
                print(k_washing_list2)
                if k_washing_list2:
                    print("-------------------")
                    print("time")
                    print(k_washing_list2[0].time)

                    if self.request.user == k_washing_list2[0].author:
                        state = 1
                    hour = int(k_washing_list2[0].finish_time.split(':')[0])
                    minute= int(k_washing_list2[0].finish_time.split(':')[1])
                    k_washing_list2[0].time = hour*60+minute-now.hour*60-now.minute
                    time_first = k_washing_list2[0].time

                    if k_washing_list2[0].time <= 0:
                        messages.warning(request, '빨래가 다 되었습니다.')
                        if len(k_washing_list2)>1:
                            hour__ = int(k_washing_list2[1].finish_time.split(':')[0])
                            minute__= int(k_washing_list2[1].finish_time.split(':')[1])
                            time__1 = minute+hour*60 - k_washing_list2[0].time
                            minute__ = time__1 % 60
                            hour__ = time__1 // 60
                            k_washing_list2[1].finish_time = str(hour__) + ":" + str(minute__)
                        k_washing_list2[0].delete()

                    if k_washing_list2[0]:
                        pk_1 = k_washing_list2[0].pk
                        if len(k_washing_list2)>1:
                            pk_2=k_washing_list2[1].pk
                        else: pk_2=0
                    else:
                        pk_1 = 0
                        pk_2=0
                else:
                    pk_1 = 0
                    pk_2=0

                print("pk_1: ")
                print(pk_1)
                print("k_washing_list2")
                print(k_washing_list2)
                return render(
                    request,
                    'k_washing/k_washing_list.html',
                    {
                        "k_washing_list2": k_washing_list2,
                        "floor_": floor_,
                        "direction_": direction_,
                        "time_": time_,
                        "state": state,
                        "time_first": time_first,
                        "pk_1": pk_1,
                        "pk_2": pk_2,
                    }
                )
            else:
                #print("15456fsd86a4f89asd4f6515sd4fa561sdf") 
                print(form.errors)
        else:
            form = k_washingForm()
        return render(request, 'k_washing/k_washing_list.html')


from django.http import JsonResponse

@login_required(login_url='common:login')
def k_washing_list_delete(request, pk_1, pk_2):
    print("삭제버튼 눌려짐")
    print("pk_1: ")
    print(pk_1)
    print("***********************")
    print("pk_2: ")
    print(pk_2)

    if pk_1 is None:
        redirect('/')
    

    k_washing_a = None
    k_washing_b = None
    try:
        k_washing_a = get_object_or_404(k_washing, pk=pk_1)
        k_washing_b = get_object_or_404(k_washing, pk=pk_2)


        print("해치웠나")
        if request.user != k_washing_a.author:
            print(request.user)
            print(k_washing_a.author)
            messages.error(request, '현재 진행중인 세탁이 없습니다.')
            return redirect('/')
        print("뭐임 ?")
        print("==========================================")
        print("아아아아아ㅏ아아아아ㅏ")
        if k_washing_b:
            hour = int(k_washing_b.finish_time.split(':')[0])
            minute= int(k_washing_b.finish_time.split(':')[1])
            time__1 = minute+hour*60 - k_washing_a.time
            minute = time__1 % 60
            hour = time__1 // 60
            k_washing_b.finish_time = str(hour) + ":" + str(minute)
            k_washing_b.save()
            print( "k_washing_b.finish_time")
            print( k_washing_b.finish_time)
        print("==========================================")
        if k_washing_a: 
            k_washing.objects.filter(pk=pk_1).delete()
            messages.warning(request, '세탁이 종료되었습니다.')
        # 삭제 후 현재 페이지에 머물도록 JSON 응답 반환
        if request.is_ajax():
            return JsonResponse({'deleted': True})
        return redirect('/')  # 혹은 적절한 리다이렉션 URL로 변경
    except:
        # k_washing_b 객체가 없는 경우에는 k_washing_a 객체만 삭제
        if k_washing_a:
            k_washing.objects.filter(pk=pk_1).delete()
            messages.warning(request, '세탁이 종료되었습니다.')
        return redirect('/')



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
            return redirect('/')
