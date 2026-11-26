#!/usr/bin/env python3
"""Analyze a sensor recording and produce summary statistics and a plot."""
import csv
import json
from pathlib import Path
from statistics import mean
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
source = ROOT / config["data_file"]

with source.open(newline="", encoding="utf-8") as handle:
    measurements = list(csv.DictReader(handle))

times = [float(row[config["time_column"]]) for row in measurements]
values = [float(row[config["signal_column"]]) for row in measurements]
if not times:
    raise ValueError("No measurements found.")

out = ROOT / config["output_dir"]
out.mkdir(parents=True, exist_ok=True)
(out / "summary.txt").write_text(
    f"Samples: {len(values)}\n"
    f"Mean amplitude (V): {mean(values):.5f}\n"
    f"Minimum amplitude (V): {min(values):.5f}\n"
    f"Maximum amplitude (V): {max(values):.5f}\n",
    encoding="utf-8",
)

width, height = 750, 360
pad_l, pad_r, pad_t, pad_b = 86, 36, 28, 70
min_t, max_t = min(times), max(times)
min_v, max_v = min(values), max(values)
if max_t == min_t or max_v == min_v:
    raise ValueError("Need varying time and amplitude values.")
points = " ".join(
    f"{pad_l + (t-min_t)/(max_t-min_t)*(width-pad_l-pad_r):.1f},"
    f"{height-pad_b-(v-min_v)/(max_v-min_v)*(height-pad_t-pad_b):.1f}"
    for t, v in zip(times, values)
)
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="white"/>
<path d="M{pad_l} {pad_t} V{height-pad_b} H{width-pad_r}" fill="none" stroke="#17324D" stroke-width="2"/>
<polyline points="{escape(points)}" fill="none" stroke="#00747A" stroke-width="3"/>
<text x="{width/2}" y="{height-18}" text-anchor="middle" font-family="Arial" font-size="19">Time (s)</text>
<text x="23" y="{height/2}" transform="rotate(-90 23 {height/2})" text-anchor="middle" font-family="Arial" font-size="19">Amplitude (V)</text>
<text x="{pad_l}" y="{height-41}" font-family="Arial" font-size="14">{min_t:.2f}</text>
<text x="{width-pad_r}" y="{height-41}" text-anchor="end" font-family="Arial" font-size="14">{max_t:.2f}</text>
</svg>"""
(out / "signal.svg").write_text(svg + "\n", encoding="utf-8")
print(f"Analysis complete. Files written to {out}")
