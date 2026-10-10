"""Valida estrutura e preservação dos arquivos históricos; não executa scripts."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["macos","web-scripts","shell","osint","python","typescript","gpo","go","javascript","assembly","cobol","mainframe","windows","linux","c","csharp","java","pascal","php","r","ruby","swift","sql"]
NEW_PYTHON = ["python/hello-world.py", "web-scripts/extract-links.py", "osint/normalize-indicators.py"]

def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def main() -> None:
    failures = []
    for category in REQUIRED:
        if not (ROOT / category / "README.md").is_file():
            failures.append(f"Categoria sem README: {category}")
    data = json.loads((ROOT / "docs/migration-map.json").read_text(encoding="utf-8"))
    seen = set()
    for item in data["files"]:
        path = item["to"]
        if path in seen:
            failures.append(f"Destino duplicado: {path}")
        seen.add(path)
        file = ROOT / path
        if not file.is_file():
            failures.append(f"Arquivo legado ausente: {path}")
        elif git_blob_sha(file.read_bytes()) != item["sha"]:
            failures.append(f"SHA original alterado: {path}")
    for rel in NEW_PYTHON:
        try:
            ast.parse((ROOT / rel).read_text(encoding="utf-8"), filename=rel)
        except (SyntaxError, OSError) as err:
            failures.append(f"Erro de sintaxe/leitura: {rel} -> {err}")
    if len(data["files"]) != data["original_script_count"]:
        failures.append("Contagem do manifesto não corresponde aos arquivos")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"OK: {len(REQUIRED)} categorias e {len(seen)} arquivos legados íntegros")

if __name__ == "__main__":
    main()
