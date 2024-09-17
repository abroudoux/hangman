class Debug:
    def __init__(self, obj):
        self.obj = obj

    def print(self, prop_name, prop_value):
        print("=================================DEBUG=================================")
        print(f"{prop_name}: {prop_value}")
        print("=================================DEBUG=================================")
        return