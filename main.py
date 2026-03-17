
import pygame
from vector_img import f
import math
from complex_num import Z

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()




class MainApp:
    n = 100
    f = f[0]
    data_length = len(f)
    
    def __init__(self) -> None:
        self.coefs = self.get_coefs()
        print(self.coefs)

    def get_coef(self, n: int):
        dt = 1/self.data_length

        cn = Z(0, 0)
        for i in range(self.data_length):
            t = i * dt
            f_t = self.f[i]
            f_t = Z(f_t[0], f_t[1])
            cn += Z.polar(1, math.degrees(-2*math.pi*n*t))*f_t*dt
        return cn
    
    def get_coefs(self):
        c = {}
        for i in range(self.n):
            c[i] = self.get_coef(i)
            c[-i] = self.get_coef(-i)
        return c

    def draw(self, t):
        p = Z(0,0)
        for freq, c in self.coefs.items():
            new_p = p + c * Z.polar(1, math.degrees(2*math.pi*freq*t))
            pygame.draw.circle(screen, "white", p.point, 2)
            pygame.draw.line(screen, "white", p.point, new_p.point)
            p = new_p
        return p.point

    def run(self):
        i = 0
        dt = 1/self.data_length
        pts = []

        while True:
            screen.fill("black")
            clock.tick(120)

            pt = self.draw(i*dt)
            pts.append(pt)

            pygame.draw.aalines(screen, "grey", False, self.f)
            if len(pts) >= 2:
                pygame.draw.aalines(screen, "yellow", False, pts)
                
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            
            if i >= self.data_length:
                i = 0
                pts.clear()
            i += 1



app = MainApp()
app.run()
