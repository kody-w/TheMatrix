# Blog Post Image Prompt Generator

**Purpose**: Generate compelling image prompts for Gemini API that support blog post content

**Usage**: After ghostwriter generates blog content, use this guide to create visual assets

---

## Image Generation Strategy for Kody's Content

### Visual Style Guidelines

Based on Kody's professional brand and content focus:

**Style**: Modern, professional, minimalist tech illustration
**Color Palette**: Blues, purples, teals (Microsoft brand-aligned)
**Mood**: Optimistic, forward-thinking, sophisticated
**Avoid**: Cartoonish, overly literal, stock photo aesthetic

### Content Type → Visual Style Mapping

**AI Agent / Orchestration Posts**:
- Abstract network visualizations
- Conductor/orchestra metaphors (literal or abstract)
- Node-and-edge diagrams with visual appeal
- Futuristic command centers

**Enterprise AI / Copilot Posts**:
- Professional office environments with holographic interfaces
- Microsoft product UI elements (stylized)
- Business professionals using AI assistants
- Workflow diagrams with visual flow

**Multi-Agent Systems Posts**:
- Multiple AI entities collaborating
- Beatles band performing (metaphor visualization)
- Orchestra with conductor (metaphor visualization)
- Parallel processing visual metaphors

**Productivity / Automation Posts**:
- Before/after transformations
- Inbox organization visuals
- Time-saving metaphors (hourglass, calendar)
- Personal workspace optimization

---

## Prompt Template Structure

```
Generate a [style] image depicting [core concept] with [specific elements].
The image should convey [mood/emotion] and feature [visual details].
Style: [artistic direction].
Avoid: [unwanted elements].
```

---

## Example Image Prompts by Blog Topic

### 1. Multi-Agent Orchestration / Conductor Architecture

**Prompt**:
```
Generate a modern, minimalist illustration of an AI conductor orchestrating multiple specialized agents. Show a central conductor figure (abstract, holographic) surrounded by 6-8 floating AI agent nodes, each with distinct visual characteristics representing different specializations. The agents are connected by glowing data streams forming a network. Use a color palette of deep blues, purples, and cyan. The scene should feel like a futuristic command center with depth and dimension. Style: sleek digital art, professional tech illustration. Avoid: cartoonish elements, literal musicians.
```

### 2. Agent Storytelling / Natural Language Interfaces

**Prompt**:
```
Generate a professional illustration showing natural language commands transforming into executable business workflows. Visualize spoken words (in elegant typography) flowing from left side, passing through an AI processing node (glowing geometric core), and emerging as structured workflow diagrams on right side. Use a clean, modern aesthetic with gradients of blue and teal. Include subtle particle effects suggesting intelligent processing. Style: infographic meets digital art, Microsoft-aligned professional. Avoid: overly complex diagrams, stock photo people.
```

### 3. Prompt Transplantation / Inbox Automation

**Prompt**:
```
Generate a split-screen before/after visualization. Left side: chaotic inbox with thousands of overlapping email icons in disarray, dark and cluttered. Right side: organized, zen-like inbox with emails neatly sorted into glowing folders, bright and calm. Center: AI agent icon (abstract geometric shape) orchestrating the transformation with flowing data streams. Color scheme: left side muted grays/reds (chaos), right side blues/greens (order). Style: modern minimalist illustration with depth. Avoid: literal screenshots, generic office imagery.
```

### 4. Demand-Driven Development

**Prompt**:
```
Generate an abstract visualization of user commands creating organic development demand. Show natural language commands (represented as glowing speech bubbles or text streams) flowing upward and forming a heat map of bright to dim colors indicating development priority. The heat map should have peaks and valleys suggesting organic demand patterns. Include subtle AI agent icons monitoring and responding to the patterns. Color palette: cool blues transitioning to warm oranges/yellows for high-demand areas. Style: data visualization meets artistic interpretation, professional tech aesthetic. Avoid: literal charts, generic business graphics.
```

### 5. The Beatles / Collaboration Metaphor

**Prompt**:
```
Generate a stylized, abstract representation of The Beatles as AI agents collaborating. Show 4 distinct AI entities (geometric, holographic forms) each with unique characteristics representing different specializations. They're arranged in a recording studio-inspired space but futuristic and abstract. Musical notes transform into data streams flowing between the agents. The central area glows with creative energy. Color scheme: vintage inspired (warm tones) blended with futuristic tech (cool blues). Style: retro-futurism meets modern minimalism. Avoid: literal band members, copyright-infringing imagery.
```

### 6. Microsoft Copilot / Enterprise Integration

**Prompt**:
```
Generate a professional illustration of Microsoft Copilot assisting enterprise workflows. Show a modern office environment (abstract, stylized) with holographic interface elements floating in space. A central AI assistant icon (Microsoft-aligned design) connects to various business applications represented as interconnected nodes (Dynamics, Office, Teams - abstract representations, not logos). Use Microsoft brand colors (blues, light blues, subtle gradients). Include flowing data connections suggesting seamless integration. Style: corporate professional with futuristic elements, clean and sophisticated. Avoid: literal product screenshots, stock business photos.
```

### 7. Expansive Agents / There and Back Again

**Prompt**:
```
Generate an epic journey visualization showing AI agents expanding outward and returning with knowledge. Center: starting point (home base, glowing). Paths radiate outward like a starburst to distant nodes (representing different exploration areas). Each path shows an agent traveling out (one color) and returning (different color) enriched with data (shown as trailing particles). The overall composition suggests a hero's journey in abstract form. Color palette: deep space blues and purples with bright journey paths in teals and golds. Style: epic scale data visualization meets narrative art. Avoid: literal maps, generic network diagrams.
```

### 8. End of UIs / AI Filtering Noise

**Prompt**:
```
Generate a conceptual visualization of AI filtering out noise from overwhelming information. Left side: dense, chaotic layers of UI elements, windows, notifications, alerts piling up and creating visual noise (grays, reds, overwhelming). Center: AI filter (elegant, translucent barrier with intelligent patterns). Right side: clean, essential information presented beautifully (minimal, calm, purposeful). Show information flowing from chaos through AI to clarity. Color progression: chaotic left (grays/reds) → processing center (blues) → peaceful right (soft blues/whites). Style: conceptual tech illustration, professional and thought-provoking. Avoid: literal screenshots, cliché "funnel" imagery.
```

---

## Gemini API Usage Template

### Environment Variable Setup (SECURE)

```bash
# Set environment variable (do NOT commit to git)
export GEMINI_API_KEY="your-actual-key-here"
```

### Python Script Template (Safe)

```python
# image_generator.py
import os
from google import genai
from google.genai import types
import mimetypes

def generate_blog_image(prompt, output_filename):
    """
    Generate image using Gemini API with environment variable for API key

    Args:
        prompt: Image generation prompt
        output_filename: Base name for output file (extension added automatically)
    """
    # Get API key from environment (NEVER hardcode)
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set!")

    client = genai.Client(api_key=api_key)

    model = "gemini-3-pro-image-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        image_config=types.ImageConfig(image_size="1K"),
        tools=[types.Tool(googleSearch=types.GoogleSearch())],
    )

    file_index = 0
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if (chunk.candidates and
            chunk.candidates[0].content and
            chunk.candidates[0].content.parts and
            chunk.candidates[0].content.parts[0].inline_data and
            chunk.candidates[0].content.parts[0].inline_data.data):

            inline_data = chunk.candidates[0].content.parts[0].inline_data
            data_buffer = inline_data.data
            file_extension = mimetypes.guess_extension(inline_data.mime_type)

            full_filename = f"{output_filename}_{file_index}{file_extension}"
            with open(full_filename, "wb") as f:
                f.write(data_buffer)
            print(f"✅ Image saved: {full_filename}")
            file_index += 1
        else:
            if hasattr(chunk, 'text'):
                print(chunk.text, end="")

# Example usage
if __name__ == "__main__":
    # Multi-agent orchestration image
    prompt = """Generate a modern, minimalist illustration of an AI conductor
    orchestrating multiple specialized agents. Show a central conductor figure
    (abstract, holographic) surrounded by 6-8 floating AI agent nodes, each with
    distinct visual characteristics representing different specializations. The
    agents are connected by glowing data streams forming a network. Use a color
    palette of deep blues, purples, and cyan. The scene should feel like a
    futuristic command center with depth and dimension. Style: sleek digital art,
    professional tech illustration. Avoid: cartoonish elements, literal musicians."""

    generate_blog_image(prompt, "blog_header_multi_agent_orchestration")
```

### Usage

```bash
# Set your API key (get a new one first!)
export GEMINI_API_KEY="your-new-key-here"

# Generate image
python image_generator.py

# Output: blog_header_multi_agent_orchestration_0.png
```

---

## Quick Reference: Prompt Patterns

### Pattern 1: Conceptual Visualization
```
Generate a [style] visualization of [abstract concept]. Show [main element]
surrounded by [supporting elements]. Use [color palette]. The image should
convey [emotion/mood]. Style: [artistic direction]. Avoid: [unwanted].
```

### Pattern 2: Before/After Transformation
```
Generate a split-screen showing [before state] on left and [after state] on right.
Center: [transformation agent/element]. Left side: [chaotic/problem description],
colors [x]. Right side: [organized/solution description], colors [y].
Style: [direction]. Avoid: [unwanted].
```

### Pattern 3: Metaphor Visualization
```
Generate a stylized representation of [metaphor] applied to [tech concept].
Show [metaphor elements] transformed into [tech elements]. Blend [traditional imagery]
with [futuristic elements]. Color scheme: [palette]. Style: [direction].
Avoid: [literal interpretation, unwanted].
```

### Pattern 4: Data Flow / Process
```
Generate a flow visualization showing [input] transforming into [output] through [process].
Visualize data as [visual element] flowing from [source] through [transformation]
to [destination]. Include [ambient elements]. Color progression: [start] → [middle] → [end].
Style: [direction]. Avoid: [unwanted].
```

---

## Integration with Ghostwriter Workflow

### Step 1: Generate Blog Post
```
Task: ghostwriter-kody
Prompt: "Write about multi-agent orchestration"
Output: blog-multi-agent-orchestration-20251121.md
```

### Step 2: Identify Visual Concept
Read blog post, identify:
- Core metaphor (Beatles, conductor, etc.)
- Key concept visualization needed
- Tone/mood of piece

### Step 3: Select/Customize Prompt
- Choose prompt template from examples above
- Customize for specific blog angle
- Adjust style/colors as needed

### Step 4: Generate Image
```bash
export GEMINI_API_KEY="your-key"
python image_generator.py
```

### Step 5: Insert in Blog Post
```markdown
# Blog Post Title

![Header Image](./images/blog_header_multi_agent_orchestration_0.png)

[Blog content...]
```

---

## Brand-Aligned Color Palettes

### Primary (Microsoft-Aligned)
- **Blues**: `#0078D4`, `#50E6FF`, `#00188F`
- **Purples**: `#5E5CE6`, `#8764B8`, `#B146C2`
- **Teals**: `#00B7C3`, `#00CC6A`, `#038387`

### Supporting
- **Warm Accents**: `#FFB900`, `#FF8C00` (for highlights)
- **Neutrals**: `#F3F2F1`, `#E1DFDD`, `#605E5C`
- **Dark**: `#201F1E`, `#323130`

### Usage
- **Backgrounds**: Deep blues/purples (`#00188F`, `#323130`)
- **Primary Elements**: Bright blues/teals (`#0078D4`, `#00B7C3`)
- **Accents/Highlights**: Cyan/gold (`#50E6FF`, `#FFB900`)
- **Text/UI**: Light neutrals (`#F3F2F1`)

---

## Security Best Practices

### ✅ DO:
- Store API keys in environment variables
- Use `.env` files (add to `.gitignore`)
- Rotate keys regularly
- Use separate keys for dev/prod
- Monitor API usage

### ❌ DON'T:
- Hardcode API keys in scripts
- Commit keys to repositories
- Share keys in conversations/emails
- Reuse keys across projects
- Leave keys in plain text files

---

## Next Steps

1. **Revoke exposed key immediately**
2. **Generate new Gemini API key**
3. **Set as environment variable**: `export GEMINI_API_KEY="new-key"`
4. **Test image generation** with example prompts above
5. **Integrate into ghostwriter workflow** for automated visual assets

---

**Ready to generate professional visual assets for your blog posts while keeping your API keys secure!** 🎨🔒