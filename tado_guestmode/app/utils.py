import os
import sys

CONFIGPATH = os.environ['CONFIGPATH']


def checkconfig():
    """Check configuration exists.

    Guide users to create their own configuration.
    """
    configexists = os.path.exists(os.path.abspath(CONFIGPATH))
    configtemplateexists = os.path.exists(CONFIGPATH + '.template')
    if not configexists:
        print('Configuration file not found.')
        if not configtemplateexists:
            os.system('cp /app/config.yml.template ' + CONFIGPATH + '.template')
        sys.exit("Create a config.yml using config.yml.template as an example.")
    else:
        print('Configuration Found. Loading file.')
