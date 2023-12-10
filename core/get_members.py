from core import server_connection


# Get cubes name.
def get_cubes():
    return server_connection.tm1.cubes.get_all_names(skip_control_cubes=True)


# Get dimensions name.
def get_dimensions(cubeType, cubeName):
    if cubeType == 'Source':
        return server_connection.tm1.cubes.get_dimension_names(cubeName, skip_control_cubes=True)
    else:
        return server_connection.tm1.cubes.get_dimension_names(cubeName, skip_control_cubes=True)


# Get elements name.
def get_elements(cubeType, dimensionName):
    if cubeType == 'Source':
        return server_connection.tm1.elements.get_element_names(dimensionName, hierarchy_name=dimensionName)
    else:
        return server_connection.tm1.elements.get_element_names(dimensionName, hierarchy_name=dimensionName)
