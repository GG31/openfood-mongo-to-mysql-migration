from unittest.mock import patch, MagicMock

from .assembly import Assembly
import config

test_config = config.get_config('test')


@patch('src.assembly.Router')
def test_start(mock_router):
    app_mock = MagicMock()
    mock_router = mock_router()
    mock_router.create_router.return_value = app_mock
    assembly = Assembly(test_config)
    assembly.start()
    app_mock.run.assert_called_once()

