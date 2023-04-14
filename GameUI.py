from tkinter import Tk, Canvas, Label
import random

class SnakeModel:
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.body = [
            [200, 200],
            [200, 210],
            [200, 220],
            [200, 230]
        ]
        self.direction = "Up"
        self.fruit = [0, 0]
        self.set_fruit_position()

    def set_fruit_position(self):
        x = random.randint(10, 390)
        y = random.randint(10, 390)
        xd = x % 10
        yd = y % 10
        x = x - xd
        y = y - yd
        self.fruit = [x, y]

    def move_body_parts(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

    def eat_fruit(self):
        if self.fruit[0] == self.body[0][0] and self.fruit[1] == self.body[0][1]:
            self.body.append([self.body[-1][0], self.body[-1][1]])
            self.set_fruit_position()
            self.score += 100
            score.config(text=f"Score: {self.score}")

    def check_game_over(self):
        if self.body[0][0] < 0 or self.body[0][0] > 390 or self.body[0][1] < 0 or self.body[0][1] > 390:
            self.lives -= 1
            if self.lives == 0:
                print("Game Over!")
                exit()
            else:
                self.body[0][0] %= 400
                self.body[0][1] %= 400
                lives_label.config(text=f"Lives: {self.lives}")

        for i in range(1, len(self.body)):
            if self.body[0] == self.body[i]:
                self.lives -= 1
                if self.lives == 0:
                    print("Game Over!")
                    exit()
                else:
                    self.lives -= 1
                    lives_label.config(text=f"Lives: {self.lives}")

    def move_up(self):
        if self.direction != "Down":
            self.move_body_parts()
            self.body[0][1] -= 10
            self.direction = "Up"
            self.eat_fruit()
            self.check_game_over()

    def move_down(self):
        if self.direction != "Up":
            self.move_body_parts()
            self.body[0][1] += 10
            self.direction = "Down"
            self.eat_fruit()
            self.check_game_over()

    def move_left(self):
        if self.direction != "Right":
            self.move_body_parts()
            self.body[0][0] -= 10
            self.direction = "Left"
            self.eat_fruit()
            self.check_game_over()

    def move_right(self):
        if self.direction != "Left":
            self.move_body_parts()
            self.body[0][0] += 10
            self.direction = "Right"
            self.eat_fruit()
            self.check_game_over()


if __name__ == '__main__':
    model = SnakeModel()
    print(model.body)
    model.move_up()
    print(model.body)


def key_pressed(e):
    key = e.keysym
    if key == "Down":
        model.move_down()
    elif key == "Up":
        model.move_up()
    elif key == "Left":
        model.move_left()
    elif key == "Right":
        model.move_right()
    canvas.delete("all")
    display_snake()
    canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")


def display_snake():
    for bp in model.body:
        canvas.create_rectangle(bp[0], bp[1], bp[0] + 10, bp[1] + 10, fill="green")


window = Tk()
model = SnakeModel()

canvas = Canvas(window, bg="white", width=400, height=400)
canvas.grid(row=0, column=0)
score = Label(text = f"Score: {model.score}")
score.grid(row=1, column=0)


display_snake()
lives_label = Label(text=f"Lives: {model.lives}")
lives_label.grid(row=2, column=0)
canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")
window.bind('<KeyRelease>', key_pressed)

window.mainloop()
