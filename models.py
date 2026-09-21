class Subject:
    def __init__(self, id, name, created_at, updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at


class Topic:
    def __init__(self, id, name, subject_id, created_at, updated_at):
        self.id = id
        self.name = name
        self.subject_id = subject_id
        self.created_at = created_at
        self.updated_at = updated_at


class Note:
    def __init__(self, id, title, content, topic_id, created_at, updated_at):
        self.id = id
        self.title = title
        self.content = content
        self.topic_id = topic_id
        self.created_at = created_at
        self.updated_at = updated_at
