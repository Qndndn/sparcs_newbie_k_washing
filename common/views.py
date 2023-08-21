from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            if user is not None:
                login(request, user)  # 로그인
                return redirect('/')
            else:
                # Authentication failed, handle this case (e.g., show an error message)
                form.add_error('username', 'Authentication failed. Please check your credentials.')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        #print(user)
        #print(request)
        if user is not None:
            login(request, user)  # 세션 처리
            return redirect('/')  # 로그인 후 리다이렉션
        else:
            # 로그인 실패 처리
            return render(request, 'common/login.html', {'error_message': '로그인 실패'})
    return render(request, 'common/login.html')