from flask import Flask
from files.config import Config
from gooddata_sdk import CatalogWorkspace

app = Flask(__name__)
sdk = Config.sdk


@app.route("/workspace/<workspace_id>/copy/<new_workspace_id>", methods=["POST"])
def workspace_copy(workspace_id: str, new_workspace_id: str):
    demo_copy = CatalogWorkspace(workspace_id=new_workspace_id, name=new_workspace_id)

    declarative_ldm = sdk.catalog_workspace_content.get_declarative_ldm(workspace_id)
    declarative_analytics_model = sdk.catalog_workspace_content.get_declarative_analytics_model(workspace_id)

    sdk.catalog_workspace.create_or_update(workspace=demo_copy)

    sdk.catalog_workspace_content.put_declarative_ldm(workspace_id=demo_copy.id, ldm=declarative_ldm)
    sdk.catalog_workspace_content.put_declarative_analytics_model(workspace_id=demo_copy.id,
                                                                  analytics_model=declarative_analytics_model)
    return "success", 200


"""
Run:
flask --app flask_server run
"""
