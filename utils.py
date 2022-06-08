def get_text_for_genetics(inp: str) -> str:
    return (f'Аденин: {inp.count("А")}\n'
            f'Гуанин: {inp.count("Г")}\n'
            f'Цитозин: {inp.count("Ц")}\n'
            f'Тимин: {inp.count("Т")}')
