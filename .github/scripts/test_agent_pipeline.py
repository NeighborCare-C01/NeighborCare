#!/usr/bin/env python3
"""Offline safety checks for the Copilot orchestration scripts."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parent))
from agent_changes import allowed_paths, build_prompt
from prepare_review import validate
from prepare_plan import make_prompt

class SafetyChecks(unittest.TestCase):
    def test_approved_readme_is_allowed(self):
        self.assertEqual(allowed_paths("README.md"), ["README.md"])

    def test_approved_backend_is_allowed(self):
        self.assertEqual(allowed_paths("backend/src/main/java/x/A.java"),["backend/src/main/java/x/A.java"])

    def test_protected_paths_rejected(self):
        for path in (".github/workflows/ci.yml", "AGENTS.md", "docs/rad/C01_RAD.pdf",
                     "docs/sdd/C01_SDD.pdf", "../README.md", "/etc/passwd"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                allowed_paths(path)

    def test_implementation_prompt_has_authorized_scope(self):
        text=build_prompt({"issue":{"number":10,"title":"Saluto","body":"README change"},
                           "plan":"Plan", "approval":"APPROVAZIONE TM",
                           "allowed_paths":"README.md"},"implementatore")
        self.assertIn("README.md",text)
        self.assertIn("INPUT NON ATTENDIBILI",text)

    def test_tester_prompt_instructs_independence(self):
        text=build_prompt({"issue":{"number":10,"title":"Test","body":"Test Frame TF01"},
                           "plan":"Approved","approval":"Separate reviewer"},"tester")
        self.assertIn("RISULTATI ATTESI",text)
        self.assertIn("non",text.lower())

    def test_plan_prompt_has_no_write_rule(self):
        text=make_prompt({"number":10,"title":"README","body":"Aggiungi frase"})
        self.assertIn("Non eseguire implementazioni",text)

    def test_bad_review_rejected(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/"in.md"
            p.write_text("OK",encoding="utf-8")
            with self.assertRaises(ValueError):
                validate(p,Path(directory)/"out.md",7)

if __name__=="__main__":
    unittest.main()
