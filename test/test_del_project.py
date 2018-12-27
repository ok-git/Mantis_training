from model.project import Project
import random


def test_delete_some_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="Test Project to delete",
                                   status="development",
                                   inherit_global=True,
                                   view_status="public",
                                   description="Description of the project"))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects
