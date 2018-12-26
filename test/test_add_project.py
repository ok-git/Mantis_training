from model.project import Project
import pytest


def test_add_project(app, db):
    old_projects = db.get_project_list()
    project = Project(name="Test Proj 6", status="development", inherit_global=True,
                      view_status="public", description="Test_Description 6")
    if len(list(filter(lambda x: x.name == project.name, old_projects))) > 0:
        pytest.skip("duplicated project name detected - %s" % project.name)
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
