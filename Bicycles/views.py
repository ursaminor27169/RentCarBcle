from django.shortcuts import render
from .models import Bsles, Marks, Type


def bicycles(request):
    Bicycles = Bsles.objects.all()
    stamps = Marks.objects.all()
    types = Type.objects.all()
    context = {'Bicycles': Bicycles, 'stamps': stamps, 'types': types}
    return render(request, 'Bicycles/Bicycles.html', context)


def filter_by_stamp(request, stamp_id):
    Bicycle = Bsles.objects.filter(stamp=stamp_id)
    stamps = Marks.objects.all()
    context = {'Bicycles': Bicycle, 'stamps': stamps}
    return render(request, 'Bicycles/by_stamps.html', context)


def filter_by_type(request, type_id):
    Bicycle = Bsles.objects.filter(type=type_id)
    types = Type.objects.all()
    context = {'Bicycles': Bicycle, 'types': types}
    return render(request, 'Bicycles/by_types.html', context)
