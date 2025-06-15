
path = 'PtSe2+Sc2NOH2-dev.hdf5'
configuration = nlread(path, object_id='DeviceConfiguration_0')[0]


kpoint_grid = MonkhorstPackGrid(
    na=61,
    )

transmission_spectrum = TransmissionSpectrum(
    configuration=configuration,
    energies=numpy.linspace(-3,3,601)*eV,
    kpoints=kpoint_grid,
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    self_energy_calculator=RecursionSelfEnergy(),
    )


nlsave('PtSe2+Sc2NOH2-10nm-0-trans.hdf5', transmission_spectrum)
nlprint(transmission_spectrum) 
