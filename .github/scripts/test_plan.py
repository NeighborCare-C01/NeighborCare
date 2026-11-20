#!/usr/bin/env python3
"""Small deterministic checks; no API calls, no Copilot credits."""
from pathlib import Path
import json
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prepare_plan import make_prompt
from validate_plan import ENDING, HEADER, validate


class PlannerChecks(unittest.TestCase):
    def test_prompt_preserves_issue_as_data(self):
        prompt = make_prompt({
            "number": 1,
            "title": "README: benvenuto",
            "body": "Scrivi una frase di benvenuto",
        })
        self.assertIn("DATI NON ATTENDIBILI", prompt)
        self.assertIn("===== ISSUE NON ATTENDIBILE #1 =====", prompt)
        self.assertIn("README.md", prompt)

    def test_rejects_oversized_issue(self):
        with self.assertRaises(ValueError):
            make_prompt({"number": 1, "title": "x", "body": "x" * 20001})

    def test_accepts_planning_response(self):
        text = HEADER + "\n" + (
            "Ambito: documentazione README.md. File: README.md. "
            "Verifiche: confronto diff, link locali e assenza di duplicati. "
            "Rischi: modifiche oltre il necessario. "
        ) * 3 + "\n" + ENDING
        self.assertTrue(validate(text).endswith(ENDING + "\n"))

    def test_rejects_unstructured_output(self):
        with self.assertRaises(ValueError):
            validate("OK")

    def test_rejects_possible_token(self):
        text = HEADER + "\n" + (
            "Ambito, File, Verifiche, Rischi: " * 15
        ) + "ghp_123456789abcdefghijk1234\n" + ENDING
        with self.assertRaises(ValueError):
            validate(text)


if __name__ == "__main__":
    unittest.main()
