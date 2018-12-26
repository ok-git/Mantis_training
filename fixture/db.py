import pymysql.cursors
from model.project import Project


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, view_state, description, inherit_global  from mantis_project_table")
            for row in cursor:
                (id, name, status, view_state, description, inherit_global) = row
                list.append(Project(id=str(id),
                                    name=name,
                                    status=self.convert_status(status),
                                    inherit_global=self.convert_inherit_global(inherit_global),
                                    view_status=self.convert_view_state(view_state),
                                    description=description))
        finally:
            cursor.close()
        return list

    def convert_status(self, status):
        status_dict = {10: "development",
                       30: "release",
                       50: "stable",
                       70: "obsolete"}
        return status_dict[status]

    def convert_inherit_global(self, inherit_global):
        if inherit_global == 1:
            return True
        else:
            return False

    def convert_view_state(self, view_state):
        view_state_dict = {10: "public",
                           50: "private"}
        return view_state_dict[view_state]

    def destroy(self):
        self.connection.close()
