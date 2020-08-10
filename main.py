import keybr_stat as ks
import gui
import actions as ac
    

def start():
    path = gui.get_file_path()
    ac.load_data(path)

    while True:
        print('Select an action(enter a number):')
        print('1) Show graph of daily progress')
        print('2) Save graph to fullHD image')
        print('3) Show graph of hourly progress on specific date')
        print('Enter Q or Ctrl+C to exit')
        inp = input()
        if inp == '1':
            ac.show_daily_graph()
        elif inp == '2':
            ac.save_daily_graph()
        elif inp == '3':
            ac.show_graph_on_day()
        elif inp == 'q':
            break


if __name__ == "__main__":
    start()
