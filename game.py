import pygame,random
def start():
    d='r'
    
    s=[100,50]
    s1=[[100,50],[90,50],[80,50]]
    x=720
    y=480
    f=[random.randint(0,x),random.randint(0,y)]
    f1=False
    a=pygame.init()
    pygame.display.set_caption('Snake Eater')
    g=pygame.display.set_mode((x,y))
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    score=0
    diff=25
    fps=pygame.time.Clock()

def gameplay(d,x,y,score,black,white,red,green,blue):
    while True:
        for event in pygame.event.get():
            if(event.key==ord('w') and d!='d'):
                d='u'
                s[1]+=10
            elif(event.key==ord('a') and d!='r'):
                d='l'
                s[0]-=10
            elif(event.key==ord('s') and d!='u'):
                d='d'
                s[1]-=10
            elif(event.key==ord('d') and d!='l'):
                d='r'
                s[0]+=10
            if(s[0]==f[0] & s[1]==f[1]):
                f=[random.randint(0,x),random.randint(0,y)]
                s1.insert(0,list(s))
                score+=1
            game_window.fill(black)
            for pos in s1:
                pygame.draw.rect(game_window,green,pygame.Rect(pos[0],pos[1],10,10))
            pygame.draw.rect(game_window,white,pygame.Rect(f[0],f[1],10,10))

            if(s[0]>x or s[1]>y or s[0]<0 or s[1]<0):
                game_over()
            for pos in s1[1:]:
                if(pos[0]==s[0] and pos[1]==s[1]):
                    game_over()
            show_score(1, white, 'consolas', 20)
            pygame.display.update()
            fps.tick(diff)
def game_over():
    my=pygame.font.SysFont('times new roman',90)
    gos=my.render('GAME OVER',True,red)
    gor=gos.get_rect()
    
            
                
            
            
