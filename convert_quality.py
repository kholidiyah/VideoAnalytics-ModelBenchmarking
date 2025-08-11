import subprocess

input_video = "road_traffic_1.mp4"

# Define output settings for each quality level
qualities = {
    "low": {
        "scale": "640:360",
        "fps": "15",
        "x264_params": "cabac=0:me=zero:subq=1",
        "preset": "ultrafast",
        "crf": "35"
    },
    "medium": {
        "scale": "1280:720",
        "fps": "25",
        "x264_params": "cabac=1:me=hex:subq=5",
        "preset": "medium",
        "crf": "28"
    },
    "high": {
        "scale": "1920:1080",
        "fps": "30",
        "x264_params": "cabac=1:me=umh:subq=10",
        "preset": "slow",
        "crf": "18"
    }
}

for quality, params in qualities.items():
    output_video = f"{quality}_quality.mp4"
    ffmpeg_cmd = [
        "ffmpeg", "-y",  # overwrite output
        "-i", input_video,
        "-vf", f"scale={params['scale']},fps={params['fps']}",
        "-c:v", "libx264",
        "-x264-params", params["x264_params"],
        "-preset", params["preset"],
        "-crf", params["crf"],
        output_video
    ]

    print(f"Generating {quality} quality video: {output_video}")
    subprocess.run(ffmpeg_cmd)
