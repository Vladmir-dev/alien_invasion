import pygame.font  # allows pygame to render text to the screen


class Button:
    def __init__(self, ai_game, msg):
        """Initialise button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # settng the dimentions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # the None attribute tells pygame to use the default font
        self.font = pygame.font.SysFont(None, 48)

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn the msg into rendered image and center it on the button"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw a blank button and then draw message
        # draws a rectangular portion of the button
        self.screen.fill(self.button_color, self.rect)
        # draws text image to the screen
        self.screen.blit(self.msg_image, self.msg_image_rect)
