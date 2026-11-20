"""
Knowledge Base Initialization Script
Issue #6 (马锦城)

Reads FitPulse-KnowledgeBase/ markdown files,
embeds them via Claude Embedding API,
and stores vectors in Chroma.

Usage:
    python scripts/init_knowledge_base.py
    # or inside Docker:
    docker compose exec backend python scripts/init_knowledge_base.py
"""
import os
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from app.config import settings


def load_knowledge_entries(base_path: str) -> list:
    """
    Load all knowledge entries from the knowledge base directory.

    Expected structure:
        FitPulse-KnowledgeBase/
        ├── exercises/        # Standard action markdown files
        ├── error-posture/     # Error posture markdown files
        ├── muscle-activation/ # Muscle activation markdown files
        ├── manifest.json      # Entry index
        └── SOURCES.md         # Source citations
    """
    entries = []

    kb_path = Path(base_path)
    if not kb_path.exists():
        print(f"Knowledge base not found at {kb_path}")
        return entries

    # Load manifest if exists
    manifest_path = kb_path / "manifest.json"
    if manifest_path.exists():
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
            entries.extend(manifest.get("entries", []))

    # Scan markdown files
    for md_file in kb_path.rglob("*.md"):
        if md_file.name == "SOURCES.md":
            continue
        # TODO: Parse markdown into structured chunks
        pass

    print(f"Loaded {len(entries)} knowledge entries")
    return entries


def embed_and_store(entries: list):
    """
    Embed entries via Claude Embedding API and store in Chroma.

    TODO: #6 马锦城 — implement
    - Use anthropic.Client().embeddings.create()
    - Store in Chroma collection "knowledge_vectors"
    """
    print(f"Embedding {len(entries)} entries...")
    # TODO: Implement
    print("Knowledge base initialization complete!")


def main():
    kb_path = os.environ.get(
        "KNOWLEDGE_BASE_PATH",
        str(Path(__file__).parent.parent / "FitPulse-KnowledgeBase"),
    )

    print(f"Initializing knowledge base from: {kb_path}")
    print(f"Chroma host: {settings.CHROMA_HOST}:{settings.CHROMA_PORT}")

    entries = load_knowledge_entries(kb_path)
    if entries:
        embed_and_store(entries)
    else:
        print("No entries found. Skipping embedding.")


if __name__ == "__main__":
    main()