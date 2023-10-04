from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.

# hien thi trang chu cua app bang cach render template'home.html'
# ham render nhan vao yeu cau request va ten template sau do tra ve mot HttpResponse chua noi dung cua template da duoc render
def home(request):
    return render(request, 'home.html')

# hien thi trang chat cua mot phong cu the
# phuong thuc GET de lay gia tri cua truong 'username' tu yeu cau, cho phep nguoi dung nhap ten de tham gia phong chat
# phuong thuc get cua doi tuong Room truyen vao dieu kien ten phong chat la 'room' gan ket qua truy van cho bien room_details
# ham render tai va hien thi template 'room.html'
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

# kiem tra mot phong chat co ton tai trong CSDL hay khong
# lay gia tri cua cac truong room_name va user_name tu yeu cau POST
# kiem tra co phong nao trong CSDL co ten la room_name khong, co thi chuyen den phong do, sai thi tao phong moi va luu vao CSDL
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

# xu ly qua trinh gui tin trong mot phong chat
# ham lay gia tri cua cac truong 'message', 'username', 'room_id'' tu yeu cau POST
# mot phien ban moi cua mo hinh Message duoc tao ra bang cach su dung phuong thuc create(), cac truong cua Message la cac bien o tren, sau do luu vao CSDL
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
    
# lay danh sach cac tin nhan trong mot phong chat va tra ve duoi dang mot JSON response
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})