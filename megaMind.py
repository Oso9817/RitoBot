from asyncio.windows_events import NULL
from keys import m_id, m_pw

import uuid
from testFunc import Mega

def start():
    unique = str(uuid.uuid4())

    mega = Mega()

    m = mega.login(m_id, m_pw)

#todo: use this snippet to check if folder exists, create folder based on response.
    query = 'yeti'
    

    folder = m.find(query, exclude_deleted=True)
    #checks nil value for folder value and t value of 1 means its a folder, 0 means files
    if folder == None or folder[1]['t'] != 1:   
        try:
            print("Folder not found, will try to create one")
            m.create_folder(query)

        except Exception as e:
            print(e)
    #todo: upload files in a loopable way to previously created dir
start()

