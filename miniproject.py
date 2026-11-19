import tkinter as tk
import random

# =========================
# WINDOW
# =========================

root = tk.Tk()
root.title("TIME FREEZE")
root.resizable(False, False)

WIDTH = 700
HEIGHT = 600

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#10152b"
)
canvas.pack()

# =========================
# GAME VARIABLES
# =========================

score = 0
lives = 3
level = 1

freeze_energy = 100
freeze_active = False
game_running = True

player_speed = 15

enemies = []
crystals = []

# =========================
# INFORMATION
# =========================

score_text = canvas.create_text(
    80, 25,
    text="Score: 0",
    fill="white",
    font=("Arial", 16, "bold")
)

lives_text = canvas.create_text(
    250, 25,
    text="Lives: 3",
    fill="white",
    font=("Arial", 16, "bold")
)

level_text = canvas.create_text(
    400, 25,
    text="Level: 1",
    fill="white",
    font=("Arial", 16, "bold")
)

energy_text = canvas.create_text(
    570, 25,
    text="Freeze: 100%",
    fill="cyan",
    font=("Arial", 16, "bold")
)

# ================== =======
# PLAYER
# =========================

player = canvas.create_oval(
    335, 500,
    365, 530,
    fill="cyan",
    outline="white",
    width=2
)

# ============== ===========
# EXIT
# =========================

exit_door = canvas.create_rectangle(
    320, 60,
    380, 110,
    fill="purple",
    outline="white",
    width=3
)

canvas.create_text(
    350, 85,
    text="EXIT",
    fill="white",
    font=("Arial", 12, "bold")
)

# =========================
# WALLS
# =========================

walls = [
    (100, 150, 300, 175),
    (400, 150, 600, 175),
    (100, 300, 250, 325),
    (450, 300, 600, 325),
    (250, 420, 450, 445)
]

for wall in walls:
    canvas.create_rectangle(
        wall,
        fill="#394867",
        outline="#7189aa"
    )

# =========================
# CREATE CRYSTALS
# =========================

def create_crystals():
    global crystals

    crystals.clear()

    positions = [
        (150, 100),
        (550, 100),
        (150, 250),
        (550, 250),
        (350, 380)
    ]

    for x, y in positions:
        crystal = canvas.create_text(
            x,
            y,
            text="*",
            fill="cyan",
            font=("Arial", 30, "bold")
        )

        crystals.append(crystal)


# =========================
# CREATE ENEMIES
# =========================

def create_enemies():
    global enemies

    enemies.clear()

    number = 3 + level

    for i in range(number):
        x = random.randint(100, 600)
        y = random.randint(120, 500)

        enemy = canvas.create_oval(
            x,
            y,
            x + 25,
            y + 25,
            fill="red",
            outline="orange"
        )

        enemies.append(enemy)


# =========================
# COLLISION
# =========================

def touching(item1, item2):

    box1 = canvas.bbox(item1)
    box2 = canvas.bbox(item2)

    if box1 is None or box2 is None:
        return False

    return (
        box1[0] < box2[2]
        and box1[2] > box2[0]
        and box1[1] < box2[3]
        and box1[3] > box2[1]
    )


# =========================
# WALL COLLISION
# =========================

def wall_collision():

    px1, py1, px2, py2 = canvas.coords(player)

    for wall in walls:

        wx1, wy1, wx2, wy2 = wall

        if (
            px1 < wx2
            and px2 > wx1
            and py1 < wy2
            and py2 > wy1
        ):
            return True

    return False


# =========================
# PLAYER MOVEMENT
# =========================

def move_player(dx, dy):

    if not game_running:
        return

    canvas.move(player, dx, dy)

    x1, y1, x2, y2 = canvas.coords(player)

    # Screen boundaries

    if x1 < 10:
        canvas.move(player, 10 - x1, 0)

    if x2 > WIDTH - 10:
        canvas.move(player, WIDTH - 10 - x2, 0)

    if y1 < 45:
        canvas.move(player, 0, 45 - y1)

    if y2 > HEIGHT - 10:
        canvas.move(player, 0, HEIGHT - 10 - y2)

    # Wall collision

    if wall_collision():
        canvas.move(player, -dx, -dy)

    check_crystals()
    check_exit()
    check_enemies()


# =========================
# CRYSTAL COLLECTION
# =========================

def check_crystals():

    global score
    global freeze_energy

    for crystal in crystals[:]:

        if touching(player, crystal):

            canvas.delete(crystal)
            crystals.remove(crystal)

            score += 20
            freeze_energy += 20

            if freeze_energy > 100:
                freeze_energy = 100

            canvas.itemconfig(
                score_text,
                text="Score: " + str(score)
            )

            update_energy()


# =========================
# EXIT
# =========================

def check_exit():

    global level

    if len(crystals) > 0:
        return

    if touching(player, exit_door):

        level += 1

        canvas.itemconfig(
            level_text,
            text="Level: " + str(level)
        )

        reset_level()


# =========================
# RESET LEVEL
# =========================

def reset_level():

    global freeze_energy

    canvas.coords(
        player,
        335, 500,
        365, 530
    )

    freeze_energy = 100

    update_energy()

    create_crystals()
    create_enemies()


# =========================
# ENEMY MOVEMENT
# =========================

def move_enemies():

    if not game_running:
        return

    if not freeze_active:

        for enemy in enemies:

            direction = random.choice(
                ["left", "right", "up", "down"]
            )

            if direction == "left":
                canvas.move(enemy, -8, 0)

            elif direction == "right":
                canvas.move(enemy, 8, 0)

            elif direction == "up":
                canvas.move(enemy, 0, -8)

            else:
                canvas.move(enemy, 0, 8)

            # Keep enemy inside screen

            x1, y1, x2, y2 = canvas.coords(enemy)

            if x1 < 10:
                canvas.move(enemy, 10 - x1, 0)

            if x2 > WIDTH - 10:
                canvas.move(
                    enemy,
                    WIDTH - 10 - x2,
                    0
                )

            if y1 < 45:
                canvas.move(enemy, 0, 45 - y1)

            if y2 > HEIGHT - 10:
                canvas.move(
                    enemy,
                    0,
                    HEIGHT - 10 - y2
                )

    check_enemies()

    root.after(150, move_enemies)


# =========================
# ENEMY COLLISION
# =========================

def check_enemies():

    global lives

    for enemy in enemies:

        if touching(player, enemy):

            lives -= 1

            canvas.itemconfig(
                lives_text,
                text="Lives: " + str(lives)
            )

            canvas.coords(
                player,
                335, 500,
                365, 530
            )

            if lives <= 0:
                game_over()

            break


# =========================
# TIME FREEZE
# =========================

def freeze_time(event=None):

    global freeze_active

    if not game_running:
        return

    if freeze_energy <= 0:
        return

    freeze_active = not freeze_active

    if freeze_active:
        canvas.itemconfig(
            energy_text,
            fill="yellow"
        )
    else:
        canvas.itemconfig(
            energy_text,
            fill="cyan"
        )


# =========================
# FREEZE ENERGY
# =========================

def update_energy():

    canvas.itemconfig(
        energy_text,
        text="Freeze: " + str(int(freeze_energy)) + "%"
    )


def use_energy():

    global freeze_energy
    global freeze_active

    if game_running and freeze_active:

        freeze_energy -= 1

        if freeze_energy <= 0:
            freeze_energy = 0
            freeze_active = False

    update_energy()

    root.after(100, use_energy)


# =========================
# GAME OVER
# =========================

def game_over():

    global game_running

    game_running = False

    canvas.create_rectangle(
        170, 220,
        530, 400,
        fill="black",
        outline="red",
        width=4
    )

    canvas.create_text(
        350, 270,
        text="GAME OVER",
        fill="red",
        font=("Arial", 35, "bold")
    )

    canvas.create_text(
        350, 320,
        text="Score: " + str(score),
        fill="white",
        font=("Arial", 20, "bold")
    )

    canvas.create_text(
        350, 360,
        text="Press R to Restart",
        fill="yellow",
        font=("Arial", 16)
    )


# =========================
# RESTART
# =========================

def restart(event=None):

    global score
    global lives
    global level
    global freeze_energy
    global freeze_active
    global game_running

    score = 0
    lives = 3
    level = 1
    freeze_energy = 100
    freeze_active = False
    game_running = True

    canvas.delete("all")

    # Background

    canvas.create_rectangle(
        0, 0,
        WIDTH, HEIGHT,
        fill="#10152b"
    )

    # Player

    global player

    player = canvas.create_oval(
        335, 500,
        365, 530,
        fill="cyan",
        outline="white",
        width=2
    )

    # Exit

    global exit_door

    exit_door = canvas.create_rectangle(
        320, 60,
        380, 110,
        fill="purple",
        outline="white",
        width=3
    )

    canvas.create_text(
        350, 85,
        text="EXIT",
        fill="white",
        font=("Arial", 12, "bold")
    )

    # Walls

    for wall in walls:
        canvas.create_rectangle(
            wall,
            fill="#394867",
            outline="#7189aa"
        )

    # Information

    global score_text
    global lives_text
    global level_text
    global energy_text

    score_text = canvas.create_text(
        80, 25,
        text="Score: 0",
        fill="white",
        font=("Arial", 16, "bold")
    )

    lives_text = canvas.create_text(
        250, 25,
        text="Lives: 3",
        fill="white",
        font=("Arial", 16, "bold")
    )

    level_text = canvas.create_text(
        400, 25,
        text="Level: 1",
        fill="white",
        font=("Arial", 16, "bold")
    )

    energy_text = canvas.create_text(
        570, 25,
        text="Freeze: 100%",
        fill="cyan",
        font=("Arial", 16, "bold")
    )

    create_crystals()
    create_enemies()


# =========================
# CONTROLS
# =========================

root.bind(
    "<Left>",
    lambda event: move_player(-player_speed, 0)
)

root.bind(
    "<Right>",
    lambda event: move_player(player_speed, 0)
)

root.bind(
    "<Up>",
    lambda event: move_player(0, -player_speed)
)

root.bind(
    "<Down>",
    lambda event: move_player(0, player_speed)
)

root.bind("<space>", freeze_time)
root.bind("<r>", restart)
root.bind("<R>", restart)

# =========================
# START
# =========================

create_crystals()
create_enemies()

move_enemies()
use_energy()

root.mainloop()
