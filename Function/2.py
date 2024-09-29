from manim import *
import numpy as np

# 贝塞尔曲线绘制函数
def bezier_curve(points, t_values=None):
    if t_values is None:
        t_values = np.linspace(0, 1, 100)
    
    bezier_curve = VMobject()
    points_on_curve = []

    for t in t_values:
        n = len(points) - 1
        point = np.zeros(3)
        for i, p in enumerate(points):
            binomial_coeff = np.math.comb(n, i)
            point += binomial_coeff * (t ** i) * ((1 - t) ** (n - i)) * p
        points_on_curve.append(point)

    bezier_curve.set_points_as_corners(points_on_curve)
    return bezier_curve

# 如果你想要测试这个函数，你可以创建一个 Manim 场景来展示这个曲线
class TestBezierCurve(Scene):
    def construct(self):
        # 定义贝塞尔曲线的控制点
        control_points = [np.array([-3, 0, 0]), np.array([0, 3, 0]), np.array([3, 0, 0])]
        # 绘制贝塞尔曲线
        curve = bezier_curve(control_points)
        self.add(curve)
        