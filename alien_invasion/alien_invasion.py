import sys
import pygame
import game_funciton as gf
from settings import Settings
from ship import Ship

def run_game():
    """游戏入口，主程序"""

    # 初始化
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # screen表示整个游戏画面中的所有元素
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)

    # 游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ship)

        # 更新屏幕
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()