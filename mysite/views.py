from django.views.generic import ListView, TemplateView
from youtube.models import Video, Channel
from django.views.generic import CreateView
from mysite.forms import CreateUserForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin


class Home(ListView):
    template_name = 'home.html'
    model = Video

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "글쓴이만 이 글의 수정과 삭제가 가능합니다."

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)