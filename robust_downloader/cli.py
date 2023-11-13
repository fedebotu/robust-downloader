import argparse
import os.path

from .__init__ import __version__
from .downloader import download


class _ShowVersionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(
            "robust-downloader {ver} at {pos}".format(
                ver=__version__, pos=os.path.dirname(os.path.dirname(__file__))
            )
        )
        parser.exit()


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-V",
        "--version",
        action=_ShowVersionAction,
        help="display version",
        nargs=0,
    )
    parser.add_argument("url", help="url to download")
    parser.add_argument("--folder", help="folder to save the file")
    parser.add_argument("--filename", help="filename to save the file")
    parser.add_argument("--key", help="key to decrypt the file")
    parser.add_argument("--proxy", help="proxy to use")
    parser.add_argument("--md5", help="md5 to check the file")
    parser.add_argument("--sha256", help="sha256 to check the file")
    parser.add_argument(
        "--max-redirect-hops", type=int, default=3, help="max redirect hops"
    )
    parser.add_argument("--verify", type=bool, help="verify the file")
    parser.add_argument("--timeout", type=int, default=60, help="timeout in seconds")
    parser.add_argument("--retry-max", type=int, default=500, help="retry max in seconds")
    parser.add_argument("--sleep-max", type=int, default=120, help="sleep max in seconds")
    parser.add_argument("--chunk-size", type=int, default=1024, help="chunk size")
    parser.add_argument("--show-progress", type=bool, default=True, help="show progress")
    parser.add_argument("--logging-level", type=int, default=20, help="logging level")

    args = parser.parse_args()

    download(
        args.url,
        folder=args.folder,
        filename=args.filename,
        key=args.key,
        proxy=args.proxy,
        md5=args.md5,
        sha256=args.sha256,
        max_redirect_hops=args.max_redirect_hops,
        verify=args.verify,
        timeout=args.timeout,
        retry_max=args.retry_max,
        sleep_max=args.sleep_max,
        chunk_size=args.chunk_size,
        show_progress=args.show_progress,
        logging_level=args.logging_level,
    )


if __name__ == "__main__":
    main()
