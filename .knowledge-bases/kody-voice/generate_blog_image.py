#!/usr/bin/env python3
"""
Blog Image Generator for Kody's Ghostwriter System

Generates professional images for blog posts using Gemini API
API key must be set as environment variable for security

Usage:
    export GEMINI_API_KEY="your-key-here"
    python generate_blog_image.py --topic "multi-agent-systems"

Or with custom prompt:
    python generate_blog_image.py --prompt "Your custom prompt here" --output "custom_name"
"""

import os
import sys
import argparse
import mimetypes
from google import genai
from google.genai import types


# Predefined prompts for common Kody blog topics
TOPIC_PROMPTS = {
    "multi-agent-systems": """Generate a modern, minimalist illustration of an AI conductor orchestrating multiple specialized agents. Show a central conductor figure (abstract, holographic) surrounded by 6-8 floating AI agent nodes, each with distinct visual characteristics representing different specializations. The agents are connected by glowing data streams forming a network. Use a color palette of deep blues, purples, and cyan. The scene should feel like a futuristic command center with depth and dimension. Style: sleek digital art, professional tech illustration. Avoid: cartoonish elements, literal musicians.""",

    "agent-storytelling": """Generate a professional illustration showing natural language commands transforming into executable business workflows. Visualize spoken words (in elegant typography) flowing from left side, passing through an AI processing node (glowing geometric core), and emerging as structured workflow diagrams on right side. Use a clean, modern aesthetic with gradients of blue and teal. Include subtle particle effects suggesting intelligent processing. Style: infographic meets digital art, Microsoft-aligned professional. Avoid: overly complex diagrams, stock photo people.""",

    "inbox-automation": """Generate a split-screen before/after visualization. Left side: chaotic inbox with thousands of overlapping email icons in disarray, dark and cluttered. Right side: organized, zen-like inbox with emails neatly sorted into glowing folders, bright and calm. Center: AI agent icon (abstract geometric shape) orchestrating the transformation with flowing data streams. Color scheme: left side muted grays/reds (chaos), right side blues/greens (order). Style: modern minimalist illustration with depth. Avoid: literal screenshots, generic office imagery.""",

    "demand-driven-dev": """Generate an abstract visualization of user commands creating organic development demand. Show natural language commands (represented as glowing speech bubbles or text streams) flowing upward and forming a heat map of bright to dim colors indicating development priority. The heat map should have peaks and valleys suggesting organic demand patterns. Include subtle AI agent icons monitoring and responding to the patterns. Color palette: cool blues transitioning to warm oranges/yellows for high-demand areas. Style: data visualization meets artistic interpretation, professional tech aesthetic. Avoid: literal charts, generic business graphics.""",

    "beatles-collaboration": """Generate a stylized, abstract representation of The Beatles as AI agents collaborating. Show 4 distinct AI entities (geometric, holographic forms) each with unique characteristics representing different specializations. They're arranged in a recording studio-inspired space but futuristic and abstract. Musical notes transform into data streams flowing between the agents. The central area glows with creative energy. Color scheme: vintage inspired (warm tones) blended with futuristic tech (cool blues). Style: retro-futurism meets modern minimalism. Avoid: literal band members, copyright-infringing imagery.""",

    "copilot-enterprise": """Generate a professional illustration of Microsoft Copilot assisting enterprise workflows. Show a modern office environment (abstract, stylized) with holographic interface elements floating in space. A central AI assistant icon (Microsoft-aligned design) connects to various business applications represented as interconnected nodes (Dynamics, Office, Teams - abstract representations, not logos). Use Microsoft brand colors (blues, light blues, subtle gradients). Include flowing data connections suggesting seamless integration. Style: corporate professional with futuristic elements, clean and sophisticated. Avoid: literal product screenshots, stock business photos.""",

    "expansive-agents": """Generate an epic journey visualization showing AI agents expanding outward and returning with knowledge. Center: starting point (home base, glowing). Paths radiate outward like a starburst to distant nodes (representing different exploration areas). Each path shows an agent traveling out (one color) and returning (different color) enriched with data (shown as trailing particles). The overall composition suggests a hero's journey in abstract form. Color palette: deep space blues and purples with bright journey paths in teals and golds. Style: epic scale data visualization meets narrative art. Avoid: literal maps, generic network diagrams.""",

    "end-of-uis": """Generate a conceptual visualization of AI filtering out noise from overwhelming information. Left side: dense, chaotic layers of UI elements, windows, notifications, alerts piling up and creating visual noise (grays, reds, overwhelming). Center: AI filter (elegant, translucent barrier with intelligent patterns). Right side: clean, essential information presented beautifully (minimal, calm, purposeful). Show information flowing from chaos through AI to clarity. Color progression: chaotic left (grays/reds) → processing center (blues) → peaceful right (soft blues/whites). Style: conceptual tech illustration, professional and thought-provoking. Avoid: literal screenshots, cliché funnel imagery.""",
}


def save_binary_file(file_name, data):
    """Save binary data to file"""
    with open(file_name, "wb") as f:
        f.write(data)
    print(f"✅ Image saved to: {file_name}")


def generate_image(prompt, output_base_name, api_key):
    """
    Generate image using Gemini API

    Args:
        prompt: Image generation prompt
        output_base_name: Base name for output file
        api_key: Gemini API key (from environment variable)
    """
    print(f"🎨 Generating image...")
    print(f"📝 Prompt: {prompt[:100]}...")

    try:
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

        tools = [
            types.Tool(googleSearch=types.GoogleSearch()),
        ]

        generate_content_config = types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
            image_config=types.ImageConfig(image_size="1K"),
            tools=tools,
        )

        file_index = 0
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if (
                chunk.candidates is None
                or chunk.candidates[0].content is None
                or chunk.candidates[0].content.parts is None
            ):
                continue

            if (chunk.candidates[0].content.parts[0].inline_data and
                chunk.candidates[0].content.parts[0].inline_data.data):

                inline_data = chunk.candidates[0].content.parts[0].inline_data
                data_buffer = inline_data.data
                file_extension = mimetypes.guess_extension(inline_data.mime_type)

                full_filename = f"{output_base_name}_{file_index}{file_extension}"
                save_binary_file(full_filename, data_buffer)
                file_index += 1
            else:
                if hasattr(chunk, 'text') and chunk.text:
                    print(chunk.text, end="")

        if file_index == 0:
            print("⚠️  No image generated. Check your prompt and API quota.")
        else:
            print(f"\n✅ Successfully generated {file_index} image(s)")

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Generate blog images using Gemini API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Available predefined topics:
  {', '.join(TOPIC_PROMPTS.keys())}

Examples:
  python generate_blog_image.py --topic multi-agent-systems
  python generate_blog_image.py --prompt "Your custom prompt" --output my_image
  python generate_blog_image.py --list-topics
        """
    )

    parser.add_argument(
        "--topic",
        choices=list(TOPIC_PROMPTS.keys()),
        help="Use predefined prompt for common blog topic"
    )

    parser.add_argument(
        "--prompt",
        help="Custom image generation prompt"
    )

    parser.add_argument(
        "--output",
        default="blog_image",
        help="Output file base name (default: blog_image)"
    )

    parser.add_argument(
        "--list-topics",
        action="store_true",
        help="List all available predefined topics"
    )

    args = parser.parse_args()

    # List topics if requested
    if args.list_topics:
        print("Available predefined topics:")
        for topic in TOPIC_PROMPTS.keys():
            print(f"  - {topic}")
        return

    # Validate arguments
    if not args.topic and not args.prompt:
        print("❌ Error: Must specify either --topic or --prompt")
        parser.print_help()
        sys.exit(1)

    # Get API key from environment
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable not set!")
        print("\nSet your API key with:")
        print("  export GEMINI_API_KEY='your-key-here'")
        print("\n⚠️  SECURITY WARNING:")
        print("  - Never hardcode API keys in code")
        print("  - Never commit API keys to git")
        print("  - Revoke any exposed keys immediately")
        sys.exit(1)

    # Get prompt (either from topic or custom)
    if args.topic:
        prompt = TOPIC_PROMPTS[args.topic]
        output_name = args.output if args.output != "blog_image" else f"blog_{args.topic}"
    else:
        prompt = args.prompt
        output_name = args.output

    # Generate image
    generate_image(prompt, output_name, api_key)


if __name__ == "__main__":
    main()
