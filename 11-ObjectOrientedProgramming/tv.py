class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print("TV is on", end="")
            if self.channel_no < len(self.channels):
                print(
                    f", channel {self.channel_no + 1}. {self.channels[self.channel_no]}",
                    end="",
                )
            print(f", volume: {self.volume}", end='')
        else:
            print("TV is off", end="")
        print()

    def set_channel(self, num):
        self.channel_no = num

    def set_channels(self, clist):
        self.channels = clist

    def show_channels(self):
        i = 1
        for channel in self.channels:
            print(f"{i}. {channel}")
            i += 1

    def increase_volume(self):
        if self.volume < 10 and self.is_on:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0 and self.is_on:
            self.volume -= 1


def main():
    tv = TV()
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.show_channels()
    tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
    tv.show_channels()
    tv.show_status()
    tv.decrease_volume()
    tv.show_status()
    for i in range(11):
        tv.increase_volume()
    tv.show_status()
    tv.turn_off()


if __name__ == "__main__":
    main()
