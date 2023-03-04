import pygame

BPM = 135
MSPB = 6e4/BPM
SCREEN_SIZE = (1920, 1080)
H2O = (255, 255, 255)
CuSO4_5H2O = (33, 111, 222)
CuSO4 = (222, 222, 222)
CuO = (33, 33, 33)
COLORS = (
    (0, H2O),
    (98, CuSO4_5H2O),
    (194, CuSO4),
    (332, CuO),
    (336, CuSO4_5H2O),
    (340, H2O),
    (380, H2O)
)
LYRICS = (
    (2, '溶解的 硫酸铜 结晶着', 12),
    (14, '梦幻的 靛蓝色 显形了', 24),
    (26, '虽是片 无生机 的沙漠', 36),
    (38, '却可以 缓解我 的干渴', 48),
    (50, '「靛蓝沙漠 / CuSO4·5H2O」', 60),
    (62, '词曲：蔗蓝', 72),
    (74, 'Vocal：诗岸', 84),
    (86, '调教：栖鸢_d', 96),
    (98, '五水合 硫酸铜 失水着', 108),
    (110, '沙漠正 渐渐地 褪色了', 120),
    (122, '幻想也 终究会 破灭吗', 132),
    (134, '算了吧 向前走 就好了', 144),
    (146, 'Ahhh...', 192),
    (194, '无水的 硫酸铜 分解着', 204),
    (206, '被暗黑 的颜色 吞噬了', 216),
    (218, '连现实 都要被 击溃了', 228),
    (230, '我剩余 的希望 在哪呢', 240),
    (299, '最后的 硫酸铜 消失着', 312),
    (315, '靛蓝色 的沙漠 永别了', 328)
)

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('靛蓝沙漠.wav')
    screen = pygame.display.set_mode(SCREEN_SIZE, flags=pygame.FULLSCREEN)
    font = pygame.font.Font(r'C:\Users\ganpi\Downloads\songhei.ttf', 100)

    screen.fill(H2O)
    pygame.display.update()

    cnt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                cnt += 1
        if cnt >= 3:
            break

    pygame.mixer.music.play()

    while True:
        beat_now = pygame.mixer.music.get_pos()/MSPB

        for i, j in enumerate(COLORS):
            if beat_now < j[0]:
                color_now = [(COLORS[i-1][1][j]*(COLORS[i][0]-beat_now)+COLORS[i][1][j]*(
                    beat_now-COLORS[i-1][0]))/(COLORS[i][0]-COLORS[i-1][0]) for j in range(3)]
                screen.fill(color_now)
                break

        for start_beat, lyric, end_beat in LYRICS:
            if start_beat <= beat_now <= end_beat:
                lrc_alpha = int(
                    min(1, min(beat_now-start_beat, end_beat-beat_now))*255)
                lrc_color = [255-i for i in color_now]
                lrc_render = font.render(lyric, True, lrc_color)
                lrc_rect = lrc_render.get_rect(center=screen.get_rect().center)
                temp_sur = pygame.Surface(lrc_rect.size, pygame.SRCALPHA)
                temp_sur.blit(lrc_render, (0, 0))
                temp_sur.set_alpha(lrc_alpha)
                screen.blit(temp_sur, lrc_rect)
                break

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
