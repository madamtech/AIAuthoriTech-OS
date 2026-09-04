# Profile A — Cardi Bag Lamp Reference

## Purpose
Profile A is the first known-good reference family for the user's 3D printed lamp workflow. It is a **reference profile, not a mandatory size**. The Cardi bag lamp should be treated as the largest/reference-scale member unless the user explicitly requests something larger.

Use this profile to preserve successful interface relationships while allowing smaller decorative bases, shorter/taller necks, different lamp-base silhouettes, and different shade sizes.

## Source Files
Primary physical source files supplied by the user:

- `cardi bag lamp(1).3mf` — Bambu Studio project containing the decorative bag base and the original neck as a separate printable object/plate.
- `Cardi LampShade.zip` — contains `Cardi LampShade.stl`, the completed shade geometry.

## Verified Mesh Dimensions
Dimensions below were read directly from the supplied mesh geometry and should be treated as reference bounding-box dimensions, not automatically as mating-interface diameters.

### Decorative Cardi Bag Base
Mesh object dimensions:
- **X:** 217.097 mm
- **Y / thickness:** 77.0004 mm
- **Z:** 228.412 mm

The user's recollection of roughly 77.5 mm thickness is therefore consistent with the actual mesh; the model bounding-box thickness is approximately **77.0 mm**.

### Original Neck
The 3MF includes a separate object named **`Original Neck (1).stl`**.

Overall mesh dimensions:
- **X:** 82.5510 mm
- **Y:** 82.5500 mm
- **Z / overall height:** 93.6640 mm

Important observed radial features from the neck mesh:
- largest outside diameter / flange region: approximately **82.55 mm**
- lower annular region: approximately **77.47–77.55 mm outside diameter**
- upper stem/ring region: approximately **29.21 mm diameter** at the top boundary

These values describe observed mesh geometry only. Before manufacturing a new mating component, derive the actual receiver, insertion, shoulder, bore, and clearance dimensions from the mesh or a physical measurement rather than assuming every observed diameter is a fit diameter.

### Completed Cardi Lampshade STL
Bounding box read from `Cardi LampShade.stl`:
- **X:** 159.0177 mm
- **Y:** 159.0100 mm
- **Z / height:** 149.0000 mm

This means the completed STL is approximately **159 mm outside envelope x 149 mm high**.

If earlier design notes, mockups, or generator settings list a different nominal shade diameter, use the **actual supplied STL geometry as the physical source of truth** for Profile A unless the user intentionally chooses to rebuild the shade.

## Lithophane Artwork References
The Cardi shade family used two coordinated high-detail monochrome glam lithophane panels. Preserve the visual treatment as the Profile A art direction:

### Panel A — Ah Ha portrait composition
Reference characteristics:
- grayscale/high-contrast luxury-glam portrait treatment
- Black woman with long sculpted waves
- `Ah Ha!!!` typography
- perfume bottle labeled `Angel Nova`
- pearls, diamonds/gems, money bag, cash, and tufted background
- deep blacks, luminous highlights, rich midtones, strong edge definition, embossed/metallic appearance

Current working image references from the project history include:
- `ChatGPT Image Aug 24, 2026, 05_24_38 PM(3).png`
- `glamorous_monochrome_ah_ha_collage.png`
- `ah_ha_silver_glamour_sticker.png`
- `ah_ha_luxury_glamour_plaque.png`

### Panel B — jeweled microphone/music composition
Reference characteristics:
- grayscale/high-contrast jeweled microphone centerpiece
- pearl/diamond framing and dense glam detail
- money/cash and perfume/luxury accents
- script/music-themed typography
- tufted background with metallic/embossed dimensional shading

Current working image references from the project history include:
- `ChatGPT Image Aug 24, 2026, 06_03_59 PM(2).png`
- `monochrome_rhinestone_rapper_bling_collage.png`
- `silver_bling_music_collage_panel.png`
- `monochrome_jeweled_microphone_music_poster.png`

For new lamps, these images are style and tonal references. The artwork itself may change while retaining the lithophane-quality rules in the Lithophane Image Art Director.

## Profile A Scaling Policy
Profile A should **not** be uniformly scaled when creating a smaller lamp.

### Lock unless intentionally re-engineered
- electrical-hardware interface
- cable path / center bore
- receiver and insertion geometry
- socket/nipple/LED hardware dimensions
- mating neck-to-base dimensions
- mating neck-to-shade dimensions
- required print clearances

### May be resized or redesigned
- decorative base body width/height/thickness
- visible neck height
- visible neck outside shape/taper/fluting
- shade diameter/width and height
- decorative trim and sculptural treatment

## Downscale Strategy
When a smaller lamp is requested:
1. choose a target overall lamp size first
2. keep hardware dimensions fixed unless different hardware is selected
3. determine whether the Profile A neck interface can remain unchanged
4. reduce the decorative base around that interface rather than blindly scaling the entire 3MF
5. resize or regenerate the shade independently
6. create a new neck variation only if the new proportions need one
7. test-print the receiver/neck/shade interface before committing to the full premium print

## Variant Naming
Use this naming convention when derivatives are created:
- **Profile A-L** — original Cardi/reference-large scale
- **Profile A-M** — medium derivative using the same interface family
- **Profile A-S** — small derivative using the same interface family
- **Profile A-XS** — compact derivative using the same interface family

If the functional interface changes materially, create a new family such as Profile B rather than calling it a scaled Profile A.

## Production Routing
Use only the user's two standard printer/slicer environments unless explicitly overridden:
- **Bambu Lab P1S -> Bambu Studio**
- **FlashForge Adventurer 5M -> FlashForge Studio**

## Status
**Profile A physical reference established from supplied 3MF and STL geometry.**

The original neck is confirmed to be present in the 3MF and is now part of the reusable reference profile.