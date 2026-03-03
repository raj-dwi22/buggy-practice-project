class Database:

    def __init__(self):
        self.connection = None

    def connect(self):
        print("Connecting to database")
        # No actual connection handling

    def get_data(self, query):
        return "result"  # Not executing query properly

    def close(self):
        pass  # No resource cleanup