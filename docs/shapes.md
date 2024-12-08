# SHACL Shapes Documentation

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#ProfileGraphShape

### NodeShape Constraints

- **sh:targetNode:** https://w3id.org/riverbench/schema/metadata#Profile

### Properties

#### Property: n919e52bf31f64cbea47ec1378b60fca8b1

**Path:** ^http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:minCount:** 1

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#ProfileShape

### NodeShape Constraints

- **sh:targetClass:** https://w3id.org/riverbench/schema/metadata#Profile

### Properties

#### Property: n919e52bf31f64cbea47ec1378b60fca8b3

**Path:** https://w3id.org/riverbench/schema/metadata#isSupersetOfProfile

**Constraints:**
- **sh:nodeKind:** http://www.w3.org/ns/shacl#IRI
- **sh:node:** {'sh:property': rdflib.term.BNode('n919e52bf31f64cbea47ec1378b60fca8b5')}

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#CategoryGraphShape

### NodeShape Constraints

- **sh:targetNode:** https://w3id.org/riverbench/schema/metadata#Category

### Properties

#### Property: nd704ac798dc3413691f7ba7e51283ba8b1

**Path:** ^http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#CategoryShape

### NodeShape Constraints

- **sh:targetNode:** https://w3id.org/riverbench/temp#category

### Properties

#### Property: nd704ac798dc3413691f7ba7e51283ba8b3

**Path:** http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:hasValue:** https://w3id.org/riverbench/schema/metadata#Category

#### Property: nd704ac798dc3413691f7ba7e51283ba8b4

**Path:** http://purl.org/dc/terms/conformsTo

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:hasValue:** https://w3id.org/riverbench/schema/metadata

#### Property: nd704ac798dc3413691f7ba7e51283ba8b5

**Path:** http://purl.org/dc/terms/identifier

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#string

#### Property: nd704ac798dc3413691f7ba7e51283ba8b6

**Path:** http://purl.org/dc/terms/title

**Constraints:**
- **sh:minCount:** 1
- **sh:datatype:** http://www.w3.org/1999/02/22-rdf-syntax-ns#langString
- **sh:uniqueLang:** true

#### Property: nd704ac798dc3413691f7ba7e51283ba8b7

**Path:** http://purl.org/dc/terms/description

**Constraints:**
- **sh:minCount:** 1
- **sh:datatype:** http://www.w3.org/1999/02/22-rdf-syntax-ns#langString
- **sh:uniqueLang:** true

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#DatasetGraphShape

### NodeShape Constraints

- **sh:targetNode:** https://w3id.org/riverbench/schema/metadata#Dataset

### Properties

#### Property: n4fead01b140144af86da1873f016e0c4b1

**Path:** ^http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#DatasetShape

### NodeShape Constraints

- **sh:targetClass:** https://w3id.org/riverbench/schema/metadata#Dataset

### Properties

#### Property: n4fead01b140144af86da1873f016e0c4b3

**Path:** http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:minCount:** 1
- **sh:hasValue:** http://www.w3.org/ns/dcat#Dataset

#### Property: n4fead01b140144af86da1873f016e0c4b4

**Path:** http://purl.org/dc/terms/conformsTo

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:nodeKind:** http://www.w3.org/ns/shacl#IRI
- **sh:hasValue:** https://w3id.org/riverbench/schema/metadata

#### Property: n4fead01b140144af86da1873f016e0c4b5

**Path:** http://purl.org/dc/terms/identifier

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#string

#### Property: n4fead01b140144af86da1873f016e0c4b6

**Path:** http://purl.org/dc/terms/title

**Constraints:**
- **sh:minCount:** 1
- **sh:datatype:** http://www.w3.org/1999/02/22-rdf-syntax-ns#langString
- **sh:uniqueLang:** true

#### Property: n4fead01b140144af86da1873f016e0c4b7

**Path:** http://purl.org/dc/terms/description

**Constraints:**
- **sh:minCount:** 1
- **sh:datatype:** http://www.w3.org/1999/02/22-rdf-syntax-ns#langString
- **sh:uniqueLang:** true

#### Property: n4fead01b140144af86da1873f016e0c4b8

**Path:** http://purl.org/dc/terms/issued

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#date

#### Property: n4fead01b140144af86da1873f016e0c4b9

**Path:** http://purl.org/dc/terms/license

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:nodeKind:** http://www.w3.org/ns/shacl#IRI
- **sh:pattern:** ^https://spdx.org/licenses/

#### Property: n4fead01b140144af86da1873f016e0c4b10

**Path:** http://purl.org/dc/terms/creator

**Constraints:**
- **sh:minCount:** 1
- **sh:nodeKind:** http://www.w3.org/ns/shacl#BlankNodeOrIRI

#### Property: n4fead01b140144af86da1873f016e0c4b11

**Path:** http://www.w3.org/ns/dcat#theme

**Constraints:**
- **sh:minCount:** 1
- **sh:nodeKind:** http://www.w3.org/ns/shacl#IRI
- **sh:pattern:** ^http://eurovoc.europa.eu/
- **sh:node:** {'sh:property': rdflib.term.BNode('n4fead01b140144af86da1873f016e0c4b13')}

#### Property: n4fead01b140144af86da1873f016e0c4b14

**Path:** http://rdfs.org/ns/void#vocabulary

**Constraints:**
- **sh:minCount:** 1
- **sh:nodeKind:** http://www.w3.org/ns/shacl#IRI

#### Property: n4fead01b140144af86da1873f016e0c4b15

**Path:** https://w3id.org/riverbench/schema/metadata#hasStreamElementCount

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#integer

#### Property: n4fead01b140144af86da1873f016e0c4b16

**Path:** https://w3id.org/stax/ontology#hasStreamTypeUsage

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 2
- **sh:node:** https://w3id.org/riverbench/schema/dataset-shacl#StreamTypeShape

#### Property: n4fead01b140144af86da1873f016e0c4b17

**Path:** https://w3id.org/riverbench/schema/metadata#hasStreamElementSplit

**Constraints:**
- **sh:nodeKind:** http://www.w3.org/ns/shacl#BlankNodeOrIRI
- **sh:node:** https://w3id.org/riverbench/schema/dataset-shacl#StreamElementSplitShape

#### Property: n4fead01b140144af86da1873f016e0c4b18

**Path:** https://w3id.org/riverbench/schema/metadata#conformsToRdf11

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#boolean

#### Property: n4fead01b140144af86da1873f016e0c4b19

**Path:** https://w3id.org/riverbench/schema/metadata#conformsToRdfStarDraft_20211217

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#boolean

#### Property: n4fead01b140144af86da1873f016e0c4b20

**Path:** https://w3id.org/riverbench/schema/metadata#usesGeneralizedRdfDatasets

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#boolean

#### Property: n4fead01b140144af86da1873f016e0c4b21

**Path:** https://w3id.org/riverbench/schema/metadata#usesGeneralizedTriples

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#boolean

#### Property: n4fead01b140144af86da1873f016e0c4b22

**Path:** https://w3id.org/riverbench/schema/metadata#usesRdfStar

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#boolean

#### Property: n4fead01b140144af86da1873f016e0c4b23

**Path:** http://www.w3.org/ns/dcat#version

**Constraints:**
- **sh:maxCount:** 0

#### Property: n4fead01b140144af86da1873f016e0c4b24

**Path:** http://purl.org/dc/terms/modified

**Constraints:**
- **sh:maxCount:** 0

#### Property: n4fead01b140144af86da1873f016e0c4b25

**Path:** http://www.w3.org/ns/dcat#landingPage

**Constraints:**
- **sh:maxCount:** 0

#### Property: n4fead01b140144af86da1873f016e0c4b26

**Path:** http://www.w3.org/ns/dcat#inSeries

**Constraints:**
- **sh:maxCount:** 0

#### Property: n4fead01b140144af86da1873f016e0c4b27

**Path:** http://www.w3.org/ns/dcat#distribution

**Constraints:**
- **sh:maxCount:** 0

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#StreamTypeShape

### NodeShape Constraints

- **sh:and:** {}

---

## Shape: n4fead01b140144af86da1873f016e0c4b31

### Properties

#### Property: n4fead01b140144af86da1873f016e0c4b32

**Path:** http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:hasValue:** https://w3id.org/stax/ontology#ConcreteRdfStreamType

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#FlatStreamTypeShape

### NodeShape Constraints

- **sh:targetNode:** https://w3id.org/stax/ontology#flatStream

### Properties

#### Property: n4fead01b140144af86da1873f016e0c4b53

**Path:** ((http://www.w3.org/2004/02/skos/core#narrower)+)/(^https://w3id.org/stax/ontology#hasStreamType)/(^https://w3id.org/stax/ontology#hasStreamTypeUsage)

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:nodeKind:** http://www.w3.org/ns/shacl#IRI

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#StreamElementSplitShape

### Properties

#### Property: n4fead01b140144af86da1873f016e0c4b60

**Path:** http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:in:** {}

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#SubjectShapeShape

### NodeShape Constraints

- **sh:targetSubjectsOf:** https://w3id.org/riverbench/schema/metadata#hasSubjectShape

### Properties

#### Property: n4fead01b140144af86da1873f016e0c4b64

**Path:** http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:minCount:** 1
- **sh:hasValue:** https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit

#### Property: n4fead01b140144af86da1873f016e0c4b65

**Path:** https://w3id.org/riverbench/schema/metadata#hasSubjectShape/(http://www.w3.org/ns/shacl#targetClass|http://www.w3.org/ns/shacl#targetSubjectsOf|http://www.w3.org/ns/shacl#targetObjectsOf|https://w3id.org/riverbench/schema/metadata#targetCustom)

**Constraints:**
- **sh:minCount:** 1
- **sh:nodeKind:** http://www.w3.org/ns/shacl#IRI

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#TaskGraphShape

### NodeShape Constraints

- **sh:targetNode:** https://w3id.org/riverbench/schema/metadata#Task

### Properties

#### Property: n6a1b63e6b8cc4767a105c234ac65a447b1

**Path:** ^http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1

---

## Shape: https://w3id.org/riverbench/schema/dataset-shacl#TaskShape

### NodeShape Constraints

- **sh:targetNode:** https://w3id.org/riverbench/temp#task

### Properties

#### Property: n6a1b63e6b8cc4767a105c234ac65a447b3

**Path:** http://www.w3.org/1999/02/22-rdf-syntax-ns#type

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:hasValue:** https://w3id.org/riverbench/schema/metadata#Task

#### Property: n6a1b63e6b8cc4767a105c234ac65a447b4

**Path:** http://purl.org/dc/terms/conformsTo

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:hasValue:** https://w3id.org/riverbench/schema/metadata

#### Property: n6a1b63e6b8cc4767a105c234ac65a447b5

**Path:** http://purl.org/dc/terms/identifier

**Constraints:**
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:datatype:** http://www.w3.org/2001/XMLSchema#string

#### Property: n6a1b63e6b8cc4767a105c234ac65a447b6

**Path:** http://purl.org/dc/terms/title

**Constraints:**
- **sh:minCount:** 1
- **sh:datatype:** http://www.w3.org/1999/02/22-rdf-syntax-ns#langString
- **sh:uniqueLang:** true

#### Property: n6a1b63e6b8cc4767a105c234ac65a447b7

**Path:** http://purl.org/dc/terms/description

**Constraints:**
- **sh:minCount:** 1
- **sh:datatype:** http://www.w3.org/1999/02/22-rdf-syntax-ns#langString
- **sh:uniqueLang:** true

#### Property: n6a1b63e6b8cc4767a105c234ac65a447b8

**Path:** http://purl.org/dc/terms/creator

**Constraints:**
- **sh:minCount:** 1
- **sh:nodeKind:** http://www.w3.org/ns/shacl#BlankNodeOrIRI

---

