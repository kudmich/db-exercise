import json
import db
from main import engine
from db import Block, Operations
from sqlalchemy.orm import Session

local_session = Session(bind = engine)

new_data2 = Block()
new_data3 = Operations(operation_type = "asdasd", operation_body = "asdsada")

local_session.add(new_data2)
local_session.add(new_data3)

local_session.commit()
