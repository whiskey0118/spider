from db import session
from db import User,Color

def test():
    new = User(id=1, name="test")
    session.add(new)
    session.commit()

test()