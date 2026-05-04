
class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role

    def submit_text(self, text):
        return f"Text submitted: {text}"

    def view_results(self):
        return "Viewing results"