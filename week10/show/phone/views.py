from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Avg
import json
from .models import SmzdmPhone


def index(request):
    contents = SmzdmPhone.objects.all()
    #采集时间选项
    options = SmzdmPhone.objects.values('updatedt').order_by(
        'updatedt').distinct()
    #采集时间 评论内容过滤
    content = request.GET.get('content', '')
    updatedt = request.GET.get('updatedt', '')
    if content:
        contents = contents.filter(content__icontains=content)
    if updatedt:
        contents = contents.filter(updatedt__exact=updatedt)
    #按手机评论数量分类（柱状图）
    sum1 = SmzdmPhone.objects.values('product').annotate(count=Count('product'))
    sum1_lable = ','.join([item['product'] for item in sum1])
    sum1_data = [item['count'] for item in sum1]
    #按舆情分析平均分
    sum2 = SmzdmPhone.objects.values('product').annotate(avg=Avg('sentiments'))
    sum2_lable = ','.join([item['product'] for item in sum2])
    sum2_data = [item['avg'] for item in sum2]
    return render(request, 'index.html', locals())