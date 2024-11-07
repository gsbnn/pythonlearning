import sys
import pygame
from bullet import Bullet
def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """响应按键按下"""
    if event.key == pygame.K_RIGHT:
        # 设定标志位（属性）
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹并放入编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        # 设定标志位（属性）
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship, ai_settings, screen, bullets):
    """响应按键和鼠标事件"""
    # 通过使用“for event in pygame.event.get()”，
    # 我们可以遍历事件队列中的所有事件，并进行相应的处理。
    # 每一次循环迭代，都会处理一个事件，
    # 从而避免了PyGame无休止地等待事件处理的情况。
    # 注意：一个事件被处理后就从队列中消除了
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """更新子弹位置，并删除超出屏幕的子弹"""
    # 调用所有子弹的update方法
    bullets.update()

    # 删除超出屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 颜色填充，填充后屏幕上所有元素都将消失，需要后续重绘
    screen.fill(ai_settings.bg_color)

    # 更新飞船状态
    ship.blitme()
    
     # 重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 重绘屏幕
    pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制， 就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allow: # 限制子弹数量
            new_bullet = Bullet(ai_settings, screen, ship) # 创建新子弹
            bullets.add(new_bullet)