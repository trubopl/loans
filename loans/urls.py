from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.urls import path
from core.views import Index, PaydayLoans, FirstFreeLoan, GenericHTMLView,\
    Companies, Blog, BlogPosts
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^kalkulator-wyniki/', Index.as_view(), name='generate'),
    url(r'^chwilowki/', PaydayLoans.as_view(), name='payday_loans'),
    url(r'^blog/$', Blog.as_view(), name="blog"),
    url(r'^blog/(?P<post>[\w-]+)/$', BlogPosts.as_view(), name="blog_posts"),
    url(r'^darmowe-pozyczki/', FirstFreeLoan.as_view(), name='first_free_loan'),
    url(r'^firmy/$', Companies.as_view(), name='companies'),
    url(r'^firmy/(?P<page>.+)$', GenericHTMLView.as_view()),

]

