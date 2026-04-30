import pygame
import random

# Helper function to load and scale images easily
def load_img(path, width, height):
    try:
        img = pygame.image.load(f"assets/{path}").convert_alpha()
        return pygame.transform.scale(img, (width, height))
    except pygame.error:
        # Fallback if image is missing: creates a colored rectangle
        surf = pygame.Surface((width, height))
        surf.fill((255, 0, 255)) # Bright pink indicates missing asset
        return surf

class Player(pygame.sprite.Sprite):
    def __init__(self, color_name):
        super().__init__()
        # In a full version, you could use f"player_{color_name}.png"
        self.image = load_img("player_car.png", 45, 80)
        self.rect = self.image.get_rect(center=(200, 500))
        self.shield_active = False

    def update(self, keys):
        # Movement with boundary checks (keeping car on the road)
        if keys[pygame.K_LEFT] and self.rect.left > 40: 
            self.rect.move_ip(-6, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < 360:
            self.rect.move_ip(6, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, base_speed):
        super().__init__()
        # Randomly choose NPC type for variety
        self.type = random.choice(["Standard", "Speeder", "Zagger"])
        
        if self.type == "Speeder":
            self.image = load_img("enemy_fast.png", 45, 80)
            self.speed = base_speed + 3
        elif self.type == "Zagger":
            self.image = load_img("enemy_truck.png", 50, 90)
            self.speed = base_speed - 1
        else:
            self.image = load_img("enemy_car.png", 45, 80)
            self.speed = base_speed

        # Randomly choose one of the 3 main lanes
        lane_x = random.choice([80, 200, 320])
        self.rect = self.image.get_rect(center=(lane_x, -100))
        self.move_direction = 1 

    def update(self):
        self.rect.move_ip(0, self.speed)
        
        # Zagger behavior: swerves left and right
        if self.type == "Zagger":
            self.rect.move_ip(self.move_direction * 2, 0)
            if self.rect.left < 50 or self.rect.right > 350:
                self.move_direction *= -1

        if self.rect.top > 650:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        # Practice 11: Weighted selection
        self.type = random.choices(
            ["Bronze", "Silver", "Gold"], 
            weights=[70, 20, 10], 
            k=1
        )[0]
        
        stats = {
            "Bronze": {"val": 1, "img": "coin_bronze.png", "size": 25},
            "Silver": {"val": 5, "img": "coin_silver.png", "size": 30},
            "Gold":   {"val": 10, "img": "coin_gold.png", "size": 35}
        }
        
        self.value = stats[self.type]["val"]
        self.image = load_img(stats[self.type]["img"], stats[self.type]["size"], stats[self.type]["size"])
        self.rect = self.image.get_rect(center=(random.randint(60, 340), -50))

    def update(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > 650:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, p_type):
        super().__init__()
        self.type = p_type
        files = {
            "Nitro": "powerup_nitro.png", 
            "Shield": "powerup_shield.png", 
            "Repair": "powerup_repair.png"
        }
        self.image = load_img(files[p_type], 40, 40)
        self.rect = self.image.get_rect(center=(random.randint(60, 340), -50))

    def update(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > 650:
            self.kill()