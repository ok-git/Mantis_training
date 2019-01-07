from model.project import Project
import pytest


def test_add_project(app, db, data_projects):
    project = data_projects
    projects_list = db.get_project_list()
    if len(list(filter(lambda x: x.name == project.name, projects_list))) > 0:
        pytest.skip("duplicated project name detected - %s" % project.name)
    old_projects = app.soap.get_project_list()
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
