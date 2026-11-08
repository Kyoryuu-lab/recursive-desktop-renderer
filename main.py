"""
==============================================================================
Project:     Recursive Desktop Renderer & Video Synthesis Engine
File:        main.py
Author:      Yevhen Biezhyn
Description: Unified CLI orchestrator generating recursive window animations
             (Droste effect) with Pygame and encoding to MP4 via OpenCV.
==============================================================================
"""

import os
import shutil
import argparse
import pygame

from modules.desktop_ui import draw_desktop_environment, draw_arrow_cursor, BG_COLOR
from modules.window_engine import render_recursion
from modules.video_encoder import compile_frames_to_mp4


def generate_animation_frames(mode: str, total_seconds: int, fps: int, output_dir: str,
                              width: int = 800, height: int = 600) -> int:
    """Generiert Bildsequenzen mit Pygame und speichert sie als PNG-Dateien ab."""
    os.makedirs(output_dir, exist_ok=True)
    pygame.init()
    surface = pygame.Surface((width, height))

    total_frames = fps * total_seconds
    start_animation_at = 150  # Start nach 5 Sekunden
    max_depth = 4 if mode == "quadruple" else 200
    depth_interval = 90 if mode == "quadruple" else 60
    app_title = "Quadruple.exe" if mode == "quadruple" else "Infinite.exe"

    # Cursor-Trajektorie vorberechnen
    target_x, target_y = width // 2, height // 2
    cursor_positions = []
    current_cursor = [0.0, float(target_y)]
    cursor_speed = 2.0

    for _ in range(total_frames):
        dx = target_x - current_cursor[0]
        if abs(dx) > 0.5:
            current_cursor[0] += dx * (cursor_speed / abs(dx)) if abs(dx) > cursor_speed else dx
        cursor_positions.append((int(current_cursor[0]), int(current_cursor[1])))

    print(f"[*] Starte Rendering von {total_frames} Frames (Modus: {mode.upper()})...")

    for frame_idx in range(total_frames):
        surface.fill(BG_COLOR)
        target_rect = draw_desktop_environment(surface, width, height, app_title)
        cx, cy = cursor_positions[frame_idx]
        draw_arrow_cursor(surface, (cx, cy))

        if frame_idx >= start_animation_at:
            if target_rect.collidepoint(cx, cy):
                depth = ((frame_idx - start_animation_at) // depth_interval) + 1
                depth = min(depth, max_depth)
                render_recursion(surface, depth=depth, mode=mode, width=width, height=height)

        frame_path = os.path.join(output_dir, f"frame_{frame_idx:04d}.png")
        pygame.image.save(surface, frame_path)

        if (frame_idx + 1) % 300 == 0 or frame_idx == total_frames - 1:
            print(f"    - Fortschritt: {frame_idx + 1}/{total_frames} Frames generiert...")

    pygame.quit()
    return total_frames


def main():
    parser = argparse.ArgumentParser(
        description="Recursive Desktop Renderer & Video Animation Suite",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--mode",
        choices=["quadruple", "infinite"],
        default="infinite",
        help="quadruple: Diskrete 4-Stufen-Fensterschachtelung\ninfinite : Tiefe kontinuierliche Droste-Rekursion (Standard)"
    )
    parser.add_argument("--duration", type=int, default=60, help="Gesamtlaufzeit des Videos in Sekunden (Standard: 60)")
    parser.add_argument("--fps", type=int, default=30, help="Bilder pro Sekunde (Standard: 30)")
    parser.add_argument("--frames-dir", type=str, default="frames", help="Verzeichnis fuer temporaere PNG-Frames")
    parser.add_argument("--output", type=str, default="output/animation.mp4", help="Zieldateiname fuer das MP4-Video")
    parser.add_argument("--keep-frames", action="store_true", help="Behaelt PNG-Frames nach dem Videoexport bei")
    args = parser.parse_args()

    print("=" * 75)
    print("  RECURSIVE DESKTOP RENDERER | PYGAME & OPENCV PIPELINE")
    print("=" * 75)

    # 1. Frames generieren
    generate_animation_frames(
        mode=args.mode,
        total_seconds=args.duration,
        fps=args.fps,
        output_dir=args.frames_dir
    )

    # 2. Video enkodieren
    compile_frames_to_mp4(
        frame_folder=args.frames_dir,
        output_filepath=args.output,
        fps=args.fps
    )

    # 3. Bereinigung
    if not args.keep_frames:
        print(f"[*] Bereinige temporaeren Frame-Ordner '{args.frames_dir}'...")
        shutil.rmtree(args.frames_dir, ignore_errors=True)

    print("\n" + "=" * 75)
    print(f"  RENDERING & ENKODIERUNG ERFOLGREICH: {args.output}")
    print("=" * 75 + "\n")


if __name__ == "__main__":
    main()
