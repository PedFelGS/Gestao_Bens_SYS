from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Assets, Categories, Departments, Suppliers
from .forms import assetForm, CategoryForm, DepartmentForm, SupplierForm
from django.contrib.auth.decorators import login_required, user_passes_test
import csv

def is_manager(user):
    return user.is_staff  

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def asset_create(req):
    if req.method == "POST":
        form = assetForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('assets_TrackerApp:asset_list')
    else:
        form = assetForm()
    return render(req, 'assets/form.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def asset_import(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            next(reader)

            for row in reader:
                try:
                    asset_data = {
                        'rfid_tag': row[0],
                        'name': row[1],
                        'price': row[2],
                        'category': row[3],
                        'department': row[4],
                        'supplier': row[5],
                        'path': row[6],
                        'availability': row[7].strip().lower() == 'true'
                    }
                    form = assetForm(asset_data)
                    if form.is_valid():
                        form.save()
                    else:
                        messages.error(request, f"Erro ao importar o ativo: {row[1]}. {form.errors}")
                except Exception as e:
                    messages.error(request, f"Erro ao processar o ativo {row[1]}: {e}")
            messages.success(request, 'Ativos importados com sucesso!')
        except Exception as e:
            messages.error(request, f"Erro ao ler o arquivo: {e}")
        return redirect('assets_TrackerApp:asset_list')

    return render(request, 'assets/import.html')

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def asset_list(request):
    departments = Departments.objects.all()
    categories = Categories.objects.all()
    suppliers = Suppliers.objects.all()

    assets = Assets.objects.all()

    if request.GET.get('department'):
        assets = assets.filter(department__name=request.GET.get('department'))
    if request.GET.get('category'):
        assets = assets.filter(category__name=request.GET.get('category'))
    if request.GET.get('supplier'):
        assets = assets.filter(supplier__name=request.GET.get('supplier'))
    if request.GET.get('availability') is not None:
        availability = request.GET.get('availability') == 'true'
        assets = assets.filter(availability=availability)
        
    if request.GET.get('export') == 'csv':

        selected_ids = request.GET.get('selected_ids')
        if selected_ids:
            id_list = selected_ids.split(',')
            assets = assets.filter(id__in=id_list)
            
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="assets.csv"'

        writer = csv.writer(response)

        writer.writerow(['ID', 'RFID', 'Name', 'Price', 'Category', 'Department', 'Supplier', 'Path', 'Availability'])
        for asset in assets:
            writer.writerow([
                asset.id,
                asset.rfid_tag,
                asset.name,
                asset.price,
                asset.category.name if asset.category else '',
                asset.department.name if asset.department else '',
                asset.supplier.name if asset.supplier else '',
                asset.path,
                asset.availability
            ])
        return response

    if request.GET.get('format') == 'json':
        asset_list = list(assets.values('id', 'name', 'price', 'category__name', 'path', 'availability'))
        return JsonResponse({"assets": asset_list})

    return render(request, 'assets/list.html', {
        'assets': assets,
        'departments': departments,
        'categories': categories,
        'suppliers': suppliers,
    })
@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def asset_detail(request, id):
    asset = get_object_or_404(Assets, id=id)
    return render(request, 'assets/detail.html', {'asset': asset})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def asset_update(request, id):
    asset = get_object_or_404(Assets, id=id)
    if request.method == 'POST':
        form = assetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('assets_TrackerApp:asset_detail', id=asset.id)
    else:
        form = assetForm(instance=asset)
    return render(request, 'assets/update.html', {'form': form, 'asset': asset})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def asset_delete(request, id):
    asset = get_object_or_404(Assets, id=id)
    if request.method == 'POST':
        asset.delete()
        messages.success(request, 'Ativo deletado com sucesso!')
        return redirect('assets_TrackerApp:asset_list')
    return render(request, 'assets/delete.html', {'asset': asset})

##

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'categories/list.html', {'categories': categories})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_detail(request, id):
    category = get_object_or_404(Categories, id=id)
    return render(request, 'categories/detail.html', {'category': category})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assets_TrackerApp:category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/form.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_update(request, id):
    category = get_object_or_404(Categories, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('assets_TrackerApp:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/update.html', {'form': form, 'category': category})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_delete(request, id):
    category = get_object_or_404(Categories, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('assets_TrackerApp:category_list')
    return render(request, 'categories/delete.html', {'category': category})

##


@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def department_list(request):
    departments = Departments.objects.all()
    return render(request, 'departments/list.html', {'departments': departments})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def department_detail(request, id):
    department = get_object_or_404(Departments, id=id)
    return render(request, 'departments/detail.html', {'department': department})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assets_TrackerApp:department_list')
    else:
        form = DepartmentForm()
    return render(request, 'departments/form.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def department_update(request, id):
    department = get_object_or_404(Departments, id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('assets_TrackerApp:department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'departments/update.html', {'form': form, 'department': department})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def department_delete(request, id):
    department = get_object_or_404(Departments, id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('assets_TrackerApp:department_list')
    return render(request, 'departments/delete.html', {'department': department})



##


@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def supplier_list(request):
    suppliers = Suppliers.objects.all()
    return render(request, 'suppliers/list.html', {'suppliers': suppliers})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def supplier_detail(request, id):
    supplier = get_object_or_404(Suppliers, id=id)
    return render(request, 'suppliers/detail.html', {'supplier': supplier})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assets_TrackerApp:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/form.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def supplier_update(request, id):
    supplier = get_object_or_404(Suppliers, id=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('assets_TrackerApp:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/update.html', {'form': form, 'supplier': supplier})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def supplier_delete(request, id):
    supplier = get_object_or_404(Suppliers, id=id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('assets_TrackerApp:supplier_list')
    return render(request, 'suppliers/delete.html', {'supplier': supplier})









