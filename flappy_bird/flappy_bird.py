import pygame,random,time
pygame.init()

#functions

#DRAWING POLES
def draw_poles(board,color,gap,x_coordinate,center):

  pygame.draw.rect(board,color,(x_coordinate,0,90,center-gap-30))
  pygame.draw.rect(board,color,(x_coordinate-10,center-gap-30,110,30))
  pygame.draw.rect(board,color,(x_coordinate,center+gap+30,90,height-center-gap))
  pygame.draw.rect(board,color,(x_coordinate-10,center+gap,110,30))


#PRINTING ANY TEXT ON PYGAME CONSOLE
def printing(text,color,coordinates,disp_surf,font,size):
  myfont=pygame.font.SysFont(font,size)
  dispsurf=myfont.render(text,True,color)
  disprect=dispsurf.get_rect()
  disprect.midtop=(coordinates)
  disp_surf.blit(dispsurf,disprect)
  pygame.display.update()
    
                     #PHYSICS
jump=700
min_speed=160
u=0
a=1800


                    #VARIABLES
speed=8
game=True
cont_inue=False
width=1366
height=700
current_pole=1
last_pole=1
space=600
frames_per_second=40
gap=90
x=[0,width]
fp=[200,240]
center=[0,random.randrange(gap+40,height-gap-40)]
fb_width=50
fb_height=35
score=0

fb_image={}
image_turn=1
                #IMAGES
fb_image[1]=pygame.transform.scale(pygame.image.load("flappybird1.png"),(fb_width,fb_height))
fb_image[2]=pygame.transform.scale(pygame.image.load("flappybird2.png"),(fb_width,fb_height))
fb_image[3]=pygame.transform.scale(pygame.image.load("flappybird3.png"),(fb_width,fb_height))
fb_bg=pygame.transform.scale(pygame.image.load("fbbg.jpg"),(width,height))



                #INITIALIZING BOARD
board=pygame.display.set_mode((width,height))
pygame.display.set_caption('Flappy Bird')
fps=pygame.time.Clock()


                     #SOUNDS
sfx_wing=pygame.mixer.Sound('sfx_wing.wav')
sfx_hit=pygame.mixer.Sound('sfx_hit.wav')
sfx_die=pygame.mixer.Sound('sfx_die.wav')
sfx_point=pygame.mixer.Sound('sfx_point.wav')

                    #COLORS
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
black=pygame.Color(0,0,0)
green=pygame.Color(50,100,0)
yellow=pygame.Color(255,255,0)


                #START PAGE(HIT ANY KEY TO CONTINUE)
cont_inue=False
while cont_inue==False:
  printing('Hit any key to continue...',yellow,(int(width/2),0),board,'monaco',120,)
  board.blit(fb_bg,(0,0))
  board.blit(pygame.transform.rotate(fb_image[int(image_turn)],u/jump*-35),fp)
  if image_turn==3.75:image_turn=1
  else:image_turn+=0.25
  pygame.display.update()
  #time.sleep(1)
  for event in pygame.event.get():
    if event.type==pygame.KEYDOWN:
      cont_inue=True
    
  
                    #INT MAIN

while True:

    
  if fp[0]>x[score+1]:
    sfx_point.play()
    score+=1
    
    
                    #FLAPPYBIRD FLAP WING ANIMATION
  if image_turn==3.75:image_turn=1
  else:image_turn+=0.25
    
    
    
                    #CHECKING FOR GAME OVER
  if fp[1]>height:
    cont_inue=False
    printing('Hit any key to quit...',yellow,(int(width/2),0),board,'monaco',120,)
    while cont_inue==False:
      for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
          cont_inue=True
    
    
    pygame.quit()
    quit()
  
  if fp[0] in range(x[current_pole]-fb_width,x[current_pole]+100) and (int(fp[1]+fb_height) not in range(center[current_pole]-gap,center[current_pole]+gap) or int(fp[1]) not in range(center[current_pole]-gap-int(fb_height/2),center[current_pole]+gap+int(fb_height/2))) and game==True:
    u=0
    sfx_hit.play()
    #time.sleep(0.3)
    sfx_die.play()
    game=False
    

  


         #CALCULATING POSITION OF BIRD, REBOUNDING AND PRINTING EVERYTHING

  u+=a/frames_per_second
  if u>-min_speed and u<0:
    u*=-1
  fp[1]+=u/frames_per_second

  if fp[1]<=0:
        fp[1]=0

  

  board.blit(fb_bg,(0,0))
  board.blit(pygame.transform.rotate(fb_image[int(image_turn)],u/jump*-35),fp)      #ROTATING FLAPPY BIRD


    
    
         #GENERATE AND PRINT POLES

  if x[last_pole]+space+80<width:
    x.append(x[i]+space)
    center.append(random.randrange(gap+40,height-gap-40))
    last_pole+=1
  
  for i in range(current_pole,last_pole+1):
    draw_poles(board,green,gap,x[i],center[i])
  

   
    
        #CALCULATION AND PRINTING SCORE
  for i in range(current_pole,last_pole+1):
    if game==True:
      x[i]-=speed

    printing("%r"%score,white,(int(width/2),int(height/5)),board,'impact',100)
    
  fps.tick(frames_per_second)
    
    
    
         #DETECT JUMP 
  for event in pygame.event.get():

    if event.type==pygame.KEYDOWN and u>0:
      if event.key==pygame.K_UP and game==True:
        u=-jump
        sfx_wing.play()
      if event.type==pygame.K_ESCAPE:
        pygame.quit()
        quit()
        
        
        
         #PLAY SOUND OF POINT INCREMENT AND UPDATE CURRENT_POLE
  if x[current_pole]<-50:
    current_pole+=1
    