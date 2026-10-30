import os
import subprocess
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

WORK_DIR = Path(r"E:\2026GEM-SKILL\115\都計建管業務\都計建管業務控管表\3D動態島資料")
HTML_PATH = WORK_DIR / "index.html"
AUDIO_PATH = WORK_DIR / "master_audio.mp3"
OUTPUT_MP4 = WORK_DIR / "馬祖四鄉五島_都計建管3D生態島_導覽動畫.mp4"
FFMPEG_EXE = r"C:\Users\A1547\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
if not os.path.exists(FFMPEG_EXE):
    FFMPEG_EXE = "ffmpeg"

VOICE_SCRIPT = (
    "歡迎蒞臨連江縣政府工務處都計建管科，馬祖四鄉五島微縮實物模型三D生態島。"
    "本系統結合即時海洋頂點波浪與雙向航行客輪。"
    "第一站南竿島，展現福澳智慧碼頭裝卸吊臂與媽祖巨神像呼吸燈籠；"
    "第二站北竿島，呈現芹壁花崗岩石屋、壓瓦石與外海龜島；"
    "第三站東引島，三百六十度旋轉探照燈塔守護國之北疆；"
    "第四站莒光雙島，東莒白犬燈塔閃耀發光，與西莒青帆港輝映。"
    "一百一十五年度全科累計發文一千七百一十件，平均辦結僅一點四五天，展現卓越行政效能。"
)

def generate_tts():
    print("[1/3] 正在使用 Edge-TTS (zh-TW-HsiaoChenNeural) 合成繁體中文導覽語音...")
    cmd = [
        "edge-tts",
        "--voice", "zh-TW-HsiaoChenNeural",
        "--rate", "+6%",
        "--text", VOICE_SCRIPT,
        "--write-media", str(AUDIO_PATH)
    ]
    subprocess.run(cmd, check=True)
    print(f"語音合成完成: {AUDIO_PATH}")

def record_webgl_video():
    print("[2/3] 正在啟動 Playwright 1080P 錄製 3D 微縮生態島動態巡航...")
    temp_video_dir = WORK_DIR / "_rec_tmp"
    temp_video_dir.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--use-gl=angle",
                "--use-angle=swiftshader",
                "--enable-webgl",
                "--ignore-gpu-blocklist",
                "--disable-web-security"
            ]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=str(temp_video_dir),
            record_video_size={"width": 1920, "height": 1080},
            device_scale_factor=1
        )
        page = context.new_page()
        page.goto(HTML_PATH.as_uri(), wait_until="domcontentloaded")
        page.wait_for_timeout(2000)

        # 1. 全景海圖波浪展示 (3.5s)
        page.evaluate("window.setOverviewCamera && window.setOverviewCamera()")
        page.wait_for_timeout(3500)

        # 2. 第一站：南竿島（福澳碼頭與媽祖神像）(5.5s)
        page.evaluate("document.getElementById('badge-nangan').click()")
        page.wait_for_timeout(5500)

        # 3. 第二站：北竿島（芹壁石屋與龜島）(5.5s)
        page.evaluate("document.getElementById('badge-beigan').click()")
        page.wait_for_timeout(5500)

        # 4. 第三站：東引島（旋轉探照燈塔 + 夕陽時相）(5.5s)
        page.evaluate("window.setTimeMode('sunset', document.getElementById('btn-sunset'))")
        page.evaluate("document.getElementById('badge-dongyin').click()")
        page.wait_for_timeout(5500)

        # 5. 第四站：莒光雙島（白犬燈塔發光 + 漁火夜景）(5.5s)
        page.evaluate("window.setTimeMode('night', document.getElementById('btn-night'))")
        page.evaluate("document.getElementById('badge-chukuang').click()")
        page.wait_for_timeout(5500)

        # 6. 展示 115年公文績效總表與全景回歸 (5.5s)
        page.evaluate("window.closeDrawer && window.closeDrawer()")
        page.wait_for_timeout(1500)
        page.evaluate("window.openModal('performance')")
        page.wait_for_timeout(2800)
        page.evaluate("window.closeModal()")
        page.evaluate("window.setTimeMode('day', document.getElementById('btn-day'))")
        page.wait_for_timeout(1500)

        video_path = Path(page.video.path())
        context.close()
        browser.close()
        return video_path

def mux_video_audio(webm_path: Path):
    print("[3/3] 正在使用 FFmpeg 封裝 H.264 MP4 高畫質影片與音軌...")
    cmd = [
        FFMPEG_EXE, "-y",
        "-i", str(webm_path),
        "-i", str(AUDIO_PATH),
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        str(OUTPUT_MP4)
    ]
    subprocess.run(cmd, check=True)
    print(f"[OK] 影片錄製與合成完成: {OUTPUT_MP4}")

if __name__ == "__main__":
    generate_tts()
    webm_file = record_webgl_video()
    mux_video_audio(webm_file)
