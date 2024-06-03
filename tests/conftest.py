from pytest_metadata.plugin import metadata_key

def pytest_html_report_title(report):
    report.title = "PetStore Api Testing with Pytest and Request"

def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "PestStore Api"
    config.stash[metadata_key]["Module"] = "User, Pet and Store Module"
    config.stash[metadata_key]["Tester"] = "Silas Francis"

def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Packages', None)
    metadata.pop('Platform', None)

