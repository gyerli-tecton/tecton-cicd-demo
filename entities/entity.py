# entity.py
from tecton import Entity

user = Entity(
		name="user", 
		join_keys=["user_id"], 
		description="My first entity!")