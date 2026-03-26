import pygame
import sys
import math
import time
import random

pygame.init()

# ── Window ───────────────────────────────────────────────────────────────
BOARD_SIZE  = 540
PANEL_WIDTH = 280
WIN_W       = BOARD_SIZE + PANEL_WIDTH
WIN_H       = BOARD_SIZE
CELL        = BOARD_SIZE // 3

screen = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("✦ TIC TAC TOE  ·  Liquid Glass Edition ✦")
clock = pygame.time.Clock()

# ── Palette: liquid lilac glass ──────────────────────────────────────────
BG_DEEP      = ( 15,   8,  35)
BG_MID       = ( 28,  14,  60)
LILAC_DARK   = ( 60,  20, 110)
LILAC_MID    = (110,  50, 180)
LILAC_LIGHT  = (160,  90, 230)
LILAC_BRIGHT = (200, 140, 255)
GLASS_WHITE  = (230, 210, 255, 60)
GLASS_EDGE   = (200, 160, 255, 120)
GLOW_PURPLE  = (180, 100, 255)
GLOW_SOFT    = (130,  70, 200)

X_BASE       = ( 30, 140, 255)   # blue
X_GLASS      = ( 80, 180, 255, 180)
X_GLOW       = (120, 200, 255)
O_BASE       = (220,  50,  80)   # red
O_GLASS      = (255, 100, 130, 180)
O_GLOW       = (255, 140, 160)

WIN_CORE     = (160,  60, 220)
WIN_GLOW_C   = (220, 140, 255)
WIN_TIP      = (255, 255, 255)

TEXT_BRIGHT  = (230, 210, 255)
TEXT_MID     = (170, 130, 220)
TEXT_DIM     = (110,  80, 160)

# ── Fonts ────────────────────────────────────────────────────────────────
try:
    FONT_TITLE  = pygame.font.SysFont("Segoe UI",    30, bold=True)
    FONT_SCORE  = pygame.font.SysFont("Segoe UI",    22, bold=True)
    FONT_LABEL  = pygame.font.SysFont("Segoe UI",    15)
    FONT_SUB    = pygame.font.SysFont("Segoe UI",    13)
    FONT_BIG    = pygame.font.SysFont("Segoe UI",    44, bold=True)
    FONT_INPUT  = pygame.font.SysFont("Consolas",    17, bold=True)
    FONT_PROMPT = pygame.font.SysFont("Consolas",    14)
except:
    FONT_TITLE  = pygame.font.Font(None, 32)
    FONT_SCORE  = pygame.font.Font(None, 24)
    FONT_LABEL  = pygame.font.Font(None, 17)
    FONT_SUB    = pygame.font.Font(None, 15)
    FONT_BIG    = pygame.font.Font(None, 46)
    FONT_INPUT  = pygame.font.Font(None, 19)
    FONT_PROMPT = pygame.font.Font(None, 16)


# ── Background with starfield ────────────────────────────────────────────
STARS = [(random.randint(0, WIN_W), random.randint(0, WIN_H),
          random.uniform(0.3, 1.0)) for _ in range(120)]

def draw_background():
    screen.fill(BG_DEEP)
    # gradient overlay
    grad = pygame.Surface((WIN_W, WIN_H), pygame.SRCALPHA)
    for y in range(WIN_H):
        t   = y / WIN_H
        r   = int(15 + t * 13)
        g   = int( 8 + t *  6)
        b   = int(35 + t * 25)
        pygame.draw.line(grad, (r, g, b, 180), (0, y), (WIN_W, y))
    screen.blit(grad, (0, 0))
    # stars
    t = time.time()
    for sx, sy, br in STARS:
        pulse = 0.5 + 0.5 * math.sin(t * br * 2 + sx)
        a     = int(60 + 140 * pulse * br)
        r     = int(1 + br)
        s     = pygame.Surface((r*2+2, r*2+2), pygame.SRCALPHA)
        pygame.draw.circle(s, (220, 200, 255, a), (r+1, r+1), r)
        screen.blit(s, (sx - r, sy - r))


# ── Glass panel helper ───────────────────────────────────────────────────
def draw_glass_rect(surface, rect, color=(110,50,180), alpha=55, radius=18,
                    edge_color=(200,160,255), edge_alpha=100, edge_w=2):
    x, y, w, h = rect
    # fill
    s = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(s, (*color, alpha), (0, 0, w, h), border_radius=radius)
    # subtle inner gradient (lighter top)
    top = pygame.Surface((w, h//2), pygame.SRCALPHA)
    top.fill((255, 255, 255, 18))
    pygame.draw.rect(top, (0,0,0,0), (0, 0, w, h//2), border_radius=radius)
    s.blit(top, (0, 0))
    surface.blit(s, (x, y))
    # edge
    e = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(e, (*edge_color, edge_alpha), (0, 0, w, h), edge_w, border_radius=radius)
    surface.blit(e, (x, y))


# ── Centered text ────────────────────────────────────────────────────────
def draw_centered_text(surface, text, font, color, cx, y, glow=False):
    if glow:
        for dx, dy in [(-1,-1),(1,-1),(-1,1),(1,1),(0,-2),(0,2),(-2,0),(2,0)]:
            gs = font.render(text, True, (*color[:3],))
            gsurf = pygame.Surface(gs.get_size(), pygame.SRCALPHA)
            gsurf.blit(gs, (0,0))
            gsurf.set_alpha(50)
            tw = gs.get_width()
            surface.blit(gsurf, (cx - tw//2 + dx, y + dy))
    t = font.render(text, True, color)
    surface.blit(t, (cx - t.get_width()//2, y))


# ── Board grid ───────────────────────────────────────────────────────────
def draw_grid(t):
    # board glass bg
    draw_glass_rect(screen, (0, 0, BOARD_SIZE, BOARD_SIZE),
                    color=(70, 30, 130), alpha=70, radius=0,
                    edge_color=(160, 90, 230), edge_alpha=80, edge_w=3)

    # animated grid lines
    pulse = 0.6 + 0.4 * math.sin(t * 1.5)
    for i in range(1, 3):
        x = i * CELL
        y = i * CELL
        # vertical
        a = int(120 + 80 * pulse)
        ls = pygame.Surface((4, BOARD_SIZE), pygame.SRCALPHA)
        for py in range(BOARD_SIZE):
            fade = math.sin(py / BOARD_SIZE * math.pi)
            pygame.draw.line(ls, (*LILAC_LIGHT, int(a * fade)), (1, py), (3, py))
        screen.blit(ls, (x - 2, 0))
        # horizontal
        ls2 = pygame.Surface((BOARD_SIZE, 4), pygame.SRCALPHA)
        for px in range(BOARD_SIZE):
            fade = math.sin(px / BOARD_SIZE * math.pi)
            pygame.draw.line(ls2, (*LILAC_LIGHT, int(a * fade)), (px, 1), (px, 3))
        screen.blit(ls2, (0, y - 2))

    # intersect glow dots
    for i in range(1, 3):
        for j in range(1, 3):
            gx, gy = i * CELL, j * CELL
            gs = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(gs, (*LILAC_BRIGHT, 160), (10, 10), 6)
            pygame.draw.circle(gs, (255, 255, 255, 200), (10, 10), 2)
            screen.blit(gs, (gx - 10, gy - 10))


# ── Draw X (glass blue) ──────────────────────────────────────────────────
def draw_X(cx, cy, t=0, anim=1.0):
    pad   = 42
    thick = 13
    surf  = pygame.Surface((CELL, CELL), pygame.SRCALPHA)
    alpha = int(255 * anim)

    # outer glow
    for off, a in [(8, 25), (5, 50), (3, 80)]:
        pygame.draw.line(surf, (*X_GLOW, a),
                         (pad-off, pad-off), (CELL-pad+off, CELL-pad+off), thick+off*2)
        pygame.draw.line(surf, (*X_GLOW, a),
                         (CELL-pad+off, pad-off), (pad-off, CELL-pad+off), thick+off*2)
    # glass fill
    pygame.draw.line(surf, (*X_BASE, alpha),
                     (pad, pad), (CELL-pad, CELL-pad), thick)
    pygame.draw.line(surf, (*X_BASE, alpha),
                     (CELL-pad, pad), (pad, CELL-pad), thick)
    # highlight streak
    pygame.draw.line(surf, (200, 230, 255, int(140*anim)),
                     (pad+4, pad+2), (CELL-pad-4, CELL-pad-2), 3)
    pygame.draw.line(surf, (200, 230, 255, int(140*anim)),
                     (CELL-pad-2, pad+4), (pad+2, CELL-pad-4), 3)
    # rounded caps
    for px, py in [(pad,pad),(CELL-pad,pad),(pad,CELL-pad),(CELL-pad,CELL-pad)]:
        pygame.draw.circle(surf, (*X_BASE, alpha), (px, py), thick//2 + 1)
        pygame.draw.circle(surf, (200, 230, 255, int(180*anim)), (px-1, py-1), 3)
    screen.blit(surf, (cx - CELL//2, cy - CELL//2))


# ── Draw O (glass red) ───────────────────────────────────────────────────
def draw_O(cx, cy, t=0, anim=1.0):
    pad   = 38
    thick = 13
    r     = CELL//2 - pad
    surf  = pygame.Surface((CELL, CELL), pygame.SRCALPHA)
    hc    = CELL // 2
    alpha = int(255 * anim)

    # outer glow rings
    for off, a in [(8, 20), (5, 45), (3, 75)]:
        pygame.draw.circle(surf, (*O_GLOW, a), (hc, hc), r+off, thick+off*2)
    # glass ring
    pygame.draw.circle(surf, (*O_BASE, alpha), (hc, hc), r, thick)
    # highlight arc (top-left)
    arc_surf = pygame.Surface((CELL, CELL), pygame.SRCALPHA)
    pygame.draw.arc(arc_surf, (255, 200, 210, int(160*anim)),
                    (hc-r-2, hc-r-2, (r+2)*2, (r+2)*2),
                    math.radians(120), math.radians(200), 4)
    surf.blit(arc_surf, (0, 0))
    screen.blit(surf, (cx - CELL//2, cy - CELL//2))


def cell_center(idx):
    row = idx // 3
    col = idx % 3
    return col * CELL + CELL//2, row * CELL + CELL//2


# ── Side panel ───────────────────────────────────────────────────────────
def draw_panel(p1_name, p2_name, scores, ties, current_mark, state, vs_ai):
    px = BOARD_SIZE
    draw_glass_rect(screen, (px, 0, PANEL_WIDTH, WIN_H),
                    color=(50, 20, 100), alpha=80, radius=0,
                    edge_color=(160, 90, 230), edge_alpha=90, edge_w=2)
    pygame.draw.line(screen, (*LILAC_LIGHT, 120), (px, 0), (px, WIN_H), 2)

    cx = px + PANEL_WIDTH // 2

    # Title
    draw_centered_text(screen, "◈  SCORE BOARD  ◈", FONT_TITLE, LILAC_BRIGHT, cx, 16, glow=True)
    pygame.draw.line(screen, (*LILAC_MID, 150), (px+20, 54), (px+PANEL_WIDTH-20, 54), 1)

    # P1 box
    draw_glass_rect(screen, (px+15, 62, PANEL_WIDTH-30, 88),
                    color=(40, 15, 90), alpha=70, radius=12,
                    edge_color=(X_BASE[0], X_BASE[1], X_BASE[2]), edge_alpha=120)
    p1_col = X_GLOW if current_mark == "X" and state == "playing" else TEXT_MID
    draw_centered_text(screen, p1_name[:14], FONT_SCORE, p1_col, cx, 70)
    draw_centered_text(screen, "✕", FONT_LABEL, (*X_BASE,), cx, 94)
    draw_centered_text(screen, str(scores[0]), FONT_BIG, X_GLOW, cx, 108, glow=True)

    # P2 box
    p2_label = "A.I." if vs_ai else (p2_name or "Player 2")
    draw_glass_rect(screen, (px+15, 162, PANEL_WIDTH-30, 88),
                    color=(40, 15, 90), alpha=70, radius=12,
                    edge_color=(O_BASE[0], O_BASE[1], O_BASE[2]), edge_alpha=120)
    p2_col = O_GLOW if current_mark == "O" and state == "playing" else TEXT_MID
    draw_centered_text(screen, p2_label[:14], FONT_SCORE, p2_col, cx, 170)
    draw_centered_text(screen, "○", FONT_LABEL, (*O_BASE,), cx, 194)
    draw_centered_text(screen, str(scores[1]), FONT_BIG, O_GLOW, cx, 208, glow=True)

    # Draws box
    draw_glass_rect(screen, (px+40, 262, PANEL_WIDTH-80, 50),
                    color=(60, 25, 110), alpha=60, radius=10,
                    edge_color=LILAC_LIGHT, edge_alpha=80)
    draw_centered_text(screen, "DRAWS", FONT_LABEL, TEXT_DIM, cx, 268)
    draw_centered_text(screen, str(ties), FONT_SCORE, TEXT_BRIGHT, cx, 284)

    pygame.draw.line(screen, (*LILAC_MID, 100), (px+20, 325), (px+PANEL_WIDTH-20, 325), 1)

    # Turn / result
    if state == "playing":
        now = p1_name if current_mark == "X" else p2_label
        col = X_GLOW if current_mark == "X" else O_GLOW
        draw_centered_text(screen, "NOW PLAYING", FONT_LABEL, TEXT_DIM, cx, 335)
        draw_centered_text(screen, now[:14], FONT_SCORE, col, cx, 354, glow=True)
        sym = "✕" if current_mark == "X" else "○"
        pulse_a = int(180 + 75 * math.sin(time.time() * 3))
        ps = FONT_BIG.render(sym, True, col)
        psurf = pygame.Surface(ps.get_size(), pygame.SRCALPHA)
        psurf.blit(ps, (0, 0))
        psurf.set_alpha(pulse_a)
        screen.blit(psurf, (cx - ps.get_width()//2, 386))

    elif state in ("win", "draw"):
        if state == "draw":
            msg  = "DRAW !"
            col  = LILAC_BRIGHT
        else:
            winner = p1_name if current_mark == "X" else p2_label
            msg  = f"{winner[:10]} WINS!"
            col  = X_GLOW if current_mark == "X" else O_GLOW
        draw_centered_text(screen, msg, FONT_BIG, col, cx, 348, glow=True)
        draw_glass_rect(screen, (px+25, 415, PANEL_WIDTH-50, 36),
                        color=(60,20,110), alpha=80, radius=10,
                        edge_color=LILAC_LIGHT, edge_alpha=100)
        draw_glass_rect(screen, (px+25, 460, PANEL_WIDTH-50, 36),
                        color=(60,20,110), alpha=80, radius=10,
                        edge_color=LILAC_LIGHT, edge_alpha=100)
        draw_centered_text(screen, "[ R ]  Rematch", FONT_PROMPT, TEXT_BRIGHT, cx, 424)
        draw_centered_text(screen, "[ Q ]  Main Menu", FONT_PROMPT, TEXT_BRIGHT, cx, 469)

    # Footer
    draw_centered_text(screen, "by Liran Martfel", FONT_SUB, TEXT_DIM, cx, WIN_H - 22)


# ── Win line animation ───────────────────────────────────────────────────
WIN_COMBOS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6),
]

def get_win_combo(board, sign):
    for combo in WIN_COMBOS:
        if all(board[i] == sign for i in combo):
            return combo
    return None


class WinLineAnim:
    def __init__(self, combo):
        self.start = cell_center(combo[0])
        self.end   = cell_center(combo[2])
        self.t     = 0.0

    def update(self, dt):
        self.t = min(1.0, self.t + dt * 1.6)

    def draw(self, surface):
        ex = self.start[0] + (self.end[0] - self.start[0]) * self.t
        ey = self.start[1] + (self.end[1] - self.start[1]) * self.t
        for width, color, alpha in [(22, WIN_GLOW_C, 40),(14, WIN_GLOW_C, 80),(6, WIN_CORE, 220)]:
            s = pygame.Surface((BOARD_SIZE, BOARD_SIZE), pygame.SRCALPHA)
            pygame.draw.line(s, (*color, alpha),
                             self.start, (int(ex), int(ey)), width)
            surface.blit(s, (0, 0))
        # glowing tip
        ts = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(ts, (*WIN_GLOW_C, 120), (15, 15), 12)
        pygame.draw.circle(ts, (255, 255, 255, 230), (15, 15), 5)
        surface.blit(ts, (int(ex)-15, int(ey)-15))


# ── AI logic (minimax) ───────────────────────────────────────────────────
def check_winner_ai(board, sign):
    for combo in WIN_COMBOS:
        if all(board[i] == sign for i in combo):
            return True
    return False

def minimax(board, depth, is_max, alpha, beta):
    if check_winner_ai(board, "O"):  return  10 - depth
    if check_winner_ai(board, "X"):  return -10 + depth
    if all(c != "" for c in board):  return 0

    if is_max:
        best = -999
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                best = max(best, minimax(board, depth+1, False, alpha, beta))
                board[i] = ""
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                best = min(best, minimax(board, depth+1, True, alpha, beta))
                board[i] = ""
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def ai_move(board):
    best_val = -999
    best_idx = -1
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            val = minimax(board, 0, False, -999, 999)
            board[i] = ""
            if val > best_val:
                best_val = val
                best_idx = i
    return best_idx


# ── Piece appear animation ───────────────────────────────────────────────
class PieceAnim:
    def __init__(self, idx, mark):
        self.idx  = idx
        self.mark = mark
        self.t    = 0.0

    def update(self, dt):
        self.t = min(1.0, self.t + dt * 4.0)

    @property
    def done(self):
        return self.t >= 1.0


# ── Main menu ────────────────────────────────────────────────────────────
def main_menu():
    buttons = [
        ("⚔  Player vs Player", "pvp"),
        ("🤖  Player vs A.I.",   "ai"),
        ("✕  Exit",              "exit"),
    ]
    hovered = -1

    while True:
        t  = time.time()
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mx, my = event.pos
                hovered = -1
                for i, (_, _) in enumerate(buttons):
                    bx = WIN_W//2 - 200
                    by = 290 + i * 80
                    if bx <= mx <= bx+400 and by <= my <= by+52:
                        hovered = i
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                for i, (_, action) in enumerate(buttons):
                    bx = WIN_W//2 - 200
                    by = 290 + i * 80
                    if bx <= mx <= bx+400 and by <= my <= by+52:
                        if action == "exit":
                            pygame.quit(); sys.exit()
                        return action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: return "pvp"
                if event.key == pygame.K_2: return "ai"
                if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

        draw_background()

        # Logo area
        draw_glass_rect(screen, (WIN_W//2 - 280, 60, 560, 160),
                        color=(70,20,140), alpha=60, radius=24,
                        edge_color=LILAC_BRIGHT, edge_alpha=130)
        draw_centered_text(screen, "TIC  TAC  TOE", FONT_BIG, LILAC_BRIGHT, WIN_W//2, 88, glow=True)
        draw_centered_text(screen, "✦  Liquid Glass Edition  ✦", FONT_LABEL, TEXT_MID, WIN_W//2, 144)
        draw_centered_text(screen, "by Liran Martfel", FONT_SUB, TEXT_DIM, WIN_W//2, 170)

        # Floating X and O
        fx = 80 + 10 * math.sin(t * 0.8)
        fy = 200 + 15 * math.cos(t * 0.6)
        draw_X(int(fx), int(fy), t)
        fo2x = WIN_W - 80 + 10 * math.cos(t * 0.7)
        fo2y = 200 + 15 * math.sin(t * 0.9)
        draw_O(int(fo2x), int(fo2y), t)

        # Buttons
        for i, (label, _) in enumerate(buttons):
            bx = WIN_W//2 - 200
            by = 290 + i * 80
            is_hov = (hovered == i)
            ec     = LILAC_BRIGHT if is_hov else LILAC_MID
            ea     = 200 if is_hov else 100
            ba     = 90  if is_hov else 55
            draw_glass_rect(screen, (bx, by, 400, 52),
                            color=(80, 30, 160) if is_hov else (50, 15, 110),
                            alpha=ba, radius=16, edge_color=ec, edge_alpha=ea)
            col = LILAC_BRIGHT if is_hov else TEXT_MID
            draw_centered_text(screen, label, FONT_SCORE, col, WIN_W//2, by+14, glow=is_hov)

        # Hint
        draw_centered_text(screen, "[ 1 ] PvP   [ 2 ] vs A.I.   [ ESC ] Quit",
                           FONT_PROMPT, TEXT_DIM, WIN_W//2, WIN_H - 30)

        pygame.display.flip()


# ── Name input ───────────────────────────────────────────────────────────
def name_input_screen(vs_ai=False):
    count    = 1 if vs_ai else 2
    names    = ["", ""]
    active   = 0
    cursor_t = 0.0
    labels   = ["Your Name  ( ✕ )", "Player 2 Name  ( ○ )"]
    colors   = [X_GLOW, O_GLOW]

    while True:
        dt = clock.tick(60) / 1000
        cursor_t += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if active < count - 1 and names[active].strip():
                        active += 1
                    elif active == count - 1 and names[active].strip():
                        p2 = "A.I." if vs_ai else names[1].strip()
                        return names[0].strip(), p2
                elif event.key == pygame.K_BACKSPACE:
                    names[active] = names[active][:-1]
                elif event.key == pygame.K_TAB:
                    if count > 1 and names[0].strip():
                        active = 1 - active
                elif event.key == pygame.K_ESCAPE:
                    return None, None
                elif len(names[active]) < 16:
                    names[active] += event.unicode

        draw_background()
        draw_glass_rect(screen, (WIN_W//2-300, 50, 600, 440),
                        color=(60,20,120), alpha=65, radius=28,
                        edge_color=LILAC_BRIGHT, edge_alpha=120)

        draw_centered_text(screen, "ENTER NAMES", FONT_TITLE, LILAC_BRIGHT, WIN_W//2, 80, glow=True)
        pygame.draw.line(screen, (*LILAC_MID, 120),
                         (WIN_W//2-240, 118), (WIN_W//2+240, 118), 1)

        for i in range(count):
            y_base = 150 + i * 140
            draw_centered_text(screen, labels[i], FONT_SCORE, colors[i], WIN_W//2, y_base)
            box_w, box_h = 380, 48
            box_x = WIN_W//2 - box_w//2
            box_y = y_base + 34
            is_active = (active == i)
            ec = LILAC_BRIGHT if is_active else LILAC_MID
            ea = 180 if is_active else 80
            draw_glass_rect(screen, (box_x, box_y, box_w, box_h),
                            color=(40,15,90), alpha=80, radius=12,
                            edge_color=ec, edge_alpha=ea)
            display = names[i] + ("|" if is_active and int(cursor_t*2)%2==0 else "")
            t_surf  = FONT_INPUT.render(display, True, TEXT_BRIGHT)
            screen.blit(t_surf, (box_x+14, box_y+14))

        if vs_ai:
            draw_centered_text(screen, "A.I.  ( ○ )", FONT_SCORE, O_GLOW, WIN_W//2, 290)
            draw_glass_rect(screen, (WIN_W//2-100, 318, 200, 44),
                            color=(40,15,90), alpha=70, radius=12,
                            edge_color=O_GLOW, edge_alpha=100)
            draw_centered_text(screen, "CPU", FONT_INPUT, TEXT_DIM, WIN_W//2, 330)

        hint = "ENTER — confirm  ·  ESC — back"
        draw_centered_text(screen, hint, FONT_PROMPT, TEXT_DIM, WIN_W//2, WIN_H - 50)

        pygame.display.flip()


# ── Game ─────────────────────────────────────────────────────────────────
def run_game(p1_name, p2_name, vs_ai, scores, ties):
    board       = [""] * 9
    turn        = 0
    signs       = ("X", "O")
    state       = "playing"
    win_anim    = None
    winner_mark = None
    pieces      = []
    ai_timer    = 0.0
    ai_thinking = False
    t_global    = 0.0

    while True:
        dt       = clock.tick(60) / 1000
        t_global += dt

        if ai_thinking:
            ai_timer += dt
            if ai_timer >= 0.6:
                ai_thinking = False
                idx = ai_move(board)
                if idx >= 0:
                    board[idx] = "O"
                    pieces.append(PieceAnim(idx, "O"))
                    combo = get_win_combo(board, "O")
                    if combo:
                        state       = "win"
                        winner_mark = "O"
                        scores[1]  += 1
                        win_anim    = WinLineAnim(combo)
                    elif all(c != "" for c in board):
                        state   = "draw"
                        ties[0] += 1
                    else:
                        turn = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.KEYDOWN:
                if state in ("win", "draw"):
                    if event.key == pygame.K_r:
                        return "rematch"
                    elif event.key == pygame.K_q:
                        return "menu"

            if event.type == pygame.MOUSEBUTTONDOWN and state == "playing":
                if not (vs_ai and turn == 1) and not ai_thinking:
                    mx, my = event.pos
                    if mx < BOARD_SIZE:
                        idx = (my // CELL) * 3 + (mx // CELL)
                        if 0 <= idx < 9 and board[idx] == "":
                            board[idx] = signs[turn]
                            pieces.append(PieceAnim(idx, signs[turn]))
                            combo = get_win_combo(board, signs[turn])
                            if combo:
                                state       = "win"
                                winner_mark = signs[turn]
                                scores[turn] += 1
                                win_anim    = WinLineAnim(combo)
                            elif all(c != "" for c in board):
                                state   = "draw"
                                ties[0] += 1
                            else:
                                turn = 1 - turn
                                if vs_ai and turn == 1:
                                    ai_thinking = True
                                    ai_timer    = 0.0

        # Update
        for p in pieces:
            p.update(dt)
        if win_anim:
            win_anim.update(dt)

        # Draw
        draw_background()
        draw_grid(t_global)

        # Hover highlight
        if state == "playing" and not ai_thinking:
            mx, my = pygame.mouse.get_pos()
            if mx < BOARD_SIZE:
                hc = (my // CELL) * 3 + (mx // CELL)
                if 0 <= hc < 9 and board[hc] == "":
                    hx = (hc % 3) * CELL
                    hy = (hc // 3) * CELL
                    hs = pygame.Surface((CELL, CELL), pygame.SRCALPHA)
                    hs.fill((*LILAC_MID, 30))
                    screen.blit(hs, (hx, hy))

        # Draw pieces
        for p in pieces:
            cx2, cy2 = cell_center(p.idx)
            if p.mark == "X":
                draw_X(cx2, cy2, t_global, p.t)
            else:
                draw_O(cx2, cy2, t_global, p.t)

        if win_anim:
            win_anim.draw(screen)

        # AI thinking indicator
        if ai_thinking:
            dots = "." * (int(t_global * 3) % 4)
            draw_centered_text(screen, f"A.I. thinking{dots}", FONT_LABEL,
                               LILAC_BRIGHT, BOARD_SIZE//2, BOARD_SIZE//2 - 20)

        cur_mark = winner_mark if state == "win" else signs[turn]
        draw_panel(p1_name, p2_name, scores, ties[0], cur_mark, state, vs_ai)

        pygame.display.flip()


# ── Entry point ──────────────────────────────────────────────────────────
def main():
    while True:
        mode = main_menu()
        vs_ai = (mode == "ai")
        p1, p2 = name_input_screen(vs_ai)
        if p1 is None:
            continue

        scores = [0, 0]
        ties   = [0]

        result = "rematch"
        while result == "rematch":
            result = run_game(p1, p2, vs_ai, scores, ties)


if __name__ == "__main__":
    main()
