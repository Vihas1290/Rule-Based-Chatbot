import arcade

MOVEMENT_SPEED = 5
WALL_SPEED = 2
WALL_TOP = 550
WALL_BOTTOM = 100


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "My Game")
        self.player_list = None
        self.player = None
        self.wall_list = None
        self.wall = None
        self.prize_list = None
        self.prize = None
        self.wall_direction = 1  # 1 = moving up, -1 = moving down

    def setup(self):
        # Player
        self.player_list = arcade.SpriteList()
        self.player = arcade.Sprite("image.png", scale=0.5)
        self.player.center_x = 400
        self.player.center_y = 300
        self.player_list.append(self.player)

        # Wall
        self.wall_list = arcade.SpriteList()
        self.wall = arcade.Sprite("wall.png", scale=0.5)
        self.wall.center_x = 600
        self.wall.center_y = 300
        self.wall_list.append(self.wall)

        # Prize
        self.prize_list = arcade.SpriteList()
        self.prize = arcade.Sprite("prize.png", scale=0.5)
        self.prize.center_x = 750
        self.prize.center_y = 300
        self.prize_list.append(self.prize)

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.wall_list.draw()
        self.prize_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()

        # Keep player inside the window
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.left < 0:
            self.player.left = 0

        # Move wall up/down, bounce at bounds
        self.wall.center_y += WALL_SPEED * self.wall_direction
        if self.wall.center_y >= WALL_TOP:
            self.wall_direction = -1
        elif self.wall.center_y <= WALL_BOTTOM:
            self.wall_direction = 1

        # Win: player touches prize
        if arcade.check_for_collision_with_list(self.player, self.prize_list):
            print("You win!")
            arcade.close_window()
            return

        # Lose: player touches wall
        if arcade.check_for_collision_with_list(self.player, self.wall_list):
            print("You hit the wall — game over.")
            arcade.close_window()
            return

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.B:
            self.player.width *= 1.5
            self.player.height *= 1.5

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.W, arcade.key.S):
            self.player.change_y = 0
        elif key in (arcade.key.A, arcade.key.D):
            self.player.change_x = 0
        elif key == arcade.key.B:
            self.player.width /= 1.5
            self.player.height /= 1.5

    def on_mouse_press(self, x, y, button, modifiers):
        self.player.angle = 45

    def on_mouse_release(self, x, y, button, modifiers):
        self.player.angle = 0


window = MyGame()
window.setup()
arcade.run()