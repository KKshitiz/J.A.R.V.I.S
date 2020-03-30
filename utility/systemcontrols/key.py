from keyboard import Keyboard


class Key:
    """
    Class Key

    Allows you control the Windows volume
    The first time a sound method is called, the system volume is fully reset.
    This triggers sound and mute tracking.
    """
    # Current volume, we will set this to 100 once initialized
    __current_volume = None

    @staticmethod
    def current_volume():
        """
        Current volume getter
        :return: int
        """
        if Key.__current_volume is None:
            return 0
        else:
            return Key.__current_volume

    @staticmethod
    def __set_current_volume(volume):
        """
        Current volumne setter
        prevents numbers higher than 100 and numbers lower than 0
        :return: void
        """
        if volume > 100:
            Key.__current_volume = 100
        elif volume < 0:
            Key.__current_volume = 0
        else:
            Key.__current_volume = volume


    # The sound is not muted by default, better tracking should be made
    __is_muted = False

    @staticmethod
    def is_muted():
        """
        Is muted getter
        :return: boolean
        """
        return Key.__is_muted


    @staticmethod
    def __track():
        """
        Start tracking the sound and mute settings
        :return: void
        """
        if Key.__current_volume == None:
            Key.__current_volume = 0
            for i in range(0, 50):
                Key.volume_up()
    @staticmethod
    def playpause():
        Keyboard.key(Keyboard.VK_MEDIA_PLAY_PAUSE)
    
    @staticmethod
    def nexttrack():
        Keyboard.key(Keyboard.VK_MEDIA_NEXT_TRACK)

    @staticmethod
    def previoustrack():
        Keyboard.key(Keyboard.VK_MEDIA_PREV_TRACK)

    @staticmethod
    def mute():
        """
        Mute or un-mute the system sounds
        Done by triggering a fake VK_VOLUME_MUTE key event
        :return: void
        """
        Key.__track()
        Key.__is_muted = (not Key.__is_muted)
        Keyboard.key(Keyboard.VK_VOLUME_MUTE)

    @staticmethod
    def volume_up():
        """
        Increase system volume
        Done by triggering a fake VK_VOLUME_UP key event
        :return: void
        """
        Key.__track()
        Key.__set_current_volume(Key.current_volume() + 2)
        Keyboard.key(Keyboard.VK_VOLUME_UP)

    @staticmethod
    def volume_down():
        """
        Decrease system volume
        Done by triggering a fake VK_VOLUME_DOWN key event
        :return: void
        """
        Key.__track()
        Key.__set_current_volume(Key.current_volume() - 2)
        Keyboard.key(Keyboard.VK_VOLUME_DOWN)


    @staticmethod
    def volume_set(amount):
        """
        Set the volume to a specific volume, limited to even numbers.
        This is due to the fact that a VK_VOLUME_UP/VK_VOLUME_DOWN event increases
        or decreases the volume by two every single time.
        :return: void
        """
        Key.__track()

        if Key.current_volume() > amount:
            for i in range(0, int((Key.current_volume() - amount) / 2)):
                Key.volume_down()
        else:
            for i in range(0, int((amount - Key.current_volume()) / 2)):
                Key.volume_up()

    @staticmethod
    def volume_min():
        """
        Set the volume to min (0)
        :return: void
        """
        Key.volume_set(0)

    @staticmethod
    def volume_max():
        """
        Set the volume to max (100)
        :return: void
        """
        Key.volume_set(100)

    """
    This part contains functions for browser controls
    """

    @staticmethod
    def browserback():
        Keyboard.key(Keyboard.VK_BROWSER_BACK)

    @staticmethod
    def browsernext():
        Keyboard.key(Keyboard.VK_BROWSER_FORWARD)

    @staticmethod
    def browserhome():
        Keyboard.key(Keyboard.VK_BROWSER_HOME)

    @staticmethod
    def browserrefresh():
        Keyboard.key(Keyboard.VK_BROWSER_REFRESH)

    @staticmethod
    def browserfav():
        Keyboard.key(Keyboard.VK_BROWSER_FAVORITES)