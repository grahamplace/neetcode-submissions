class Logger:

    THRESHOLD = 10 

    def __init__(self):
        self.messages: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        
        if timestamp < self.messages[message] + self.THRESHOLD:
            return False
        
        self.messages[message] = timestamp
        return True
        




        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
