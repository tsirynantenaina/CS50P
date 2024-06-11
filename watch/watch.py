import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Utiliser une expression régulière pour trouver une URL YouTube dans un attribut src d'un élément iframe
    match = re.search(r'<iframe[^>]*\bsrc="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
