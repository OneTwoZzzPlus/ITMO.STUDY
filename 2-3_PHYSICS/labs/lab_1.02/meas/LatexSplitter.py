class LatexSplitter:
    def __init__(self, file_path):
        self.file_path = file_path
        self._chunks = []
        content = self.read_file()
        self.split_text(content)

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден.")
            return None

    def split_text(self, content):
        if content is None:
            return

        # Разделяем текст по "<<<" и ">>>"
        parts = content.split('<<<')
        for part in parts:
            if '>>>' in part:
                # Берем текст до ">>>" как внешний
                external_text = part.split('>>>')[1].strip()
                if external_text:  # Добавляем только непустые куски
                    self._chunks.append(external_text)
            else:
                # Если ">>>" нет, это внешний текст
                if part.strip():  # Добавляем только непустые куски
                    self._chunks.append(part.strip())

    @property
    def chunks(self):
        return self._chunks
        

# Пример использования
if __name__ == "__main__":
    file_path = 'example.txt'  # Укажите путь к вашему файлу
    sp = LatexSplitter(file_path)

    for i, chunk in enumerate(sp._chunks, 1):
        print(f"Кусок {i}:\n{chunk}\n")