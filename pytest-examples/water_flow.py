def water_column_height(tower_height, tank_height):
    column_height = tower_height  + (3 * tank_height)/4
    return column_height
def pressure_gain_from_water_height(height):
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    lp = (-friction_factor * pipe_length * 998.2 * fluid_velocity * fluid_velocity) / (2000 * pipe_diameter)
    return lp
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    plf = (-0.04 * 998.2 *  quantity_fittings * fluid_velocity * fluid_velocity) / 2000
    return plf 