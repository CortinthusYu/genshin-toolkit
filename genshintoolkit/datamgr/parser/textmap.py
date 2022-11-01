from pathlib import Path
import json
from typing import Text

class TextmapMgr:
    def __init__(self) -> None:
        pass # load texpmaps

    def get_text(self,text_id:int,language:str) -> str:
        '''
        language: support cn jp en
        '''
        return ''

    def __del__(self):
        '''release all files
        '''

mgr=TextmapMgr()

