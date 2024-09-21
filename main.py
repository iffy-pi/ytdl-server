import sys

from yt_dlp import YoutubeDL
from yt_dlp.utils import download_range_func
from contextlib import redirect_stdout
from pathlib import Path
import io

def main():
    youtube_id = "GDRyigWvUFg"

    # Youtube DL parameters
    # Was created using convert_cli_to_embed.py
    # See Issue #1 for more details
    ctx = {
        # 'download_ranges': download_range_func([], [[10, 20]]),
        'extract_flat': 'discard_in_playlist',
        'format': 'mp4',
        'fragment_retries': 10,
        'ignoreerrors': 'only_download',
        'retries': 10,
        "outtmpl": {'default': "-"},
        'logtostderr': True,
        'quiet': True,
        'postprocessors': [{'key': 'FFmpegConcat',
                    'only_multi_video': True,
                    'when': 'playlist'}],
    }

    buffer = io.BytesIO()
    with redirect_stdout(buffer), YoutubeDL(ctx) as foo:
        foo.download([youtube_id])

    # Write out the buffer to save to a file, in this case we can just send the buffer as a response
    Path(f"output3.mp4").write_bytes(buffer.getvalue())
    print('Done')

if __name__ == '__main__':
    sys.exit(main())