from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('auctions/<int:catId>', views.auctions, name='auctions'),
    # path('auction/<int:id>/', views.auction, name='auction'),
    # path('auction/<int:id>/bid/', views.bid, name='bid'),
    # path('auction/<int:id>/comment/', views.comment, name='comment'),
    # path('auction/<int:id>/watchlist/', views.watchlist, name='watchlist'),
    # path('auction/<int:id>/close/', views.close, name='close'),

    # path('categories/', views.categories, name='categories'),
    # path('category/<int:id>/', views.category, name='category'),

    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register, name='register'),

    # path('watchlist/', views.watchlist, name='watchlist'),
    # path('watchlist/<int:id>/remove/', views.remove, name='remove'),
    # path('watchlist/<int:id>/add/', views.add, name='add'),

    path('create/', views.create, name='create'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/<int:id>/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
