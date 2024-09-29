from manim import *

# 同名类会被覆盖
class myStar(Scene):
    def construct(self):
        star = Star(5)
        
        self.play(Create(star))
        self.wait(2)