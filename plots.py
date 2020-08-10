import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import keybr_stat as ks

def show_daily_graph(data : dict):
    df = pd.DataFrame(data)

    fig, wpm = plt.subplots()
    fig.subplots_adjust(right=0.75)

    time = wpm.twinx()
    accuracy = wpm.twinx()
    accuracy.spines['right'].set_position(('axes', 1.2))

    wpm.set_ylabel('WPM')
    
    wpm.set_xlabel('Date')
    time.set_ylabel('Time practising (minutes)')
    time.yaxis.label.set_color('#009c3e')
    accuracy.set_ylabel('Avarage errors')
    accuracy.yaxis.label.set_color('red')

    wpm.plot('date', 'avarage_wpm', data=df, color='orange', label='avarage wpm')
    wpm.plot('date', 'top_wpm', data=df, color='blue', label='top wpm')
    time.bar('date', 'time_spent', data=df, color='#009c3e', alpha=0.2)
    accuracy.plot('date', 'accuracy', data=df, color='red')

    wpm.legend()

    plt.show()


def save_daily_graph(data : dict, path : str):
    df = pd.DataFrame(data)

    fig, wpm = plt.subplots()
    fig.subplots_adjust(right=0.75)

    time = wpm.twinx()
    accuracy = wpm.twinx()
    accuracy.spines['right'].set_position(('axes', 1.2))

    wpm.set_ylabel('WPM', )
    wpm.set_xlabel('Date')
    time.set_ylabel('Time practising (minutes)')
    time.yaxis.label.set_color('#009c3e')
    accuracy.set_ylabel('accuracy(%)')
    accuracy.yaxis.label.set_color('red')

    wpm.plot('date', 'avarage_wpm', data=df, color='orange', label='avarage wpm', linewidth=3)
    wpm.plot('date', 'top_wpm', data=df, color='blue', label='top wpm', linewidth=3)
    time.bar('date', 'time_spent', data=df, color='#009c3e', alpha=0.2, linewidth=3)
    accuracy.plot('date', 'accuracy', data=df, color='red', linewidth=3)

    wpm.legend()

    fig.set_size_inches(32, 18)
    matplotlib.rcParams.update({'font.size': 32})

    plt.savefig(path)


def show_hourly_progress_graph(data : dict):
    df = pd.DataFrame(data)

    fig, wpm = plt.subplots()

    accuracy = wpm.twinx()

    wpm.set_ylabel('WPM')
    
    wpm.set_xlabel('Time')
    accuracy.set_ylabel('Accuracy')
    accuracy.yaxis.label.set_color('red')

    wpm.plot('time', 'wpm', data=df, color='blue', label='top wpm')
    accuracy.plot('time', 'accuracy', data=df, color='red')

    wpm.legend()
    
    plt.xticks(rotation='vertical')
    plt.show()
