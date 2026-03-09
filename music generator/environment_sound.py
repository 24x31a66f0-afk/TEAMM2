def detect_environment(scene):

    scene = scene.lower()

    sounds = []

    if "rain" in scene:
        sounds.append("sounds/rain.wav")

    if "thunder" in scene or "storm" in scene:
        sounds.append("sounds/thunder.wav")

    if "wind" in scene or "forest" in scene:
        sounds.append("sounds/wind.wav")

    return sounds