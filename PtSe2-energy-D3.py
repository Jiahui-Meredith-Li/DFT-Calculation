# -*- coding: utf-8 -*-
setVerbosity(MinimalLog)

# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = Hexagonal(3.742315493496491*Angstrom, 24.0*Angstrom)

# Define elements
elements = [Platinum, Selenium, Selenium]

# Define coordinates
fractional_coordinates = [[ 0.249874871094,  0.249872941419,  0.499999579619],
                          [ 0.583189730823,  0.9165364505  ,  0.555926104731],
                          [ 0.916534398082,  0.583189608081,  0.44407431565 ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
basis_set = [
    BasisGGAPseudoDojo.Selenium_High,
    BasisGGAPseudoDojo.Platinum_High,
    ]

k_point_sampling = MonkhorstPackGrid(
    na=33,
    nb=33,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=120.0*Hartree,
    k_point_sampling=k_point_sampling,
    occupation_method=FermiDirac(300.0*Kelvin*boltzmann_constant),
    )

iteration_control_parameters = IterationControlParameters(
    tolerance=1e-06,
    )

#----------------------------------------
# Grimme DFTD3
#----------------------------------------
correction_extension = GrimmeDFTD3(
    exchange_correlation=GGA.PBE,
    maximum_neighbour_distance=30.0*Ang,
    include_three_body_term=False,
    )

calculator = LCAOCalculator(
    basis_set=basis_set,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    correction_extension=correction_extension,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('PtSe2-energy-D3', bulk_configuration)

# -------------------------------------------------------------
# Total Energy
# -------------------------------------------------------------
total_energy = TotalEnergy(bulk_configuration)
nlsave('PtSe2-energy-D3', total_energy)
nlprint(total_energy)
