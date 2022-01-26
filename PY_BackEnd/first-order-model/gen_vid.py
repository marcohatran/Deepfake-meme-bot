import subprocess

def gen_vid(config="config/vox-adv-256.yaml", 
            driving_video="vid.mp4", 
            source_image="mala.png", 
            checkpoint="vox-adv-cpk.pth.tar",
            result_video="result.mp4"
        ):
    subprocess.run([
        "python", "demo.py", 
        "--config", config, 
        "--checkpoint", checkpoint, 
        "--source_image", source_image, 
        "--driving_video", driving_video, 
        "--result_video", result_video,
        "--relative", "--adapt_scale", "--cpu"])
    return result_video

if __name__ == "__main__":
    result_path = gen_vid(
        config="config/vox-adv-256.yaml", 
        driving_video="vid.mp4", 
        source_image="mala.png", 
        checkpoint="vox-adv-cpk.pth.tar",
        result_video="result01.mp4"
    )
    print(result_path)