# Lithophane Tool Profiles

## Purpose
Use this reference whenever the user wants to convert an approved source image into a printable lithophane model. The two primary tools are:

1. **ItsLitho** (`itslitho.com` / `tool.itslitho.com`)
2. **MakerWorld MakerLab — Make My Lithophane** (`makerworld.com/makerlab/makeMyLithophane`)

Treat image creation and lithophane-model generation as separate stages. First optimize the image; then give the user tool-specific model settings and slicer settings for the requested physical object.

## Required Intake Before Giving Final Settings
Resolve as many of these as possible from the user's request and prior context:
- tool: ItsLitho or MakerWorld MakerLab
- object type: flat panel, framed artwork, lightbox, night light, lampshade, cylinder, arc, round lamp, bell, sphere, etc.
- desired physical size in mm
- printer model and nozzle diameter
- filament type and color
- light source and available internal clearance
- whether a frame, slot, ledge, or mounting interface must fit an existing printed part
- whether the image is monochrome or CMYK/color lithophane

If exact fit dimensions are required and not known, ask for them rather than inventing a size. If the user only asks for a general small/cute lamp, provide a practical starter size and label it as a starting profile that can be resized.

---

# ItsLitho — Primary Profile

## Tool Scope
ItsLitho supports multiple model shapes including Plane, Cylinder, Sphere, Arc, Pumpkin, Vases, Bell, and Lamp. It also provides frame/border controls and a quality control based on mm per pixel.

## Default Monochrome Lithophane Starting Profile
Use these as safe starting values when the user has not supplied a proven filament-specific profile:

- **Minimum thickness:** 0.8 mm
- **Maximum thickness:** 3.0–3.2 mm
- **Resolution / mm per pixel:** 0.10 mm/px for high-detail work when practical
- **Image mode:** grayscale for monochrome lithophanes
- **Preview/model quality:** use a lower preview resolution only while editing; restore high/final quality before download
- **Frame:** only when the final object or holder needs one
- **Angle:** 0° for a simple flat reinforced frame unless a specific frame design calls for an angled edge

Do not blindly use 5 mm maximum thickness for every project. Some published ItsLitho projects use 5 mm for specific lightbox/frame designs, but 3.0–3.2 mm is a better general monochrome starting range for strong contrast with typical white PLA. Adjust for filament transmission and the actual lamp/frame design.

## Small Cute Lamp — Starter Profile
When the user asks for a cute/small lamp and does not give dimensions, start around:

- **Overall lithophane height:** 85–110 mm
- **Diameter / width:** approximately 75–100 mm depending on shape
- **Minimum thickness:** 0.8 mm
- **Maximum thickness:** 3.0–3.2 mm
- **Resolution:** 0.10 mm/px
- **Shape:** choose Lamp, Cylinder, Arc, or another appropriate ItsLitho shape based on the user's design intent
- **Frame/base:** size to the actual LED puck, tea light, socket, or printed base; do not guess the mounting diameter if a specific light is being used

For a cylindrical or lamp form, ensure the user's printer build volume can accommodate the full height and diameter.

## Flat Framed Artwork — Starter Profile
For a flat image intended for a frame or backlit panel:

- **Shape:** Plane
- **Minimum thickness:** 0.8 mm
- **Maximum thickness:** 3.0–3.2 mm
- **Resolution:** 0.10 mm/px
- **Frame:** enable only if the frame itself needs printed stiffness or a matching edge
- **Frame thickness/depth:** derive from the receiving groove or holder dimensions
- **Image crop:** match the exact physical aspect ratio before export

A published framed ItsLitho example uses 0.8 mm minimum, 3.2 mm maximum, and a reinforcing frame; another square lightbox example uses 0.8 mm minimum, 5 mm maximum, 0.1 mm/px, and a 5 mm frame. Treat those as project-specific examples, not universal defaults.

---

# MakerWorld MakerLab — Make My Lithophane

## Tool Scope
MakerWorld MakerLab's **Make My Lithophane** is the primary MakerWorld lithophane generator. It is especially useful when the user wants a MakerWorld/Bambu-oriented workflow, including standard lithophane panels, compatible frames, lightboards, and CMYK/color workflows.

## Model-Creation Guidance
When using MakerLab:
- crop the source image to the required final aspect ratio before model generation
- choose monochrome or color/CMYK intentionally
- size the lithophane to the receiving frame or lightboard rather than scaling later when exact fit matters
- retain the highest practical image detail during upload
- use the final generated model dimensions as the source of truth before slicing
- if using a MakerWorld frame or lightbox model, follow that model's specified lithophane dimensions exactly

## Monochrome Print Starting Profile
For a typical Bambu-oriented monochrome lithophane:

- **Filament:** white PLA or another tested translucent/light-colored PLA
- **Layer height:** 0.10–0.12 mm for strong detail
- **Infill:** 100% or effectively solid
- **Walls:** enough to ensure the lithophane region is solid; published MakerWorld profiles commonly use 2–4 walls with 100% infill, while all-wall methods are also valid
- **Supports:** normally none for a simple flat vertical lithophane; use only where the frame/base geometry requires them
- **Speed:** slower visible-wall printing is preferred for detail; around 30–45 mm/s is a strong quality starting point for the lithophane itself

If the user is using a 0.2 mm nozzle for maximum detail, 0.04–0.08 mm layers may be appropriate but print time increases sharply. For a 0.4 mm nozzle, 0.10–0.12 mm is a practical high-detail starting range.

## MakerWorld Frame / Lightboard Rule
MakerWorld models often target specific physical inserts and LED backlight boards. Never assume a generic panel size when the user references a specific MakerWorld frame, lightbox, or lamp model. Resolve the model's required width, height, maximum thickness, slot depth, and lightboard size before recommending final values.

---

# Slicer Settings — General Lithophane Baseline

Unless a tested printer/filament profile overrides these values, recommend:

- **Layer height:** 0.10–0.12 mm
- **Infill:** 100% / fully solid lithophane body
- **Print speed:** approximately 30–45 mm/s for the lithophane detail region
- **Orientation for a flat panel:** vertical/on edge when practical for best XY image detail; add brim/support stabilization as needed
- **Seam:** place away from the image face or on the back/least-visible edge
- **Filament:** white PLA is the standard monochrome starting material; silver/gray may also work, but thickness should be tuned to transmission
- **Cooling and temperatures:** begin with the filament manufacturer's proven PLA profile, then tune only if print artifacts appear

Do not give nozzle temperature, bed temperature, flow ratio, or pressure advance as universal lithophane constants; those depend on the actual filament and printer profile.

## Bambu P1S Baseline
When the user is printing on a Bambu Lab P1S with a 0.4 mm nozzle and standard white PLA:

- 0.10–0.12 mm layer height
- 100% infill or an all-wall strategy that produces a fully solid lithophane
- slow the lithophane's visible/outer wall to roughly 30–45 mm/s
- use a brim for tall thin vertical panels if stability requires it
- place the seam on the back or least-visible edge
- disable unnecessary supports on the image surface

Treat these as starting values and preserve any previously calibrated filament-specific temperature/flow settings.

---

# Tool-Specific Response Contract

When the user says, for example, **“I want to make a small lamp in ItsLitho”**, return the settings in this order:

1. **Source image** — aspect ratio, orientation, image size, grayscale/color guidance
2. **ItsLitho or MakerLab model settings** — shape, physical dimensions, min/max thickness, resolution, frame/base/interface values
3. **Export** — STL/3MF or tool-supported format
4. **Slicer settings** — printer/nozzle, layer height, walls/infill, orientation, speed, brim/support, seam
5. **Lighting/fit check** — light-source clearance and heat/safety note
6. **QA before printing** — preview contrast, wall solidity, dimensions, frame fit, and slice inspection

Always distinguish between **generator settings** and **slicer settings** so the user knows where each value belongs.

# Safety and Lighting
Prefer low-heat LED lighting for lithophane lamps and framed backlit art. Do not design PLA lithophane parts to sit against high-heat incandescent bulbs. Maintain clearance around the light source and follow the light hardware's rated enclosure/ventilation requirements.
