from django.shortcuts import render
from django.db.models import Count, Sum
from assets_TrackerApp.models import Assets, Movements, Departments
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login')
def dashboard_view(request):
    total_assets = Assets.objects.count()
    available_assets = Assets.objects.filter(availability=True).count()
    unavailable_assets = Assets.objects.filter(availability=False).count()
    total_movements = Movements.objects.count()
    departments = Departments.objects.count()

    total_value = Assets.objects.aggregate(total_value=Sum('price'))['total_value'] or 0

    asset_types = Assets.objects.values('category__name').annotate(count=Count('id'))
    asset_pie_data = {item['category__name']: item['count'] for item in asset_types if item['category__name']}

    asset_locations = Assets.objects.values('department__name').annotate(count=Count('id'))
    asset_bar_data = {item['department__name']: item['count'] for item in asset_locations if item['department__name']}

    context = {
        'total_assets': total_assets,
        'available_assets': available_assets,
        'unavailable_assets': unavailable_assets,
        'total_movements': total_movements,
        'departments': departments,
        'total_value': total_value,
        'asset_pie_data': asset_pie_data,
        'asset_bar_data': asset_bar_data,
    }

    return render(request, 'pages/dashboard.html', context)
