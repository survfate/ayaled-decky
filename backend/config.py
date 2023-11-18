import logging
import subprocess
from helpers import get_homebrew_path,get_home_path,get_user

# Log configuration
try:
    LOG_LOCATION = "/tmp/ayaled_decky_py.log"
    logging.basicConfig(
        level = logging.DEBUG,
        filename = LOG_LOCATION,
        format="[%(asctime)s | %(filename)s:%(lineno)s:%(funcName)s] %(levelname)s: %(message)s",
        filemode = 'w',
        force = True)
except Exception as e:
    logging.error(f"Unexpected log configuration|{e}")

# Gather device information
try:
    PRODUCT_NAME = open("/sys/devices/virtual/dmi/id/product_name", "r").read().strip()
except Exception as e:
    logging.error(f"Unexpected error when gather device information|{e}")

# Lighting effect offset configuration
try:
    if PRODUCT_NAME in (
        "AIR",
        "AIR Pro",
        "AIR 1S"
        "AYANEO 2",
        "AYANEO 2S",
        "AYANEO GEEK",
        "AYANEO GEEK 1S",
        ):
        FAN_MANUAL_OFFSET=0x4a
        FAN_RPMWRITE_OFFSET=0x4b
        FAN_RPMREAD_OFFSET=0x76
        FAN_RPMWRITE_MAX=100
        FAN_IS_ADAPTED=True
except Exception as e:
    logging.error(f"Unexpected lighting effect offset configuration|{e}")
