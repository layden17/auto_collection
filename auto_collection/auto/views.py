from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm


def car_list(request):
    query = request.GET.get('query')
    filter_by = request.GET.get('filter_by')

    if query and filter_by:
        if filter_by == 'brand':
            cars = Car.objects.filter(brand__icontains=query)
        elif filter_by == 'model':
            cars = Car.objects.filter(model__icontains=query)
        elif filter_by == 'year':
            cars = Car.objects.filter(year__icontains=query)
        elif filter_by == 'price':
            cars = Car.objects.filter(price__icontains=query)
        else:
            cars = Car.objects.all()
    else:
        cars = Car.objects.all()

    return render(request, 'cars/car_list.html', {'cars': cars})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})

def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_confirm_delete.html', {'car': car})



