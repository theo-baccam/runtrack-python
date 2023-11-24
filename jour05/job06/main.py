def lighthouse(steps, step_height):
    weekly = (steps * step_height) * 2 * 7 / 100
    print(f"Pour marcher {steps} marches de {step_height}cm, le gardien parcourt {weekly}m par semaine.")

lighthouse(40,7.5)