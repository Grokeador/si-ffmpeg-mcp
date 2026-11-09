# SI-FFmpeg-MCP: GPU NVENC & -14 LUFS Audio Automation Command Builder for Claude

**Created by [SI NEWS](https://www.youtube.com/channel/UC4m6veQiZdc_pAfxKQluRgA) • Official companion repo for *"FFmpeg MCP and Local AI: Automate Any Video and Audio Workflow on PC for Free"*.**

When AI agents write raw `ffmpeg` commands on Windows, they frequently hallucinate broken filtergraph quotes, default to slow CPU `libx264` instead of hardware `h264_nvenc`, or clip audio levels.

`si-ffmpeg-mcp` provides a zero-dependency Python 3 stdio MCP server & CLI (`si_ffmpeg_mcp.py`) + Claude skill (`SKILL.md`) that exposes deterministic, tested media pipelines:
1. **GPU NVENC Fast Transcode (`build_nvenc_encode_cmd`)**: Hardware-accelerated 1080p/4K MP4 encoding with `+faststart`.
2. **YouTube `-14 LUFS` Broadcast Audio Normalization (`build_lufs_normalize_cmd`)**: EBU R128 loudness normalization (`loudnorm=I=-14:TP=-1.5:LRA=11`).
3. **Auto Silence Stripper (`build_silence_remove_cmd`)**: Cuts dead air (`silenceremove`) from tutorials and voiceovers automatically.
4. **Lossless Stream Loop / Clip Extractor**: Extends B-roll or extracts clips in milliseconds with `-c copy`.

## Quick Start (Windows PowerShell)
```powershell
git clone https://github.com/Grokeador/si-ffmpeg-mcp
cd si-ffmpeg-mcp
python -m unittest discover -s tests -v
python si_ffmpeg_mcp.py --preset nvenc-1080p --input raw.mp4 --output final.mp4
```

MIT Licensed — Built by [SI NEWS](https://www.youtube.com/channel/UC4m6veQiZdc_pAfxKQluRgA).
