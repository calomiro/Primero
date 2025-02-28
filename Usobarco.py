from manim import *
from LibreriaBarco import *

class gonzalo(Scene):
    def construct(self):
        flotaccion = 1.5
        for escora in range(0, 45, 5):
            barco = Objeto_barco() 
            linea, sup,inf = barco.corta(flotaccion,escora)
            #texto = Text(f"Escora = {ang} grados").next_to(inf, DOWN)
            texto = Text(f"Escora = {escora} grados").next_to(sup, UP)
            
            self.play(FadeIn(linea), FadeIn(sup), FadeIn(inf), FadeIn(texto), run_time=2)
            self.remove(linea, sup,inf, texto)
        