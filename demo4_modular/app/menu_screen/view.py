from coremon_main import EngineEvTypes, EventReceiver
import pygame


class MenuScreenView(EventReceiver):

    def __init__(self):
        super().__init__(self)
        self._bg_color= (255, 50, 60)  # red, green, blue format
        ft = pygame.font.Font(None,19)
        self.img=ft.render('press mouse button to change state',True,(0,0,0))
        self.img_pos=(200,180)
        
    #override
    def proc_event(self,ev,source=None):
        if ev.type==EngineEvTypes.PAINT:
            ev.screen.fill(self._bg_color)
            ev.screen.blit(self.img, self.img_pos)
