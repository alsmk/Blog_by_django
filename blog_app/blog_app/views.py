from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

def index(request):
    # return HttpResponseRedirect(reverse(('app_blog: blog_list')))
    # return HttpResponse("Hello, world. You're at the index.")
    return HttpResponseRedirect(reverse('app_blog:blog_list'))


