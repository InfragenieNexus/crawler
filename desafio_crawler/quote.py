import requests
from bs4 import BeautifulSoup
import logging
import pandas as pd

import chromedriver_autoinstaller
from utils.screenshot import FullScreenScreenshot
from utils.name_generator import NameGenerator
from utils.logger import setup_logger

# Instalação automática do ChromeDriver
chromedriver_autoinstaller.install()
setup_logger()


class SiteScraper:
    def __init__(self, site_url):
        self.site_url = site_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 86.0.4240.198 Safari / 537.36"
        }
        self.soup = self._make_request()
        logging.info(f"Conectado ao site: {self.site_url}")

    def _make_request(self) -> BeautifulSoup:
        """here make a request to the site and return a BeautifulSoup object"""
        try:
            response = requests.get(self.site_url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except Exception as e:
            logging.error(f"Falha na requisição ao site: {str(e)}")
            raise

    def _get_quotes_info(self) -> list:
        """here return a list of dictionaries with the quotes information"""
        quote_divs = self.soup.find_all("div", class_="quote")
        quotes_info = []
        for quote in quote_divs:
            quote_text = quote.find("span", class_="text").text
            autor = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]
            quotes_info.append({"Quote": quote_text, "Author": autor, "Tags": tags})
        return quotes_info

    def get_list_of_tags(self, tag=None) -> list:
        """here return a top ten of tags that have the request"""
        tags_span = self.soup.find_all("span", class_="tag-item")
        tags = [span.find("a", class_="tag").text for span in tags_span]
        return tags

    def get_list_of_authors(self, author=None) -> list:
        """here return a list of authors that have the request"""
        authors_span = self.soup.find_all("small", class_="author")
        authors = [span.text for span in authors_span]
        return authors

    def get_all_quotes_and_save_to_csv(self) -> None:
        """Return all quotes and save to a CSV file"""
        try:
            quotes_info = self._get_quotes_info()
            df = pd.DataFrame(quotes_info, columns=["Author", "Tags", "Quote"])

            csv_filename = NameGenerator.generate_name_with_timestamp(None, None)
            df.to_csv(csv_filename + ".csv", index=False)

            pic = FullScreenScreenshot(url=self.site_url)
            pic.take_screenshot(f"{csv_filename}.png")

            logging.info(f"Citações salvas em {csv_filename}")
        except Exception as e:
            logging.error(f"Falha ao obter citações e salvar em CSV: {str(e)}")

    def get_quotes_by_author(self, author=None) -> None:
        """Return quotes by a specific author and save to a CSV file"""
        try:
            quotes_info = self._get_quotes_info()
            if author:
                quotes_info = [
                    quote for quote in quotes_info if quote["Author"] == author
                ]

            csv_filename = NameGenerator.generate_name_with_timestamp(author, None)
            df = pd.DataFrame(quotes_info, columns=["Author", "Tags", "Quote"])

            df.to_csv(f"{csv_filename}+.csv", index=False)

            pic = FullScreenScreenshot(url=self.site_url)
            pic.take_screenshot(f"{csv_filename}.png")
            logging.info(f"Citações de {author} salvas em {csv_filename}")
        except Exception as e:
            logging.error(
                f"Falha ao obter citações por autor e salvar em CSV: {str(e)}"
            )

    def _create_url_with_tag(self, tag) -> str:
        """here create a url with the tag"""
        return f"{self.site_url}/tag/{tag}"

    def get_quotes_by_tag(self, tag=None) -> None:
        """Return quotes by a specific tag and save to a CSV file"""
        try:
            quotes_info = self._get_quotes_info()
            if tag:
                quotes_info = [quote for quote in quotes_info if tag in quote["Tags"]]
                csv_filename = NameGenerator.generate_name_with_timestamp(None, tag)
                df = pd.DataFrame(quotes_info, columns=["Author", "Tags", "Quote"])

            df.to_csv(f"{csv_filename}.csv", index=False)
            url_tag = self._create_url_with_tag(tag)
            pic = FullScreenScreenshot(url=url_tag)
            pic.take_screenshot(f"{csv_filename}.png")
            logging.info(f"Citações com a tag {tag} salvas em {csv_filename}")
        except Exception as e:
            logging.error(f"Falha ao obter citações por tag e salvar em CSV: {str(e)}")
