from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def create(self, Project):
        wd = self.app.wd
        self.open_project_create_page()
        self.fill_project_form(Project)
        # submit project creation
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.app.open_homepage()
        self.project_cache = None

    def fill_project_form(self, Project):
        self.change_field_value("name", Project.name)
        self.change_field_value("group_header", Group.header)
        self.change_field_value("group_footer", Group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_project_create_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_create_page.php"):
            wd.get("http: //localhost/mantisbt-1.2.20/manage_proj_create_page.php")

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
