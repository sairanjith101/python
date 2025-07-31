class watch:

    def intro(self):
        print('Watchs provide the time of a day')

    def hand(self):
        print('A watch have 3 hands')

class hour_hand(watch):
    
    def hand(self):
        print('Hour hand is showing hours')

class minute_hand(watch):

    def hand(self):
        print('Minute hand is showing minutes')

class sec_hand(watch):

    def hand(self):
        print('Sec hand is showing sec')

obj_watch = watch()
obj_hour = hour_hand()
obj_min = minute_hand()
obj_sec = sec_hand()

obj_watch.intro()
obj_watch.hand()

obj_hour.intro()
obj_hour.hand()

obj_min.intro()
obj_min.hand()

obj_sec.intro()
obj_sec.hand()