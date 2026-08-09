# Four-Color Vector Production Standard

Use one consistent `viewBox` per bundle unless the blank requires multiple aspect ratios. Express each palette color as a six-digit hex value. Put printable geometry inside exactly four top-level groups with stable IDs: `color-1` through `color-4`.

Use closed paths and fills whenever possible. Expand strokes and text when reliable tooling is available. Remove hidden objects, empty groups, metadata that exposes private information, linked resources, scripts, animation, gradients, filters, patterns, and embedded images. Avoid self-intersections and duplicate stacked paths where they could confuse slicer import.

Keep features large enough for the user's final physical size and printer setup. When the minimum printable feature is unknown, flag it instead of claiming production readiness. Preserve a clean SVG master and render the PNG from that master so both formats match.

The four colors are a constraint, not fixed brand values. Choose them for the current subject, sufficient contrast, and easy slicer reassignment. Do not count transparency as a fifth color.
