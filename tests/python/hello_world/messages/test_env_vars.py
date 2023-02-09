import os

def test_env_var():
    envs = {k: v for k,v in os.environ.items() if k.startswith('ENV_')}
    assert envs["ENV_TARGET"] == 'target'
    assert envs["ENV_ALL"] == 'target'

    assert envs["ENV_TOML"] == 'toml'
    assert envs["ENV_DOCKER"] == 'docker'
