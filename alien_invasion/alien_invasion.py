import sys
import pygame
import game_funciton as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    """游戏入口，主程序"""

    # 初始化,创建所有实例
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # screen表示整个游戏画面中的所有元素
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # 游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ship, ai_settings, screen, bullets)

        # 更新屏幕
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()