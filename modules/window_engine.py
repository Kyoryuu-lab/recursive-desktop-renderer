"""
==============================================================================
Module:      window_engine.py
Description: Recursive window drawing engine supporting fixed (Quadruple)
             and continuous multi-scale (Infinite Droste) recursion.
==============================================================================
"""

import pygame

TITLE_HEIGHT = 20
BOTTOM_BORDER_HEIGHT = 10
MIN_WINDOW_WIDTH = 4
MIN_WINDOW_HEIGHT = TITLE_HEIGHT + BOTTOM_BORDER_HEIGHT + 1

TITLE_BAR_COLOR = (50, 50, 50)
BUTTON_COLOR = (60, 60, 60)
BORDER_COLOR = (40, 40, 40)
CONTENT_COLOR = (255, 255, 255)
TEXT_COLOR = (200, 200, 200)


def get_content_rect(window_rect: pygame.Rect) -> pygame.Rect:
    """Berechnet den nutzbaren Inhaltsbereich innerhalb der Fensterrahmen."""
    return pygame.Rect(
        window_rect.x + 2,
        window_rect.y + TITLE_HEIGHT,
        window_rect.width - 4,
        window_rect.height - TITLE_HEIGHT - BOTTOM_BORDER_HEIGHT
    )


def draw_window_frame(surface: pygame.Surface, rect: pygame.Rect, title_text: str) -> None:
    """Zeichnet ein vollstaendiges Desktop-Fenster mit UI-Elementen."""
    # Titelleiste
    title_rect = pygame.Rect(rect.x, rect.y, rect.width, TITLE_HEIGHT)
    pygame.draw.rect(surface, TITLE_BAR_COLOR, title_rect)

    # Schliess- und Minimier-Buttons
    button_size = 15
    close_btn = pygame.Rect(title_rect.right - button_size * 2, title_rect.y, button_size, button_size)
    min_btn = pygame.Rect(close_btn.left - button_size - 5, title_rect.y, button_size, button_size)
    pygame.draw.rect(surface, BUTTON_COLOR, close_btn)
    pygame.draw.rect(surface, BUTTON_COLOR, min_btn)

    pygame.draw.line(surface, TEXT_COLOR, (close_btn.x + 3, close_btn.y + 3), (close_btn.x + 12, close_btn.y + 12), 2)
    pygame.draw.line(surface, TEXT_COLOR, (close_btn.x + 3, close_btn.y + 12), (close_btn.x + 12, close_btn.y + 3), 2)
    pygame.draw.line(surface, TEXT_COLOR, (min_btn.centerx, min_btn.top + 3), (min_btn.centerx, min_btn.bottom - 3), 2)

    # Fenstertitel
    font = pygame.font.SysFont('Arial', 14)
    rendered_title = font.render(title_text, True, TEXT_COLOR)
    surface.blit(rendered_title, rendered_title.get_rect(center=title_rect.center))

    # Fensterrahmen
    pygame.draw.line(surface, BORDER_COLOR, (rect.x, rect.y), (rect.x, rect.bottom), 2)
    pygame.draw.line(surface, BORDER_COLOR, (rect.right - 1, rect.y), (rect.right - 1, rect.bottom), 2)
    pygame.draw.rect(surface, BORDER_COLOR, pygame.Rect(rect.x, rect.bottom - BOTTOM_BORDER_HEIGHT, rect.width, BOTTOM_BORDER_HEIGHT))

    # Weisser Inhaltsbereich
    content_area = pygame.Rect(rect.x, title_rect.bottom, rect.width, rect.height - TITLE_HEIGHT - BOTTOM_BORDER_HEIGHT)
    pygame.draw.rect(surface, CONTENT_COLOR, content_area)


def render_recursion(surface: pygame.Surface, depth: int, mode: str, width: int, height: int, scale_factor: float = 0.98) -> None:
    """Rendert die rekursive Fensterschachtelung gemaess gewaehltem Modus."""
    current_rect = None
    title = "Quadruple Recursion" if mode == "quadruple" else "Infinite Recursion"

    for layer in range(depth):
        if layer == 0:
            if mode == "quadruple":
                rect = pygame.Rect((width - 600) // 2, (height - 400) // 2, 600, 400)
            else:
                rect = pygame.Rect(0, 0, width, height)
        else:
            content_area = get_content_rect(current_rect)

            if mode == "quadruple":
                gap = min(content_area.width, content_area.height) * 0.125
                effective_area = content_area.inflate(-2 * gap, -2 * gap)
                next_w = max(effective_area.width * scale_factor, MIN_WINDOW_WIDTH)
                next_h = max(effective_area.height * scale_factor, MIN_WINDOW_HEIGHT)
                if effective_area.width < MIN_WINDOW_WIDTH or effective_area.height < MIN_WINDOW_HEIGHT:
                    break
                next_x = effective_area.centerx - (next_w / 2)
                next_y = effective_area.centery - (next_h / 2)
            else:
                if (content_area.width < MIN_WINDOW_WIDTH or
                        content_area.height < (MIN_WINDOW_HEIGHT - TITLE_HEIGHT - BOTTOM_BORDER_HEIGHT)):
                    break
                next_w = max(content_area.width * scale_factor, MIN_WINDOW_WIDTH)
                next_h = max(content_area.height * scale_factor, MIN_WINDOW_HEIGHT - TITLE_HEIGHT - BOTTOM_BORDER_HEIGHT)
                next_x = content_area.centerx - (next_w / 2)
                next_y = content_area.centery - (next_h / 2)

            rect = pygame.Rect(next_x, next_y, next_w, next_h)

        draw_window_frame(surface, rect, title)
        current_rect = rect
