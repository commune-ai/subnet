import commune as c
class Vali(c.Vali):
    def score(self, module , a=1, b=1):
        result = module.generate(a, b)
        difference = result - (a+b)
        return 1 - difference