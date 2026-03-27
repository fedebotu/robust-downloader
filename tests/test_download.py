import os

from robust_downloader import download
import requests

def test_download():
    url = "https://raw.githubusercontent.com/fedebotu/robust-downloader/main/README.md"
    output = "/tmp/testing"

    with requests.Session() as s:
        s.headers['Content-Disposition'] = f'attachment; filename="README.md'
        # Download file
        download(url, output, "README.md", session=s)

        # Check if file exists and has data
        assert os.path.exists(output + "/README.md")
        assert os.path.getsize(output + "/README.md") > 0

        os.remove(output + "/README.md")
