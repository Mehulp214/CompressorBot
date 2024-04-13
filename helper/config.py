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
    APP_ID = 12
    API_HASH = "15jdkenskw7"
    BOT_TOKEN = "70:JALR-qiS15Q"
    OWNER = 564
    LOG = -1001
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)

#try:
    # APP_ID = config("APP_ID", cast=int)
    # API_HASH = config("API_HASH")
    # BOT_TOKEN = config("BOT_TOKEN")
    # OWNER = config("OWNER_ID", default=1322549723, cast=int)
    # LOG = config("LOG_CHANNEL", cast=int)
#except Exception as e:
    # LOGS.info("Environment vars Missing")
    # LOGS.info("something went wrong")
    # LOGS.info(str(e))
    #exit(1)
    
