from api.longform_episode_generator import get_intro_system_prompt, intro_user_prompt


dialogue_prompts = {
    "intro_system_prompt": get_intro_system_prompt(),
    "intro_user_prompt": intro_user_prompt,
}
