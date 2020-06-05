from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView, View
from youtube.models import Video, Channel
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class AddVideo(LoginRequiredMixin, CreateView):
    model = Video
    fields = ('title', 'video', 'thumbnail')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        try:
            form.instance.channel = Channel.objects.get(owner=self.request.user)
        except:
            return HttpResponseRedirect(reverse('youtube:addChannel'))
        else:
            return super(AddVideo, self).form_valid(form)


class UpdateVideo(OwnerOnlyMixin, UpdateView):
    model = Video
    fields = ['title', 'video', 'thumbnail']
    success_url = reverse_lazy('home')

class PlayVideo(DetailView):
    model = Video
    template_name = 'youtube/playVideo.html'
    def get_queryset(self):
        user = self.request.user
        video = Video.objects.get(pk=self.kwargs['pk'])
        if video.good.filter(id = user.id).exists():
            video.whether = False
            video.save()
            return Video.objects.all()
        else:
            video.whether = True
            video.save()
            return Video.objects.all()

    def get_context_data(self, **kwargs):
        user = self.request.user
        video = Video.objects.get(pk=self.kwargs['pk'])
        channel = Channel.objects.get(owner=video.owner)
        context = super(PlayVideo, self).get_context_data(**kwargs)
        video = Video.objects.get(pk=self.kwargs['pk'])
        if channel.subscribe.filter(id=user.id).exists():
            channel.whether = True
            channel.save()
            context['channel'] = video.channel
            return context
        else:
            channel.whether = False
            channel.save()
            context['channel'] = video.channel
            return context

class DeleteVideo(OwnerOnlyMixin, DeleteView):
    model = Video
    success_url = reverse_lazy('home')


class addChannel(LoginRequiredMixin, CreateView):
    model = Channel
    template_name = 'channel/channel_form.html'
    fields = ('name', 'channel_photo')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if Channel.objects.filter(owner=self.request.user).exists():
            return HttpResponseRedirect(reverse('youtube:channel'))
        else:
            form.instance.owner = self.request.user
            return super().form_valid(form)

class UpdateChannel(OwnerOnlyMixin, UpdateView):
    model = Channel
    template_name = 'channel/channel_form.html'
    fields = ('name', 'channel_photo')
    success_url = reverse_lazy('youtube:channel')

class DeleteChannel(OwnerOnlyMixin, DeleteView):
    model = Channel
    template_name = 'channel/channel_confirm_delete.html'
    success_url = reverse_lazy('home')

@login_required
def MyChannel(request):
    user = request.user
    try:
        channel = get_object_or_404(Channel, owner=user)
    except:
        return HttpResponseRedirect(reverse('youtube:addChannel'))
    else:
        try:
            video = Video.objects.filter(owner=user)
        except:
            return render(request, 'chanel/myChannel.html', {
                'channel': channel,
            })
        else:
            return render(request, 'channel/myChannel.html', {
                'channel': channel,
                'video': video,
            })


class SomeoneChannel(DetailView):
    model = Channel
    template_name = 'channel/channel.html'

    def get_context_data(self, **kwargs):
        channel = Channel.objects.get(pk=self.kwargs['pk'])
        context = super(SomeoneChannel, self).get_context_data(**kwargs)
        context['video'] = Video.objects.filter(owner=channel.owner)
        return context

class VideoList(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'youtube/video_list.html'

    def get_queryset(self):
        return Video.objects.filter(owner=self.request.user)

def seeVideo(request, title):
    video = Video.objects.get(title=title)
    video_id = int(video.id)
    return HttpResponseRedirect(reverse('youtube:playVideo', args=(video_id,)))