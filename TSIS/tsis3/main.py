import pygame
import time
import random
import sys
from persistence import update_leaderboard, get_settings, load_json
from ui import Button, draw_text
from racer import Player, Enemy, PowerUp, Coin

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcade Racer: Pro Edition")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 24)

# Load Visual Assets
try:
    ROAD_IMG = pygame.image.load("assets/road.png").convert()
    ROAD_IMG = pygame.transform.scale(ROAD_IMG, (WIDTH, HEIGHT))
except:
    ROAD_IMG = pygame.Surface((WIDTH, HEIGHT))
    ROAD_IMG.fill((50, 50, 50))

# Load Audio Assets
try:
    BGM = pygame.mixer.Sound("assets/background_music.mp3")
    COIN_SFX = pygame.mixer.Sound("assets/coin.wav")
    CRASH_SFX = pygame.mixer.Sound("assets/crash.wav")
    BGM.set_volume(0.3)
except:
    BGM = COIN_SFX = CRASH_SFX = None

def game_loop(username):
    settings = get_settings()
    is_sound_on = settings.get("sound", True)
    
    # Start Music
    if is_sound_on and BGM:
        BGM.play(loops=-1)

    # Initialize Objects
    player = Player(settings.get("color", "Red"))
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)
    
    # Game State Variables
    score = 0
    distance = 0
    coin_count = 0
    base_speed = 5 if settings.get("difficulty") == "Easy" else 8
    bg_y = 0
    
    # Power-up Timers
    nitro_end_time = 0
    shield_active = False
    active_buff = "None"

    running = True
    while running:
        current_time = time.time()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 1. Speed and Scrolling Logic
        is_nitro = current_time < nitro_end_time
        move_speed = base_speed * 1.8 if is_nitro else base_speed
        
        bg_y += move_speed
        if bg_y >= HEIGHT:
            bg_y = 0
            
        distance += (move_speed / 20) # Distance accumulation
        
        # 2. Spawning Logic
        # Spawn Enemies
        if random.random() < 0.02:
            new_enemy = Enemy(move_speed)
            if not pygame.sprite.spritecollideany(new_enemy, enemies):
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Spawn Coins (Weighted)
        if random.random() < 0.03:
            new_coin = Coin(move_speed)
            if not pygame.sprite.spritecollideany(new_coin, enemies):
                coins.add(new_coin)
                all_sprites.add(new_coin)

        # Spawn Power-ups
        if random.random() < 0.005:
            new_pw = PowerUp(random.choice(["Nitro", "Shield", "Repair"]))
            powerups.add(new_pw)
            all_sprites.add(new_pw)

        # 3. Updates
        keys = pygame.key.get_pressed()
        player.update(keys)
        enemies.update()
        coins.update(move_speed)
        powerups.update(move_speed)

        # 4. Collision Logic
        # Coin Collection
        coins_hit = pygame.sprite.spritecollide(player, coins, True)
        for c in coins_hit:
            score += c.value
            coin_count += 1
            if is_sound_on and COIN_SFX:
                COIN_SFX.play()
            base_speed += 0.05 # Practice 11: Speed increases on collection

        # Power-up Collection
        pw_hit = pygame.sprite.spritecollideany(player, powerups)
        if pw_hit:
            if pw_hit.type == "Nitro":
                nitro_end_time = current_time + 5
                active_buff = "NITRO"
            elif pw_hit.type == "Shield":
                shield_active = True
                active_buff = "SHIELD"
            elif pw_hit.type == "Repair":
                # Clear all enemies on screen
                for e in enemies: e.kill()
            pw_hit.kill()

        # Traffic Collision
        hit_enemy = pygame.sprite.spritecollideany(player, enemies)
        if hit_enemy:
            if shield_active:
                shield_active = False
                active_buff = "None"
                hit_enemy.kill()
            else:
                if is_sound_on and CRASH_SFX:
                    BGM.stop()
                    CRASH_SFX.play()
                update_leaderboard(username, score, distance)
                return score, int(distance), coin_count

        # 5. Rendering
        SCREEN.blit(ROAD_IMG, (0, bg_y))
        SCREEN.blit(ROAD_IMG, (0, bg_y - HEIGHT))
        
        all_sprites.draw(SCREEN)

        # HUD Overlay
        draw_text(SCREEN, f"Driver: {username}", 18, 80, 20, (255, 255, 255))
        draw_text(SCREEN, f"Score: {score}", 22, 80, 50, (255, 215, 0))
        draw_text(SCREEN, f"Coins: {coin_count}", 18, 330, 50, (255, 255, 255))
        draw_text(SCREEN, f"Dist: {int(distance)}m", 18, 330, 20, (200, 200, 200))
        
        if active_buff != "None":
            color = (0, 255, 255) if active_buff == "SHIELD" else (255, 50, 50)
            draw_text(SCREEN, f"BUFF: {active_buff}", 22, 200, 100, color)

        pygame.display.flip()
        CLOCK.tick(60)

def main_menu():
    user = ""
    entering_name = True
    
    while True:
        SCREEN.fill((10, 10, 10))
        
        if entering_name:
            draw_text(SCREEN, "ARCADE RACER", 45, 200, 100, (255, 0, 0))
            draw_text(SCREEN, "Enter Driver Name:", 24, 200, 220)
            draw_text(SCREEN, f"> {user}_", 30, 200, 270, (0, 255, 0))
            draw_text(SCREEN, "Press ENTER to continue", 16, 200, 550, (100, 100, 100))
        else:
            draw_text(SCREEN, "MAIN MENU", 40, 200, 100, (255, 255, 255))
            btn_play = Button("START RACE", 100, 200, 200, 50, (50, 200, 50))
            btn_leader = Button("LEADERBOARD", 100, 270, 200, 50, (150, 150, 150))
            btn_quit = Button("EXIT", 100, 340, 200, 50, (200, 50, 50))
            
            for b in [btn_play, btn_leader, btn_quit]: b.draw(SCREEN, FONT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if entering_name and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user != "":
                    entering_name = False
                elif event.key == pygame.K_BACKSPACE:
                    user = user[:-1]
                else:
                    if len(user) < 12 and event.unicode.isalnum():
                        user += event.unicode
            
            if not entering_name and event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.is_clicked(event.pos):
                    s, d, c = game_loop(user)
                    game_over_screen(s, d, c)
                if btn_leader.is_clicked(event.pos):
                    show_leaderboard()
                if btn_quit.is_clicked(event.pos):
                    pygame.quit(); sys.exit()

        pygame.display.flip()
        CLOCK.tick(30)

def game_over_screen(s, d, c):
    while True:
        SCREEN.fill((20, 0, 0))
        draw_text(SCREEN, "WRECKED!", 50, 200, 120, (255, 0, 0))
        draw_text(SCREEN, f"Score: {s}", 28, 200, 220, (255, 215, 0))
        draw_text(SCREEN, f"Distance: {d}m", 24, 200, 260)
        draw_text(SCREEN, f"Coins Collected: {c}", 20, 200, 300)
        
        btn_restart = Button("TRY AGAIN", 100, 380, 200, 50, (100, 100, 255))
        btn_restart.draw(SCREEN, FONT)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_restart.is_clicked(event.pos): return

        pygame.display.flip()

def show_leaderboard():
    scores = load_json("leaderboard.json", [])
    while True:
        SCREEN.fill((15, 15, 15))
        draw_text(SCREEN, "HALL OF FAME", 35, 200, 60, (255, 215, 0))
        
        # Display top 10
        for i, entry in enumerate(scores[:10]):
            txt = f"{i+1}. {entry['name']:<12} {entry['score']:>5}"
            draw_text(SCREEN, txt, 20, 200, 120 + (i * 35), (200, 200, 200))
        
        btn_back = Button("BACK", 125, 500, 150, 45, (100, 100, 100))
        btn_back.draw(SCREEN, FONT)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_back.is_clicked(event.pos): return
        
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()