import json
from main import engine
from db import Block, Operations
from sqlalchemy.orm import Session


with open('data.json', 'r') as read_file:
    data = json.load(read_file)

for i in range(len(data['result']["ops"])-1):
    data_to_operation_body = Operations(operation_body=str(data["result"]["ops"][i]["op"]["value"]))
    data_to_block_table = Block()
    local_session = Session(bind=engine)
    local_session.add(data_to_operation_body)
    local_session.add(data_to_block_table)
    local_session.commit()


local_session.close()
