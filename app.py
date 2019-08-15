# -*- coding: utf-8 -*-
import os
from server import icityServer

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

# Need to import all resources
from workspaces.home.controller import HomeRoutes

# Register all Blueprint
icityServer.icity_app.register_blueprint(icityServer.icity_bp)

# run dev, prod
if __name__ == '__main__':
    icityServer.run()
