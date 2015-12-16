'''
Project Name: GraPyCal
Version: 1.0
Author: Manikiran P
Last Modified Date: 12/16/2015
Requirements: Python 2.7 & Pygame
'''
import pygame,sys
def check(x,y):
    try:
        return eval(y.lower())
    except:
        return False
def f(x,y):
    return eval(y.lower())
class GraPyCal(object):
    def __init__(self):
        pygame.display.set_caption("GraPyCal v1.0")
        screen=pygame.display.set_mode((800,500))
        myfont=pygame.font.SysFont("Arial",16)
        myfont_32=pygame.font.SysFont("Arial",32)
        myfont_20=pygame.font.SysFont("Arial",20)
        points=[]
        points_r=[]
        y="x"
        err=0
        btns_t=["Y","X","C","Clear","7","8","9","+","-","4","5","6","/","*","1","2","3","^","%","0",".","(",")","K"]
        btns=[(520,100,40,40),(575,100,40,40),(630,100,40,40),(685,100,95,40),(520,160,40,40),(575,160,40,40),(630,160,40,40),(685,160,40,40),(740,160,40,40),(520,220,40,40),(575,220,40,40),(630,220,40,40),(685,220,40,40),(740,220,40,40),(520,280,40,40),(575,280,40,40),(630,280,40,40),(685,280,40,40),(740,280,40,40),(520,340,40,40),(575,340,40,40),(630,340,40,40),(685,340,40,40),(740,340,40,40)]
        for i in range(-10,11):
            points.append((250+i*25,250-f(i,y)*25))
            points_r.append((i,f(i,y)))
        while 1:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif e.type==pygame.MOUSEBUTTONDOWN:
                    mpos=pygame.mouse.get_pos()
                    for i in range(len(btns)):
                        if pygame.Rect(btns[i]).collidepoint(mpos):
                            if i==3:
                                y=y[:-1]
                            else:
                                y+=btns_t[i]
                        elif pygame.Rect(580,420,140,50).collidepoint(mpos):
                            if check(1,y):
                                err=0
                                points,points_r=[],[]
                                for i in range(-10,11):
                                    points.append((250+i*25,250-f(i,y)*25))
                                    points_r.append((i,f(i,y)))
                            else:
                                err=1
            screen.fill((255,255,255))
            for i in range(10):
                if i==5:
                    col=(0,0,0)
                else:
                    col=(0,200,0)
                for j in range(10):
                    pygame.draw.line(screen,(0,200,0),(i*50+j*10,0),(i*50+j*10,500))
                    pygame.draw.line(screen,(0,200,0),(0,i*50+j*10),(500,i*50+j*10))
                pygame.draw.line(screen,col,(i*50,0),(i*50,500),2)
                pygame.draw.line(screen,col,(0,i*50),(500,i*50),2)
            pygame.draw.lines(screen,(0,0,0),0,[(245,5),(250,0),(255,5)],2)
            pygame.draw.lines(screen,(0,0,0),0,[(5,245),(0,250),(5,255)],2)
            pygame.draw.lines(screen,(0,0,0),0,[(245,495),(250,500),(255,495)],2)
            pygame.draw.lines(screen,(0,0,0),0,[(495,245),(500,250),(495,255)],2)
            pygame.draw.circle(screen,(0,0,0),(251,251),4)
            pygame.draw.lines(screen,(0,0,200),0,points,2)
            for i in range(len(points)):
                pygame.draw.circle(screen,(200,0,0),(points[i][0]+1,points[i][1]),2)
                temp=myfont.render(str(points_r[i]),1,(0,0,0))
                screen.blit(temp,(points[i][0]+5,points[i][1]-10))
            pygame.draw.rect(screen,(0,0,0),(500,0,300,500))
            pygame.draw.rect(screen,(255,255,255),(520,20,260,60))
            y_txt=myfont_32.render(("y="+y).upper(),1,(0,0,0))
            screen.blit(y_txt,(540,30))
            pygame.draw.rect(screen,(200,200,200),(580,420,140,50))
            temp=myfont_32.render("Graph",1,(0,0,0))
            screen.blit(temp,(650-temp.get_width()/2,425))
            for i in range(len(btns)):
                pygame.draw.rect(screen,(200,200,200),btns[i])
                temp=myfont_20.render(btns_t[i],1,(0,0,0))
                screen.blit(temp,(btns[i][0]+btns[i][2]/2-temp.get_width()/2,btns[i][1]+btns[i][3]/2-temp.get_height()/2))
            if err:
                temp=myfont.render("INVALID FUNCTION",1,(200,0,0))
                screen.blit(temp,(650-temp.get_width()/2,400))
            pygame.display.flip()
if __name__=="__main__":
    pygame.init()
    GraPyCal()
