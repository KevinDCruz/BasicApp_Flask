import os
if os.environ['ENV'] == 'prod':
    config = ProductionConfig()
else:
    config = DevelopmentConfig()
