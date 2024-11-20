import sys
import pygame
import game_funciton as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from pygame.sprite import Group

def run_game():
    """游戏入口，主程序"""

    # 初始化,创建所有实例
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # screen表示整个游戏画面中的所有元素
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ship, ai_settings, screen, bullets)
        
        # 更新元素
        if stats.game_active:   
            # 确定哪些功能在激活状态下运行
            ship.update() # 更新坐标
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens) # 更新坐标
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets) 
        
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens) #重绘屏幕


run_game()