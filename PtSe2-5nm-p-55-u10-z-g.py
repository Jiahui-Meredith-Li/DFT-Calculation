# Define names of output files
filename= 'PtSe2-5nm-p-55-u10-z-g.hdf5'

device_configuration = nlread('PtSe2-5nm-p-55-u10-z.hdf5', object_id='DeviceConfiguration_0')[0]
calculator = device_configuration.calculator()
# Set the source-drain voltage of the calculator
calculator=calculator(electrode_voltages=(0.65*Volt, 0.0*Volt))

# Get the metallic regions
metallic_regions = device_configuration.metallicRegions()

# Define gate_voltages
gate_voltage_list=numpy.linspace(1.7,0.4,14)*Volt

for gate_voltage in gate_voltage_list:
   # Change the gate voltages
    new_regions = [m(value = gate_voltage) for m in metallic_regions]
    device_configuration.setMetallicRegions(new_regions) 

   # make a copy of the calculator and attach it to the configuration
    # restart from the previous scf state
    device_configuration.setCalculator(calculator(),
         initial_state=device_configuration)
    device_configuration.update()
    nlsave(filename, device_configuration,object_id='confs'+str(gate_voltage))

    kpoint_grid = MonkhorstPackGrid(
    na=61,
    )

    transmission_spectrum = TransmissionSpectrum(
    configuration=device_configuration,
    energies=numpy.linspace(-5,5,1001)*eV,
    kpoints=kpoint_grid,
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    self_energy_calculator=RecursionSelfEnergy(),
    )


    nlsave(filename, transmission_spectrum,object_id='trans'+str(gate_voltage))
    nlprint(transmission_spectrum)
    # Calculate the current and convert the units in A/m
    # in the periodic direction of (A) 
 
    current=transmission_spectrum.current().inUnitsOf(Ampere)/    \
                        ((6.481880572688119*Ang).inUnitsOf(Meter))
  
    nlprint (gate_voltage)
    nlprint (current)

 
