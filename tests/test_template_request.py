from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_plugin_is_installed(tmpdir):
    templates = tmpdir / "templates"
    templates.mkdir()
    pages = tmpdir / "templates" / "pages"
    pages.mkdir()
    (pages / "demo.html").write_text(
        "request.args = {{ request.args._data|safe }}", "utf-8"
    )
    datasette = Datasette([], memory=True, template_dir=str(templates))
    response = await datasette.client.get("/demo?foo=bar")
    assert response.status_code == 200
    assert response.text == "request.args = {'foo': ['bar']}"
