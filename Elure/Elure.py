from manim import *

# 1
class Elure(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self=self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=False
        )

    def construct(self):
        # 定义一个矩阵A 
        murix = [[1,2],[2,1]]
        murix_tex= MathTex("A = \\begin{bmatrix} 1 & 2 \\\ 2 & 1 \\end{bmatrix}").to_edge(UL).add_background_rectangle()
        
        self.add(murix_tex)
        
        # 一个向量
        a = Dot([1,2,0])
        b = Dot([2,1,0])
        arrow1 = Arrow(ORIGIN, a, buff=0, color=RED)
        arrow2 = Arrow(ORIGIN, b, buff=0, color=GREEN)
        
        # 显示向量
        self.play(Write(arrow1), Write(arrow2))
        
        self.wait(4)
        
        # 应用线性变换
        self.apply_matrix(murix)

# 2
class DtFourierScene(Scene):
    def construct(self):
        axes = Axes()# 坐标轴
        vec1 = Vector(RIGHT, color=YELLOW)
        cir1 = Circle(radius=1, color=BLUE)
        gup1 = VGroup(vec1, cir1)
        
        vec2 = Vector(RIGHT, color=YELLOW)
        cir2 = Circle(radius=1, color=BLUE)
        gup2 = VGroup(vec2, cir2)
        gup2.save_state()
        
        #更新函数中dt的用法
        def anim1(obj, dt):
            obj.rotate(dt, about_point=ORIGIN)
        
        def anim2(obj):
            obj.restore()
            obj.rotate(-vec1.get_angle())
            obj.shift(vec1.get_vector())
        
        gup1.add_updater(anim1)
        gup2.add_updater(anim2)
        
        path = TracedPath(vec2.get_end, stroke_width=6, stroke_color=ORANGE)
        path.add_updater(lambda a, dt:a.shift(DOWN*dt))
        self.add(axes, gup1, gup2, path)
        self.wait(10)
