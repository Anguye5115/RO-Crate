from rocrate.rocrate import ROCrate
from rocrate.model.person import Person

crate = ROCrate()
yaml = crate.add_file("working/pfhub.yaml", properties={
    "name": "PFHub meta data file",
    "encodingFormat": "text/yaml"
})
csv = crate.add_file("working/free_energy_1a.csv", properties={
    "name": "Free Energy",
    "encodingFormat": "text/csv"
})

wheeler_id = "https://orcid.org/0000-0002-2653-7418"

wheeler = crate.add(
    Person(
        crate,
        wheeler_id,
        properties=dict(name="Daniel Wheeler", affiliation="NIST")
    )
)

#crate["author"] = wheeler

crate.write("exp_crate")



