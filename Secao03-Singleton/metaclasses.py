class Nandi(type):
    def __call__(cls, *args, **kwargs):
        print(f"+++ Estes são os arqumentos: {args}")
        return type.__call__(cls, *args, **kwargs)

class Cleber(metaclass=Nandi):
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

obj = Cleber(36, 40)
print(obj)