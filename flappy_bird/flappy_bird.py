import pygame,random,time
pygame.init()

#functions
def draw_poles(gap,x_coordinate,center):

  pygame.draw.rect(board,green,(x_coordinate,0,90,center-gap-30))
  pygame.draw.rect(board,green,(x_coordinate-10,center-gap-30,110,30))
  pygame.draw.rect(board,green,(x_coordinate,center+gap+30,90,height-center-gap))
  pygame.draw.rect(board,green,(x_coordinate-10,center+gap,110,30))


                     #PHYSICS
jump=550
min_speed=100
u=0
a=800

                    #VARIABLES
speed=10
game=True
cont_inue=False
width=1366
height=911
current_pole=1
last_pole=1
space=800
frames_per_second=35
gap=90
x=[0,width]
fp=[40,240]
center=[0,random.randrange(gap+40,height-gap-40)]
fb_width=45
fb_height=49


                #IMAGES
fb_image=pygame.transform.scale(pygame.image.load("flappybird.png"),(fb_width,fb_height))
fb_bg=pygame.transform.scale(pygame.image.load("fbbg.jpg"),(width,height))




board=pygame.display.set_mode((width,height))
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

font=pygame.font.SysFont('monaco',40)
myfont=pygame.font.SysFont('monaco',120)

start_surf=myfont.render('hit any key to continue...',True,yellow)
start_rect=start_surf.get_rect()
start_rect.center=(int(width/2),int(height/2))
board.blit(start_surf,start_rect)
pygame.display.update()

while cont_inue==False:
  for event in pygame.event.get():
    if event.type==pygame.KEYDOWN:
      cont_inue=True
        
while True:

    
        #CHECKING FOR GAME OVER
  if fp[1]>height:
    time.sleep(2)
    pygame.quit()
  
  if fp[0]+fb_width in range(x[current_pole]-10,x[current_pole]+100) and (int(fp[1]+fb_height) not in range(center[current_pole]-gap,center[current_pole]+gap) or int(fp[1]) not in range(center[current_pole]-gap,center[current_pole]+gap)) and game==True:
    u=0
    sfx_hit.play()
    time.sleep(0.3)
    sfx_die.play()
    game=False
    

  
         #CALCULATING POSITION OF BIRD AND PRINTING EVERYTHING

  u+=a/frames_per_second
  if u>-min_speed and u<0:
    u*=-1
  fp[1]+=u/frames_per_second

  board.blit(fb_bg,(0,0))
  board.blit(fb_image,fp)


         #GENERATE POLES

  if x[last_pole]+space+80<width:
    x.append(x[i]+space)
    center.append(random.randrange(gap+40,height-gap-40))
    last_pole+=1
  
  for i in range(current_pole,last_pole+1):
    draw_poles(gap,x[i],center[i])
  

   
    
        #CALCULATION SCORE
  for i in range(current_pole,last_pole+1):
    if game==True:
      x[i]-=speed
  text=font.render('Score:%r'%current_pole,True,white)
  rect=text.get_rect()
  rect.midtop=(width-100,100)
  board.blit(text,rect)
  pygame.display.update()
  fps.tick(frames_per_second)
    
    
    
         #DETECT JUMP 
  for event in pygame.event.get():

    if event.type==pygame.KEYDOWN and u>0:
      if event.key==pygame.K_SPACE and game==True:
        u=-jump
        sfx_wing.play()
      if event.type==pygame.K_ESCAPE:
        pygame.quit()
        
        
        
         #PLAY SOUND OF POINT INCREMENT
  if fp[0]>=x[current_pole]+120:
    current_pole+=1
    sfx_point.play()