import pygame
from random import randint, choice

class Game:
    NoOfElements = 20
    score = {"stone":NoOfElements, "paper":NoOfElements, "scissor":NoOfElements}
    
    def __init__(self,screen, obj, width, height, size, font):
        self.screen = screen    
        self.width = width
        self.height = height    
        self.size = size
        self.font = font
        self.obj = obj
        
        # sprite
        self.stones = [obj["stone"] for _ in range(self.NoOfElements)]  
        self.scissors = [obj["scissor"] for _ in range(self.NoOfElements)]  
        self.papers = [obj["paper"] for _ in range(self.NoOfElements)]  
        # sprite positions
        self.stones_pos = [(randint(0, width//size)*size, (randint(0, height//size)*size)) for _ in range(self.NoOfElements)]  
        self.scissors_pos = [(randint(0, width//size)*size, (randint(0, height//size)*size)) for _ in range(self.NoOfElements)]  
        self.papers_pos = [(randint(0, width//size)*size, (randint(0, height//size)*size)) for _ in range(self.NoOfElements)]  
     
    def draw(self):
        self.screen.fill((0, 0, 0))
        for sp in range(self.score['stone']):  self.screen.blit(self.stones[sp], self.stones_pos[sp])
        for sp in range(self.score['scissor']): self.screen.blit(self.scissors[sp], self.scissors_pos[sp])
        for sp in range(self.score['paper']): self.screen.blit(self.papers[sp], self.papers_pos[sp])            
        self.scoreboard()
        self.gameover()
        pygame.display.update()
    
    def gameover(self):
        for obj in self.score:
            if self.score[obj]==60:
                text = self.font.render(f'Game over {obj} wins', True, (255,0,0))
                self.screen.blit(text, (100,200))
    
    def scoreboard(self):
        text = self.font.render(f'Stone: {self.score["stone"]} Paper: {self.score["paper"]} Scissor: {self.score["scissor"]}', True, (255,0,0))
        self.screen.blit(text, (0,490))
        
    def collision(self):
        for st in range(self.score['stone']):
            for sc in range(self.score['scissor']):
                try:
                    if self.stones_pos[st] == self.scissors_pos[sc]:  
                        self.score['stone'] += 1
                        self.score['scissor'] -= 1
                        self.scissors.pop(sc)
                        self.stones.append(self.obj['stone'])
                        self.stones_pos.append(self.scissors_pos.pop(sc))
                except IndexError:
                    pass
                    
        for st in range(self.score['stone']):
            for pa in range(self.score['paper']):
                try:
                    if self.stones_pos[st] == self.papers_pos[pa]:  
                        self.score['paper'] += 1
                        self.score['stone'] -= 1
                        self.stones.pop(st)
                        self.papers.append(self.obj['paper'])
                        self.papers_pos.append(self.stones_pos.pop(st))
                except IndexError:
                    pass
                    
        for sc in range(self.score['scissor']):
            for pa in range(self.score['paper']):
                try:
                    if self.scissors_pos[sc] == self.papers_pos[pa]:  
                        self.score['scissor'] += 1
                        self.score['paper'] -= 1
                        self.papers.pop(pa)
                        self.scissors.append(self.obj['scissor'])
                        self.scissors_pos.append(self.papers_pos.pop(pa))
                except IndexError:
                    pass
            
    def random_pos(self, pos, dim):
        factor = choice((-1,0,1))
        if pos<0: print("Oops! Game crashed!"); exit()
        if (dim=="w" and (0 <= pos+factor <= self.width)):  return factor*self.size + pos
        elif (dim=="h" and (0 <= pos+factor <= self.width)):  return factor*self.size + pos
        return self.random_pos(pos, dim)
            
    def move(self):
        for sp in range(self.score['stone']): self.stones_pos[sp] = self.random_pos(self.stones_pos[sp][0],'w'), self.random_pos(self.stones_pos[sp][1], 'h')
        for sp in range(self.score['scissor']): self.scissors_pos[sp] = self.random_pos(self.scissors_pos[sp][0],'w'), self.random_pos(self.scissors_pos[sp][1], 'h')
        for sp in range(self.score['paper']): self.papers_pos[sp] = self.random_pos(self.papers_pos[sp][0],'w'), self.random_pos(self.papers_pos[sp][1], 'h')
            
    def wait_and_run(self, time):
        event = pygame.USEREVENT+ 1
        pygame.time.set_timer(event ,time) 
        return event