import pygame
import random
import psycopg2
import sys
from datetime import datetime

def connect_db():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="akzhan11",
        host="localhost",
        port="5432"
    )
def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn =connect_db()
    cur =conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    row =cur.fetchone()
    if row:
        user_id = row[0]
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY updated_at DESC LIMIT 1", (user_id,))
        data = cur.fetchone()
        cur.close()
        conn.close()
        if data:
            return user_id, data[0], data[1]
        return user_id, 0, 1
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, 0, 1)", (user_id,))
        conn.commit()
        cur.close()
        conn.close()
        return user_id, 0, 1

def save_progress(user_id, score, level):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, score, level, updated_at) VALUES (%s, %s, %s, %s)",
                (user_id, score, level, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Enhanced")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 28)
colors = {
    "bg": (0, 0, 0),
    "snake": (0, 255, 0),
    "food": {1: (0, 255, 0), 2: (0, 100, 255), 3: (255, 255, 0)},
    "text": (255, 255, 255),
    "wall": (100, 100, 100)
}
def draw_text(text, x, y):
    img = font.render(text, True, colors["text"])
    screen.blit(img, (x, y))
def generate_food(snake):
    while True:
        x = random.randint(0, WIDTH // CELL - 1) * CELL
        y = random.randint(0, HEIGHT // CELL - 1) * CELL
        if (x, y) not in snake:
            weight = random.choice([1, 2, 3])
            return {"pos": (x, y), "weight": weight, "spawn": pygame.time.get_ticks()}

def get_walls(level):
    if level == 2:
        return [(x, 200) for x in range(0, WIDTH, CELL)]
    elif level == 3:
        return [(300, y) for y in range(0, HEIGHT, CELL)]
    elif level >= 4:
        return [(x, x) for x in range(0, WIDTH, CELL)]
    return []
def main():
    create_tables()
    username = input("Enter your name: ")
    user_id, score, level = get_or_create_user(username)
    speed = 10 + (level - 1) * 2

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    food = generate_food(snake)
    paused = False
    running = True

    while running:
        screen.fill(colors["bg"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_progress(user_id, score, level)
                        print("Paused. Progress saved.")
                elif not paused:
                    if event.key == pygame.K_UP and direction != "DOWN":
                        direction = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        direction = "DOWN"
                    elif event.key == pygame.K_LEFT and direction != "RIGHT":
                        direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        direction = "RIGHT"

        if not paused:
            head_x, head_y = snake[0]
            if direction == "UP":
                head_y -= CELL
            elif direction == "DOWN":
                head_y += CELL
            elif direction == "LEFT":
                head_x -= CELL
            elif direction == "RIGHT":
                head_x += CELL
            new_head = (head_x, head_y)

            if new_head in snake or head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
                break

            walls = get_walls(level)
            if new_head in walls:
                break

            snake.insert(0, new_head)

            if new_head == food["pos"]:
                score += food["weight"]
                if score % 5 == 0:
                    level += 1
                    speed += 1
                food = generate_food(snake)
            else:
                snake.pop()

            for wall in walls:
                pygame.draw.rect(screen, colors["wall"], (wall[0], wall[1], CELL, CELL))
            for segment in snake:
                pygame.draw.rect(screen, colors["snake"], (segment[0], segment[1], CELL, CELL))
            pygame.draw.rect(screen, colors["food"][food["weight"]], (*food["pos"], CELL, CELL))

            if pygame.time.get_ticks() - food["spawn"] > 5000:
                food = generate_food(snake)

            draw_text(f"Score: {score}", 10, 10)
            draw_text(f"Level: {level}", 10, 30)

        pygame.display.update()
        clock.tick(speed)

    save_progress(user_id, score, level)
    pygame.quit()
    print("Game over. Final score:", score)
if __name__ == "__main__":
    main()
