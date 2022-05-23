
from operator import methodcaller


class AlgorithmDataPipeline:
    @staticmethod
    def compare(arg1: str, arg2: str):
        for x, y in zip(arg1.lower().strip(), arg2.lower().strip()):
            if ord(x) > ord(y):
                return True
            elif ord(x) < ord(y):
                return False
        if len(arg1) > len(arg2):
            return True
        return False  # equal or more

    @staticmethod
    def updateRecord(arg1: object):
        print("\n" + "=" * 15 + "EDIT PACKAGE" +"=" * 15 )
        while 1:
            raw_package = input(
                "Change package name (input nothing to skip): ").strip()
            if raw_package != "":
                if not raw_package.replace(" ", "").isalpha():
                    print("Must contain only letters")
                    continue
                arg1.package_name = raw_package
            break
        while 1:
            raw_customer = input(
                "Change customer name (input nothing to skip): ").strip()
            if raw_customer != "":
                if not raw_package.replace(" ", "").isalpha():
                    print("Must contain only letters")
                    continue
                arg1.customer_name = raw_customer
            break
        while 1:
            try:
                raw_pax = input("Change number of pax (input nothing to skip): ").strip()
                if raw_pax != "":
                    pax = int(raw_pax)
                    arg1.number_of_pax = pax
                break
            except:
                print("Not valid pax")
               
        while 1:
            try: 
                raw_package_cost = input("Change package cost per pax(input nothing to skip): ").strip()
                if raw_package_cost !="":
                    package_cost = float(raw_package_cost)
                    arg1.package_cost_per_pax = package_cost
                break
            except:
                print("Not valid package cost")
        print("=" * 36)
        return arg1
        


#print(AlgorithmDataPipeline.compare("a", "b"))
