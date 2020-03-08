#!/usr/bin/env python3
import sys

import pygame
import OpenGL.GL as gl

from imgui.integrations.pygame import PygameRenderer
import imgui
import main_frame
from main_frame import init
import time
import math

def menubar():
    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):

            clicked_quit, selected_quit = imgui.menu_item(
                "Quit", 'Cmd+Q', False, True
            )

            if clicked_quit:
                exit(1)
            imgui.end_menu()
        if imgui.begin_menu("About", True):

            clicked_about, _ = imgui.menu_item(
                "About me..", 'F1', True, True
            )

            if clicked_about:
                imgui.open_popup("about-p")
            imgui.end_menu()
    imgui.end_main_menu_bar()


class simple_window1:
    def __call__(self):
        _, show = imgui.begin("LOL", True)
        if not show:
            main_frame.s1 = False
        imgui.text("BarBar")
        imgui.text_colored("Eggs", 0.7, 0.4, 0.2)
        imgui.end()

class simple_window2:
    def __call__(self):
        _, show = imgui.begin("ROFL", True)
        if not show:
            main_frame.s1 = False
        imgui.text("BarB.B")
        imgui.text(str(math.fabs(math.sin(time.time()))))
        imgui.text_colored("Egg", 1., 0.1, 0.2)
        imgui.end()

class MainFrame:

    @classmethod
    def draw(cls, impl):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            impl.process_event(event)
        imgui.new_frame()
        if main_frame.s1:
            simple_window1()()
            simple_window2()()
            menubar()


def draw(s, impl):
    MainFrame.draw(impl)

    # note: cannot use screen.fill((1, 1, 1)) because pygame's screen
    #       does not support fill() on OpenGL sufraces
    x = math.fabs(math.sin(time.time()))
    y = math.fabs(math.cos(time.time()))
    gl.glClearColor(x, y, x, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    imgui.render()
    impl.render(imgui.get_draw_data())
    pygame.display.flip()


def main():
    screen, impl = init()
    clock = pygame.time.Clock()
    while True:
        draw(screen, impl)
        clock.tick(30)


if __name__ == "__main__":
    main()
