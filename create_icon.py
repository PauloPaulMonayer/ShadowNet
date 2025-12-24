from PIL import Image, ImageDraw

def create_icon():
    # גודל האייקון (סטנדרטי)
    size = (256, 256)
    
    # יצירת תמונה חדשה עם רקע שקוף
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # ציור עיגול חיצוני (אפור כהה)
    draw.ellipse([10, 10, 246, 246], fill=(40, 40, 40), outline=(20, 20, 20))
    
    # ציור "עין" אדומה במרכז
    draw.ellipse([70, 70, 186, 186], fill=(200, 0, 0), outline=(100, 0, 0))
    
    # אישון שחור
    draw.ellipse([110, 110, 146, 146], fill=(0, 0, 0))
    
    # שמירה כקובץ ICO
    img.save("shadownet.ico", format='ICO', sizes=[(256, 256)])
    print("[+] Icon 'shadownet.ico' created successfully!")

if __name__ == "__main__":
    create_icon()