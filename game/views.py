from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">黄金矿工</h1>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line3 = '<hr>'
    line2 = '<img src="https://cdn.acwing.com/media/article/image/2022/05/24/41662_a9fb9754da-goldminer-home.png" width=1000>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line4 = '<a href="/">返回主界面</a><hr>'
    line2 = '<img src="https://cdn.acwing.com/media/article/image/2022/05/24/41662_c9dec791da-top.jpg" width=1000>'
    line3= '<img src="https://cdn.acwing.com/media/article/image/2022/05/24/41662_b42889f2da-bg.jpg" width=1000>'
    return HttpResponse(line1 + line4 + line2 + line3)
