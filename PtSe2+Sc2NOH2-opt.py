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
fractional_coordinates = [[ 0.429833189531,  0.236821026178,  0.339568359524],
                          [ 0.096499826747,  0.570154388962,  0.339568359524],
                          [ 0.763166552315,  0.903487751746,  0.339568359524],
                          [ 0.763175283537,  0.236821821949,  0.373123517905],
                          [ 0.429841920753,  0.570155184733,  0.373123517905],
                          [ 0.096508557969,  0.903488547517,  0.373123517905],
                          [ 0.096512610781,  0.236833085158,  0.406679432972],
                          [ 0.763179336349,  0.570166447942,  0.406679432972],
                          [ 0.429845973565,  0.903499810726,  0.406679432972],
                          [ 0.528666133501,  0.362222327354,  0.487559287828],
                          [ 0.028666089325,  0.362222327354,  0.487559287828],
                          [ 0.528666133501,  0.86222237153 ,  0.487559287828],
                          [ 0.028666089325,  0.86222237153 ,  0.487559287828],
                          [ 0.528482001113,  0.361939826873,  0.512108943365],
                          [ 0.028481956937,  0.361939826873,  0.512108943365],
                          [ 0.528482001113,  0.861939871049,  0.512108943365],
                          [ 0.028481956937,  0.861939871049,  0.512108943365],
                          [ 0.861757652964,  0.028466842878,  0.543232211207],
                          [ 0.361757608788,  0.028466842878,  0.543232211207],
                          [ 0.861757652964,  0.528466887054,  0.543232211207],
                          [ 0.361757608788,  0.528466887054,  0.543232211207],
                          [ 0.695079554055,  0.195085309847,  0.573990937599],
                          [ 0.195079509879,  0.195085309847,  0.573990937599],
                          [ 0.695079554055,  0.695085354023,  0.573990937599],
                          [ 0.195079509879,  0.695085354023,  0.573990937599],
                          [ 0.528395775919,  0.361725308805,  0.60476594394 ],
                          [ 0.028395731743,  0.361725308805,  0.60476594394 ],
                          [ 0.528395775919,  0.861725352981,  0.60476594394 ],
                          [ 0.028395731743,  0.861725352981,  0.60476594394 ],
                          [ 0.861673171999,  0.028277107657,  0.635880772447],
                          [ 0.361673127823,  0.028277107657,  0.635880772447],
                          [ 0.861673171999,  0.528277151833,  0.635880772447],
                          [ 0.361673127823,  0.528277151833,  0.635880772447],
                          [ 0.861616879217,  0.028060597012,  0.660431640476],
                          [ 0.361616835041,  0.028060597012,  0.660431640476],
                          [ 0.861616879217,  0.528060641188,  0.660431640476],
                          [ 0.361616835041,  0.528060641188,  0.660431640476]]

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
k_point_sampling = MonkhorstPackGrid(
    na=18,
    nb=18,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=130.0*Hartree,
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
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    correction_extension=correction_extension,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('PtSe2+Sc2NOH2-opt', bulk_configuration)

# -------------------------------------------------------------
# Optimize Geometry
# -------------------------------------------------------------
bulk_configuration = OptimizeGeometry(
    bulk_configuration,
    max_forces=0.005*eV/Ang,
    max_steps=200,
    max_step_length=0.2*Ang,
    trajectory_filename='PtSe2+Sc2NOH2-opt_trajectory.hdf5',
    trajectory_interval=5.0*Minute,
    restart_strategy=RestartFromTrajectory(),
    disable_stress=True,
    optimizer_method=LBFGS(),
    enable_optimization_stop_file=True,
)
nlsave('PtSe2+Sc2NOH2-opt', bulk_configuration)
nlprint(bulk_configuration)

# -------------------------------------------------------------
# Fat Bandstructure
# -------------------------------------------------------------
fat_bandstructure = FatBandstructure(
    configuration=bulk_configuration,
    route=['G', 'M', 'K', 'G'],
    points_per_segment=40,
    bands_above_fermi_level=All,
    projections=ProjectOnTags,
)
nlsave('PtSe2+Sc2NOH2-opt', fat_bandstructure)
