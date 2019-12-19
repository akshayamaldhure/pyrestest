import os.path as osp

from lemoncheesecake.fixture import load_fixtures_from_directory
from lemoncheesecake.project import Project
from lemoncheesecake.suite import load_suites_from_directory

try:
    from core.common.init import init_session
except:
    print("Error! Please ensure following:\n- PYTHONPATH/TEST_ENV environment variables are set properly before"
          " running any tests.\n- All test URLs are valid and reachable.")
    exit(1)


class MyProject(Project):
    def pre_run(self, cli_args, report_dir):
        init_session()

    def post_run(self, cli_args, report_dir):
        print("Finished executing all the tests")

    def load_suites(self):
        return load_suites_from_directory(osp.join(self.dir, "tests"))

    def load_fixtures(self):
        return load_fixtures_from_directory(osp.join(self.dir, "core/fixtures"))


project_dir = osp.dirname(__file__)
project = MyProject(project_dir)
