# Installer for WeatherLink Live (WLL) driver for WeeWX
# Copyright 2020 Jon Otaegi
# Distributed under the terms of the GNU Public License (GPLv3)

from setup import ExtensionInstaller

def loader():
    return WLLInstaller()

class WLLInstaller(ExtensionInstaller):
    def __init__(self):
        super(WLLInstaller, self).__init__(
            version="0.1",
            name='wll',
            description='Periodically poll weather data from a WeatherLink Live device',
            author="Jon Otaegi",
            config={
                'WLL': {
                    'host': '1.2.3.4',
                    'poll_interval': 10,
                    'driver': 'user.wwl'
                }
            },
            files=[('bin/user', ['bin/user/wll.py'])])
