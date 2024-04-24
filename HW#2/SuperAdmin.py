from user.user import User

class SuperAdmin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
    
    def somemethod(self, someParams):
        return someParams
    