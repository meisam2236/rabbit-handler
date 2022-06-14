class Routing:
    def create(self, ID, name, age):
        return {
            "routing": {
                "action": "create",
                "body": {
                    "ID": ID,
                    "name": name,
                    "age": age
                }
            }
        }

    def print(self):
        return {
            "routing": {
                "action": "print",
                "body": {
                }
            }
        }

