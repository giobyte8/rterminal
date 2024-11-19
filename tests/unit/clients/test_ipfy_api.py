import pytest
from rterminal.clients import ipfy_api
from unittest.mock import AsyncMock, patch


def mock_http_response(status: int, content: str) -> AsyncMock:
    """Mocks responses for requests done through aiohttp library

    Args:
        status (int): Desired http status for response
        content (str): Desired text conent for response

    Returns:
        AsyncMock: A mocked async context manager that can be used \
                    as a mock for aiohttp responses
    """
    res = AsyncMock()

    # Async context managers uses '__aenter__' and '__aexit__' methods,
    # hence, we mock it to return our desired response
    res.__aenter__.return_value = AsyncMock(
        status = status,
        text = AsyncMock(return_value=content)
    )

    return res


@pytest.mark.asyncio
@patch('rterminal.clients.ipfy_api._aiohttp_session')
async def test_get_ipv4_successful(m_http: AsyncMock) -> None:
    TEST_IP = '123.123.123.123'
    m_res = mock_http_response(
        status=200,
        content=TEST_IP
    )
    m_http.get.return_value = m_res

    ipv4 = await ipfy_api.get_public_ipv4()

    m_res.__aenter__.assert_awaited_once()
    assert ipv4 == TEST_IP
