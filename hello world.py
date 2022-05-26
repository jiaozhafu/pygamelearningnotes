import sys

import pygame   # 引入库


def main():
    pygame.init()   # 初始化相关模块

    screen = pygame.display.set_mode((800, 400))    # 游戏窗口核心参数
    pygame.display.set_caption("Hello World")       # 窗口标题

    logo = pygame.image.load("pygame.png")          # 加载图片
    logo_rect = logo.get_rect()                     # 调用surface对象的get_rect()函数
    logo_rect.center = (400, 200)                   # 把图像移动到中间

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                          # 实现游戏循环

        screen.fill((255, 255, 255))                # 窗口填充为白色
        screen.blit(logo, logo_rect)                # 把logo surface绘制到screen surface上，
        pygame.display.flip()                       # 更新屏幕内容


if __name__ == "__main__":
    main()
