from neomodel import StructuredNode, StringProperty, RelationshipTo


class CodeFile(StructuredNode):
    path = StringProperty(unique_index=True, required=True)
    desc = StringProperty(required=True)
    file_type = StringProperty(required=True)  # config_required, definition_required etc.
    category = StringProperty(required=True)  # 对称密码，

    depends_on = RelationshipTo('CodeFile', 'DEPENDS_ON')