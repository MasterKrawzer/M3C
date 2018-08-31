import cx_Freeze

APP = ['main_gui.py']
APP_NAME = 'M3C'
DATA_FILES = ['text.py', 'text_gui.py', 'config.cfg']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Minecraft Code Compiler",
        'CFBundleIdentifier': "com.thedeveloper.osx.m3c",
        'CFBundleVersion': "0.0.1",
        'CFBundleShortVersionString': "0.0.1",
        'NSHumanReadableCopyright': "Copyright 2018, Alexey Tkackenko, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
