from nis import match
from genshintoolkit.gtcommon.atfdata import *
from genshintoolkit.gtcommon.gtenum import *
from pathlib import Path

import json
import yaml
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["genshindata"]



def parse_atf_mainstat_value():
    col=mydb['ReliquaryLevelExcelConfigData']
    
    
