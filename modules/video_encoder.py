"""
==============================================================================
Module:      video_encoder.py
Description: OpenCV VideoWriter pipeline compiling PNG frame sequences
             into H.264/MP4 encoded high-definition video files.
==============================================================================
"""

import os
import cv2
from typing import Optional


def compile_frames_to_mp4(frame_folder: str, output_filepath: str, fps: int = 30) -> Optional[str]:
    """
    Liest alle PNG-Bilder geordnet aus frame_folder und erzeugt eine MP4-Videodatei.
    """
    if not os.path.exists(frame_folder):
        raise FileNotFoundError(f"Frame-Ordner '{frame_folder}' existiert nicht.")

    frames = sorted([f for f in os.listdir(frame_folder) if f.endswith(('.png', '.jpg'))])
    if not frames:
        raise ValueError(f"Keine Bilddateien im Ordner '{frame_folder}' gefunden.")

    first_frame_path = os.path.join(frame_folder, frames[0])
    sample_img = cv2.imread(first_frame_path)
    height, width, _ = sample_img.shape

    out_dir = os.path.dirname(output_filepath)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_filepath, fourcc, fps, (width, height))

    print(f"[*] Enkodiere {len(frames)} Frames nach '{output_filepath}' ({width}x{height} @ {fps} FPS)...")
    for frame_name in frames:
        img_path = os.path.join(frame_folder, frame_name)
        frame_data = cv2.imread(img_path)
        writer.write(frame_data)

    writer.release()
    cv2.destroyAllWindows()
    print(f"[+] Video-Export erfolgreich abgeschlossen: {output_filepath}")
    return output_filepath
