filename = 'PtSe2-5nm-n-55-u10-z-g.hdf5'
transmission_spectrum = nlread(filename, object_id='trans-0.1 V')[0]
energies=transmission_spectrum.energies()
spectralCurrent=transmission_spectrum.spectralCurrent()

for i in range(len(energies)):
    nlprint (energies[i].inUnitsOf(eV))

for i in range(len(energies)):
    nlprint (spectralCurrent[i].inUnitsOf(Ampere/eV))

