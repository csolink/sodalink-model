---
title: "Understanding the Sodalink Model"
parent: "Sodalink Model Guidelines"
layout: default
nav_order: 1
---

# Understanding the Sodalink Model

Sodalink Model is a high-level data model built to provide a schema for representing compulogical and systems knowledge. The model itself is agnostic to the graph formalism used to represent knowledge. i.e. You can use Sodalink Model as a schema for labelled property graphs (Neo4j) or for edge labelled graphs (RDF). 

Sodalink Model was built with the following aims:
- Bridge between labelled property graphs and edge labelled graphs
- Formal representation where the semantics are well defined within the model
- Focus on the actual schema and its semantics instead of being weighed down by limitations of a technology
- Extensible, self-documenting, and unambiguous
- Maps to external ontologies, thesauri, controlled vocabularies, and taxonomies

To that end, Sodalink Model makes use of [LinkML](https://github.com/biolink/biolinkml) (Link Modeling Language) for defining the various semantics of the model.

## Understanding the Link Modeling Language

LinkML is a general purpose modeling language that follows object-oriented and ontological principles. The modeling language inherits features from the Web Ontology Language (OWL) and thus is capable of representing semantics in addition to the standard object-oriented hierarchy of a data model.

Models are authored in YAML;  using LinkML one can generate a variety of artifacts including JSON-Schema, OWL, RDF, Python data classes, Shape Expressions, and Markdown.

The modeling language provides the following idioms,
- **Class definition**
  - Used to define classes
- **Slot definition**
  - Used to define class properties
- **Type definition**
  - Used to define data types
- **Schema definition**
  - Used to define properties of the model itself

Refer to [LinkML on GitHub](https://github.com/biolink/biolinkml) for a more detailed guide on LinkML.

> **Note:** Sodalink Model is authored using LinkML. One can use LinkML to author any schema for any domain.


## Structure of the Model

Sodalink Model is a high-level data model where entities, associations, and predicates are arranged in a hierarchy. The model also defines node properties, edge properties, and types.

The model itself is organized using LinkML Class definition (class), Slot definition (slot), Type definition (type) and Schema definition.

> **Conventions**
> 
> In [Sodalink Model YAML](../sodalink-model.yaml) any class, slot, or type is defined in `sentence case` form. When this model is compiled to various forms (like JSON-Schema, OWL, Markdown) the representation is based on the following convention,
>   - classes are named in `CamelCase` form
>   - slots are named in `snake_case` form
>   - types are named in `snake_case` form
>
> To avoid ambiguity in semantics, prefixes are MUST for classes and certain slots.
>
> To avoid ambuguity it semantics, prefixes are RECOMMENDED for all slots.


At a glance the structure is as follows,
- [Classes](#classes)
    - [Entities](#entities)
    - [Associations](#associations)
    - [Mixins](#mixins)
- [Slots](#slots)
    - [Predicates](#predicates)
    - [Node Properties](#node-properties)
    - [Edge Properties](#edge-properties)
- [Types](#types)


### Classes

A class represents an entity or an association. A class can have one more more slots (properties).

In RDF sense, a class is basically `rdfs:Class`.

Within the Sodalink Model there are two hierarchies of classes:
  - [Entities](#entities)
  - [Associations](#associations)

where Entities are disjoint from Associations.


##### Entities

Entities are classes that represent real world entities such as componentservice, errors, control actors, etc.

In a graph formalism, entities are represented by nodes in a graph.

Each Entity class has one or more slots (properties).

The root of all entities is the `named thing` class.

> **Note:** While we say `named thing` when defining the model using LinkML, the actual CURIE for this class is `sodalink:NamedThing`


##### Associations

Associations are classes that represent an assertion or statement. 

In RDF sense, an association is an `rdf:Statement`.

In a graph formalism, associations are represented using edges in a graph.

Each class has one or more slots (or properties).

The root of all associations is the `association` class.

> **Note:** While we say `association` when defining the model using LinkML, the acutal CURIE for this class is `sodalink:Association`


##### Mixins

Mixins are classes that contain slots (properties) or  slots  which embody a generic slot semantic definition, for use across several other classes or slots.

Mixins are abstract classes/slots and they cannot be instantiated by themselves. That is, there cannot be an instance of a mixin class or slot value (e.g. predicate slot) used as 'data'.  

However, a class `mixin` _**may**_ be given as the `domain` or `range` specification of an association or a `mixin` slot may be  given as a `subproperty_of` constraint, with the strict understanding that when the given association  or slot is deployed as an element in a knowledge graph, that the actual values used in the instantiated nodes and edges of the graph will be "concrete" classes or slots that have or inherited those `mixin` elements as `mixins`.

Mixins are defined as a way of encouraging reuse of specific slots (properties) while ensuring a clear inheritance chain.

For example, the `entity to feature or error qualifiers` class is a mixin that defines slots `severity qualifier` and `onset qualifier`. The mixin also inherits the slot `frequency qualifier` from its parent mixin class `frequency qualifier mixin`. 

The mixin class `entity to feature or error qualifiers` is used in the `entity to observable feature association` class and thus by design the class will have `severity qualifier`, `onset qualifier`, and `frequency qualifier` in addition to all other slots it inherits from its own parent `association` class.

> **Note:** Even though `entity to observable feature association` uses the mixin class `entity to feature or error qualifiers` that does not mean that `entity to observable feature association` is a child of `entity to feature or error qualifiers`. i.e. Mixins do not contribute to the inheritance hierarchy of the class that uses them.



### Slots

In Sodalink Model, slots represent properties that a class can have.

A slot is similar to `rdf:Property` where it can link
  - an instance of a class to another instance of a class
  - an instance of a class to a literal/data type


In Sodalink Model slots are used to represent
  - [Predicates](#predicates)
  - [Node Properties](#node-properties)
  - [Edge Properties](#edge-properties)


#### Predicates

Predicates are slots that connect instances of classes. 

In a graph formalism, predicates are relationships that link two instances.

In an OWL sense, predicates are similar to `owl:ObjectProperty`.

For example, a predicate `repairs` can be used to link an instance of class `control actor` with an instance of class `error`.


#### Node Properties

Node properties are slots that an entity class (i.e, a node) can have.

The root of all node properties is `node property` slot.

In an OWL sense, node properties are similar to `owl:DataTypeProperty`.

For example, `id` and `name` are children of the `node property` slot and they are assigned to the entity class `named thing`. So all instances of this class can have `id` and `name` as properties that further describes the instance.


> **Note:** In many cases you may see node properties without the `sodalink` prefix. This is normal since we can assume that if there is a sodalink typed node in a graph, with `id` and `name` as its properties, then they correspond to `sodalink:id` and `sodalink:name`. But to be sure of the semantics it is advised to use the full CURIE to represent property names in your graph.


#### Edge Properties

Edge properties are slots that an association class (i.e., an edge) can have.

The root of all edge properties is `association slot` slot.

In an OWL sense, edge properties are similar to `owl:DataTypeProperty`.

For example, `subject`, `predicate`, and `object` are children of the `association_slot` slot and they are assigned to association class `association`. So all instances of this class can have `subject`, `predicate`, and `object` as its properties that further describes the instance.

> **Note:** In many cases you may see edge properties without the `sodalink` prefix. This is normal since we can assume that if there is a sodalink typed edge in a graph with `subject`, `predicate`, and `object` as its properties then they correspond to `sodalink:subject`, `sodalink:predicate`, and `sodalink:object`, respectively. But to be sure of the semantics it is advised to use the full CURIE to represent property names in your graph.


### Types

LinkML provides a handful of inbuilt data types. But you can also define custom data types using the modeling language.

In Sodalink Model we have several data types.

Data types do not have any inheritance and thus are not arranged in any hierarchy.

For example, `iri type` is a type defined in the Sodalink Model where the value space is constrained to `uriorcurie`.

> **Note**: `uriorcurie` is an inbuilt data type provided by LinkML where the value space is constrained to either a URI or a CURIE representation.
