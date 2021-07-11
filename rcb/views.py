from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from Comments.models import Comments
from Comments.forms import CommentForm


class HomeListView(FormMixin, ListView):
    model = Comments
    template_name = "rcb/main.html"
    context_object_name = 'list_comments'
    form_class = CommentForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_num'] = len(User.objects.all())
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateComment(UpdateView):
    model = Comments
    template_name = "rcb/main.html"
    form_class = CommentForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        kwargs["update"] = True
        return super().get_context_data(**kwargs)


class DeleteComment(DeleteView):
    model = Comments
    template_name = "rcb/main.html"
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        kwargs["update"] = True
        return super().get_context_data(**kwargs)