from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm
from .models import Comment


@login_required
def edit_comments(
        request, id=None, name=None, template_name='edit_comments.html'):
    """Wiki space for user comments and discussion."""
    try:
        comment = Comment.objects.get(product_id=id)
    except Comment.DoesNotExist:
        comment = None

    comment_form = CommentForm(instance=comment, id=id, name=name)

    if request.POST:
        comment = comment_form.save(commit=False)
        comment.product_id = id
        comment.comment_wiki = request.POST['comment_wiki']
        comment.save()
        messages.add_message(request, messages.SUCCESS, 'Comment Saved')
        return redirect('products')

    args = {'comment_form': comment_form, 'name': name}
    return render(request, template_name, args)


def view_comments(request, id=None, name=None, template_name='comments.html'):
    """Wiki space for user comments and discussion."""
    try:
        comment = Comment.objects.get(product_id=id)
    except Comment.DoesNotExist:
        comment = None

    if comment is None:
        return redirect('edit_comments', id=id, name=name)

    args = {'comment': comment, 'id': id, 'name': name}
    return render(request, template_name, args)
