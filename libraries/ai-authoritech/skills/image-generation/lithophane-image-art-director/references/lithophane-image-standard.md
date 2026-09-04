# Lithophane Image Standard

## Objective
Create grayscale source artwork that produces visually strong, dimensional, readable lithophane relief when converted and backlit.

## Aesthetic Target
The preferred look is **dark, detailed, sculpted, high-resolution grayscale** with intentional tonal separation rather than a pale photo filter.

The strongest source images typically combine:
- deep shadow anchors
- bright but limited highlights
- many distinct midtones
- crisp focal features
- directional lighting
- layered objects
- visible material texture
- strong silhouettes
- dense but readable composition

## Tonal Architecture
Think of the grayscale image as a depth map with visual hierarchy.

### Dark Anchors
Use connected dark regions to establish weight and depth. Good examples include hair interiors, deep fabric folds, plaque shadows, background recesses, eye makeup, and negative spaces between objects.

### Midtone Structure
Midtones should not collapse into one gray value. Use several clearly separated gray zones so cheeks, hair waves, fabric, metallic surfaces, glass, and background texture retain dimensionality.

### Highlight Control
Reserve the brightest values for intentional accents. Pearls, gemstones, eyes, gloss, metallic edges, and rim highlights work well because they create obvious light-transmission contrast.

## Strategic Contrast
Do not maximize contrast uniformly.

Use the strongest contrast at:
- the main face or focal subject
- text that must remain readable
- foreground objects
- important silhouettes

Use slightly softer contrast in the background so the image retains visual depth.

## Local Contrast Rule
Every important object should differ in tone from its immediate surroundings. If two adjacent objects are both mid-gray or both near-black, separate them with lighting, edge highlights, shadows, or tonal reassignment.

## Edge Definition
Important features should have crisp, print-readable boundaries. Slightly stronger edge definition is preferred over photographic softness because 3D conversion and printing may soften subtle detail.

## Directional Lighting
Use lighting that creates modeled form: a clear light side, shadow side, and transitions between them. Flat frontal illumination tends to produce weak visual depth.

## Depth Layers
Use at least three perceptual depth zones when the scene supports them:
1. foreground accents
2. primary subject
3. background texture or environment

The foreground should generally be the sharpest. The background should remain detailed but slightly less dominant.

## High-Resolution Standard
Use the largest practical native generation size. High resolution improves the fidelity of:
- hair waves and strands
- facial features
- fabric texture
- typography edges
- jewelry and gemstones
- surface embossing
- grayscale transitions

Preferred source guidance:
- PNG
- 3000+ px on the long edge when practical
- 4K-class or larger for complex artwork when supported
- maintain the target aspect ratio from initial generation
- avoid repeated lossy resizing

High resolution helps preserve detail, but does not compensate for poor contrast, muddy midtones, or weak edge definition.

## Dense Detail vs Noise
Dense compositions can perform beautifully in lithophanes when the detail is structured. Favor recognizable texture and form over random micro-speckle.

Good detail:
- tufted upholstery
- quilt stitching
- pearls
- larger gems
- defined curls
- carved lettering
- metal engraving
- folds and seams

Weak detail:
- tiny low-contrast speckles
- thin hairline text
- busy texture with no tonal separation
- small elements that merge at print scale

## Portrait Standard
Portraits should maintain natural anatomy while slightly strengthening feature readability. Protect the eyes, brows, lips, nostrils, jawline, cheek shadows, and hairline from soft tonal merging.

## Negative Conditions
Avoid:
- washed-out grayscale
- foggy low contrast
- huge pale empty areas
- crushed black regions with no internal detail
- blown highlights with no shape
- adjacent objects with nearly identical gray values
- weak silhouettes
- excessive blur
- tiny decorative elements as the only source of detail
- JPEG artifacts

## Flat Artwork Rule
If the lithophane or lampshade software accepts a normal image, supply a straight, flat rectangular PNG. Do not bake a curved lampshade silhouette into the source image unless specifically required.

## Final Acceptance Test
An image should remain visually understandable when viewed as a small thumbnail. The focal subject, major objects, and darkest/lightest relationships should still read clearly. If the thumbnail becomes a gray mass, revise before lithophane conversion.
