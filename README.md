# Robust Downloader

A minimal Python downloader with robustness in mind - resumable downloads, retries, and more.

## Installation

```bash
pip install robust-downloader
```

## Usage

### From Python
```python
from robust_downloader import download

download("https://raw.githubusercontent.com/fedebotu/robust-downloader/main/README.md")
```

### From CLI

```bash
$ robust-downloader --help
usage: robust-downloader [-h] [-V] [--folder FOLDER] [--filename FILENAME] [--key KEY]
                         [--proxy PROXY] [--md5 MD5]
                         [--max-redirect-hops MAX_REDIRECT_HOPS] [--verify VERIFY]
                         [--timeout TIMEOUT] [--retry-max RETRY_MAX]
                         [--sleep-max SLEEP_MAX] [--chunk-size CHUNK_SIZE]
                         [--show-progress SHOW_PROGRESS] [--logging-level LOGGING_LEVEL]
                         url
```

Example:
```bash
$ robust-downloader https://raw.githubusercontent.com/fedebotu/robust-downloader/main/README.md
```


### Available Arguments
```
positional arguments:
  url                   url to download

options:
  -h, --help            show this help message and exit
  -V, --version         display version (default: None)
  --folder FOLDER       folder to save the file (default: None)
  --filename FILENAME   filename to save the file (default: None)
  --key KEY             key to decrypt the file (default: None)
  --proxy PROXY         proxy to use (default: None)
  --md5 MD5             md5 to check the file (default: None)
  --max-redirect-hops MAX_REDIRECT_HOPS
                        max redirect hops (default: 3)
  --verify VERIFY       verify the file (default: None)
  --timeout TIMEOUT     timeout in seconds (default: 60)
  --retry-max RETRY_MAX
                        retry max in seconds (default: 500)
  --sleep-max SLEEP_MAX
                        sleep max in seconds (default: 120)
  --chunk-size CHUNK_SIZE
                        chunk size (default: 1024)
  --show-progress SHOW_PROGRESS
                        show progress (default: True)
  --logging-level LOGGING_LEVEL
                        logging level (default: 20)
```


## Acknowledgements

This repository was inspired by [gdown](https://github.com/wkentaro/gdown/tree/main).

## Contributing
Feel free to contribute to this repository by creating a pull request or submitting an issue!