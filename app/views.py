from django.forms import ModelForm
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from app.models import Article, Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = 'article',


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comment_form'] = CommentForm(self.request.POST)
        return data


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article-detail', kwargs=self.kwargs)
