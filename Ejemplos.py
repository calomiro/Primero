from manim import *
# https://docs.manim.community/en/stable/examples.html
# source env_manim/bin/activate
# source /home/gonzalo/env_manim/bin/activate
#  manim -pql primerman.py 
# deactivate
class Demoshapes(Scene):
    def construct(self):
        c = Circle(1).move_to([-4,-2,0])
        c.set_fill(YELLOW,opacity=0.2)
        s = Square().next_to(c) 
        s.set_fill(BLUE,opacity=0.5)   
        t=Triangle().next_to(s)
        t.set_fill(GREEN,opacity=0.5)   
        r = Rectangle().next_to(t)
        r.set_fill(PURE_BLUE, opacity=0.5)

        
        self.add(c,s,t,r)
        self.wait(2)
        self.remove(t,r)
        self.wait(2)
        self.remove(c)
        self.wait(3)

class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=GREEN, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        Gonzalito_text=Text("Gonzalito Texto", font_size=23).next_to(i, DOWN)
        self.play(FadeIn(intersection_text,Gonzalito_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeOut(Gonzalito_text))
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()

class VMobjectDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
            np.array([-2, -1, 0]),  # start of first curve
            np.array([-3, 1, 0]),
            np.array([0, 3, 0]),
            np.array([1, 3, 0]),  # end of first curve
            np.array([1, 3, 0]),  # start of second curve
            np.array([0, 1, 0]),
            np.array([4, 3, 0]),
            np.array([4, -2, 0]),  # end of second curve
        ]
        handles = [
            Dot(point, color=RED) for point in
            [[-3, 1, 0], [0, 3, 0], [0, 1, 0], [4, 3, 0]]
        ]
        handle_lines = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color=RED,
                stroke_width=2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]
        self.add(plane, *handles, *handle_lines, my_vmobject)
from manim import *

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class SineCosine_Curve(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()

        self.wait()
    def show_axis(self):
        x_start = np.array([-6,2,0])
        x_end = np.array([3,2,0])

        y_start = np.array([-4,-3,0])
        y_end = np.array([-4,3.5,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_xy_labels()

        self.orgin_point = np.array([-4,2,0])
        self.curve_start = np.array([-3,2,0])

    def add_xy_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        y_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):  # -2 -1 0 1
            x_labels[i].scale(0.6)
            x_labels[i].next_to(np.array([-2+i,2,0]), DOWN )
            self.add(x_labels[i])

        for i in range(len(y_labels)):  # 1 0 -1 -2
            y_labels[i].scale(0.6)
            y_labels[i].rotate(-PI/2)
            y_labels[i].next_to(np.array([-4, 1-i,0]), LEFT )
            self.add(y_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.orgin_point)

        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        orgin_point = self.orgin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(orgin_point, dot.get_center(), color=BLUE)

        ### sine
        def get_line_to_sine():
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.sine_curve = VGroup()
        self.sine_curve.add(Line(self.curve_start,self.curve_start))
        def get_sine_curve():
            last_line = self.sine_curve[-1]
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.sine_curve.add(new_line)

            return self.sine_curve

        ### cosine
        def get_line_to_cosine():
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )

        self.cosine_curve = VGroup()
        self.cosine_curve.add(Line(self.curve_start, self.curve_start))

        def get_cosine_curve():
            last_line = self.cosine_curve[-1]
            x = dot.get_center()[0]
            y = self.curve_start[1] - self.t_offset * 2
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.cosine_curve.add(new_line)

            return self.cosine_curve


        dot.add_updater(go_around_circle) #move dot around the circle

        origin_to_circle_line = always_redraw(get_line_to_circle) # from circle origin to dot

        dot_to_sine_line = always_redraw(get_line_to_sine) # from dot to sine curve
        sine_curve_line = always_redraw(get_sine_curve) # sine curve

        dot_to_cosine_line = always_redraw(get_line_to_cosine)  # from dot to cosine curve
        cosine_curve_line = always_redraw(get_cosine_curve)  # cosine curve

        self.add(dot, orbit)
        self.add(origin_to_circle_line,
                 dot_to_sine_line, sine_curve_line,
                 dot_to_cosine_line, cosine_curve_line,
         )
        self.wait(8.5)

        dot.remove_updater(go_around_circle)
