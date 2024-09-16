import commune as c
class Miner(c.Module):
    @c.endpoint()
    def generate(self, a=0, b=0):
        return a + b