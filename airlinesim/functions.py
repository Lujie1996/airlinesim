from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def wordcount(request):
    return render(request, 'wordcount.html')


def countresult(request):
    words = request.GET['usertext']
    paras = dict()
    paras['wordcount'] = len(words.split(' '))
    paras['charactercount'] = len(words)
    paras['usertext'] = words
    word_count = dict()
    for word in words:
       if word not in word_count:
           word_count[word] = 1
       else:
           word_count[word] += 1
    sorted_wordcount = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    paras['wordfreq'] = sorted_wordcount
    return render(request, 'countresult.html', paras)


def home(request):
    id = request.POST['id']
    psw = request.POST['password']
    paras = dict()
    paras['id'] = id
    if id == 'lujie' and psw == '123456':
        return render(request, 'home.html', paras)
    else:
        return redirect('/')


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