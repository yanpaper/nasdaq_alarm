import urllib.request
import ssl

# def get_redirected_url(url):
context = ssl._create_unverified_context()
#return urllib.request.urlopen(url, context=context)
readdr = urllib.request.urlopen("https://kauth.kakao.com/oauth/authorize?client_id=b328b5caff640883672534d3fd6f277a&redirect_uri=https://example.com/oauth&response_type=code", context=context)
print (readdr)
#print get_redirected_url(r"https://kauth.kakao.com/oauth/authorize?client_id=b328b5caff640883672534d3fd6f277a&redirect_uri=https://example.com/oauth&response_type=code").geturl()
# import urllib.request
# response = urllib.request.urlopen('https://kauth.kakao.com/oauth/authorize?client_id=b328b5caff640883672534d3fd6f277a&redirect_uri=https://example.com/oauth&response_type=code')
# response.geturl()