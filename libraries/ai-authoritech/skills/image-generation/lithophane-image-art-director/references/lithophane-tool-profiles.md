# Lithophane Tool Profiles

## Purpose
Use this reference whenever the user wants to convert an approved source image into a printable lithophane model.

The two primary lithophane-generation tools are:
1. **ItsLitho** (`itslitho.com` / `tool.itslitho.com`)
2. **MakerWorld MakerLab — Make My Lithophane** (`makerworld.com/makerlab/makeMyLithophane`)

The user's two primary print environments are:
1. **Bambu Lab P1S** using **Bambu Studio**
2. **FlashForge Adventurer 5M** using **FlashForge Studio**

Treat image creation, lithophane-model generation, and slicing as separate stages. First optimize the image; then generate the model in ItsLitho or MakerLab; then provide slicer settings for the selected approved printer.

## Required Intake Before Giving Final Settings
Resolve as many of these as possible from the user's request and prior context:
- tool: ItsLitho or MakerWorld MakerLab
- object type: flat panel, framed artwork, lightbox, night light, lampshade, cylinder, arc, round lamp, bell, sphere, etc.
- desired physical size in mm
- printer: P1S or Adventurer 5M
- nozzle diameter
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
- **Preview/model quality:** use lower preview resolution only while editing; restore high/final quality before download
- **Frame:** only when the final object or holder needs one
- **Angle:** 0° for a simple flat reinforced frame unless a specific frame design calls for an angled edge

Do not blindly use 5 mm maximum thickness for every project. Treat thicker profiles as project-specific and adjust for filament transmission and the actual lamp/frame design.

## Small Cute Lamp — Starter Profile
When the user asks for a cute/small lamp and does not give dimensions, start around:
- **Overall lithophane height:** 85–110 mm
- **Diameter / width:** approximately 75–100 mm depending on shape
- **Minimum thickness:** 0.8 mm
- **Maximum thickness:** 3.0–3.2 mm
- **Resolution:** 0.10 mm/px
- **Shape:** choose Lamp, Cylinder, Arc, or another appropriate ItsLitho shape based on design intent
- **Frame/base:** size to the actual LED puck, tea light, socket, or printed base; do not guess the mounting diameter if a specific light is being used

## Flat Framed Artwork — Starter Profile
For a flat image intended for a frame or backlit panel:
- **Shape:** Plane
- **Minimum thickness:** 0.8 mm
- **Maximum thickness:** 3.0–3.2 mm
- **Resolution:** 0.10 mm/px
- **Frame:** enable only if the frame itself needs printed stiffness or a matching edge
- **Frame thickness/depth:** derive from the receiving groove or holder dimensions
- **Image crop:** match the exact physical aspect ratio before export

---

# MakerWorld MakerLab — Make My Lithophane

## Tool Scope
MakerWorld MakerLab's **Make My Lithophane** is the primary MakerWorld lithophane generator. It is especially useful for standard lithophane panels, compatible frames, lightboards, and CMYK/color workflows.

## Model-Creation Guidance
When using MakerLab:
- crop the source image to the required final aspect ratio before model generation
- choose monochrome or color/CMYK intentionally
- size the lithophane to the receiving frame or lightboard rather than scaling later when exact fit matters
- retain the highest practical image detail during upload
- use the final generated model dimensions as the source of truth before slicing
- if using a MakerWorld frame or lightbox model, follow that model's specified lithophane dimensions exactly

## Monochrome Starting Profile
- **Filament:** white PLA or another tested translucent/light-colored PLA
- **Layer height:** 0.10–0.12 mm for strong detail with a 0.4 mm nozzle
- **Infill/body:** fully solid; 100% infill or validated all-wall strategy
- **Walls:** enough to ensure the lithophane region remains solid
- **Supports:** normally none for a simple flat vertical lithophane; use only where frame/base geometry requires them
- **Visible-detail speed:** approximately 30–45 mm/s as a quality-oriented starting range

For a 0.2 mm nozzle, finer layers may be appropriate but print time increases sharply. Do not assume a generic panel size for a specific MakerWorld frame or lightbox.

---

# General Lithophane Slicer Baseline

Unless a tested printer/filament profile overrides these values, recommend:
- **Layer height:** 0.10–0.12 mm with a 0.4 mm nozzle
- **Body:** 100% / fully solid lithophane
- **Visible-detail speed:** approximately 30–45 mm/s as a quality-first starting point
- **Flat-panel orientation:** vertical/on edge when practical for image detail, stabilized as needed
- **Seam:** back or least-visible edge
- **Supports:** avoid on the image surface unless geometry requires them
- **Filament:** white PLA is the standard monochrome starting material
- **Temperature/flow:** use the tested/calibrated filament profile rather than universal numbers

## Bambu Lab P1S — Bambu Studio
When printing on a **Bambu Lab P1S**:
- use Bambu Studio terminology and controls
- start at 0.10–0.12 mm layers with a 0.4 mm nozzle
- keep the lithophane fully solid
- slow visible/outer lithophane walls to roughly 30–45 mm/s when quality requires it
- use a brim for tall thin vertical panels if stability requires it
- place the seam on the back or least-visible edge
- disable unnecessary support on the image surface
- preserve calibrated filament temperature, flow, and pressure settings
- inspect solidity, seam placement, color/material assignment, and first-layer stability in Preview

## FlashForge Adventurer 5M — FlashForge Studio
When printing on a **FlashForge Adventurer 5M**:
- use FlashForge Studio terminology and controls
- start at 0.10–0.12 mm layers with a 0.4 mm nozzle for high-detail monochrome work
- keep the lithophane fully solid using the appropriate shell/infill strategy in FlashForge Studio
- use approximately 30–45 mm/s as a quality-first visible-wall/detail starting range when the selected filament profile allows it
- orient flat panels vertically/on edge when practical and stabilize tall narrow panels with brim/adhesion support when needed
- place the seam on the back or least-visible edge where the slicer permits
- avoid supports touching the image face unless the model requires them
- preserve tested filament temperature and flow settings instead of copying Bambu values
- inspect wall solidity, support contacts, small isolated features, and first-layer stability before printing

## Cross-Printer Rule
Do not copy every numeric field directly between Bambu Studio and FlashForge Studio. Preserve the same **quality intent**—fine layers, solid body, controlled visible-wall speed, protected image face, stable vertical orientation—and map that intent to the correct slicer controls.

---

# Tool-Specific Response Contract

When the user says, for example, **“I want to make a small lamp in ItsLitho”**, return the settings in this order:
1. **Source image** — aspect ratio, orientation, image size, grayscale/color guidance
2. **ItsLitho or MakerLab model settings** — shape, physical dimensions, min/max thickness, resolution, frame/base/interface values
3. **Export** — STL/3MF or tool-supported format
4. **Printer / slicer selection** — P1S + Bambu Studio or Adventurer 5M + FlashForge Studio
5. **Slicer settings** — nozzle, layer height, walls/infill, orientation, speed, brim/support, seam
6. **Lighting/fit check** — light-source clearance and heat/safety note
7. **QA before printing** — preview contrast, wall solidity, dimensions, frame fit, and slice inspection

Always distinguish between **generator settings** and **slicer settings** so the user knows where each value belongs.

# Safety and Lighting
Prefer low-heat LED lighting for lithophane lamps and framed backlit art. Do not design PLA lithophane parts to sit against high-heat incandescent bulbs. Maintain clearance around the light source and follow the light hardware's rated enclosure/ventilation requirements.
