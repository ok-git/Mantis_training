from model.project import Project
from selenium.webdriver.support.ui import Select

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, Project):
        wd = self.app.wd
        self.open_project_create_page()
        self.fill_project_form(Project)
        # submit project creation
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.app.open_home_page()

    def fill_project_form(self, Project):
        self.change_field_value("name", Project.name)
        self.change_dropdown_value("status", Project.status)
        self.change_inherit_global_value(Project.inherit_global)
        self.change_dropdown_value("view_state", Project.view_status)
        self.change_field_value("description", Project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_dropdown_value(self, dropdown_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(dropdown_field_name).click()
            Select(wd.find_element_by_name(dropdown_field_name)).select_by_visible_text(text)

    def change_inherit_global_value(self, inherit_global):
        wd = self.app.wd
        # default value in the Web is True
        if inherit_global is not True:
            wd.find_element_by_name("inherit_global").click()

    def open_project_create_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_create_page.php"):
            wd.get("http://localhost/mantisbt-1.2.20/manage_proj_create_page.php")

    def open_manage_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("[href^='manage_proj_edit_page.php?project_id=%s']" % id).click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_manage_project_page()
        self.select_project_by_id(id)
        # first submit deletion
        wd.find_element_by_name("delete").click()
        # second submit deletion
        wd.find_element_by_name("delete").click()
        self.app.open_home_page()


