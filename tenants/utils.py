from django.apps import apps
from app.models import TenantAwareModel
import json

def get_all_fixture_paths():
    #   TODO: right logic to traverse all *fixtures/*.json files and append their paths into the list
    return ["app/fixtures/app.json"]

def install_fixtures(tenant):
    all_fixture_paths = get_all_fixture_paths()
    for path in all_fixture_paths:
        with open(path, 'r') as file:
            json_instances = json.load(file)
            for fixture_instance in json_instances:
                '''
                create an instance of a model from a dict represantation
                '''
                app_label, model_name = fixture_instance.get("model").split(".")
                model_class = apps.get_model(app_label=app_label, model_name=model_name)
                if issubclass(model_class, TenantAwareModel):
                    fixture_instance["fields"]["tenant"] = tenant
                    
                fixture_instance["fields"]["id"] = int(fixture_instance.get("pk"))
                model_class.objects.create(**fixture_instance.get("fields"))