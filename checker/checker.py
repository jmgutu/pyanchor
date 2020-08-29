import requests
from bs4 import BeautifulSoup


class LinkResults():
    """TODO:"""

    def __init__(self, url: str):
        self.base_url = url
        self.all_atags = self.find_all_atags(self.base_url)
        self.results = self.build_results_dictionary()


    def __str__(self) -> str:
        """TODO:"""
        return f'All links for {self.base_url}'


    def check_link_for_http_scheme(self, href: str) -> str:
        """TODO: """

        if href.startswith(self.base_url):
            return href
        elif href.startswith("/"):
            href = self.base_url + href
            return href
        else:
            return None  # TODO: Deal with ./ or ../ relative links.


    def find_all_atags(self, url: str): # Returns -> bs4.element.ResultSet
        """TODO:"""

        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html.parser")
            return soup.find_all("a")

        else:  # If not a 200 response, then an Exception is raised
            raise Exception(f"The requested page is unavailable -> {url}") #TODO: Find better exception type/create custom Exception


    def build_results_dictionary(self) -> dict:
        """TODO:"""

        results = dict()
        for tag in self.all_atags:
            href = tag.get("href")
            parsed_url = self.check_link_for_http_scheme(href)

            if parsed_url is not None:
                results[parsed_url] = requests.get(parsed_url).status_code
            else: 
                pass
            
        return results

    # @property
    # def check_anchor_tags_attributes(self, tags):
    #     """TODO:"""
    #     return 
