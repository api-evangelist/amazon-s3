#!/usr/bin/env python3
"""Build the Amazon S3 API tube-style map.

S3 has 3 OpenAPI surfaces (REST, Control, Tables) but each carries 5–7
tag-based functional areas; 17 of those are mapped here as stations onto
4 product lines:

- Storage — Buckets: top arc (REST API)
- Storage — Operations: short arc (REST API + Control API)
- Access & Security: sine wave (REST API + Control API)
- Tables — Analytics: CLOSED PENTAGON LOOP (Tables API)

Each station links to whichever of the 3 apis.io pages backs its tag.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Multi-Region Access Points": "Multi-Region APs",
}

LINES = [
    {
        "name": "Storage — Buckets",
        "color": "#E0245E",   # red
        # Concave-up arc — middle stations sit higher than the endpoints.
        "stations": [
            ("Buckets",              (310, 200)),
            ("Bucket Configuration", (510, 175)),
            ("Objects",              (710, 175)),
            ("Multipart Upload",     (910, 200)),
        ],
    },
    {
        "name": "Storage — Operations",
        "color": "#E68B1F",   # orange
        # Short concave-up arc parallel below.
        "stations": [
            ("Tagging",         (380, 320)),
            ("Storage Lens",    (610, 290)),
            ("Batch Operations",(840, 320)),
        ],
    },
    {
        "name": "Access & Security",
        "color": "#1E5BD0",   # royal blue
        # Sine wave across the middle of the canvas.
        "stations": [
            ("Access Control",              (260, 480)),
            ("Access Grants",               (430, 445)),
            ("Access Points",               (600, 480)),
            ("Public Access Block",         (770, 445)),
            ("Multi-Region Access Points",  (940, 480)),
        ],
    },
    {
        "name": "Tables — Analytics",
        "color": "#0E9D6E",   # forest green
        # Closed pentagon — 5 stations evenly spaced around a circle.
        # Center (640, 700), radius 80. Anchored "top" first, going clockwise.
        "closed": True,
        "stations": [
            ("Table Buckets",      (640, 620)),  # 12 o'clock
            ("Tables",             (716, 675)),  # ~2 o'clock
            ("Table Maintenance",  (687, 765)),  # ~5 o'clock
            ("Table Policy",       (593, 765)),  # ~7 o'clock
            ("Namespaces",         (564, 675)),  # ~10 o'clock
        ],
    },
]

# All stations are sub-areas (tags) within one of three top-level APIs.
# Each link points to whichever apis.io page backs that tag.
REST_API = "https://apis.apis.io/apis/amazon-s3/amazon-s3-rest-api/"
CONTROL_API = "https://apis.apis.io/apis/amazon-s3/amazon-s3-control-api/"
TABLES_API = "https://apis.apis.io/apis/amazon-s3/amazon-s3-tables-api/"

URL_OVERRIDES = {
    # REST API
    "Buckets":                    REST_API,
    "Bucket Configuration":       REST_API,
    "Objects":                    REST_API,
    "Multipart Upload":           REST_API,
    "Tagging":                    REST_API,
    "Access Control":             REST_API,
    # Control API
    "Storage Lens":               CONTROL_API,
    "Batch Operations":           CONTROL_API,
    "Access Grants":              CONTROL_API,
    "Access Points":              CONTROL_API,
    "Public Access Block":        CONTROL_API,
    "Multi-Region Access Points": CONTROL_API,
    # Tables API
    "Table Buckets":      TABLES_API,
    "Tables":             TABLES_API,
    "Table Maintenance":  TABLES_API,
    "Table Policy":       TABLES_API,
    "Namespaces":         TABLES_API,
}


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)

    build_subway(
        title="The Amazon S3 API · Underground Map",
        subtitle=f"{n_unique} functional areas · 3 APIs · {len(LINES)} subway lines · "
                 f"click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: amazon-s3/openapi/*.yml · github.com/api-evangelist/amazon-s3",
        out_dir=Path(__file__).resolve().parent,
        out_basename="amazon-s3-subway-map",
        provider_id="amazon-s3",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
