# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_domain(url):
            tokens = url.split("/")
            return tokens[2]
        
        print(get_domain(startUrl))
        
        
        queue = collections.deque([startUrl])
        visited = set()
        visited.add(startUrl)
        ans = []
        
        while queue:
            url = queue.popleft()
            ans.append(url)
            
            for n in htmlParser.getUrls(url):
                if get_domain(n) == get_domain(url) and n not in visited:
                    queue.append(n)
                    visited.add(n)
        return ans
        