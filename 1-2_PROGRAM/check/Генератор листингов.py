import os
import re
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
import chardet

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "_", filename).replace(" ", "_").rstrip('_')

def detect_encoding(filepath):
    with open(filepath, 'rb') as f:
        return chardet.detect(f.read())['encoding']

def generate_code_images(input_dir, output_dir, lines_per_page=45, latex_file="latex.txt", ignore=[]):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    lexer = PythonLexer()
    base_style = {
        'font_name': 'DejaVu Sans Mono',
        'font_size': 12,
        'line_number_bg': '#f0f0f0',
        'image_pad': 15,
        'encoding': 'utf-8'
    }

    fig_counter = 1  # Счетчик для сквозной нумерации рисунков

    with open(os.path.join(output_dir, latex_file), 'w', encoding='utf-8') as latex_f:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith(".py") and file not in ignore:
                    filepath = os.path.join(root, file)
                    clean_name = sanitize_filename(file[:-3])
                    
                    try:
                        encoding = detect_encoding(filepath) or 'utf-8'
                        with open(filepath, 'r', encoding=encoding, errors='replace') as f:
                            code = f.readlines()

                        line_counter = 1
                        part_num = 1
                        total_lines = len(code)
                        
                        while line_counter <= total_lines:
                            end_line = min(line_counter + lines_per_page - 1, total_lines)
                            part_code = ''.join(code[line_counter-1:end_line])
                            
                            # Генерация изображения
                            img_filename = f"code_{clean_name}_part_{part_num}.png"
                            img_path = os.path.join(output_dir, img_filename)
                            
                            formatter = ImageFormatter(
                                style='colorful',
                                line_numbers=True,
                                linenostart=line_counter,
                                **base_style
                            )
                            
                            highlight(part_code, lexer, formatter, img_path)
                            
                            # Генерация LaTeX-кода
                            label = f"{img_filename[:-4]}"
                            caption = (
                                f"Код в файле <<{file}>> часть {part_num}"
                            )
                            
                            latex_code = (
                                f"\\begin{{figure}}[H]\n"
                                f"    \\centering\n"
                                f"    \\includegraphics[width=1\\linewidth]{{code/{img_filename}}}\n"
                                f"    \\caption{{{caption}}}\n"
                                f"    \\label{{{label}}}\n"
                                f"\\end{{figure}}\n\n"
                            )
                            
                            latex_f.write(latex_code)
                            print(f"Добавлен рисунок {fig_counter}: {file} часть {part_num}")
                            
                            line_counter = end_line + 1
                            part_num += 1
                            fig_counter += 1

                    except Exception as e:
                        print(f"Ошибка обработки файла {file}: {str(e)}")
                        continue

if __name__ == "__main__":
    ignore = ["Генератор листингов.py", "MNK.py", "Tools.py", "IndirectMultipleMeasurment.py"]
    generate_code_images(".", "code_images", 50, ignore=ignore)
