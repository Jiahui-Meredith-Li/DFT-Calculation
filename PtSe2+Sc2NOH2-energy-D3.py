# -*- coding: utf-8 -*-
setVerbosity(MinimalLog)

# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = Hexagonal(6.48188*Angstrom, 40.0*Angstrom)

# Define elements
elements = [Selenium, Selenium, Selenium, Platinum, Platinum, Platinum,
            Selenium, Selenium, Selenium, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Oxygen, Oxygen, Oxygen, Oxygen, Scandium, Scandium,
            Scandium, Scandium, Nitrogen, Nitrogen, Nitrogen, Nitrogen,
            Scandium, Scandium, Scandium, Scandium, Oxygen, Oxygen, Oxygen,
            Oxygen, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.427689176887,  0.232595254097,  0.361993387268],
                          [ 0.095042662873,  0.567216432682,  0.361969696028],
                          [ 0.762657253455,  0.899463966389,  0.361949502213],
                          [ 0.762219061259,  0.233376696586,  0.39638786223 ],
                          [ 0.428707208547,  0.566604106857,  0.396481437268],
                          [ 0.093838486412,  0.89898369302 ,  0.396814835426],
                          [ 0.09510679581 ,  0.235429849863,  0.431115273648],
                          [ 0.757693820285,  0.562047215559,  0.431582337839],
                          [ 0.430577843928,  0.900302637617,  0.430551797268],
                          [ 0.547644288255,  0.380014529899,  0.481274492203],
                          [ 0.037335209554,  0.348828553086,  0.481539898564],
                          [ 0.515899821852,  0.867772994145,  0.481679719129],
                          [ 0.02156576599 ,  0.856218251947,  0.480917695983],
                          [ 0.526938178196,  0.361820784475,  0.50599067129 ],
                          [ 0.028591659654,  0.364433246653,  0.506333220275],
                          [ 0.530327863197,  0.862167714893,  0.506653209171],
                          [ 0.029269144571,  0.863585191356,  0.50561254141 ],
                          [ 0.862253013676,  0.029961038551,  0.534867876771],
                          [ 0.362396199166,  0.029646502383,  0.534746716301],
                          [ 0.86187896703 ,  0.529659663275,  0.534787103506],
                          [ 0.361946849696,  0.529552166712,  0.534894564583],
                          [ 0.695420812838,  0.196466446803,  0.566408475997],
                          [ 0.195418016677,  0.196123237103,  0.566403060147],
                          [ 0.695639969725,  0.696384995809,  0.566432103146],
                          [ 0.195228626317,  0.696473298342,  0.56640977371 ],
                          [ 0.528781767437,  0.363014536784,  0.596655277875],
                          [ 0.028693135721,  0.36305476526 ,  0.596677574563],
                          [ 0.528661680555,  0.863045796673,  0.596689311792],
                          [ 0.028762032409,  0.862978780042,  0.596635828976],
                          [ 0.862059396145,  0.029691441814,  0.627679012793],
                          [ 0.361992584997,  0.029696107259,  0.627668885265],
                          [ 0.861991636411,  0.529704424825,  0.627666755467],
                          [ 0.362011393423,  0.529641394127,  0.627698741567],
                          [ 0.861937198575,  0.029569624509,  0.652206225556],
                          [ 0.361567396615,  0.029802736242,  0.652196370349],
                          [ 0.86169206162 ,  0.529751471133,  0.652193039632],
                          [ 0.361810328398,  0.529458418308,  0.652228603444]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add tags
bulk_configuration.addTags('H_O',               [9, 10, 11, 12, 33, 34, 35, 36])
bulk_configuration.addTags('Left Interface 0',  [0, 1, 2, 3, 4, 5, 6, 7, 8])
bulk_configuration.addTags('Right Interface 0', [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                                 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                                                 35, 36])

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
basis_set = [
    BasisGGAPseudoDojo.Hydrogen_High,
    BasisGGAPseudoDojo.Nitrogen_High,
    BasisGGAPseudoDojo.Oxygen_High,
    BasisGGAPseudoDojo.Scandium_High,
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
nlsave('PtSe2+Sc2NOH2-energy-D3', bulk_configuration)

# -------------------------------------------------------------
# Total Energy
# -------------------------------------------------------------
total_energy = TotalEnergy(bulk_configuration)
nlsave('PtSe2+Sc2NOH2-energy-D3', total_energy)
nlprint(total_energy)
