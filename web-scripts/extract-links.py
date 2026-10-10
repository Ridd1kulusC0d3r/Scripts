"""Extrai links de um arquivo HTML local, sem acesso à rede."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path

class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_file", type=Path, help="Arquivo HTML local")
    args = parser.parse_args()
    extractor = LinkExtractor()
    extractor.feed(args.html_file.read_text(encoding="utf-8"))
    print(json.dumps(sorted(set(extractor.links)), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
