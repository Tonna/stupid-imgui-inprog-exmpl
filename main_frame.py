import pygame
import imgui
from imgui.integrations.pygame import PygameRenderer

s1 = True

def init():
    global show_about
    show_about = True
    pygame.init()
    size = 500, 500

    screen = pygame.display.set_mode(size, pygame.DOUBLEBUF
                                     | pygame.OPENGL
                                     )
    pygame.display.set_caption("Mom get the camera! I'm metaprogramming!!!")

    imgui.create_context()
    impl = PygameRenderer()

    io = imgui.get_io()
    io.display_size = size
    return screen, impl
