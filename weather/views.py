from django.shortcuts import render, redirect
from .models import meteoData
import json
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import openpyxl
import pandas as pd
# Create your views here.
def base(request):
    return render(request, 'base.html')
def getMeteoData(request):
    data = meteoData.objects.all()
    data_json = serializers.serialize('json', data)
    return JsonResponse(data_json, safe=False)
@csrf_exempt 
def add_data_to_excel(request):
    if request.method == 'POST':
        file_name = 'weather.xls'
        json_data = json.loads(request.body)
        new_data = [
                json_data.get('stn', ''),
                json_data.get('sdate', ''),
                json_data.get('RRR', ''),
                json_data.get('Tmax', ''),
                json_data.get('T2', ''),
                json_data.get('soil_temp_mean', ''),
                json_data.get('RH', ''),
                json_data.get('AH', ''),
                json_data.get('ff', ''),
                json_data.get('dirn', ''),
                json_data.get('dp', ''),
            ]
        data = {'stn': new_data[0], 'sdate':new_data[1], 'RRR':new_data[2], 'Tmax':new_data[3], 'T2':new_data[4], 'soil_temp_mean':new_data[5], 'RH':new_data[6], 'AH':new_data[7], 'ff':new_data[8], 'dirn':new_data[9], 'dp':new_data[10]}
        
        new_entry_df = pd.DataFrame(data, index=[0])
        print(new_entry_df)

        # Write the updated DataFrame back to the Excel file
        # new_entry_df.to_excel(file_name, index=False, engine='openpyxl')
        with pd.ExcelWriter("weather.xlsx", mode='a') as writer:
            new_entry_df.to_excel(writer, sheet_name='Sheet1', if_sheet_exists="overlay") 
        return JsonResponse({'success': True, 'message': 'Success'})  # Redirect to a success page

    return JsonResponse({'success': False, 'message': 'Invalid JSON data'})