class HttpMessage:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return {"message": self.value}