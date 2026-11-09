import unittest
import si_ffmpeg_mcp as m


class TestSiFfmpegMcp(unittest.TestCase):
    def test_nvenc_command_uses_h264_nvenc_and_faststart(self):
        cmd = m.build_nvenc_encode_cmd("in.mp4", "out.mp4", 1920, 1080, 21)
        self.assertIn("h264_nvenc", cmd)
        self.assertIn("+faststart", cmd)
        self.assertEqual(cmd[-1], "out.mp4")

    def test_lufs_normalize_uses_loudnorm_minus_14(self):
        cmd = m.build_lufs_normalize_cmd("voice.wav", "voice_norm.wav")
        af_idx = cmd.index("-af") + 1
        self.assertIn("loudnorm=I=-14.0:TP=-1.5:LRA=11", cmd[af_idx])

    def test_silence_remove_builds_filter(self):
        cmd = m.build_silence_remove_cmd("raw.wav", "tight.wav", -40, 0.4)
        af_idx = cmd.index("-af") + 1
        self.assertIn("silenceremove=stop_periods=-1:stop_duration=0.40:stop_threshold=-40dB", cmd[af_idx])

    def test_cli_prints_json_command(self):
        rc = m.main(["--preset", "nvenc-1080p", "--input", "a.mp4", "--output", "b.mp4"])
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
