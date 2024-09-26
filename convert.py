import os
import os.path

# Fonction pour convertir un fichier markdown en quarto file
def convert_markdown_to_quarto(file_path):
    # Lire le fichier markdown
    with open(file_path, 'r') as file:
        markdown_content = file.read()

    # Écrire le contenu dans un fichier quarto
    new_file_path = os.path.splitext(file_path)[0] + '.qmd'
    with open(new_file_path, 'w') as new_file:
        new_file.write('---\ntitle: ' + os.path.basename(file_path) + '\n---\n\n' + markdown_content)

# Fonction pour convertir les fichiers markdown en quarto files dans un dossier
def convert_markdown_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if file_path.endswith('.md'):
                convert_markdown_to_quarto(file_path)

# Chemin du dossier où se trouvent les fichiers markdown
directory = 'D:\\Home\\dbelveze\\Desktop\\CFCB_IA'

if __name__ == '__main__':
    convert_markdown_files(directory)