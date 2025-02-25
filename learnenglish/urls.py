from django.contrib import admin
from django.urls import path
from index.views import index, dictionary, grammar_page, practice, subscription_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dictionary/', dictionary, name='dictionary'),
    path('grammar/', grammar_page, name='grammar'),
    path('practice/', practice, name='practice'),
    path("subscriptions/", subscription_view, name="subscriptions"),
]