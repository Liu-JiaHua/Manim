from manim import *

class ThreeSVG(VGroup):
    """一键三连"""
    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        svg1 = SVGMobject("..\\res\\good.svg").set_opacity(1).set_color(RED)
        svg2 = SVGMobject("..\\res\\coin.svg").set_opacity(1).set_color(ORANGE)
        svg3 = SVGMobject("..\\res\\favo.svg").set_opacity(1).set_color(PINK)
        VGroup(svg1,svg2,svg3).arrange_submobjects(buff=1.3)
        self.add(svg1,svg2,svg3)

class ThreeSVGScene(Scene):
    def construct(self):
        three_svg = ThreeSVG()
        self.play(FadeIn(three_svg), run_time=3)  # 使用 FadeIn 动画
        # self.add(three_svg)
        self.wait(4)  # 等待3秒钟，以便查看渲染效果)
        
    
    