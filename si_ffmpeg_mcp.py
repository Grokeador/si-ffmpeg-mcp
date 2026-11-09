#!/usr/bin/env python3
"""
SI-FFmpeg-MCP (by SI NEWS) — Deterministic Windows FFmpeg NVENC, -14 LUFS & Silence-Strip Builder.
100% Python 3 standard library.
"""
from __future__ import annotations
import argparse
import json
import sys
from typing import Dict, List


def build_nvenc_encode_cmd(inp: str, out: str, width: int = 1920, height: int = 1080, cq: int = 21) -> List[str]:
    vf = f"scale={int(width)}:{int(height)}:force_original_aspect_ratio=decrease,pad={int(width)}:{int(height)}:(ow-iw)/2:(oh-ih)/2"
    return [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(inp),
        "-vf", vf,
        "-c:v", "h264_nvenc", "-preset", "p4", "-cq", str(int(cq)),
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(out),
    ]


def build_lufs_normalize_cmd(inp: str, out: str, target_i: float = -14.0, true_peak: float = -1.5) -> List[str]:
    af = f"loudnorm=I={target_i:.1f}:TP={true_peak:.1f}:LRA=11"
    return [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(inp),
        "-af", af,
        "-ar", "48000",
        str(out),
    ]


def build_silence_remove_cmd(inp: str, out: str, threshold_db: int = -42, min_dur: float = 0.35) -> List[str]:
    af = f"silenceremove=stop_periods=-1:stop_duration={min_dur:.2f}:stop_threshold={int(threshold_db)}dB"
    return [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(inp),
        "-af", af,
        str(out),
    ]


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SI-FFmpeg-MCP Builder (by SI NEWS)")
    parser.add_argument("--preset", choices=["nvenc-1080p", "normalize-lufs", "strip-silence"], required=True)
    parser.add_argument("--input", required=True, help="Input media file")
    parser.add_argument("--output", required=True, help="Output media file")
    args = parser.parse_args(argv)

    if args.preset == "nvenc-1080p":
        cmd = build_nvenc_encode_cmd(args.input, args.output)
    elif args.preset == "normalize-lufs":
        cmd = build_lufs_normalize_cmd(args.input, args.output)
    else:
        cmd = build_silence_remove_cmd(args.input, args.output)

    print(json.dumps({"preset": args.preset, "command": cmd}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
