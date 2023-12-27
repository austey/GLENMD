from setuptools import setup, find_packages

setup(
    name="GlenMD",
    version="0.0.1",
    author="austey",
    author_email="junglekst@snu.ac.kr",
    url="https://github.com/austey/GLENMD",
    download_url="https://github.com/austey/GLENMD/",
    install_requies=["numpy>=1.22.4", "yaml>=6.0.1", "scipy>=1.10.4", "tqdm>=4.66", "ase>=3.19"],
    description="Molecular Simulation CODE",
    packages=find_packages(),
    keywords=["MLFF", "LAMMPS", "GROMACS", "CP2K", ],
    python_requires=">=3.9",
    package_data={"": ["*"]},
    entry_points={
        # make the scripts available as command line scripts
        "console_scripts": [
            "glenmd-run = glenmd.cli.run:main",
        ]
    },
    zip_safe=False,
)
