import json

import keybr_stat as ks
import gui
import plots as pl


data = {}


def load_data(path : str):
    f = open(path, 'r')
    global data
    data = json.load(f)


def show_daily_graph():
    data = ks.get_daily_stats()
    pl.show_daily_graph(data)


def save_daily_graph():
    data = ks.get_daily_stats()
    path = gui.get_save_file_path()
    pl.save_daily_graph(data, path)


def choose_date():
    dates = ks.get_dates()
    year = ''
    month = ''
    day = 0
    if len(dates) == 1:
        year = list(dates.keys())[0]
        print('Selected year: %s' % year)
    else:
        print('Enter the year:')
        count = 1
        for date in dates:
            print(str(count) + ') ' + date)
            count += 1
        while True:
            year = input()
            if year not in dates:
                print('>>>Wrong input<<<')
            else:
                print('Selected year: %s' % year)
                break

    months = dates[year]
    if len(months) == 1:
        month = list(months.keys())[0]
        print('Selected month: %s' % month)
    else:
        print('Enter the month:')
        count = 1
        for date in months:
            print(str(count) + ') ' + date)
            count += 1
        while True:
            month = input()
            if month not in months:
                print('>>>Wrong input<<<')
            else:
                print('Selected month: %s' % month)
                break

    days = months[month]
    if len(days) == 1:
        day = list(months.keys())[0]
        print('Selected month: %s' % day)
    else:
        print('Enter the month:')
        count = 1
        for date in days:
            print(str(count) + ') ' + date)
            count += 1
        while True:
            day = input()
            if day not in days:
                print('>>>Wrong input<<<')
            else:
                print('Selected month: %s' % day)
                break

    date = year + '-' + month + '-' + day 
    print('Selected date: ' + date)
    return date

def show_graph_on_day():
    date = choose_date()
    stat = ks.get_hourly_stat(date)
    pl.show_hourly_progress_graph(stat)
