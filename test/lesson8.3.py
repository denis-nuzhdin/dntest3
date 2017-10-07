
class TV(object):


    def __init__(self):
        self.volume = 5
        self.channel = 1

    def __str__(self):
        rep = "объект класса"
        rep += "громкость:" + self.volume +"; "+ "канал:" + self.channel +"; "
        return  rep


    @property
    def choice_channel(self):
        choice_ch = self.channel
        if 0 >= choice_ch >10:
            m = "нет канала"
        else:
            m = "ваш канал "+ str(self.channel)
        return m

    @property
    def choice_volume(self):
        choice_vl = self.volume
        if 0 < choice_vl <10:
            m = "ваша громкость " + str(self.volume)
        elif choice_vl == 0:
            m = "mute"
        else:
            m = "max"
        return m


    def talk(self):
        print("канал №: ", self.channel, " громкость ", self.volume, "\n")

    def change_channel(self, channel=1):
        channel = int(input("какой канал? "))
        #print(self.channel)
        self.channel = channel
        print(self.choice_channel)

    def volume_down(self):
        self.volume -=1
        if self.volume<0:
            self.volume=0
        else:
            self.volume
        print(self.choice_volume)

    def volume_up(self):
        self.volume +=1
        if self.volume>10:
            self.volume=10
        else:
            self.volume
        print(self.choice_volume)

def main():
    television = TV()

    choice = None

    while choice !="0":
        print \
            ("""
            ТВ
            0 - выход
            1 - выбрать канал
            2 - уменьшить громкость
            3 - прибавить громкость
            """)
        choice = input("ваш выбор: ")
        if choice =="0":
            print("goodbay")

        elif choice == "1":
            television.change_channel()

        elif choice == "2":
            television.volume_down()

        elif choice == "3":
            television.volume_up()

        else:
            print("no choice")

        #print(Critter.__pass_time.hunger)
        #print(Critter.hunger)

main()