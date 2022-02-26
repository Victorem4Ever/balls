import pygame
import win32api
import win32con
import win32gui
from ball import Ball
from pynput import mouse
import random


class Game:

    def __init__(self):

        self.running = False

     
        self.info = pygame.display.Info()

        self.w = self.info.current_w
        self.h = self.info.current_h

        self.screen = pygame.display.set_mode((self.w, self.h), pygame.NOFRAME)


        self.color = (255, 0, 128)

        self.hwnd = pygame.display.get_wm_info()["window"]

        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*self.color), 0, win32con.LWA_COLORKEY)

        self.clock = pygame.time.Clock()

        listener = mouse.Listener(
            on_click=self.on_click,
            on_scroll=self.on_click
        )
        listener.start()


    def update(self):

        for ball in self.balls:
            ball.draw()
        

    def generate_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.right:
            self.balls = []
            return

        self.balls.append(Ball(self.screen, (x,y), self.w, self.h, self.generate_color(), random.randint(5, 25), random.randint(1, 10)))

    def run(self):

        self.balls = []

        self.running = True
        while self.running:

            win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

            self.screen.fill(self.color)
            self.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    return

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    
    pygame.init()
    game = Game()
    game.run()