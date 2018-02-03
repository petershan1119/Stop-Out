from django.urls import path
from . import views

urlpatterns = [
    path('', views.webtoon_list, name='webtoon-list'),
    path('<int:webtoon_id>', views.webtoon_detail, name='webtoon-detail'),
]