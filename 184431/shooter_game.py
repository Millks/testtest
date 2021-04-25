from pygame import *
from random import randint

#фоновая музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

# here
# font.init()
# font2 = font.Font(None, 36)

# 3
# font1 = font.Font(None, 80)
# win = font1.render('YOU WIN!', True, (255, 255, 255))
# lose = font1.render('YOU LOSE!', True, (180, 0, 0))


 
#нам нужны такие картинки:
img_back = "galaxy.jpg" #фон игры
img_hero = "rocket.png" #герой
# img_bullet = "bullet.png" #пуля 3

 
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
   def fire(self):
       pass
#   def fire(self):
#       bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
#       bullets.add(bullet)



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        # global lost
        if self.rect.y > 500:
            self.rect.x = randint(0,620)
            self.rect.y = 0
            # lost = lost + 1


# #класс спрайта-пули  
# class Bullet(GameSprite):
# #    #движение врага
#     def update(self):
#         self.rect.y += self.speed
#         #исчезает, если дойдет до края экрана
#         if self.rect.y < 0:
#             self.kill()



# # here
# score = 0 #сбито кораблей
# lost = 0 #пропущено кораблей
# max_lost = 3


#Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
 
#создаем спрайты
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
monster = Enemy( "ufo.png",randint(0,620),0,80,80,randint(1,5))
#monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты

# here
monsters = sprite.Group()
for i in range(1, 6):
   monster = Enemy("ufo.png", randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
   monsters.add(monster)

# 3
# bullets = sprite.Group()

finish = False
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
   for e in event.get():
       if e.type == QUIT:
           run = False
 
   if not finish:
       #обновляем фон
       window.blit(background,(0,0))
    #    here
    #    text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
    #    window.blit(text, (10, 20))
    #    text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
    #    window.blit(text_lose, (10, 50))


 
       #производим движения спрайтов
       ship.update()
 
       #обновляем их в новом местоположении при каждой итерации цикла
       ship.reset()
    #    monster.update()
    #    monster.reset()
       monsters.update()
       monsters.draw(window)

 
       display.update()
   #цикл срабатывает каждые 0.05 секунд
   time.delay(50)