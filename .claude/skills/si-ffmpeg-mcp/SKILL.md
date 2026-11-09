---
name: si-ffmpeg-mcp
description: Build and execute GPU NVENC video encoding, -14 LUFS EBU R128 audio normalization, and automatic silence removal on Windows via si_ffmpeg_mcp.py.
---

# SI-FFmpeg-MCP Skill

1. **Always Prefer GPU NVENC**: Use `--preset nvenc-1080p` (`h264_nvenc -preset p4 -cq 21`) instead of slow CPU encoding.
2. **Broadcast Audio (`-14 LUFS`)**: Run `--preset normalize-lufs` on every voiceover track before final muxing.
3. **Strip Dead Air**: Run `--preset strip-silence` on raw microphone recordings to tighten tutorial pacing.
