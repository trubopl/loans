from __future__ import absolute_import, unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist
from django.http import Http404
from django.utils import timezone
from .forms import SliderForm
from .models import Post
from loans import settings


class Index(View):

    slider_form = SliderForm
    main_page = settings.TEMPLATES_MAIN_PREFIX + "/main_page.html"
    after_slider = settings.TEMPLATES_MAIN_PREFIX + '/after_slider.html'

    def post(self, request):
        form = self.slider_form(request.POST)

        if form.is_valid():

            context = {
                'form': form,
            }
            return render(request, self.after_slider, context)
        else:
            context = {
                'form': form,
            }
            return render(request, self.main_page, context)

    def get(self, request):
        form = self.slider_form
        context = {
            'form': form
        }
        return render(request, self.main_page, context)


class PaydayLoans(View):

    def post(self, request):
        pass

    def get(self, request):
        return render(request,
                      settings.TEMPLATES_MAIN_PREFIX + '/payday_loans.html')


class FirstFreeLoan(View):

    def post(self, request):
        pass

    def get(self, request):
        return render(request,
                      settings.TEMPLATES_MAIN_PREFIX + '/first_free_loan.html')


class Companies(View):

    def post(self, request):
        pass

    def get(self, request):
        return render(request,
                      settings.TEMPLATES_MAIN_PREFIX + '/all_companies.html')

class GenericHTMLView(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = settings.TEMPLATES_COMPANIES_PREFIX +\
                             '/' + page + '.html'
        response = super(GenericHTMLView, self).get(request, *args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()

class Blog(View):
    def post(self, request):
        pass

    def get(self, request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).\
            order_by('published_date')

        context = {
            'posts': posts,
        }

        return render(request,
                      settings.TEMPLATES_MAIN_PREFIX + "/blog.html", context)

class BlogPosts(View):
    def post(self, request):
        pass

    def get(self, request, post):
        single_post = get_object_or_404(Post, slug=post)

        context = {
            'post': single_post

        }
        return render(request, settings.TEMPLATES_MAIN_PREFIX + "/single_blog_posts.html", context)





