import os
from quote import SiteScraper
from logger.show_logs import show_logs_until_enter


def apresentacao():
    print("Bem-vindo ao Desafio Crawler! Como você gostaria de receber citações hoje?")
    print("1. Ver citações por autor")
    print("2. Ver citações por tag")
    print("3. Ver todas as citações")
    print("4. Ver logs")
    print("5. Sair")


def main():
    url = os.environ.get("SITE_URL", "https://quotes.toscrape.com/")
    site_instance = SiteScraper(url)

    while True:
        apresentacao()
        choice = input("Escolha uma opção digitando o número desejado: ")

        if choice == "1":
            print("Autores disponíveis:")
            authors = site_instance.get_list_of_authors()
            for author in authors:
                print(f"- {author}")
            author = input("Digite o nome do autor para ver suas citações: ")
            site_instance.get_quotes_by_author(author)
        elif choice == "2":
            print("Tags disponíveis:")
            tags = site_instance.get_list_of_tags()
            for tag in tags:
                print(f"- {tag}")
            tag = input("Digite a tag desejada para ver citações relacionadas: ")
            site_instance.get_quotes_by_tag(tag)
        elif choice == "3":
            site_instance.get_all_quotes_and_save_to_csv_db()
            print("Todas as citações foram salvas em um arquivo CSV.")
        elif choice == "4":
            show_logs_until_enter()
        elif choice == "5":
            print("Obrigado por usar o Desafio Crawler. Até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
