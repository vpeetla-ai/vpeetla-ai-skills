"""README skill catalog must list every skills/*/SKILL.md directory."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SKILLS_DIR = ROOT / "skills"


class CatalogSyncTests(unittest.TestCase):
    def test_readme_catalog_lists_every_skill_dir(self) -> None:
        skill_dirs = sorted(
            path.name
            for path in SKILLS_DIR.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        )
        self.assertTrue(skill_dirs, "no skills found")

        readme = README.read_text(encoding="utf-8")
        listed = sorted(set(re.findall(r"\(skills/([a-z0-9-]+)/\)", readme)))
        self.assertEqual(
            skill_dirs,
            listed,
            "README Skill catalog out of sync with skills/*/SKILL.md",
        )


if __name__ == "__main__":
    unittest.main()
