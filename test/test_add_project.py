from model.project import Project


def test_add_project(app):
    project = Project(name="Test Proj 1", status="development", inherit_global=True,
                      view_status="public", description="Test_Description")
    app.project.create(project)
