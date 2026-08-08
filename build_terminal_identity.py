"""Build one self-contained terminal-identity.svg from the three animated panels.

SVG files referenced with a relative <image href> are blocked by some browsers when
the parent SVG is opened directly. This builder embeds each panel as a base64 data
URL, keeping the final file portable for localhost and GitHub README rendering.
"""

from __future__ import annotations

import base64
from pathlib import Path


ROOT = Path(__file__).parent
OUTPUT = ROOT / "terminal-identity.svg"
AVATAR = ROOT / "ascii-portrait-animated.svg"
NAME = ROOT / "name-banner-animated.svg"
CONTRIBUTIONS = ROOT / "contributions-animated.svg"


def data_url(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def main() -> None:
    avatar = data_url(AVATAR)
    name = data_url(NAME)
    contributions = data_url(CONTRIBUTIONS)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="480" viewBox="0 0 860 480" role="img" aria-labelledby="title description">
  <title id="title">Terminal Identity — Ritik Chawla</title>
  <desc id="description">One terminal frame containing an animated ASCII avatar, name banner, and GitHub contribution graph.</desc>
  <defs>
    <linearGradient id="window" x1="0" y1="0" x2="0" y2="1">
      <stop stop-color="#171d1a"/><stop offset="1" stop-color="#101512"/>
    </linearGradient>
  </defs>
  <rect x="5" y="8" width="850" height="472" rx="25" fill="url(#window)"/>
  <rect x="5" y="8" width="850" height="57" rx="25" fill="#1a211d"/>
  <rect x="5" y="40" width="850" height="25" fill="#1a211d"/>
  <circle cx="30" cy="38" r="6" fill="#ff5f56"/><circle cx="51" cy="38" r="6" fill="#ffbd2e"/><circle cx="72" cy="38" r="6" fill="#27c93f"/>
  <text x="99" y="43" fill="#aeb8b1" font-family="Arial, sans-serif" font-size="17" font-weight="700">Terminal Identity</text>
  <rect x="21" y="82" width="352" height="267" rx="14" fill="#111722"/>
  <rect x="383" y="82" width="468" height="267" rx="14" fill="#111722"/>
  <image x="58" y="82" width="278" height="267" preserveAspectRatio="xMidYMid slice" href="{avatar}"/>
  <image x="428" y="85" width="378" height="260" preserveAspectRatio="xMidYMid meet" href="{name}"/>
  <rect x="21" y="359" width="830" height="102" rx="14" fill="#111722"/>
  <image x="245" y="359" width="380" height="102" preserveAspectRatio="xMidYMid meet" href="{contributions}"/>
</svg>
'''
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"Wrote self-contained {OUTPUT.name} ({OUTPUT.stat().st_size:,} bytes).")


if __name__ == "__main__":
    main()
