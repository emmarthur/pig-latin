"""Terminal Pig Latin translator."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from pig_latin_core import english_to_pig_latin  # noqa: E402

print("Igpay Atinlay (Pig Latin)\nEnter your message:")
result = english_to_pig_latin(input("> "))
print(result)
