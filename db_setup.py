# db_setup.py

# Define option_links with at least one option.
option_links = {
    "Ae": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/Ae/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/aerospace-minor-ae/"
    },
    "APh": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/APh/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/applied-physics-option-aph/"
    },
    "ACM": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/ACM/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/applied-and-computational-mathematics-acm/"
    },
    "Ay": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/Ay/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/astrophysics-option-and-minor-ay/"
    },
    "BE": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/BE/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/bioengineering-option-be/"
    },
    "Bi": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/Bi/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/biology-option-and-minor-bi/"
    },
    "BEM": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/BEM/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/business-economics-and-management-option-bem/"
    },
    "ChE": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/ChE/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/chemical-engineering-option-and-minor-che/"
    },
    "Ch": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/Ch/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/chemistry-option-and-minor-ch/"
    },
    "CNS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/CNS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/computation-and-neural-systems-option-cns/"
    },
    "CS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/CS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/computer-science-option-and-minor-cs/"
    },
    "CDS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/CDS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/control-and-dynamical-systems-minor-cds/"
    },
    "Ec": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/Ec/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/economics-option-ec/"
    },
    "EE": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/EE/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/electrical-engineering-option-ee/"
    },
    "EAS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/EAS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/engineering-and-applied-science-option-eas/"
    },
    "En": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/En/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/english-option-and-minor-en/"
    },
    "ESE": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/ESE/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/environmental-science-and-engineering-option-and-minor-ese/"
    },
    "GPS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/GPS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/geological-and-planetary-sciences-option-and-minor-gps/"
    },
    "H": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/H/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/history-option-and-minor-h/"
    },
    "HPS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/HPS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/history-and-philosophy-of-science-option-and-minor-hps/"
    },
    "IDS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/IDS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/information-and-data-sciences-option-and-minor-ids/"
    },
    "MS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/MS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/materials-science-option-ms/"
    },
    "Ma": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/Ma/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/mathematics-option-ma/"
    },
    "ME": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/ME/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/mechanical-engineering-option-me/"
    },
    "Ph": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/Ph/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/physics-option-ph/"
    },
    "PS": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/PS/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/political-science-option-ps/"
    },
    "VC": {
        "catalog": "https://catalog.caltech.edu/current/2024-25/department/VC/",
        "requirements": "https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/visual-culture-minor-vc/"
    }
}
