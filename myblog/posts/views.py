from django.shortcuts import get_object_or_404
from .models import Post
from .models import PostForm
from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect


# HOME PAGE
def post_home(request):
    context = {
        'post_obj': Post.objects.all(),
    }
    return render(request, 'blog/post_home.html', context)


# Post Details
def post_details(request, id):
    context = {
        'post': get_object_or_404(Post, id=id)
    }
    return render(request, 'blog/post_details.html', context)


# Create Post Form
def post_form(request):

    if request.method == 'POST':
        form_obj = PostForm(request.POST)

        if form_obj.is_valid():
            instance = form_obj.save()
            instance.save()
            return HttpResponseRedirect(reverse('post_home'))

    else:
        form_obj = PostForm()

    context = {'form': form_obj}
    return render(request, 'blog/post_form.html', context)


# Edit Post Form
def post_edit(request, id):
    instance = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form_obj = PostForm(request.POST, instance=instance)

        if form_obj.is_valid():
            form_obj.save()
            return HttpResponseRedirect(
                reverse('post_details',
                kwargs={'id': id})
            )

    else:
        form_obj = PostForm()

    context = {
        'post': get_object_or_404(Post, id=id),
        'form': form_obj,
    }
    return render(request, 'blog/post_edit.html', context)


# Delete Post
def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('post_home'))
