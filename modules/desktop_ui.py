"""
==============================================================================
Module:      desktop_ui.py
Description: Desktop user interface renderer, vector application icons
             (Word, Excel, PowerPoint), taskbar, and cursor kinematics.
==============================================================================
"""

import math
import pygame
from typing import Tuple, List

# Farbdefinitionen
BG_COLOR = (40, 40, 50)
TASKBAR_COLOR = (20, 20, 30)
CURSOR_COLOR = (255, 255, 255)


def draw_arrow_cursor(surface: pygame.Surface, pos: Tuple[int, int]) -> None:
    """Zeichnet einen nach links gerichteten Pfeil-Cursor."""
    x, y = pos
    pygame.draw.polygon(surface, CURSOR_COLOR, [
        (x, y),
        (x - 10, y - 5),
        (x - 10, y + 5)
    ])
    pygame.draw.line(surface, CURSOR_COLOR, (x, y), (x - 20, y), 2)


def draw_desktop_environment(surface: pygame.Surface, width: int, height: int, app_title: str) -> pygame.Rect:
    """Rendert die Desktop-Oberflaeche, Taskleiste und Vektor-Icons."""
    # 1. Taskleiste
    pygame.draw.rect(surface, TASKBAR_COLOR, (0, height - 50, width, 50))

    # 2. Vektor-Icons
    # Word-Icon mit horizontalen Farbgradienten
    w_x, w_y = 100, 400
    pygame.draw.rect(surface, (52, 152, 185), (w_x, w_y, 100, 100), 3)
    w_colors = [(173, 216, 230), (135, 197, 217), (94, 178, 205), (52, 152, 185)]
    for i, col in enumerate(w_colors):
        pygame.draw.rect(surface, col, pygame.Rect(w_x + 3, w_y + 3 + (i * 25), 94, 25))
    sq_w = pygame.Rect(w_x - 25, w_y + 25, 50, 50)
    pygame.draw.rect(surface, (52, 152, 185), sq_w)
    font_large = pygame.font.SysFont('Arial', 40)
    w_text = font_large.render('W', True, (255, 255, 255))
    surface.blit(w_text, w_text.get_rect(center=sq_w.center))

    # Excel-Icon mit vertikalen Teilungen
    e_x, e_y = 300, 400
    pygame.draw.rect(surface, (64, 189, 64), (e_x, e_y, 100, 100), 3)
    e_colors = [(144, 238, 144), (119, 221, 119), (92, 205, 92), (64, 189, 64)]
    for i, col in enumerate(e_colors):
        darker = (max(0, col[0] - 30), max(0, col[1] - 30), max(0, col[2] - 30))
        pygame.draw.rect(surface, darker, pygame.Rect(e_x + 3, e_y + 3 + (i * 25), 47, 25))
        pygame.draw.rect(surface, col, pygame.Rect(e_x + 3 + 47, e_y + 3 + (i * 25), 47, 25))
    sq_e = pygame.Rect(e_x - 25, e_y + 25, 50, 50)
    pygame.draw.rect(surface, (64, 189, 64), sq_e)
    x_text = font_large.render('X', True, (255, 255, 255))
    surface.blit(x_text, x_text.get_rect(center=sq_e.center))

    # PowerPoint-Icon mit Kreissegmenten
    p_x, p_y = 500, 400
    pygame.draw.rect(surface, (180, 90, 0), (p_x, p_y, 100, 100), 3)
    pygame.draw.arc(surface, (180, 90, 0), (p_x + 3, p_y + 3, 94, 94), math.pi, 2 * math.pi, 94)
    pygame.draw.arc(surface, (205, 115, 0), (p_x + 3, p_y + 3, 94, 94), math.pi / 2, math.pi, 94)
    pygame.draw.arc(surface, (255, 165, 0), (p_x + 3, p_y + 3, 94, 94), 0, math.pi / 2, 94)
    sq_p = pygame.Rect(p_x - 25, p_y + 25, 50, 50)
    pygame.draw.rect(surface, (180, 90, 0), sq_p)
    p_text = font_large.render('P', True, (255, 255, 255))
    surface.blit(p_text, p_text.get_rect(center=sq_p.center))

    # Zielprogramm-Button in der Mitte
    target_rect = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 100)
    pygame.draw.rect(surface, (255, 255, 255), target_rect)
    pygame.draw.rect(surface, (0, 0, 0), target_rect, 3)
    font_med = pygame.font.SysFont('Arial', 24)
    lbl = font_med.render(app_title, True, (0, 0, 0))
    surface.blit(lbl, lbl.get_rect(center=target_rect.center))

    return target_rect
