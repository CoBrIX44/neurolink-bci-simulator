"""Add the selected settled poster to frame zero and verify the MP4."""
from pathlib import Path
import json
import subprocess

root = Path(__file__).resolve().parent
video = root / 'brag.mp4'
poster = root / 'brag.jpg'
staged = root / 'brag.poster.mp4'

def run(args):
    subprocess.run(args, check=True)

def probe(path):
    return json.loads(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(path)
    ], text=True))

before = probe(video)
run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-ss', '20.8', '-i', str(video),
     '-frames:v', '1', '-q:v', '2', str(poster)])
run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(video), '-i', str(poster),
     '-filter_complex', "[0:v][1:v]overlay=0:0:enable='eq(n,0)'[v]",
     '-map', '[v]', '-map', '0:a?', '-c:v', 'libx264', '-crf', '18', '-preset', 'slow',
     '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', str(staged)])
after = probe(staged)
old_v = next(s for s in before['streams'] if s['codec_type'] == 'video')
new_v = next(s for s in after['streams'] if s['codec_type'] == 'video')
assert (new_v['width'], new_v['height']) == (1920, 1080)
assert new_v['r_frame_rate'] == '30/1'
assert old_v['nb_frames'] == new_v['nb_frames'] == '660'
assert abs(float(after['format']['duration']) - 22) < .05
assert any(s['codec_type'] == 'audio' for s in after['streams'])
assert staged.resolve().parent == root and video.resolve().parent == root
staged.replace(video)
(root / 'media-verification.json').write_text(json.dumps(after, indent=2), encoding='utf-8')
run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(video), '-frames:v', '1',
     str(root / 'qc-frames' / 'final-first-frame.png')])
run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-ss', '15.9', '-i', str(video),
     '-frames:v', '1', str(root / 'qc-frames' / 'final-demo-frame.png')])
print(json.dumps({'video':str(video),'duration':after['format']['duration'],
                  'frames':new_v['nb_frames'],'resolution':'1920x1080','fps':30,
                  'size_bytes':video.stat().st_size,'poster_time':20.8},indent=2))
