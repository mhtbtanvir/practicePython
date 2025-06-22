import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
CIRCLE_RADIUS = 200
CIRCLE_CENTER = (WIDTH // 2, HEIGHT // 2)
BALL_RADIUS = 12
BLUE_BALL_RADIUS = 16
GREEN_BALL_RADIUS = 8
CONSISTENT_SPEED = 3.0
DAMPING = 0.995
BOUNCE_FACTOR = 0.95

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 100, 100)
BLUE = (100, 150, 255)
GREEN = (100, 255, 100)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
YELLOW = (255, 255, 100)
LIGHT_GRAY = (200, 200, 200)
SMOKE_GRAY = (150, 150, 150)
ASH_COLOR = (128, 128, 128)

# --- Sound Effects (Example) ---
split_sound = pygame.mixer.Sound(
    "D:/Python projects/practice_python/wrap/sounds/split.wav")
powerup_sound = pygame.mixer.Sound(
    "D:/Python projects/practice_python/wrap/sounds/powerup.wav")
gameover_sound = pygame.mixer.Sound(
    "D:/Python projects/practice_python/wrap/sounds/gameover.wav")

# --- Load Background Image (Example) ---
# background_image = pygame.image.load("background.png").convert()
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


class Particle:
    def __init__(self, x, y, vx, vy, color, life, size=3):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.life = life
        self.max_life = life
        self.size = size

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.98  # Friction
        self.vy *= 0.98
        self.life -= 1
        return self.life > 0

    def draw(self, screen):
        if self.life > 0:
            alpha = int(255 * (self.life / self.max_life))
            if alpha > 0:
                particle_surface = pygame.Surface(
                    (self.size * 2, self.size * 2), pygame.SRCALPHA)
                color_with_alpha = (*self.color, alpha)
                pygame.draw.circle(
                    particle_surface, color_with_alpha, (self.size, self.size), self.size)
                screen.blit(particle_surface,
                            (int(self.x - self.size), int(self.y - self.size)))


class Ball:
    def __init__(self, x, y, vx=None, vy=None, is_blue=False, is_green=False):
        self.x = x
        self.y = y
        self.is_blue = is_blue
        self.is_green = is_green

        if is_blue:
            self.radius = BLUE_BALL_RADIUS
        elif is_green:
            self.radius = GREEN_BALL_RADIUS
        else:
            self.radius = BALL_RADIUS

        # Random velocity if not specified
        if vx is None or vy is None:
            angle = random.uniform(0, 2 * math.pi)
            self.vx = math.cos(angle) * CONSISTENT_SPEED
            self.vy = math.sin(angle) * CONSISTENT_SPEED
        else:
            self.vx = vx
            self.vy = vy

        # Normalize to consistent speed
        self.normalize_speed()

    def normalize_speed(self):
        """Maintain consistent ball speed"""
        current_speed = math.sqrt(self.vx * self.vx + self.vy * self.vy)
        if current_speed > 0:
            self.vx = (self.vx / current_speed) * CONSISTENT_SPEED
            self.vy = (self.vy / current_speed) * CONSISTENT_SPEED
        else:
            # Give stopped ball a random direction
            angle = random.uniform(0, 2 * math.pi)
            self.vx = math.cos(angle) * CONSISTENT_SPEED
            self.vy = math.sin(angle) * CONSISTENT_SPEED

    def update(self):
        # Update position
        self.x += self.vx
        self.y += self.vy

        # Check collision with circle boundary
        dx = self.x - CIRCLE_CENTER[0]
        dy = self.y - CIRCLE_CENTER[1]
        distance_from_center = math.sqrt(dx * dx + dy * dy)

        # If ball hits the circle boundary, reflect it
        if distance_from_center + self.radius >= CIRCLE_RADIUS:
            # Normalize the direction vector
            if distance_from_center > 0:
                normal_x = dx / distance_from_center
                normal_y = dy / distance_from_center

                # Reflect velocity perfectly
                dot_product = self.vx * normal_x + self.vy * normal_y
                self.vx -= 2 * dot_product * normal_x
                self.vy -= 2 * dot_product * normal_y

                # Maintain consistent speed after bounce
                self.normalize_speed()

                # Move ball back inside the circle with some padding
                self.x = CIRCLE_CENTER[0] + normal_x * \
                    (CIRCLE_RADIUS - self.radius - 2)
                self.y = CIRCLE_CENTER[1] + normal_y * \
                    (CIRCLE_RADIUS - self.radius - 2)

    def handle_ball_collisions(self):
        # This will be handled in the main game loop for all balls
        pass

    def draw(self, screen):
        if self.is_blue:
            color = BLUE
        elif self.is_green:
            color = GREEN
        else:
            color = RED

        pygame.draw.circle(
            screen, color, (int(self.x), int(self.y)), self.radius)

        # Add a white outline
        pygame.draw.circle(screen, WHITE, (int(self.x),
                           int(self.y)), self.radius, 2)

        # Add highlights for special balls
        if self.is_blue:
            pygame.draw.circle(
                screen, WHITE, (int(self.x - 5), int(self.y - 5)), 5)
        elif self.is_green:
            pygame.draw.circle(
                screen, YELLOW, (int(self.x - 4), int(self.y - 4)), 4)

    def is_clicked(self, mouse_pos):
        mx, my = mouse_pos
        distance = math.sqrt((mx - self.x) ** 2 + (my - self.y) ** 2)
        return distance <= self.radius

    def split(self):
        """Create two new balls when this ball is clicked"""
        if self.is_blue or self.is_green:
            return []  # Special balls don't split

        # Create two new balls with random directions
        angle1 = random.uniform(0, 2 * math.pi)
        # Roughly opposite direction
        angle2 = angle1 + math.pi + random.uniform(-0.5, 0.5)

        speed = CONSISTENT_SPEED  # Use consistent speed

        # Create balls with better separation to avoid immediate clustering
        offset_distance = self.radius + 5
        ball1 = Ball(
            self.x + math.cos(angle1) * offset_distance,
            self.y + math.sin(angle1) * offset_distance,
            math.cos(angle1) * speed,
            math.sin(angle1) * speed
        )

        ball2 = Ball(
            self.x + math.cos(angle2) * offset_distance,
            self.y + math.sin(angle2) * offset_distance,
            math.cos(angle2) * speed,
            math.sin(angle2) * speed
        )

        return [ball1, ball2]


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ball Splitting Game")
        self.clock = pygame.time.Clock()

        # Game state
        self.balls = []
        self.ball_count = 0
        self.game_over = False
        self.win = False
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.death_mode = False
        self.missed_clicks = 0
        self.particles = []  # Visual effects particles
        self.miss_effect_timer = 0
        self.miss_effect_pos = (0, 0)
        self.score = 0  # Add score
        self.combo = 1  # Add combo multiplier
        self.split_streak = 0  # Track consecutive splits
        self.black_hole_active = False  # Black hole active flag
        self.black_hole_timer = 0  # Black hole timer

        # Load high score
        self.high_score = self.load_high_score()

        # Start with one ball in the center
        self.add_initial_ball()

    def load_high_score(self):
        """Load high score from file"""
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Save high score to file"""
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

    def add_initial_ball(self):
        """Add the first ball in the center"""
        x = CIRCLE_CENTER[0] + random.uniform(-50, 50)
        y = CIRCLE_CENTER[1] + random.uniform(-50, 50)
        self.balls.append(Ball(x, y))
        self.ball_count = 1

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.handle_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and (self.game_over or self.win):
                    self.restart_game()
                elif event.key == pygame.K_d and not (self.game_over or self.win):
                    self.toggle_death_mode()
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True

    def handle_click(self, mouse_pos):
        if self.game_over or self.win:
            return

        # Check if click is inside the circle
        dx = mouse_pos[0] - CIRCLE_CENTER[0]
        dy = mouse_pos[1] - CIRCLE_CENTER[1]
        if math.sqrt(dx * dx + dy * dy) > CIRCLE_RADIUS:
            return

        # Check if any ball was clicked
        clicked_ball = None
        for ball in self.balls:
            if ball.is_clicked(mouse_pos):
                clicked_ball = ball
                break

        if clicked_ball:
            self.handle_ball_click(clicked_ball)
            self.create_hit_effect(
                clicked_ball.x, clicked_ball.y, clicked_ball)
        else:
            # Missed click - add penalty in death mode
            if self.death_mode:
                self.handle_missed_click()
            self.create_miss_effect(mouse_pos[0], mouse_pos[1])

    def handle_ball_click(self, clicked_ball):
        if clicked_ball.is_blue:
            # Blue ball clicked - reduce balls by half!
            self.balls.remove(clicked_ball)  # Remove the blue ball first
            pygame.mixer.Sound.play(powerup_sound)  # Play powerup sound

            if len(self.balls) > 1:
                # Remove half of the remaining balls randomly
                balls_to_remove = len(self.balls) // 2
                balls_copy = self.balls.copy()
                random.shuffle(balls_copy)

                for i in range(balls_to_remove):
                    if balls_copy[i] in self.balls:
                        self.balls.remove(balls_copy[i])

            # If no balls left, add one
            if len(self.balls) == 0:
                self.add_initial_ball()

        elif clicked_ball.is_green:
            # Green ball clicked - add 6 balls!
            self.balls = []
            self.ball_count = 0
            pygame.mixer.Sound.play(powerup_sound)  # Play powerup sound
        else:
            # Regular ball clicked - split it
            self.balls.remove(clicked_ball)
            new_balls = clicked_ball.split()
            self.balls.extend(new_balls)
            self.ball_count += 1  # Net increase of 1 ball (removed 1, added 2)
            self.score += 10 * self.combo  # Increase score
            self.combo += 1  # Increase combo
            pygame.mixer.Sound.play(split_sound)  # Play split sound
            self.split_streak += 1  # Increment split streak

            # Check for black hole activation
            if self.split_streak >= 3 and not self.black_hole_active:
                self.activate_black_hole()

            # Every 10 balls, add special balls
            if self.ball_count % 5 == 0 and self.ball_count > 0:
                self.add_blue_ball()

                if self.death_mode:
                    # Add 2 green balls in death mode
                    self.add_green_ball()
                else:
                    self.split_streak = 0  # Reset split streak if not a regular ball

    def handle_missed_click(self):
        """Handle missed clicks in death mode"""
        self.missed_clicks += 1
        # Add 3 balls for each missed click
        for _ in range(2):
            self.add_random_ball()
        self.combo = 1  # Reset combo on miss
        self.split_streak = 0  # Reset split streak on miss

    def activate_black_hole(self):
        """Activate the black hole power-up"""
        self.black_hole_active = True
        self.black_hole_timer = FPS * 10  # 10 seconds
        self.split_streak = 0  # Reset split streak

    def add_blue_ball(self):
        """Add a blue power-up ball"""
        # Find a good position for the blue ball
        attempts = 0
        while attempts < 50:
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(
                50, CIRCLE_RADIUS - BLUE_BALL_RADIUS - 20)
            x = CIRCLE_CENTER[0] + math.cos(angle) * distance
            y = CIRCLE_CENTER[1] + math.sin(angle) * distance

            # Check if position is clear
            valid_position = True
            for ball in self.balls:
                if math.sqrt((x - ball.x) ** 2 + (y - ball.y) ** 2) < (BLUE_BALL_RADIUS + ball.radius + 10):
                    valid_position = False
                    break

            if valid_position:
                self.balls.append(Ball(x, y, is_blue=True))
                break

            attempts += 1

    def add_green_ball(self):
        """Add a green power-up ball"""
        # Find a good position for the green ball
        attempts = 0
        while attempts < 50:
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(
                50, CIRCLE_RADIUS - GREEN_BALL_RADIUS - 20)
            x = CIRCLE_CENTER[0] + math.cos(angle) * distance
            y = CIRCLE_CENTER[1] + math.sin(angle) * distance

            # Check if position is clear
            valid_position = True
            for ball in self.balls:
                if math.sqrt((x - ball.x) ** 2 + (y - ball.y) ** 2) < (GREEN_BALL_RADIUS + ball.radius + 10):
                    valid_position = False
                    break

            if valid_position:
                self.balls.append(Ball(x, y, is_green=True))
                break

            attempts += 1

    def add_random_ball(self):
        """Add a random regular ball"""
        attempts = 0
        while attempts < 50:
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(30, CIRCLE_RADIUS - BALL_RADIUS - 20)
            x = CIRCLE_CENTER[0] + math.cos(angle) * distance
            y = CIRCLE_CENTER[1] + math.sin(angle) * distance

            # Check if position is clear
            valid_position = True
            for ball in self.balls:
                if math.sqrt((x - ball.x) ** 2 + (y - ball.y) ** 2) < (BALL_RADIUS + ball.radius + 5):
                    valid_position = False
                    break

            if valid_position:
                self.balls.append(Ball(x, y))
                break

            attempts += 1

    def create_hit_effect(self, x, y, ball):
        """Create smoky particle effect when ball is hit"""
        # Determine effect color based on ball type
        if ball.is_blue:
            effect_color = BLUE
            num_particles = 8
        elif ball.is_green:
            effect_color = GREEN
            num_particles = 12  # More particles for green balls
        else:
            effect_color = SMOKE_GRAY
            num_particles = 6

        # Create smoke particles
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 3)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            life = random.randint(15, 30)
            size = random.randint(2, 4)

            particle = Particle(x, y, vx, vy, effect_color, life, size)
            self.particles.append(particle)

    def create_miss_effect(self, x, y):
        """Create subtle red ring effect for missed clicks"""
        self.miss_effect_timer = 20  # Effect duration in frames
        self.miss_effect_pos = (x, y)

        # Create red particles for miss effect
        for _ in range(4):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.5, 1.5)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            life = random.randint(10, 20)
            size = random.randint(1, 9)

            particle = Particle(x, y, vx, vy, RED, life, size)
            self.particles.append(particle)

    def toggle_death_mode(self):
        """Toggle death mode on/off"""
        self.death_mode = not self.death_mode
        self.missed_clicks = 0  # Reset missed clicks when toggling

    def handle_ball_collisions(self):
        """Handle elastic ball-to-ball collisions"""
        for i, ball1 in enumerate(self.balls):
            for j, ball2 in enumerate(self.balls[i+1:], i+1):
                dx = ball2.x - ball1.x
                dy = ball2.y - ball1.y
                distance = math.sqrt(dx * dx + dy * dy)
                min_distance = ball1.radius + ball2.radius

                if distance <= min_distance:
                    if distance == 0:
                        # Balls are exactly on top of each other - separate randomly
                        angle = random.uniform(0, 2 * math.pi)
                        dx = math.cos(angle)
                        dy = math.sin(angle)
                        distance = 0.1

                    # Normalize collision vector
                    nx = dx / distance
                    ny = dy / distance

                    # Separate balls to prevent overlap
                    overlap = min_distance - distance
                    separation = overlap * 0.5 + 1  # Add 1px buffer

                    ball1.x -= nx * separation
                    ball1.y -= ny * separation
                    ball2.x += nx * separation
                    ball2.y += ny * separation

                    # Keep balls inside the circle
                    self.keep_ball_in_bounds(ball1)
                    self.keep_ball_in_bounds(ball2)

                    # Calculate relative velocity along collision normal
                    dvx = ball2.vx - ball1.vx
                    dvy = ball2.vy - ball1.vy
                    dvn = dvx * nx + dvy * ny

                    # Only resolve if objects are approaching
                    if dvn > 0:
                        continue

                    # Perfect elastic collision (equal mass assumed)
                    # Exchange velocity components along collision normal
                    ball1.vx += dvn * nx
                    ball1.vy += dvn * ny
                    ball2.vx -= dvn * nx
                    ball2.vy -= dvn * ny

                    # Maintain consistent speeds after collision
                    ball1.normalize_speed()
                    ball2.normalize_speed()

    def keep_ball_in_bounds(self, ball):
        """Ensure ball stays within the circle boundary"""
        dx = ball.x - CIRCLE_CENTER[0]
        dy = ball.y - CIRCLE_CENTER[1]
        distance = math.sqrt(dx * dx + dy * dy)

        if distance + ball.radius > CIRCLE_RADIUS:
            if distance > 0:
                # Move ball back inside
                factor = (CIRCLE_RADIUS - ball.radius - 2) / distance
                ball.x = CIRCLE_CENTER[0] + dx * factor
                ball.y = CIRCLE_CENTER[1] + dy * factor

    def check_game_over(self):
        """Check if the circle is too crowded with balls"""
        if len(self.balls) > 80:  # Lower threshold due to smaller balls
            self.game_over = True
            pygame.mixer.Sound.play(gameover_sound)  # Play game over sound

        # Alternative: check if balls are too densely packed
        total_ball_area = sum(math.pi * ball.radius **
                              2 for ball in self.balls)
        circle_area = math.pi * CIRCLE_RADIUS ** 2

        if total_ball_area > circle_area * 0.6:  # 60% filled for better gameplay
            self.game_over = True
            pygame.mixer.Sound.play(gameover_sound)  # Play game over sound

    def update(self):
        if self.game_over or self.win:
            return

        # Update all balls
        for ball in self.balls:
            ball.update()

        # Handle ball collisions
        self.handle_ball_collisions()

        # Maintain consistent speeds for all balls
        for ball in self.balls:
            ball.normalize_speed()

        # Update particles
        self.particles = [p for p in self.particles if p.update()]

        # Update miss effect timer
        if self.miss_effect_timer > 0:
            self.miss_effect_timer -= 1

        # Handle black hole
        if self.black_hole_active:
            self.handle_black_hole()
            self.black_hole_timer -= 1
            if self.black_hole_timer <= 0:
                self.black_hole_active = False

        # Check game over condition
        self.check_game_over()

    def handle_black_hole(self):
        """Handle the black hole effect: remove balls close to the center"""
        black_hole_radius = 25  # Radius of the black hole effect
        balls_to_remove = []
        for ball in self.balls:
            dx = ball.x - CIRCLE_CENTER[0]
            dy = ball.y - CIRCLE_CENTER[1]
            distance = math.sqrt(dx * dx + dy * dy)
            if distance < black_hole_radius:
                balls_to_remove.append(ball)

        for ball in balls_to_remove:
            self.balls.remove(ball)
            self.ball_count -= 1
            self.score += 5  # Award points for balls consumed by black hole

    def draw(self):
        ocean_blue = (70, 130, 180)  # Define ocean blue color
        self.screen.fill(ocean_blue)

        # --- Draw Background Image (Example) ---
        # self.screen.blit(background_image, (0, 0))

        # Draw the boundary circle
        circle_color = LIGHT_GRAY  # Change this color
        pygame.draw.circle(self.screen, circle_color,
                           CIRCLE_CENTER, CIRCLE_RADIUS, 3)

        # Draw black hole
        if self.black_hole_active:
            # Obsidian Abyss: A swirling vortex of deep, shadowy blues and purples
            black_hole_color = (
                random.randint(0, 50),  # Deep blue hues
                random.randint(0, 20),  # Hints of purple
                random.randint(30, 70)   # Shadowy undertones
            )
            pygame.draw.circle(
                self.screen, black_hole_color, CIRCLE_CENTER, 25)
        # Draw all balls
        for ball in self.balls:
            ball.draw(self.screen)

        # Draw particles (smoke effects)
        for particle in self.particles:
            particle.draw(self.screen)

        # Draw miss effect (subtle red ring)
        if self.miss_effect_timer > 0:
            alpha = int(255 * (self.miss_effect_timer / 20))
            if alpha > 0:
                # Create expanding red ring
                ring_size = int(15 * (1 - self.miss_effect_timer / 20))
                if ring_size > 0:
                    miss_surface = pygame.Surface(
                        (ring_size * 4, ring_size * 4), pygame.SRCALPHA)
                    color_with_alpha = (*RED, alpha // 2)
                    pygame.draw.circle(
                        miss_surface, color_with_alpha, (ring_size * 2, ring_size * 2), ring_size, 2)
                    self.screen.blit(
                        miss_surface, (self.miss_effect_pos[0] - ring_size * 2, self.miss_effect_pos[1] - ring_size * 2))

        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (5, 10))

        count_text = self.small_font.render(
            f"Clicks: {self.ball_count}", True, WHITE)
        self.screen.blit(count_text, (5, 50))

        next_blue = 5 - (self.ball_count %
                         10) if self.ball_count % 5 != 0 else 5
        blue_text = self.small_font.render(
            f"Next blue ball in: {next_blue} clicks", True, BLUE)
        self.screen.blit(blue_text, (5, 75))

        # Death mode indicator
        mode_text = self.small_font.render(
            f"Death Mode: {'ON' if self.death_mode else 'OFF'} \n(Press D to toggle)", True, RED if self.death_mode else WHITE)
        self.screen.blit(mode_text, (5, 100))

        if self.death_mode:
            missed_text = self.small_font.render(
                f"Missed clicks: {self.missed_clicks}", True, RED)
            self.screen.blit(missed_text, (5, 125))

        # Black hole indicator
        if self.black_hole_active:
            black_hole_timer_text = self.small_font.render(
                f"Black Hole Active: {self.black_hole_timer // FPS} seconds", True, GRAY)
            self.screen.blit(black_hole_timer_text, (5, 150))

        # Instructions
        instruction1 = self.small_font.render(
            "Click balls to split them", True, WHITE)
        instruction2 = self.small_font.render(
            "Blue balls reduce by half!", True, BLUE)
        if self.death_mode:
            instruction3 = self.small_font.render(
                "Green balls add 6 balls!", True, GREEN)
            instruction4 = self.small_font.render(
                "Missed clicks add 3 balls!", True, RED)
        else:
            instruction3 = self.small_font.render(
                "Press D for Death Mode!", True, YELLOW)
            instruction4 = self.small_font.render(
                "Don't let the circle fill up!", True, RED)

        self.screen.blit(instruction1, (WIDTH - 250, 10))
        self.screen.blit(instruction2, (WIDTH - 250, 35))
        self.screen.blit(instruction3, (WIDTH - 250, 60))
        self.screen.blit(instruction4, (WIDTH - 250, 85))

        if self.game_over:
            if self.death_mode:
                game_over_text = self.font.render(
                    f"DEATH MODE DEFEAT! Missed {self.missed_clicks} clicks!", True, RED)
            else:
                game_over_text = self.font.render(
                    "GAME OVER! Circle is full!", True, RED)
            restart_text = self.small_font.render(
                "Press R to restart", True, WHITE)
            high_score_text = self.small_font.render(
                f"High Score: {self.high_score}", True, YELLOW)

            text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            restart_rect = restart_text.get_rect(
                center=(WIDTH//2, HEIGHT//2 + 40))
            high_score_rect = high_score_text.get_rect(
                center=(WIDTH//2, HEIGHT//2 + 80))

            # Draw background for text
            pygame.draw.rect(self.screen, BLACK, text_rect.inflate(20, 10))
            pygame.draw.rect(self.screen, BLACK, restart_rect.inflate(20, 10))
            pygame.draw.rect(self.screen, BLACK,
                             high_score_rect.inflate(20, 10))

            self.screen.blit(game_over_text, text_rect)
            self.screen.blit(restart_text, restart_rect)
            self.screen.blit(high_score_text, high_score_rect)

            # Save high score if needed
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()

        pygame.display.flip()

    def restart_game(self):
        death_mode_state = self.death_mode  # Preserve death mode setting
        self.__init__()
        self.death_mode = death_mode_state
        self.particles = []  # Clear any remaining particles
        self.miss_effect_timer = 0

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
