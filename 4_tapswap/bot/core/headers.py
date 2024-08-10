from fake_useragent import UserAgent

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://app.tapswap.club',
    'Referer': 'https://app.tapswap.club/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': UserAgent(os='android').random,
    'Sec-Ch-Ua': '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?1',
    'Sec-Ch-Ua-Platform': '"Android"',
    'X-App': 'tapswap_server',
    'X-Cv': '',
    'X-Touch': '',
}