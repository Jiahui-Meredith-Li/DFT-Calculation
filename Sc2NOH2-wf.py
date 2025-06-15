# -*- coding: utf-8 -*-
setVerbosity(MinimalLog)

# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = Hexagonal(3.2306322389810136*Angstrom, 30.0*Angstrom)

# Define elements
elements = [Oxygen, Oxygen, Nitrogen, Scandium, Scandium, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.750318120558,  0.719790636107,  0.418646897641],
                          [ 0.082992741086,  0.386082973738,  0.583676003085],
                          [ 0.416609115991,  0.052886555094,  0.501156223287],
                          [ 0.083372211495,  0.386293482232,  0.460144588098],
                          [ 0.749889084461,  0.719534050381,  0.542189565076],
                          [ 0.750883121472,  0.719987372276,  0.385914023593],
                          [ 0.082559719835,  0.385762538041,  0.61641049379 ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add tags
bulk_configuration.addTags('H_O', [5, 6])

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
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

poisson_solver = FastFourier2DSolver(
    boundary_conditions=[[PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [NeumannBoundaryCondition(),DirichletBoundaryCondition()]]
    )

calculator = LCAOCalculator(
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    poisson_solver=poisson_solver,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('Sc2NOH2-wf', bulk_configuration)

# -------------------------------------------------------------
# Chemical Potential
# -------------------------------------------------------------
chemical_potential = ChemicalPotential(bulk_configuration)
nlsave('Sc2NOH2-wf', chemical_potential)
nlprint(chemical_potential)
