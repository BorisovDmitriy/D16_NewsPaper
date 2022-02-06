from django.urls import path
from .views import PostsList, PostDetail, PostsSearchList, PostCreate, PostUpdate, PostDelete, subscription
from django.views.decorators.cache import cache_page  # D11 п.53.1

urlpatterns = [
    # path означает "путь". В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', cache_page(60*5)(PostsList.as_view())),  # Основная страница.
    path('<int:pk>', PostDetail.as_view(), name='post'),  # Вывод по одному объекту
    path('search/', PostsSearchList.as_view(), name='posts_filters'),  # Поиск объектов
    path('add/', PostCreate.as_view(), name='post_create'),  # Создание объектов
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),  # Редактирование объектов
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),  # Удаление объектов as_view()!!!
    path('subscription/', subscription, name='subscription'),  # поле подписаться
            ]
