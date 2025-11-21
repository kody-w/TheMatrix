# Quick Copy-Paste Image Prompts

**Use these prompts immediately with your Gemini API** (after getting a new key!)

---

## 🚨 FIRST: Get a New API Key

Your current key is compromised. Go to:
https://aistudio.google.com/app/apikey

1. Revoke: `AIzaSyBWpPPKkyWTHs19T0ksLSM0gooEMQbmKpk`
2. Create new key
3. Set as environment variable: `export GEMINI_API_KEY="new-key"`

---

## Ready-to-Use Prompts (Copy-Paste)

### 1. Multi-Agent Orchestration / Conductor Architecture

```
Generate a modern, minimalist illustration of an AI conductor orchestrating multiple specialized agents. Show a central conductor figure (abstract, holographic) surrounded by 6-8 floating AI agent nodes, each with distinct visual characteristics representing different specializations. The agents are connected by glowing data streams forming a network. Use a color palette of deep blues, purples, and cyan. The scene should feel like a futuristic command center with depth and dimension. Style: sleek digital art, professional tech illustration. Avoid: cartoonish elements, literal musicians.
```

**Use for**: Blog posts about multi-agent systems, orchestration, conductor patterns

---

### 2. Agent Storytelling / Natural Language Workflows

```
Generate a professional illustration showing natural language commands transforming into executable business workflows. Visualize spoken words (in elegant typography) flowing from left side, passing through an AI processing node (glowing geometric core), and emerging as structured workflow diagrams on right side. Use a clean, modern aesthetic with gradients of blue and teal. Include subtle particle effects suggesting intelligent processing. Style: infographic meets digital art, Microsoft-aligned professional. Avoid: overly complex diagrams, stock photo people.
```

**Use for**: Agent storytelling, NL interfaces, demand-driven development

---

### 3. Inbox Automation / Prompt Transplantation

```
Generate a split-screen before/after visualization. Left side: chaotic inbox with thousands of overlapping email icons in disarray, dark and cluttered. Right side: organized, zen-like inbox with emails neatly sorted into glowing folders, bright and calm. Center: AI agent icon (abstract geometric shape) orchestrating the transformation with flowing data streams. Color scheme: left side muted grays/reds (chaos), right side blues/greens (order). Style: modern minimalist illustration with depth. Avoid: literal screenshots, generic office imagery.
```

**Use for**: Productivity automation, inbox management, transformation stories

---

### 4. Demand-Driven Development

```
Generate an abstract visualization of user commands creating organic development demand. Show natural language commands (represented as glowing speech bubbles or text streams) flowing upward and forming a heat map of bright to dim colors indicating development priority. The heat map should have peaks and valleys suggesting organic demand patterns. Include subtle AI agent icons monitoring and responding to the patterns. Color palette: cool blues transitioning to warm oranges/yellows for high-demand areas. Style: data visualization meets artistic interpretation, professional tech aesthetic. Avoid: literal charts, generic business graphics.
```

**Use for**: Demand-driven methodologies, priority management, user-driven systems

---

### 5. Beatles Collaboration Metaphor

```
Generate a stylized, abstract representation of The Beatles as AI agents collaborating. Show 4 distinct AI entities (geometric, holographic forms) each with unique characteristics representing different specializations. They're arranged in a recording studio-inspired space but futuristic and abstract. Musical notes transform into data streams flowing between the agents. The central area glows with creative energy. Color scheme: vintage inspired (warm tones) blended with futuristic tech (cool blues). Style: retro-futurism meets modern minimalism. Avoid: literal band members, copyright-infringing imagery.
```

**Use for**: Collaboration posts, team dynamics, multi-agent systems with Beatles metaphor

---

### 6. Microsoft Copilot / Enterprise AI

```
Generate a professional illustration of Microsoft Copilot assisting enterprise workflows. Show a modern office environment (abstract, stylized) with holographic interface elements floating in space. A central AI assistant icon (Microsoft-aligned design) connects to various business applications represented as interconnected nodes (Dynamics, Office, Teams - abstract representations, not logos). Use Microsoft brand colors (blues, light blues, subtle gradients). Include flowing data connections suggesting seamless integration. Style: corporate professional with futuristic elements, clean and sophisticated. Avoid: literal product screenshots, stock business photos.
```

**Use for**: Copilot posts, enterprise integration, Microsoft ecosystem

---

### 7. Expansive Agents / Hero's Journey

```
Generate an epic journey visualization showing AI agents expanding outward and returning with knowledge. Center: starting point (home base, glowing). Paths radiate outward like a starburst to distant nodes (representing different exploration areas). Each path shows an agent traveling out (one color) and returning (different color) enriched with data (shown as trailing particles). The overall composition suggests a hero's journey in abstract form. Color palette: deep space blues and purples with bright journey paths in teals and golds. Style: epic scale data visualization meets narrative art. Avoid: literal maps, generic network diagrams.
```

**Use for**: Expansive agents, exploration, learning systems

---

### 8. End of UIs / AI Filtering Noise

```
Generate a conceptual visualization of AI filtering out noise from overwhelming information. Left side: dense, chaotic layers of UI elements, windows, notifications, alerts piling up and creating visual noise (grays, reds, overwhelming). Center: AI filter (elegant, translucent barrier with intelligent patterns). Right side: clean, essential information presented beautifully (minimal, calm, purposeful). Show information flowing from chaos through AI to clarity. Color progression: chaotic left (grays/reds) → processing center (blues) → peaceful right (soft blues/whites). Style: conceptual tech illustration, professional and thought-provoking. Avoid: literal screenshots, cliché funnel imagery.
```

**Use for**: Future of UIs, information filtering, AI simplification

---

## Quick Setup Instructions

### Option 1: Python Script (Recommended - Secure)

```bash
# 1. Install dependencies
pip install google-genai

# 2. Set API key (NEW key, not the exposed one!)
export GEMINI_API_KEY="your-new-key-here"

# 3. Run script
cd /Users/kodywildfeuer/Documents/GitHub/m365-agents-for-python/TheMatrix/.knowledge-bases/kody-voice/
python generate_blog_image.py --topic multi-agent-systems

# Or list all topics
python generate_blog_image.py --list-topics

# Or use custom prompt
python generate_blog_image.py --prompt "Your prompt here" --output custom_name
```

### Option 2: Manual Code (Copy-Paste Your Code)

```python
# Replace INSERT_INPUT_HERE with any prompt above
# Make sure GEMINI_API_KEY is set as environment variable
# NEVER hardcode the API key!

import os
from google import genai
from google.genai import types
import mimetypes

def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-pro-image-preview"

    # Paste any prompt from above here:
    prompt = """[PASTE PROMPT HERE]"""

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
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

            filename = f"blog_image_{file_index}{file_extension}"
            with open(filename, "wb") as f:
                f.write(data_buffer)
            print(f"✅ Saved: {filename}")
            file_index += 1
        else:
            if hasattr(chunk, 'text'):
                print(chunk.text, end="")

if __name__ == "__main__":
    generate()
```

---

## Workflow Integration

### After Ghostwriter Generates Blog Post

1. **Read blog post** → Identify core metaphor/concept
2. **Choose prompt** from list above (or customize)
3. **Generate image**:
   ```bash
   python generate_blog_image.py --topic [topic-name]
   ```
4. **Add to blog**:
   ```markdown
   # Blog Title

   ![Header](./blog_multi_agent_systems_0.png)

   [Content...]
   ```

---

## Color Reference (Microsoft-Aligned)

Copy these hex codes for custom prompts:

**Blues**: `#0078D4`, `#50E6FF`, `#00188F`
**Purples**: `#5E5CE6`, `#8764B8`, `#B146C2`
**Teals**: `#00B7C3`, `#00CC6A`, `#038387`
**Warm**: `#FFB900`, `#FF8C00`
**Neutrals**: `#F3F2F1`, `#E1DFDD`, `#605E5C`
**Dark**: `#201F1E`, `#323130`

---

## Security Checklist

Before generating images:

- [ ] Revoked exposed API key
- [ ] Generated new API key
- [ ] Set as environment variable (not hardcoded)
- [ ] Tested with example prompt
- [ ] Added `.env` to `.gitignore` if using env files

---

**Ready to generate! Just:**
1. Get new API key
2. Set environment variable
3. Copy-paste a prompt above
4. Generate your image 🎨