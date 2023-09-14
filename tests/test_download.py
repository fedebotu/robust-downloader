import os

from robust_downloader import download


def test_download():
    url = "https://raw.githubusercontent.com/fedebotu/robust-downloader/main/README.md"
    output = "/tmp/testing"

    # Download file
    download(url, output, "README.md")

    # Check if file exists and has data
    assert os.path.exists(output + "/README.md")
    assert os.path.getsize(output + "/README.md") > 0

    os.remove(output + "/README.md")
