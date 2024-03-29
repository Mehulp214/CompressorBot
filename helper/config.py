#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("APP_ID","23322236",cast=int)
    API_HASH = config("API_HASH","e7cc5d762451079c046202fc1d926677")
    BOT_TOKEN = config("BOT_TOKEN","7160872230:AAHmmk7eDW2FwtVkRLwl3dwzJALR-qiS15Q")
    OWNER = config("OWNER_ID","5642570692", default=1322549723, cast=int)
    LOG = config("LOG_CHANNEL","-1001817380537", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
