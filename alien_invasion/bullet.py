import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # (0, 0)处创建一个Rect,并指定宽和高
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
                                ai_settings.bullet_height)
        
        # 将Rect移动到飞船上部中心位置，即子弹从飞船头部射出
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 获取子弹纵坐标
        self.y = float(self.rect.y)

        # 设置子弹颜色和速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""

        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)