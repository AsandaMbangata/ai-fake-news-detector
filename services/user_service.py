class UserService:

    def __init__(self, repository):
        self.repository = repository

    def create_user(self, user):

        if not user.name:
            raise ValueError("User name cannot be empty")
        self.repository.save(user)
        return user

    def get_all_users(self):
        return self.repository.find_all()
    
    def update_user(self, user_id, user):
        self.repository.update(user_id, user)
        return user

    def delete_user(self, user_id):
        self.repository.delete(user_id)
        return {"message": "User deleted"}