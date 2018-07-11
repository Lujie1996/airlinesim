from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        id = request.POST.get('id')
        psw = request.POST.get('password')
        if id == 'lujie' and psw == '123456':
            return render(request, 'mycompany.html')
        else:
            return render(request, 'signin.html', {'msg': 'Username or Password incorrect'})


def mycompany(request):
    airline_name = 'Gakki Airline'
    airline_ceo = 'Jie Lu'
    start_time = 'July 1, 2018'
    location = 'Naha, Japan'
    passenger_transported_total = '12,234,201'
    passenger_transported_last_month = '32,455'
    number_of_flights = '125'
    number_of_planes = '64'
    number_of_airports = '102'
    profit_last_week = '$523,302'
    profit_last_month = '$232,435'
    most_profitable_flight = 'GK102'
    most_popular_flight = 'GK211'
    most_popular_city = 'RJTT, Tokyo Haneda Intl.'
    return render(request, 'mycompany.html', locals())


def flight(request):
    flight_no = request.GET.get('flight_no')
    if flight_no is None:
        # Show all flights
        return render(request, 'flight.html', locals())
    else:
        # Show this flight
        return render(request, 'oneflight.html', locals())