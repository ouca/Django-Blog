from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import Http404, HttpResponse
from django.views import generic


# Create your views here.
def paginate_queryset(request, queryset, count):

    paginator = Paginator(queryset, count)
    page = request.GET.get('page',1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

def post_list(request):
    posts = Post.objects.all()
    page_obj = paginate_queryset(request, posts, 12)
    print(page_obj.object_list)
    return render(request, 'blog.html', {
        'posts': posts,
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
    })


def PostDetail(request, pk):
    article = get_object_or_404(Post,id=pk)
    return render(request, 'article.html',{
        'article': article
    })

def List_Python(request):
   Big_Category = Post.objects.filter(category__parent__name='Python')
   page_obj = paginate_queryset(request, Big_Category, 12)
   print(page_obj.object_list)
   return render(request, 'python-big.html', {
        'bigs':Big_Category,
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
                                })

def List_CShrp(request):
   CShrap_Category = Post.objects.filter(category__parent__name='C#')
   page_obj = paginate_queryset(request, CShrap_Category, 12)
   print(page_obj.object_list)
   return render(request, 'C#-big.html', {
        'CS':CShrap_Category,
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
                                })

def List_creation(request):
   creation_Category = Post.objects.filter(category__parent__name='創作物')
   page_obj = paginate_queryset(request, creation_Category, 12)
   print(page_obj.object_list)
   return render(request, 'creation.html', {
        'Creation':creation_Category,
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
                                })

def Small_List(request):
   small_Django = Post.objects.filter(category__name='Django')
   page_obj = paginate_queryset(request, small_Django, 12)
   print(page_obj.object_list)
   return render(request, 'small-Django.html',{
       'sDjango': small_Django,
       'post_list': page_obj.object_list,
       'page_obj': page_obj,
   })

def Small_List_image(request):
   small_image= Post.objects.filter(category__name='画像')
   page_obj = paginate_queryset(request, small_image, 12)
   print(page_obj.object_list)
   return render(request, 'small-img-display.html',{
       'sImg': small_image,
       'post_list': page_obj.object_list,
       'page_obj': page_obj,
   })
