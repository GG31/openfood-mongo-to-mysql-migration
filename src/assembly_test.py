from unittest.mock import patch

from .assembly import Assembly
import config

test_config = config.get_config('test')

@patch('src.assembly.app.run')
def test_start(mock_app_run):
    mock_app_run.return_value = True
    assembly = Assembly(test_config)
    assembly.start()
    mock_app_run.assert_called_once()

