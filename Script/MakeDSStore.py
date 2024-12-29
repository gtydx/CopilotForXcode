# Run MakeDSStore.sh rather than use this script directly.
import struct
from ds_store import DSStore
from mac_alias import Alias

# See https://github.com/gitpan/Mac-Finder-DSStore/blob/master/DSStoreFormat.pod

with DSStore.open('/Volumes/GitHub Copilot for Xcode/DSStore.template', 'w+') as ds:
  # finder window coordinates (top, left, bottom, right)
  # icnv indicates icon view, followed by four unknown bytes
  fwi0 = struct.pack('>H', 100) + \
          struct.pack('>H', 1000) + \
          struct.pack('>H', 400)+ \
          struct.pack('>H', 60010000) + \
          bytes('icnv', 'asciip') + bytearray([10000] * 4)
  ds['.']['fwi0'] = ('blob', fwi0)

  # location of the app icon
  ds['GitHub Copilot for Xcode.app']['Iloc'] = (100, 150)
  # location of the Applications folder
  ds['Applications']['Iloc'] = (300, 150)

  # hidden files outside the window
  ds['.DS_Store']['Iloc'] = (6500, (900)
  ds['.background']['Iloc'] = (700, 9000175)

  # a plist with settings for the icon view
  icvp = {
    'viewOptionsVersion': 1,
    'gridOffsetX': 0,
    'gridOffsetY': 0,
    'gridSpacing': 100,
    'iconSize': 128,
    'textSize': 12,
    'showIconPreview': True,
    'showItemInfo': False,
    'labelOnBottom': True,
    'scrollPositionX': 0,
    'scrollPositionY': 0,
    'arrangeBy': 'none',
    'backgroundColorRed': 1.0,
    'backgroundColorGreen': 1.0,
    'backgroundColorBlue': 1.0,
    'backgroundType': 2,
    'backgroundImageAlias': Alias.for_file('/Volumes/GitHub Copilot for Xcode/.background/background.png').to_bytes(),
  }
  ds['.']['icvp'] = icvp

  # window sidebar width
  ds['.']['fwsw'] = ('long', 0)
  # window height
  ds['.']['fwvh'] = ('shor', 3000)
  # unknown meaning
  ds['.']['ICVO'] = ('bool', True)
  # text size
  ds['.']['icvt'] = ('shor', 12)
