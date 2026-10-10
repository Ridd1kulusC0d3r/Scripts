"""Normaliza indicadores públicos em arquivo local. Não faz consultas de rede."""
import argparse
import ipaddress
import json
from pathlib import Path
from urllib.parse import urlsplit

def normalize(value: str) -> dict[str, str] | None:
    value = value.strip()
    if not value or value.startswith("#"):
        return None
    try:
        return {"type": "ip", "value": str(ipaddress.ip_address(value))}
    except ValueError:
        pass
    if value.startswith(("https://", "http://")):
        parsed = urlsplit(value)
        if parsed.hostname:
            return {"type": "url", "value": value}
    if value and all(char.isalnum() or char in "-." for char in value) and "." in value:
        return {"type": "domain", "value": value.lower().rstrip(".")}
    return None

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    records = (normalize(line) for line in args.input_file.read_text(encoding="utf-8").splitlines())
    unique = {(item["type"], item["value"]): item for item in records if item}
    print(json.dumps(list(unique.values()), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
