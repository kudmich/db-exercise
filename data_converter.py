import json
import db
from main import engine
from db import Block, Operations
from sqlalchemy.orm import Session



# json_obj = open('data.json')
# json_dict = json.load(json_obj)

with open('data.json', 'r') as read_file:
    data = json.load(read_file)

for i in range(10):
    data_to_operation_body = Operations(operation_body=str(data["result"]["ops"][i]["op"]["value"]))
    local_session = Session(bind=engine)

    local_session.add(data_to_operation_body)
    local_session.commit()



# new_data2 = Block()
# new_data3 = Operations(operation_body="asdsada")

# local_session.add(new_data2)
# local_session.add(new_data3)

# local_session.commit()
