from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from core.models import Transaction
from django.http import HttpResponse
@csrf_exempt 
def home(request):
    data = request.body.decode('utf-8').split('\n')
    nedded_data = data[1:]
   # print(request)
    print(nedded_data)

    #Meter number
    meter = nedded_data[0]
    splited_meter_list = meter.split(':',1)
    meter_only = splited_meter_list[1]
   # print(meter_only)

    #Date
    date = nedded_data[2]
    splited_date_list = date.split(':',1)
    date_only = splited_date_list[1]
    #print(date_only)

    #Token
    token = nedded_data[1]
    splited_token_list = token.split(':',1)
    token_only = splited_token_list[1]
    #print(token_only)

    #Units
    unit = nedded_data[3]
    splited_unit_list = unit.split(':',1)
    unit_only = splited_unit_list[1]
    #print(unit_only)

    #Amount
    amount = nedded_data[4]
    splited_amount_list = amount.split(':',1)
    amount_only = splited_amount_list[1]
    #print(amount_only)

    #Token amount
    token_amount = nedded_data[5]
    splited_tokenamount_list = token_amount.split(':',1)
    token_amount_only = splited_tokenamount_list[1]
    print(token_amount_only)

    #VAT
    VAT = nedded_data[6]
    splited_VAT_list = VAT.split(':',1)
    VAT_only = splited_VAT_list[1]
    print(VAT_only)

    #Fuel index charge
    Fuel_energy_charge = nedded_data[7]
    splited_fuel_energy_charge = Fuel_energy_charge.split(':',1)
    fuel_energy_charge_only = splited_fuel_energy_charge[1]
    print(fuel_energy_charge_only)

    #Forex charge
    Forex_charge = nedded_data[8]
    splited_forex_charge = Forex_charge.split(':',1)
    Forex_charge_only = splited_forex_charge[1]
    print(Forex_charge_only)

    #EPRA charge
    EPRA_charge = nedded_data[9]
    splited_EPRA_charge = EPRA_charge.split(':',1)
    EPRA_charge_only = splited_EPRA_charge[1]
    print(EPRA_charge_only)

    #Warma charge
    Warma_charge = nedded_data[10]
    splited_Warma_charge = Warma_charge.split(':',1)
    Warma_charge_only = splited_Warma_charge[1]
    print(Warma_charge_only)


    #REP Charge
    REP_charge = nedded_data[11]
    splited_REP_charge = REP_charge.split(':',1)
    REP_charge_only = splited_REP_charge[1]
    print(REP_charge_only)
    
    #Inflation adjustment
    Inflation_adjustment = nedded_data[12]
    splited_Inflation_adjustment = Inflation_adjustment.split(':',1)
    Inflation_adjustment_only = splited_Inflation_adjustment[1]
    print(Inflation_adjustment_only)

    t = Transaction(meter_no  = meter_only, token = token_only, date = date_only, units = unit_only , amount = amount_only, token_amount = token_amount_only, vat = VAT_only, fuel_energy_charge = fuel_energy_charge_only, forex_charge = Forex_charge_only, Epra_charge =EPRA_charge_only, warma_charge = Warma_charge_only, rep_charge = REP_charge_only, inflation_adjustment = Inflation_adjustment_only)
    t.save()
    return render(request, 'home.html', {})

def token(request, toke_balance):
    return HttpResponse("<h2>This is the balance</h2>")




