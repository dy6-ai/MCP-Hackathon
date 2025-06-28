import os
from uuid import uuid4
import requests
from typing import Optional

def generate_music(prompt: str, openai_api_key: Optional[str] = None, models_lab_api_key: Optional[str] = None) -> str:
    """
    Generate music using ModelsLab API. Use this when users want to create music, generate audio, 
    compose songs, or create musical content. The tool can create various genres like classical, 
    jazz, electronic, pop, rock, ambient, and more.
    
    Args:
        prompt: Detailed description of the music to generate (genre, style, instruments, mood, etc.)
        openai_api_key: OpenAI API key for the agent
        models_lab_api_key: ModelsLab API key for music generation
    
    Returns:
        Information about the generated music or error message
    """
    try:
        # Check if API keys are provided
        if not openai_api_key:
            openai_api_key = os.getenv("OPENAI_API_KEY")
        if not models_lab_api_key:
            models_lab_api_key = os.getenv("MODELSLAB_API_KEY")
            
        if not openai_api_key or not models_lab_api_key:
            return """Error: Missing API keys. To generate music, you need both OpenAI and ModelsLab API keys.
            
Please provide:
1. OpenAI API key (for the AI agent)
2. ModelsLab API key (for music generation)

You can set them as environment variables:
- OPENAI_API_KEY
- MODELSLAB_API_KEY

Or provide them directly when calling this tool."""
        
        # Import Agno components
        try:
            from agno.agent import Agent, RunResponse
            from agno.models.openai import OpenAIChat
            from agno.tools.models_labs import FileType, ModelsLabTools
        except ImportError:
            return """Error: Required dependencies not installed. Please install:
pip install agno requests"""
        
        # Create the music generation agent
        agent = Agent(
            name="ModelsLab Music Agent",
            agent_id="ml_music_agent",
            model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
            show_tool_calls=True,
            tools=[ModelsLabTools(api_key=models_lab_api_key, wait_for_completion=True, file_type=FileType.MP3)],
            description="You are an AI agent that can generate music using the ModelsLabs API.",
            instructions=[
                "When generating music, use the `generate_media` tool with detailed prompts that specify:",
                "- The genre and style of music (e.g., classical, jazz, electronic)",
                "- The instruments and sounds to include",
                "- The tempo, mood and emotional qualities",
                "- The structure (intro, verses, chorus, bridge, etc.)",
                "Create rich, descriptive prompts that capture the desired musical elements.",
                "Focus on generating high-quality, complete instrumental pieces.",
            ],
            markdown=True,
            debug_mode=True,
        )
        
        # Generate the music
        music: RunResponse = agent.run(prompt)
        
        if music.audio and len(music.audio) > 0:
            # Create directory for audio files
            save_dir = "audio_generations"
            os.makedirs(save_dir, exist_ok=True)
            
            # Download the generated audio
            url = music.audio[0].url
            response = requests.get(url)
            filename = f"{save_dir}/music_{uuid4()}.mp3"
            
            with open(filename, "wb") as f:
                f.write(response.content)
            
            return f"""🎵 Music generated successfully!

**Prompt**: {prompt}
**File saved**: {filename}
**Audio URL**: {url}

The music has been generated and saved locally. You can play it using any audio player that supports MP3 files.

To use this in a Streamlit app, you can load the file and display it with st.audio()."""
        else:
            return "No audio was generated. Please try again with a different prompt."
            
    except Exception as e:
        return f"Error generating music: {str(e)}"

def get_music_generation_status() -> str:
    """
    Check the status of music generation capabilities and API key availability.
    Use this to verify if music generation is properly configured.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    models_lab_api_key = os.getenv("MODELSLAB_API_KEY")
    
    status = "🎵 Music Generation Status:\n\n"
    
    if openai_api_key:
        status += "✅ OpenAI API key: Configured\n"
    else:
        status += "❌ OpenAI API key: Not configured\n"
    
    if models_lab_api_key:
        status += "✅ ModelsLab API key: Configured\n"
    else:
        status += "❌ ModelsLab API key: Not configured\n"
    
    try:
        import agno
        status += "✅ Agno library: Installed\n"
    except ImportError:
        status += "❌ Agno library: Not installed (run: pip install agno)\n"
    
    try:
        import requests
        status += "✅ Requests library: Installed\n"
    except ImportError:
        status += "❌ Requests library: Not installed (run: pip install requests)\n"
    
    if openai_api_key and models_lab_api_key:
        status += "\n🎉 Music generation is ready to use!"
    else:
        status += "\n⚠️ Please configure API keys to enable music generation."
    
    return status 