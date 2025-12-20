import os
from google import genai
from google.genai import types
from PIL import Image
import io

# ==========================================
# CONFIGURATION
# ==========================================
# API Key from AI Studio
API_KEY = ""

# Ensure the static/img/projects directory exists
PROJECT_DIR = "static/img/projects"
os.makedirs(PROJECT_DIR, exist_ok=True)

# Define the style suffix to maintain consistency
STYLE_SUFFIX = " ... in a cinematic, professional photography style. Premium, moody atmosphere with high-tech industrial lighting (subtle blue/orange accents). Sharp focus with cinematic depth of field. 8k resolution, photorealistic."

# Dictionary of { filename: prompt }
PROJECT_PROMPTS = {
    "tank-inspection.png": "A small, rugged micro-aerial vehicle with powerful LED spotlights flying inside a dark, cavernous, rusted metal industrial ballast water tank. The spotlights illuminate the texture of the rusted walls and structural ribs. Gritty industrial photography style.",
    "mimosa.png": "A conceptual 3D visualization of a robot's perception. A complex indoor environment represented as a high-density point cloud where layers of thermal (orange/red), visible light (realistic), and LiDAR (neon blue) data overlap and fuse together. Futuristic, analytical data-rich aesthetic.",
    "darpa-subt.png": "A team of diverse robots—a four-legged robotic dog and a specialized quadrotor—navigating a dark, fog-filled underground tunnel. Dust particles catch the beams of their onboard lights. Cinematic, epic scale, high-stakes competition atmosphere.",
    "rmf-owl.png": "A specialized indoor flying robot with a protective spherical carbon-fiber cage. It is bouncing gently off a concrete wall in a dark industrial hallway, with small sparks or dust reacting to the impact. Dynamic motion, focus on the rugged cage design.",
    "aerial-chain.png": "A series of five miniature quadrotors linked together by flexible mechanical joints, forming a long 'snake-like' chain. They are flying through a very narrow, curved architectural opening. Technical, sleek design, focus on the unique mechanical connection.",
    "radiation-mapping.png": "A quadrotor flying over a decommissioned industrial site. Overlaying the scene is a semi-transparent heatmap (green to red) indicating radiation intensity gradients. Professional technical visualization, clean and informative but cinematic.",
    "uas.png": "A clean, studio shot of a high-end flight controller board and various sensors (LiDAR, Cameras) laid out on a dark reflective surface. Vibrant circuitry traces glow slightly. Product photography style for high-end engineering."
}

# ==========================================
# GENERATION SCRIPT
# ==========================================

def generate_and_save():
    client = genai.Client(api_key=API_KEY)
    
    # Testing with only one image first
    for filename, prompt in [("test-nano.png", PROJECT_PROMPTS["tank-inspection.png"])]:
        save_path = os.path.join(PROJECT_DIR, filename)
        
        full_prompt = prompt + STYLE_SUFFIX
        print(f"Generating image for: {filename} using nano-banana-pro-preview...")
        
        try:
            response = client.models.generate_images(
                model='nano-banana-pro-preview',
                prompt=full_prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                )
            )
            
            for i, generated_image in enumerate(response.generated_images):
                img_data = generated_image.image.image_bytes
                with open(save_path, 'wb') as f:
                    f.write(img_data)
                print(f"Successfully saved to {save_path}")
                
        except Exception as e:
            print(f"Error generating {filename}: {e}")
            print("-" * 30)

if __name__ == "__main__":
    print("Starting automated image generation...")
    generate_and_save()
    print("Task completed.")
