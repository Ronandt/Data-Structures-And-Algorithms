
class AlgorithmDataPipeline:
    @staticmethod
    def compare(arg1: str, arg2: str):
        count = 0
        for x,y in zip(arg1.lower(), arg2.lower()):
            print(count)
            if ord(x) > ord(y):
                return True
            elif ord(x) < ord(y):
                return False
        if len(arg1) > len(arg2):
                return True
        elif len(arg1) < len(arg2):
                return False
        return "Equal" 

    

