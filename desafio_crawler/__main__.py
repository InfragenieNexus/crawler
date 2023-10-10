from quote import SiteScraper


def apresentacao():
    print("Bem-vindo ao Desafio Crawler! Como você gostaria de receber citações hoje?")
    print("1. Ver citações por autor")
    print("2. Ver citações por tag")
    print("3. Sair")


def main():
    url = input(
        "Digite a URL do site de citações (ou pressione Enter para usar 'https://quotes.toscrape.com/'): "
    )
    url = (
        url.strip() or "https://quotes.toscrape.com/"
    )  # Usar a URL padrão se nenhum URL for fornecido
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
            print("Obrigado por usar o Desafio Crawler. Até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

        ### adicionar para pegar todas sem filtro algum


if __name__ == "__main__":
    main()
