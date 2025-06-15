import numpy as np

filename='PtSe2-5nm-p-55-u10-z-g.hdf5'

Vglist = gate_voltage_list=[1.7,1.6,1.5,1.4,1.3,1.2,1.1,1.0,0.9,0.8,0.7,0.6,0.5,0.4]*Volt
for Vg in Vglist:
    device_configuration = nlread(filename, object_id='confs'+str(Vg))[0]
    mulliken_population = MullikenPopulation(device_configuration)
    nlsave(filename, mulliken_population, object_id='charge'+str(Vg))
    nlprint(mulliken_population)

    central_region = device_configuration.centralRegion()
    metal_region0 = central_region.metallicRegions()[0]
    cartesiancoordinates = central_region.cartesianCoordinates()
 
    zmin = metal_region0.zmin()
    zmax = metal_region0.zmax()
    charge = 0
    for i in range(len(cartesiancoordinates)):
        if cartesiancoordinates[i][2] > zmin and cartesiancoordinates[i][2] < zmax:
            charge += mulliken_population.atoms()[0][i]
    
    nlprint (Vg)
    nlprint (charge)

