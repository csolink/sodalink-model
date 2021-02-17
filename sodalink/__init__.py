# Sodalink model file locations
import os

basedir = os.path.abspath(os.path.join(__file__, '..', '..'))
SODALINK_MODEL_YAML = os.path.join(basedir, 'sodalink-model.yaml')
SODALINK_MODEL_JSONLD = os.path.join(basedir, 'context.jsonld')
SODALINK_MODEL_SHEX = os.path.join(basedir, 'shex', 'sodalink-model.shex')
SODALINK_MODEL_RDF = os.path.join(basedir, 'rdf', 'sodalink-model.ttl')
SODALINK_MODEL_OWL = os.path.join(basedir, 'ontology', 'sodalink-model.owl')
SODALINK_MODEL_JSON = os.path.join(basedir, 'sodalink-model.json')
SODALINK_MODEL_JSON_SCHEMA = os.path.join(basedir, 'json-schema', 'sodalink-model.json')
SODALINK_MODEL_JAVA = os.path.join(basedir, 'java')
SODALINK_MODEL_PYTHON = os.path.join(basedir, 'sodalink', 'model.py')
