
class AlgorithmDataPipeline:
    @staticmethod
    def compare(arg1: str, arg2: str):
        for x,y in zip(arg1.lower(), arg2.lower()):
            if ord(x) > ord(y):
                return True
            elif ord(x) < ord(y):
                return False
        if len(arg1) > len(arg2):
                return True
        return False #equal or more

    

#print(AlgorithmDataPipeline.compare("a", "b"))