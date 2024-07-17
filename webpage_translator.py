from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator as translator

def translate_webpage_inplace(url, target_lang):
    # path to HTML file
    html_file_path = "index.htm"

    with open(html_file_path, "rb") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Iterate over specific tags that typically contain text (adjust as needed)
    for tag in soup.find_all(['p', 'span', 'h1', 'h2', 'h3', 'a', 'li']):  # Add or remove tags as per your HTML structure
        text_to_translate = tag.text.strip()
        if text_to_translate:

            # Chunking to avoid deep_translator word limit
            chunk_size = 4500  # Adjust as needed
            text_chunks = [text_to_translate[i:i + chunk_size] for i in range(0, len(text_to_translate), chunk_size)]
            translated_text = ""
            for chunk in text_chunks:
                translated_text += translator(source='auto', target='hi').translate(chunk)
            tag.string = translated_text  # Replaces the text within the tag only , preserving the tag itself

    # Save the translated content to a new file
    with open("index_trans.htm", "w", encoding="utf-8") as f:
        f.write(str(soup))


translate_webpage_inplace("https://www.classcentral.com", "hi")  # With minor changes , usable with urls as well
print("Translation complete. Check the 'index_trans.htm' file.")