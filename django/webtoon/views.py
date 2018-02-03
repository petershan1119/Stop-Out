from django.shortcuts import render
from .models import Webtoon

def webtoon_list(request):
    webtoons = Webtoon.objects.all()
    context = {
        'webtoons': webtoons,
    }
    return render(
        request=request,
        template_name='webtoon/webtoon_list.html',
        context=context,
    )

def webtoon_detail(request, pk):
    context = {
        'webtoon': Webtoon.objects.get(pk=pk),
    }
    return render(
        request=request,
        template_name='webtoon/webtoon_detail.html',
        context=context,
    )