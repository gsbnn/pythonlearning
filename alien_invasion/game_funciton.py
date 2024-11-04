import sys
import pygame

def check_events(ship):
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
                if event.key == pygame.K_RIGHT:
                    # 设定标志位（属性）
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                     ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # 设定标志位（属性）
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                     ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 设置颜色
    screen.fill(ai_settings.bg_color)

    # 更新飞船状态
    ship.blitme()
    
    # 重绘屏幕
    pygame.display.flip()