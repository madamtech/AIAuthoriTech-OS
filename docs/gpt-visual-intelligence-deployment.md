# Deploying the GPT Visual Intelligence Enhancement

## What this repository change does
The enhancement adds a reusable visual decision and quality-control layer to AIAuthoriTech-OS. It connects a host GPT's existing evaluation behavior to the repository's established image-generation skill library.

It does not replace the host GPT and does not independently render images.

## What must be configured for each GPT
For every live GPT or agent, record:
1. verified GPT name and owner;
2. purpose and primary audience;
3. current instructions source or version;
4. enabled tools, especially image creation or editing capability;
5. knowledge and action dependencies;
6. applicable business and brand boundaries;
7. evaluation prompt or quality policy;
8. installation method for repository skills;
9. deployment date and validation evidence.

Then add a record to `registries/gpts.json` and map the GPT to `gpt-visual-intelligence-enhancement`.

## Installation pattern
Add an instruction or runtime loader equivalent to:

> Preserve this GPT's established role, rules, and expertise. For visual creation or editing requests, activate the AIAuthoriTech-OS `gpt-visual-intelligence-enhancement` skill. Route first through `personalized-capability-framework`, apply the GPT's standard evaluation process, preserve explicit locks, use an available image-capable tool, evaluate the result, and revise only the requested or failed elements.

Where the runtime supports repository-native skills, load the SKILL.md directly. Where it does not, include the deployment instruction and the relevant skill package in the GPT's approved knowledge or application layer.

## How to use it
The user can speak naturally:
- “Create a premium product image for this fragrance.”
- “Touch up this picture without changing her facial features.”
- “Make a transparent design for a one-color 3D print.”
- “Create a NetExam course thumbnail that matches the existing catalog.”
- “Change only the background; everything else stays exactly the same.”

The host GPT should automatically:
1. identify the project and intended use;
2. preserve the host GPT's domain rules;
3. identify references and locks;
4. compile a production-ready visual brief;
5. route the appropriate image-generation skills;
6. call the image tool when available;
7. evaluate the result against the request;
8. preserve approved elements during revision.

## Expected results
Compared with a basic image-generation instruction, the enhancement is designed to improve:
- first-pass alignment with the user's actual request;
- preservation of faces, products, wording, layouts, and other locked elements;
- brand separation across AI AuthoriTech, i-PRO, MadamAllure, and project-specific campaigns;
- technical decisions for transparency, aspect ratio, print, course thumbnails, and 3D-reference artwork;
- controlled revisions that do not unnecessarily redesign the full image;
- honesty about model and file-format limitations.

## Validation scenarios
Each mapped GPT should pass at least these checks:
1. New generation with incomplete optional details proceeds using labeled safe assumptions.
2. Editing without a usable source image requests the image rather than inventing a target.
3. “Change only X” freezes all other approved elements.
4. Exact text is treated as a lock and verified after generation.
5. Business branding does not leak into another business or project.
6. The GPT does not claim that a raster output is a true vector or print-ready file without verification.
7. One-at-a-time delivery is followed when requested.

## GPT inventory status
The repository did not contain a dedicated, authoritative live Custom GPT registry at the time of this implementation. `registries/gpts.json` has been added as the governed source of truth, but live GPT records must be imported from verified configurations rather than reconstructed from memory.
