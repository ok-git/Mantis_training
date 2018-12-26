from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, inherit_global=None, view_status=None, description=None, id=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_status = view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s: %s; %s; %s; %s" % (self.id, self.name, self.status, self.inherit_global, self.view_status)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name \
            and self.status == self.status and self.inherit_global == self.inherit_global \
            and self.view_status == self.view_status

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
