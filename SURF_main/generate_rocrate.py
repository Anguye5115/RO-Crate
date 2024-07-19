from rocrate.rocrate import ROCrate
from rocrate.model.person import Person
from rocrate.model.entity import Entity
from rocrate.model.computationalworkflow import ComputationalWorkflow
from rocrate.model.contextentity import ContextEntity
from frictionless import Schema, Resource
import yaml
import toolz
from toolz.curried import curry, pipe
from toolz.curried import map as fmap


# See this: https://www.researchobject.org/workflow-run-crate/profiles/process_run_crate/

def read_yaml(filepath):
    with open(filepath, 'r') as file:
        yaml_content = yaml.safe_load(file)
    return yaml_content


@curry
def set_value(obj, key, value):
    obj[key] = value
    return obj


@curry
def set_attr(obj, key, value):
    setattr(obj, key, value)
    return obj


@curry
def crateadd(crate, thing):
    return crate.add(thing)


@curry
def add_authors(authors, crate):
    return pipe(
        authors,
        fmap(lambda x: crate.add(
            Person(
                crate,
                x['orcid'],
                properties=dict(
                    name=x['name'],
                    affiliation=x['affiliation']
                )
            )
        )),
        list,
        set_root("author", crate=crate)
    )


@curry
def add_license(license, crate):
    return pipe(
        license,
        lambda x: crate.add(Entity(
            crate,
            identifier=license['identifier'],
            properties={
                "@type": "CreativeWork",
                "name": license["name"],
                "description": license["description"],
                "url": license["url"]
           }
        )),
        set_attr(crate, "license")
    )


@curry
def add_files(files, crate):
    list(fmap(lambda x: crate.add_file(
        x["path"],
        properties=dict(
            name=x["name"],
            encodingFormat=x["encodingFormat"],
            description=x["description"]
        )), files))
    return crate


@curry
def add_column(path, crate, column):
    identifier = path + "#" + column['identifier']
    crate.add_jsonld({
        "@id": identifier,
        "@type": "PropertyValue",
        "unitCode": column["unit"],
        "name": column["identifier"],
        "description": column["description"]
    })
    return {"@id": identifier}
    


@curry
def add_columns(columns, path, crate):
    return list(fmap(
        add_column(path, crate),
        columns
    ))

                
@curry
def add_tabular_file(file, crate):
    crate.add_file(
        file["path"],
        properties={
            "@type": ["File", "Dataset"],
            "description": file["description"],
            "encodingFormat": file["encodingFormat"],
            "variableMeasured": add_columns(file.get("columns", []), file["path"], crate),
        }
    )
    return crate


@curry
def add_tabular_files(files, crate):
    list(fmap(add_tabular_file(crate=crate), files))
    return crate


@curry
def set_root(key, value, crate):
    crate.root_dataset[key] = value
    return crate


@curry
def add_workflow(workflow, crate):
    pipe(
        crate.add_workflow(workflow["identifier"]),
        set_attr(key="programmingLanguage", value=workflow["programmingLanguage"]),
        set_attr(key="license", value=crate.license),        
        set_value(key="dateCreated", value=workflow["dateCreated"]),
        set_value(key="name", value=workflow["name"]),
        set_value(key="creator", value=[{"@id": workflow["creator"]}])
    )
    return crate

    
# def debug(x):
#     print('debug:', x)
#     import ipdb; ipdb.set_trace();
#     # x.root_dataset["conformsTo"] = [x.root_dataset["conformsTo"], {"@id": 'test'}]
#     # # set_root("conformsTo", 'testing', x)
#     return x
    
def generate(data):

    return pipe(
        ROCrate(),
        # debug,
        set_attr(key='description', value=data['description']),
        set_root('title', data['title']),
        add_authors(data['authors']),
        add_license(data['license']),
        add_files(data['files']),
        add_tabular_files(data['tabular_files']),
        add_workflow(data['workflow']),
        lambda x: x.write(data["crate-directory"])
    )


if __name__ == '__main__':
    data = read_yaml("config.yaml")
    crate = generate(data)
