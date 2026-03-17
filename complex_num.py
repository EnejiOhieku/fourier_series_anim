import math

class Z:
    # complex number class

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def point(self):
        return (self.real, self.imag)
    
    @property
    def magnitude(self):
        return (self.real**2 + self.imag**2)**0.5

    @property
    def direction(self):
        direction = math.degrees(math.atan2(self.imag, self.real))
        return (direction + 360) % 360
    
    @property
    def polar_form(self):
        return f"{round(self.magnitude, 4)}cis{round(self.direction, 2)}"

    @property
    def rectangular_form(self):
        real, imag = self.real, self.imag
        return f"{round(real, 4)} {'-' if imag < 0 else '+'} j{round(abs(imag), 4)}"
    
    @staticmethod
    def polar(magnitude, direction):
        real = magnitude*math.cos(math.radians(direction))
        imag = magnitude*math.sin(math.radians(direction))
        return Z(real, imag)
    
    def __str__(self):
        return self.rectangular_form
    
    def __repr__(self):
        return self.polar_form
    
    def __add__(self, z):
        real = self.real + z.real
        imag = self.imag + z.imag
        return Z(real, imag)
    
    def __sub__(self, z):
        real = self.real - z.real
        imag = self.imag - z.imag
        return Z(real, imag)
    
    def __neg__(self):
        return Z(-self.real, -self.imag)
    
    def __mul__(self, z):
        if type(z) in [int, float]:
            return Z.polar(self.magnitude*z, self.direction)
        
        magnitude = self.magnitude * z.magnitude
        direction = self.direction + z.direction
        return Z.polar(magnitude, direction)
    
    def __rmul__(self, z):
        return self.__mul__(z)

    def __truediv__(self, z):
        magnitude = self.magnitude / z.magnitude
        direction = self.direction - z.direction
        return Z.polar(magnitude, direction)
    
    def __pow__(self, n):
        return self.pow(n)
    
    def pow(self, n):
        assert type(n) == int, "n must be an int"
        magnitude = self.magnitude ** n
        direction = self.direction * n
        return Z.polar(magnitude, direction)
    
    def root(self, n):
        assert type(n) == int, "n must be an int"

        roots = []
        magnitude = self.magnitude**(1/n)
        for i in range(n):
            direction = self.direction / n + (360 * i) / n
            roots.append(Z.polar(magnitude, direction))
        return roots

# print(Z(2, 3).root(5))