import pygame

def main():
    pygame.init()
    screen =pygame.display.set_mode((640, 480))
    clock =pygame.time.Clock()
    radius =15
    mode ='blue'
    tool ='brush'
    points =[]
    while True:
        pressed =pygame.key.get_pressed()
        alt_held =pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held =pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key ==pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key== pygame.K_r:
                    mode = 'red'
                elif event.key== pygame.K_g:
                    mode = 'green'
                elif event.key== pygame.K_b:
                    mode = 'blue'

                elif event.key== pygame.K_c:
                    tool = 'circle'
                elif event.key== pygame.K_l:
                    tool = 'brush'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key ==pygame.K_t:
                    tool = 'rectangle'
                elif event.key == pygame.K_s:
                    tool = 'square'
                elif event.key== pygame.K_h:
                    tool = 'right_triangle'
                elif event.key== pygame.K_q:
                    tool = 'equilateral_triangle'
                elif event.key== pygame.K_d:
                    tool = 'rhombus'

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, tool, mode))
                points = points[-256:]
        screen.fill((0, 0, 0))
        for i, (pos, tool, color) in enumerate(points):
            if tool == 'brush':
                drawLineBetween(screen, i, pos, pos, radius, color)
            elif tool == 'circle':
                pygame.draw.circle(screen, getColor(color, i), pos, radius)
            elif tool =='eraser':
                pygame.draw.circle(screen, (0, 0, 0), pos, radius)
            elif tool =='rectangle':
                pygame.draw.rect(screen, getColor(color, i), (pos[0] - radius, pos[1] - radius, radius * 2, radius * 2))
            elif tool =='square':
                size =radius * 2
                pygame.draw.rect(screen, getColor(color, i), (pos[0], pos[1], size, size))
            elif tool == 'right_triangle':
                points_tri = [(pos[0], pos[1]), (pos[0] + radius * 2, pos[1]), (pos[0], pos[1] + radius * 2)]
                pygame.draw.polygon(screen, getColor(color, i), points_tri)
            elif tool =='equilateral_triangle':
                points_tri = [
                    (pos[0], pos[1] - radius),
                    (pos[0]-radius,pos[1] + radius),
                    (pos[0]+radius, pos[1] + radius)
                ]
                pygame.draw.polygon(screen, getColor(color, i), points_tri)
            elif tool =='rhombus':
                points_rh = [
                    (pos[0],pos[1]-radius),
                    (pos[0] -radius,pos[1]),
                    (pos[0],pos[1] +radius),
                    (pos[0]+ radius,pos[1])
                ]
                pygame.draw.polygon(screen, getColor(color, i), points_rh)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    color = getColor(color_mode, index)
    pygame.draw.circle(screen, color, start, width)
def getColor(color_mode, index):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode =='blue':
        return (c1, c1, c2)
    elif color_mode =='red':
        return (c2, c1, c1)
    elif color_mode =='green':
        return (c1, c2, c1)
    return (255, 255, 255)

main()