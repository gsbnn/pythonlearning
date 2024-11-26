import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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

def check_play_button(ai_settings, screen, ship, stats, sb, play_button, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        """ 检查鼠标单击位置是否在Play按钮的rect内,并重置游戏状态"""
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        pygame.mouse.set_visible(False) # 设置光标不可见

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 重置记分牌
        sb.prep_score() # 将得分置零
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 创建一群新的外星人， 并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_events(ship, ai_settings, screen, aliens, bullets, stats, sb, play_button):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() # 获取单击时鼠标的x和y坐标
            check_play_button(ai_settings, screen, ship, stats, sb, play_button,
                               aliens, bullets, mouse_x, mouse_y)
            




def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移， 并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """响应被外星人撞到飞船"""
    if stats.ships_left > 0:
        # 将飞船数量减一
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人， 并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        ai_settings.initialize_dynamic_settings() # 重置游戏设置
        pygame.mouse.set_visible(True) # 设置光标可见

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘， 并更新整群外星人的位置"""
    # 判读外星人是否与飞船相撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
    
    # 判读外星人是否到达屏幕底部
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets) 
    
    # 判断外星人是否接触屏幕边缘
    check_fleet_edges(ai_settings, aliens)
    
    # 更新外星人位置
    aliens.update() # Group自带的方法





def delete_bullets_overscreen(bullets):
    """删除超出屏幕的子弹"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_score(ai_settings, stats, sb, collisions, aliens):
    """计算得分"""
    for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
    sb.prep_score()

def check_high_score(stats, sb):
    """检查是否诞生新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_bullets_aliens_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检测子弹与外星人碰撞后，删除子弹和外星人"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # 如果子弹击中外星人，删除相应的子弹和外星人
    
    if collisions: # 计分
        update_score(ai_settings, stats, sb, collisions, aliens)
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed() #提高游戏难度
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens):
    """更新子弹位置，并删除超出屏幕的子弹"""
    # 判断并删除超出屏幕的子弹
    delete_bullets_overscreen(bullets)

    # 判断并删除与外星人相撞的子弹
    check_bullets_aliens_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    # 更新子弹位置
    bullets.update() # Group自带的方法





def update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 颜色填充，填充后屏幕上所有元素都将消失，需要后续重绘
    screen.fill(ai_settings.bg_color)

    # 重绘飞船
    ship.blitme()

    # 重绘外星人
    aliens.draw(screen) # Group自带的方法
    
    # 重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 绘制得分信息
    sb.show_score()

    # 重绘屏幕
    pygame.display.flip()





def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制， 就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allow: # 限制子弹数量
            new_bullet = Bullet(ai_settings, screen, ship) # 创建新子弹
            bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """在当前行创建一个外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_number * alien_width * 2
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + row_number * alien.rect.height * 2
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, 
                         row_number)
