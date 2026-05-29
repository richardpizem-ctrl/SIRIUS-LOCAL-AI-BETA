class KGEntity:
    def __init__(self, name: str, attributes=None):
        self.name = name
        self.attributes = attributes or {}

class KGRelation:
    def __init__(self, source: str, relation: str, target: str):
        self.source = source
        self.relation = relation
        self.target = target

class KnowledgeGraph:
    def __init__(self):
        self.entities = {}
        self.relations = []

    def add_entity(self, name: str, attributes=None):
        self.entities[name] = KGEntity(name, attributes)

    def add_relation(self, source: str, relation: str, target: str):
        self.relations.append(KGRelation(source, relation, target))

    def get_relations(self, entity: str):
        return [r for r in self.relations if r.source == entity or r.target == entity]
