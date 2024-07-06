import django_filters
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Avg, Min, Max
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from requests import Response
from rest_framework import viewsets
from .models import SimpleModel
from .serializers import SimpleModelSerializer
from .filters import MonthFilter
from .utils import UploadingModel


class MineralViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = SimpleModel.objects.all()
    serializer_class = SimpleModelSerializer
    ordering_fields = ['create_time']
    ordering = ['-create_time', ]

    #Фильтрация по месяцу
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = MonthFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        if self.action == 'create':
            serializer = SimpleModelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user.username)

        return Response(serializer.data)

class HomeView(TemplateView):
    template_name = 'index.html'


@login_required()
def minavgmaxconc(request, pk):
    context = {}
    list_m2 = ['iron_content', 'si_content', 'al_content', 'ca_content', 'sulfur_content']
    sm = SimpleModel.objects.filter(create_time__month=pk)
    for value in list_m2:
        context[value] = sm.aggregate(Min(value), Avg(value), Max(value))

    context['current_page'] = pk
    return render(request, 'minim.html', context)

@login_required()
def download_model(request):
    if request.POST:
        file = request.FILES['file']
        uploading_file = UploadingModel({"file": file, "request_user": request.user})
        return redirect('/mineral/')
    return render(request, 'download.html', locals())
