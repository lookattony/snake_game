import tkinter
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPACE_SIZE = 20
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
SNAKE_INITIAL_LENGTH = 3

game = tkinter.Tk()
game.title("Snake Game")

canvas = tkinter.Canvas(game, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

score = 0
score_label = tkinter.Label(game, text=f"Score: {score}", font=('Terminal', 20))
score_label.pack()

snake = [(0, 0)] * SNAKE_INITIAL_LENGTH
snake_direction = "right"
for x, y in snake:
    canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")

def place_food():
    x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
    y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
    return x, y

food_position = place_food()
canvas.create_rectangle(food_position[0], food_position[1], food_position[0] + SPACE_SIZE, food_position[1] + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def change_direction(new_direction):
    global snake_direction
    if new_direction == "left" and snake_direction != "right":
        snake_direction = "left"
    elif new_direction == "right" and snake_direction != "left":
        snake_direction = "right"
    elif new_direction == "up" and snake_direction != "down":
        snake_direction = "up"
    elif new_direction == "down" and snake_direction != "up":
        snake_direction = "down"

def move_snake():
    global snake, food_position, score
    head_x, head_y = snake[0]

    if snake_direction == "left":
        head_x -= SPACE_SIZE
    elif snake_direction == "right":
        head_x += SPACE_SIZE
    elif snake_direction == "up":
        head_y -= SPACE_SIZE
    elif snake_direction == "down":
        head_y += SPACE_SIZE

    new_head = (head_x, head_y)

    if head_x < 0 or head_x >= GAME_WIDTH or head_y < 0 or head_y >= GAME_HEIGHT or new_head in snake:
        game_over()
        return

    snake = [new_head] + snake[:-1]

    if new_head == food_position:
        snake.append(snake[-1])
        canvas.delete("food")
        food_position = place_food()
        canvas.create_rectangle(food_position[0], food_position[1], food_position[0] + SPACE_SIZE, food_position[1] + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
        score += 1
        score_label.config(text=f"Score: {score}")

    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")

    game.after(100, move_snake)

def game_over():
    canvas.delete("all")
    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, text="GAME OVER", fill="red", font=('Terminal', 40))

game.bind("<Left>", lambda event: change_direction("left"))
game.bind("<Right>", lambda event: change_direction("right"))
game.bind("<Up>", lambda event: change_direction("up"))
game.bind("<Down>", lambda event: change_direction("down"))

move_snake()
game.mainloop()
