import json
import actions as ac


def daily_fill_keys(result : dict, date : str,  wpm_sum : int, top_wpm : int, accuracy : int, samples_count : int, time_spent : int):
    date_split = date.split('-')
    date_formated = '%s/%s' % (date_split[2], date_split[1])
    result['date'].append(date_formated)
    avarage_wpm = wpm_sum / samples_count
    result['avarage_wpm'].append(avarage_wpm)
    result['top_wpm'].append(top_wpm)
    result['accuracy'].append(accuracy)
    result['samples_count'].append(samples_count)
    time_spent_minutes = time_spent / 60000
    result['time_spent'].append(time_spent_minutes)


def get_daily_stats():
    data = ac.data
    keys = ['date', 'avarage_wpm', 'top_wpm', 'accuracy', 'samples_count', 'time_spent']
    result = dict((i, [],) for i in keys)
    wpm_sum = top_wpm = errors_sum = samples_count = characters_sum = time_spent = 0
    date_record = data[0]['timeStamp'].split('T')[0]
    for i in data:
        date = i['timeStamp'].split('T')[0]
        if date != date_record:
            accuracy = (1 - errors_sum / characters_sum) * 100
            daily_fill_keys(result, date_record, wpm_sum, top_wpm, accuracy, samples_count, time_spent)
            date_record = date
            wpm_sum = top_wpm = errors_sum = samples_count = characters_sum = time_spent = 0

        time_spent += i['time']
        wpm = i['speed'] / 5
        if top_wpm < wpm:
            top_wpm = wpm
        wpm_sum += wpm
        characters_sum += i['length']
        errors_sum += i['errors']
        samples_count += 1
    accuracy = (1 - errors_sum / characters_sum) * 100
    daily_fill_keys(result, date_record, wpm_sum, top_wpm, accuracy, samples_count, time_spent)
    return result


def hourly_fill_keys(result : dict, time : str, wpm : int, accuracy : int):
    result['time'].append(time)
    result['wpm'].append(wpm)
    result['accuracy'].append(accuracy)


def get_hourly_stat(selected_date : str):
    correct_day_data = []
    
    for i in ac.data:
        date = i['timeStamp'].split('T')[0]
        if date == selected_date:
            correct_day_data.append(i)

    keys = ['time', 'wpm', 'accuracy']
    result = dict((i, [],) for i in keys)
    wpm = errors = characters_sum = 0
    for i in correct_day_data:
        time = i['timeStamp'].split('T')[1]
        characters_sum = i['length']
        errors = i['errors']
        accuracy = (1 - errors / characters_sum) * 100
        wpm = i['speed'] / 5
        hourly_fill_keys(result, time, wpm, accuracy)
    return result


def get_dates():
    dates = []
    for i in ac.data:
        date = i['timeStamp'].split('T')[0]
        dates.append(date)
    dates_splitted = [date.split('-') for date in dates]
    dates_sorted = {}
    for date in dates_splitted:
        if date[0] not in dates_sorted:
            dates_sorted.update({date[0] : {}})
        if date[1] not in dates_sorted[date[0]]:
            dates_sorted[date[0]].update({date[1] : []})
        if date[2] not in dates_sorted[date[0]][date[1]]:
            dates_sorted[date[0]][date[1]].append(date[2])
    return dates_sorted
