# simple_solar_system.py

from solar_system_3d import SolarSystem, Sun

solar_system = SolarSystem(400, projection_2d=True)

sun = Sun(solar_system)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()